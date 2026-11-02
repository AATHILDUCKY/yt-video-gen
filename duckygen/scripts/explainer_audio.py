#!/usr/bin/env python3
"""Measure narration, synthesize small cues, and stream a speech-led explainer mix.

Dependencies: NumPy; FFmpeg on PATH for build. No network calls or model downloads.
"""
import argparse
from collections import OrderedDict
from contextlib import ExitStack
import json
import math
import os
from pathlib import Path
import subprocess
import tempfile
import wave

import numpy as np

KINDS = {"click": .12, "tap": .20, "swipe": .55,
         "paper": .45, "marker": .24, "chime": .65}
OUTPUTS = ("voice.wav", "effects.wav", "soundtrack.wav", "captions.srt",
           "narration.txt", "timeline.json", "audio-report.json")


def number(value, label, low, high):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError(f"{label} must be a number")
    value = float(value)
    if not math.isfinite(value) or not low <= value <= high:
        raise ValueError(f"{label} must be between {low} and {high}")
    return value


def fade(signal, rate, attack=.003, release=.025):
    signal = signal.copy()
    for count, edge in [(min(len(signal)//2, round(attack*rate)), "in"),
                        (min(len(signal)//2, round(release*rate)), "out")]:
        if count:
            ramp = np.sin(np.linspace(0, np.pi/2, count)) ** 2
            if edge == "in":
                signal[:count] *= ramp
            else:
                signal[-count:] *= ramp[::-1]
    return signal


def synth(kind, rate):
    """Fixed-seed band-shaped noise with damped body; no external sound assets."""
    n = round(KINDS[kind]*rate)
    t = np.arange(n)/rate
    rng = np.random.default_rng(914 + list(KINDS).index(kind))
    frequencies = np.fft.rfftfreq(n, 1/rate)
    band = (1-np.exp(-(frequencies/280)**4))*np.exp(-(frequencies/5500)**4)
    noise = np.fft.irfft(np.fft.rfft(rng.normal(size=n))*band, n)
    noise /= max(np.sqrt(np.mean(noise**2)), 1e-9)
    if kind in ("click", "tap"):
        decay = 85 if kind == "click" else 45
        sound = .22*noise*np.exp(-t*decay)
        sound += np.sin(2*np.pi*370*t)*np.exp(-t*38)*.35
    elif kind == "swipe":
        sound = noise*np.exp(-.5*((t/.55-.50)/.18)**2)
    elif kind == "paper":
        sound = noise*np.sin(np.pi*t/.45)**2*.35
        for at in (.055, .13, .22):
            sound += noise*np.exp(-np.maximum(t-at, 0)*110)*(t >= at)*.2
    elif kind == "marker":
        sound = noise*np.sin(np.pi*t/.24)**2*(.6+.4*np.sin(2*np.pi*35*t))
    else:
        sound = sum(np.sin(2*np.pi*f*t)*np.exp(-t*(8+i*3))/(i+1)**1.5
                    for i, f in enumerate((660, 990, 1320)))
    sound -= np.mean(sound)
    sound = fade(sound, rate)
    return (sound*(.7/max(np.max(np.abs(sound)), 1e-9))).astype(np.float32)


def wav_open(path, rate):
    writer = wave.open(str(path), "wb")
    writer.setparams((1, 2, rate, 0, "NONE", "not compressed"))
    return writer


def pcm(signal):
    return np.rint(np.clip(signal, -1, 32767/32768)*32768).astype("<i2").tobytes()


def decode(source, target, rate, limit):
    command = [os.environ.get("FFMPEG_PATH", "ffmpeg"), "-nostdin", "-v", "error",
               "-protocol_whitelist", "file,pipe", "-i", str(source), "-t", str(limit+.1),
               "-vn", "-ac", "1", "-ar", str(rate), "-f", "s16le", "-y", str(target)]
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=90)
    except FileNotFoundError as exc:
        raise ValueError("FFmpeg missing; reuse an installed runtime or set FFMPEG_PATH") from exc
    if result.returncode:
        raise ValueError(f"Cannot decode {source.name}: {result.stderr[-1200:]}")
    n = target.stat().st_size//2
    if not n or n > round(limit*rate):
        raise ValueError(f"{source.name}: expected nonempty audio no longer than {limit}s")
    return n


class PCMReader:
    """Bound file handles and memory regardless of the number of scene clips."""
    def __init__(self):
        self.handles = OrderedDict()

    def read(self, path, start, count):
        if path not in self.handles:
            self.handles[path] = open(path, "rb")
        handle = self.handles.pop(path)
        self.handles[path] = handle
        if len(self.handles) > 12:
            self.handles.popitem(last=False)[1].close()
        handle.seek(start*2)
        return np.frombuffer(handle.read(count*2), dtype="<i2").astype(np.float32)/32768

    def close(self):
        for handle in self.handles.values():
            handle.close()


def path_input(base, value, label, out):
    if not isinstance(value, str) or not value:
        raise ValueError(f"{label}: supply a local audio path")
    source = (base/value).expanduser().resolve()
    if not source.is_file():
        raise ValueError(f"{label}: missing file {source}")
    if source.is_relative_to(out):
        raise ValueError("Keep input audio outside the generated output folder")
    return source


def prepare(plan, base, temp, out):
    if not isinstance(plan, dict):
        raise ValueError("Plan must be a JSON object")
    rate = plan.get("sample_rate", 24000)
    if type(rate) is not int or rate not in (24000, 48000):
        raise ValueError("sample_rate must be 24000 or 48000")
    voice_gain = number(plan.get("voice_gain", 1), "voice_gain", 0, 4)
    duck = number(plan.get("duck_db", 8), "duck_db", 0, 18)
    tail = number(plan.get("tail", .4), "tail", 0, 5)
    scenes = plan.get("scenes")
    if not isinstance(scenes, list) or not 1 <= len(scenes) <= 500:
        raise ValueError("Supply 1–500 phrase scenes")
    converted, generated, ids, timeline, voices, cues = {}, {}, set(), [], [], []

    def convert(source, limit):
        key = (source, limit)
        if key not in converted:
            target = temp/f"decoded-{len(converted)}.pcm"
            converted[key] = (target, decode(source, target, rate, limit))
        return converted[key]

    cursor = 0
    for scene in scenes:
        if not isinstance(scene, dict):
            raise ValueError("Each scene must be an object")
        identity, text = scene.get("id"), scene.get("text")
        if not isinstance(identity, str) or not identity.strip() or identity in ids:
            raise ValueError("Scene ids must be nonempty unique strings")
        if not isinstance(text, str) or not text.strip():
            raise ValueError(f"{identity}: text is required")
        ids.add(identity)
        source = path_input(base, scene.get("voice"), identity, out)
        target, length = convert(source, 600)
        pause = number(scene.get("pause_after", .2), "pause_after", 0, 5)
        minimum = number(scene.get("min_duration", 0), "min_duration", 0, 120)
        end = cursor + max(length + round(pause*rate), round(minimum*rate))
        if end > 600*rate:
            raise ValueError("Output exceeds the ten-minute limit")
        voices.append((cursor, cursor+length, target))
        timing = {"id": identity, "text": " ".join(text.split()), "voice": str(source),
                  "start": cursor/rate, "voice_end": (cursor+length)/rate,
                  "end": end/rate, "sounds": []}
        sounds = scene.get("sounds", [])
        if not isinstance(sounds, list):
            raise ValueError(f"{identity}: sounds must be a list")
        for cue in sounds:
            if not isinstance(cue, dict) or (("type" in cue) == ("file" in cue)):
                raise ValueError("Each sound needs exactly one of type or file")
            offset = number(cue.get("offset"), "sound offset", 0, 600)
            at = cursor + round(offset*rate)
            if at >= end:
                raise ValueError(f"{identity}: cue starts outside its scene")
            gain = number(cue.get("gain", .16), "cue gain", 0, 2)
            if "type" in cue:
                kind = cue["type"]
                if not isinstance(kind, str) or kind not in KINDS:
                    raise ValueError(f"Unknown cue type {kind!r}; choose {', '.join(KINDS)}")
                if kind not in generated:
                    target = temp/f"cue-{kind}.pcm"
                    signal = synth(kind, rate)
                    target.write_bytes(pcm(signal))
                    generated[kind] = (target, len(signal))
                target, size = generated[kind]
                record = {"type": kind, "origin": "procedural"}
            else:
                source = path_input(base, cue["file"], "cue", out)
                target, size = convert(source, 5)
                record = {"file": str(source), "origin": "external; retain its license"}
            cues.append((at, at+size, target, gain))
            timing["sounds"].append({**record, "at": at/rate, "gain": gain})
            if len(cues) > 2000:
                raise ValueError("Too many cues; use at most 2000")
        timeline.append(timing)
        cursor = end
    # Both supported sample rates divide exactly into a 60fps frame grid.
    frame = rate//60
    total = math.ceil((cursor+round(tail*rate))/frame)*frame
    if total > rate*600:
        raise ValueError("Output including tail exceeds ten minutes")
    return rate, voice_gain, duck, total, timeline, voices, sorted(cues)


def stamp(seconds):
    milliseconds = round(seconds*1000)
    h, remainder = divmod(milliseconds, 3600000)
    m, remainder = divmod(remainder, 60000)
    s, ms = divmod(remainder, 1000)
    return f"{h:02}:{m:02}:{s:02},{ms:03}"


def build(args):
    plan_path = args.plan.expanduser().resolve()
    out = args.out.expanduser().resolve()
    if plan_path.is_relative_to(out):
        raise ValueError("Keep the audio plan outside its generated output folder")
    if out.exists() and (not out.is_dir() or (any(out.iterdir()) and not args.replace)):
        raise ValueError("Output exists; use a new folder or explicit --replace")
    # Reject symlinked outputs before any conversion or output replacement.
    if any((out/name).is_symlink() for name in OUTPUTS):
        raise ValueError("Generated output files must not be symbolic links")
    plan = json.loads(plan_path.read_text(encoding="utf-8"))
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="explainer-audio-", dir=out.parent) as directory:
        temp = Path(directory)
        rate, voice_gain, duck_db, total, timeline, voices, cues = prepare(
            plan, plan_path.parent, temp, out)
        reader = PCMReader()
        peaks, energy, duck_gain = [0., 0., 0.], 0., 1.
        block = rate//50
        try:
            with open(temp/"mix.f32", "wb") as raw:
                for start in range(0, total, block):
                    count = min(block, total-start)
                    voice, effects = np.zeros(count, np.float32), np.zeros(count, np.float32)
                    for begin, end, source in voices:
                        if begin >= start+count:
                            break
                        lo, hi = max(start, begin), min(start+count, end)
                        if hi > lo:
                            sample = reader.read(source, lo-begin, hi-lo)*voice_gain
                            positions = np.arange(lo-begin, hi-begin)
                            edge = np.minimum(1., positions/(rate*.003))
                            edge *= np.minimum(1., (end-begin-1-positions)/(rate*.003))
                            voice[lo-start:hi-start] += sample*edge
                    rms = float(np.sqrt(np.mean(voice**2)))
                    # Continuous ramps avoid gain jumps at block boundaries; release leaves room for tails.
                    activity = min(1., max(0., (rms-.004)/.025))
                    target_gain = 10**(-duck_db*activity/20)
                    tau = .015 if target_gain < duck_gain else .18
                    envelope = target_gain+(duck_gain-target_gain)*np.exp(-np.arange(1, count+1)/(rate*tau))
                    duck_gain = float(envelope[-1])
                    for begin, end, source, gain in cues:
                        if begin >= start+count:
                            break
                        lo, hi = max(start, begin), min(start+count, end)
                        if hi > lo:
                            sample = reader.read(source, lo-begin, hi-lo)*gain
                            positions = np.arange(lo-begin, hi-begin)
                            edge = np.minimum(1., positions/(rate*.002))
                            edge *= np.minimum(1., (end-begin-1-positions)/(rate*.02))
                            effects[lo-start:hi-start] += sample*edge
                    effects *= envelope
                    # Fade only film edges; preserve narration's natural interior transients.
                    positions = np.arange(start, start+count)
                    voice *= np.minimum(1., positions/(rate*.003)) * np.minimum(1., (total-1-positions)/(rate*.005))
                    effects *= np.minimum(1., (total-1-positions)/(rate*.025))
                    mix = voice+effects
                    for index, signal in enumerate((voice, effects, mix)):
                        peaks[index] = max(peaks[index], float(np.max(np.abs(signal))))
                    energy += float(np.sum(voice.astype(np.float64)**2))
                    raw.write(np.column_stack((voice, effects)).astype("<f4").tobytes())
        finally:
            reader.close()
        ceiling = 10**(-1/20)
        gain = min(1., ceiling/max(max(peaks), 1e-12))
        with ExitStack() as stack:
            streams = [stack.enter_context(wav_open(temp/name, rate)) for name in OUTPUTS[:3]]
            raw = stack.enter_context(open(temp/"mix.f32", "rb"))
            while chunk := raw.read(block*8):
                pair = np.frombuffer(chunk, dtype="<f4").reshape(-1, 2)*gain
                for stream, signal in zip(streams, (pair[:, 0], pair[:, 1], pair.sum(axis=1))):
                    stream.writeframesraw(pcm(signal))
        duration = total/rate
        (temp/"timeline.json").write_text(json.dumps({"duration": duration, "sample_rate": rate,
            "caption_timing": "measured clip boundaries; not word alignment", "scenes": timeline},
            ensure_ascii=False, indent=2)+"\n", encoding="utf-8")
        captions = [f"{i}\n{stamp(scene['start'])} --> {stamp(scene['voice_end'])}\n{scene['text']}\n"
                    for i, scene in enumerate(timeline, 1)]
        (temp/"captions.srt").write_text("\n".join(captions), encoding="utf-8")
        (temp/"narration.txt").write_text("\n\n".join(s["text"] for s in timeline)+"\n", encoding="utf-8")
        warnings = []
        if peaks[0] < .02:
            warnings.append("Voice is silent or very quiet; inspect before delivery")
        if gain < .5:
            warnings.append("Heavy global attenuation; reduce cue or voice gain and inspect")
        report = {"duration": duration, "sample_rate": rate, "channels": 1,
                  "voice_speed": 1, "duck_db": duck_db, "global_gain": gain,
                  "pre_gain_sample_peaks": dict(zip(("voice", "effects", "mix"), peaks)),
                  "output_mix_sample_peak": peaks[2]*gain,
                  "voice_rms_before_gain": math.sqrt(energy/total),
                  "true_peak_lufs": "not measured", "warnings": warnings}
        (temp/"audio-report.json").write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
        out.mkdir(parents=True, exist_ok=True)
        for name in OUTPUTS:
            os.replace(temp/name, out/name)
        print(json.dumps({"out": str(out), "duration": duration, "scenes": len(timeline),
                          "global_gain": gain, "warnings": warnings}))


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    cue = sub.add_parser("sfx", help="Generate one deterministic procedural cue")
    cue.add_argument("--type", choices=KINDS, required=True)
    cue.add_argument("--out", type=Path, required=True)
    cue.add_argument("--sample-rate", type=int, choices=(24000, 48000), default=24000)
    cue.add_argument("--replace", action="store_true")
    mixer = sub.add_parser("build", help="Measure clips, emit captions, and stream the audio mix")
    mixer.add_argument("plan", type=Path)
    mixer.add_argument("--out", type=Path, required=True)
    mixer.add_argument("--replace", action="store_true")
    args = parser.parse_args()
    try:
        if args.command == "build":
            build(args)
        else:
            if args.out.exists() and not args.replace:
                raise ValueError("Output exists; choose a new file or explicit --replace")
            args.out.parent.mkdir(parents=True, exist_ok=True)
            with wav_open(args.out, args.sample_rate) as writer:
                writer.writeframes(pcm(synth(args.type, args.sample_rate)))
            print(f"Created procedural {args.type}: {args.out}")
    except (ValueError, OSError, subprocess.TimeoutExpired) as exc:
        parser.exit(1, f"Audio build failed: {exc}\n")


if __name__ == "__main__":
    main()
