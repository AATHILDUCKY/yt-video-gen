# Narration and sound

Inspect installed TTS first; use one suitable neural voice and one set of settings. A connected voice service is acceptable for normal synthetic narration. Retain transcript, voice settings, returned URL and actual decoded audio. Do not assume an HTML playback page is an audio file. A returned preview is a full source clip only if its audio contains the entire submitted phrase; never silently use a truncated preview.

Generate phrase/scene clips, measure durations, and map their actual starts/ends. Keep original recordings. Trim quiet edges with around 30–70ms consonant margins and 3–8ms edge fades. For an observed excessive quiet run, shorten its center and preserve both speech edges. Inspect/listen at joins. A silence detector can remove a quiet fricative if used carelessly; it cannot assign words to time. Do not globally speed speech or apply a gate to hide a slow edit.

Typical tight joins are 100–250ms. Avoid fixed multi-second `min_duration` padding after every scene. If a fixed runtime leaves space, use sourced useful context or an intentional brief visual beat. Do not truncate the last phrase. Narration carries the explanation, captions carry the actual words, and visuals show the mechanism; those three tracks must agree.

## Bundled cues

`assets/soundeffects/generated/` contains deterministic procedural cues: click-soft, tap-contact, paper-turn, marker-write, transition-swipe, zoom-in, zoom-out, reveal-pop, impact-low and resolution-chime. `assets/soundeffects/cc0/` contains selected Kenney interface cues, tactile impacts and a few computer/sci-fi textures with licenses in the adjacent `licenses/` folder. Search the asset index by action with `--kind sfx --limit 5`. Use subtle contact sounds for ordinary mechanisms; glitches and energy/engine textures are optional subject-specific accents, not default transitions. Reuse an existing file before downloading or generating; do not regenerate the bank on each project. Original procedural cues are synthetic, not recorded foley or music. Cache useful new generic effects with the source, settings and reuse terms as described in assets.md.

Cue placement examples:
- Click/tap at a cursor or object contact.
- Marker at the first drawn stroke, not throughout all narration.
- Paper at a fold/turn.
- A short swipe under a directional mask or camera move.
- A restrained low hit at the most important reveal.
- A chime at a resolved mechanism if the tone fits.

Use a few cue families consistently and vary placement/intensity with the action. Not every cut needs a sound; not every change needs music. Speech dominates. The bundled mixer can read a selected cue via its `file` field, ducks effects from measured voice energy, and preserves voice speed. Do not upload external licensed material into the shared bank without provenance and reuse terms.

Music, when requested/appropriate: use an original code score or verified licensed track; record BPM and measure a supplied beat map. Chapter-level tonal/rhythmic evolution prevents a repetitive loop. Compose a beat-led short with OfflineAudioContext if requested. For long speech-led films a subtler bed is often better than a kick under every sentence. Align strong hits to actions without forcing narration onto the music grid.

## Change music with the situation

Write a compact music cue map alongside the measured edit plan: `start/end | story state | bed/stem | transition | intensity | voice ducking`. Implement these cues in the final mixed audio; a label in JSON does not change the soundtrack. Choose the emotional arc from the actual topic rather than assigning suspense to every technology story.

| Story situation | Possible musical direction | Editorial purpose |
| --- | --- | --- |
| Hook or unanswered question | Sparse pulse, short motif, restrained low texture | Establish curiosity without overpowering the first sentence |
| Mechanism explanation | Lower density, steadier soft rhythm, less bass movement | Make room for reasoning and labels |
| Evidence or uncertainty | Reduced percussion, restrained unresolved texture | Invite attention without implying guilt or certainty |
| Escalation or consequence | Add a rhythmic layer or controlled harmonic tension | Support a meaningful increase in stakes |
| Distinction or correction | Brief musical space, then a clearer arrangement | Give the key contrast room to land |
| Resolution or takeaway | Resolve the motif, warmer voicing, reduced tension | Provide closure that matches what the evidence supports |

Keep a shared motif, timbre or compatible key so these changes belong to one film. A situation change may call for a different bed; a change of texture or instrumentation can be enough when the scene still belongs to the same section. Avoid restarting a stock loop every 3–5 seconds. Place musical transitions at the relevant spoken turn and a compatible phrase boundary. Use an audio crossfade, short bridge or intentional cut based on the music; audio crossfades do not authorize visual crossfades. For composed music, preserve rhythmic phase and avoid discontinuities. Leave reverb/effect tails room without padding the narration timeline.

Under a dense explanation, lower musical complexity as well as level. Keep transitions free of sudden bass/volume jumps, and duck music and effects under voice. Preserve separate stems and license/source notes. Listen across music changes when supported, and measure the final encoded mix after changes. Do not report a cue-map review as a listening pass or claim a licensed track can be cached for redistribution without checking its terms.

The mixer reports sample peaks, not LUFS/true peak. Measure the actual encoded delivery with FFmpeg loudnorm when needed. A useful spoken-video starting target is around −16 LUFS integrated with headroom, adjusted by actual material; do not claim a loudness result from metadata or impose normalization without checking the mix. Avoid clipping/masking and excessive pumping. Preview player and export must use the same final mix. A decode, waveform analysis or running ffplay without audible access is not listening.

For the final channel CTA, follow [ending.md](ending.md). Measure and include the spoken subscribe line within the requested runtime. Carry an appropriate resolution arrangement under it, duck for intelligibility, and let the music land briefly after the final word. Keep the narrator and musical identity consistent; do not tack an unrelated jingle or a silent outro onto an otherwise tight film.

## Audio-plan format

```
{
  "sample_rate": 24000,
  "voice_gain": 1,
  "duck_db": 8,
  "tail": 0.35,
  "scenes": [
    {"id":"request", "text":"The browser sends the request.",
     "voice":"narration/request.wav", "pause_after":0.16,
     "sounds":[{"offset":0.4,"file":"assets/soundeffects/generated/click-soft.wav","gain":0.1}]}
  ]
}
```

All input paths are local and relative to the plan. Each scene has an actual nonempty voice clip. Optional `min_duration` is a conscious silent hold, not speech stretching. Cues use either `file` or a built-in `type` (click/tap/swipe/paper/marker/chime). Offsets are scene-relative and mark onset. Save outputs in a separate folder:

```
python3 <skill>/scripts/explainer_audio.py build project/audio-plan.json --out project/audio
```

Outputs: voice/effects/soundtrack WAVs, narration.txt, phrase-level captions.srt, timeline.json and audio-report.json. Rebuilding generated outputs uses `--replace`; preserve the input clips. Music can be mixed after this step, with fresh loudness/peak checks and the browser mix rebuilt. The helper streams blocks and caps each job at ten minutes; use measured chapter jobs and offset their timelines/captions for longer films rather than silently discarding the rest.
