# Portable project and render workflow

The package includes its own scaffold, palette, original assets, font, motion helpers, measured audio mixer and 60fps renderer. Reuse installed Python/NumPy, Node/Playwright, Chrome and FFmpeg; inspect availability before installing anything. `PLAYWRIGHT_MODULE`, `CHROME_PATH`, `FFMPEG_PATH` and `FFPROBE_PATH` are optional environment overrides. Do not bundle node_modules, voice models or a browser into the ZIP.

For Hyperframes authoring/rendering, use [hyperframes.md](hyperframes.md) and the bundled companion contract instead of assuming this Canvas scaffold is already a valid Hyperframes composition. Preserve the brief's resolution, fps, narration and sampling requirements whichever route is selected. Keep the art direction and music cue map in the project plan and review their implementation in actual frames/audio.

## Author

```
python3 <skill>/scripts/create_project.py --output ./my-film --title 'The real topic' --duration 180
```

Set runtime from the measured narration; 180 is an example, not a rule. The scaffold allows longer work up to two hours per initialization; for larger jobs build chapters rather than allocating a huge single render. A short explicitly beat-led job can use `--mode beat-led --duration 15 --bpm 120`. The scaffold is marked `isDemo:true` and the project manifest `is_demo:true`; both must change only after its sample story/copy is replaced.

Use `--font manrope --heading-font barlow-condensed` or another intentional pairing from [typography](typography.md). `--accent-font ibm-plex-mono` adds an optional code/data role. Omitting supporting fonts keeps one family. Selected files and licenses are copied into project assets and embedded, role choices are recorded in `typography.json`, and font loads are awaited before rendering. Choose fonts for the brief rather than rotating them between scenes.

The resulting HTML embeds the font, selected SVG assets, shared motion helpers, data and drawing code. Source copies stay in project/assets for editing/reuse, with provenance in asset-manifest.json. Browser player controls appear only via watch.html / film.html?player=1. Export uses the plain film.html and contains only the full 1920×1080 canvas.

Implement the actual topic in `drawFilm(t)` and store authoritative shots/captions in embedded `film-data`. Expose `window.filmShots` with measured start/end and `window.filmReviewTimes` for optional peak-motion samples. Keep drawing deterministic and wait for fonts/images through `window.motionFilmReady`. Newly generated assets must be copied into project/assets and then selectively inlined/loaded with readiness checks. Do not leave references to the skill's installed folder inside the delivery project.

The sample `drawAsset(id,x,y,w,h,{progress,ink})` supports revealed drawings and charcoal/coral/green variants; use masks deliberately. Runtime helpers are in assets/runtime/motion.js. Keep editing JSON/runtime source readable and avoid copying a framework into the output for simple diagrams.

## Narration, cues and long films

```
python3 <skill>/scripts/explainer_audio.py build my-film/audio-plan.json --out my-film/audio
```

See audio.md for the plan. For more than ten minutes, build manageable chapter jobs (under ten minutes each) and join their measured stems/timelines:

```
python3 <skill>/scripts/merge_chapters.py my-film/ch01/audio my-film/ch02/audio --out my-film/assembled-audio
```

The joiner streams voice/effects/soundtrack WAVs at 1×, offsets all phrase/cue times, and rebuilds SRT/narration. Matching stems must have the same sample rate/channel format, and each stem must match its chapter duration. It does not align words, remove chapter pauses, normalize loudness or add music. Use short intentional tails at chapter joins. Inspect/loudness-check the actual joined mix.

When adding music/mastering, keep the final mix length on the renderer's 60fps grid and preserve the last spoken phrase. Add that final mix to the player, for example as audio/playback.m4a derived from soundtrack.wav; use the same source in export. The sample OfflineAudioContext score is a demo/short-bumper starting point, not narration or a finished long-film music bed. Do not deliver its effects-only export as a completed narrated explanation.

## Preview and inspect

```
node <skill>/scripts/render_film.cjs my-film/film.html --preview --subframes 1
```

Long narrated projects use `filmConfig.reviewMode='shots'`: capture shot entrances, short settled entrances, interiors, outgoing frames, first/last frames and optional review times. This avoids thousands of redundant beat thumbnails while still covering the cuts. A beat-led short uses `reviewMode='beats'` and captures every beat. Inspect the images/contact sheets. Check real composition changes, spatial/caption bounds, object contacts and the handoff between adjacent shots; fix failures before asserting review. Metadata alone is not a visual review.

```
node <skill>/scripts/render_film.cjs my-film/film.html --reviewed --subframes 3 --audio my-film/audio/soundtrack.wav --output my-film/final.mp4
```

Three samples per output frame are averaged in disjoint triplets with FFmpeg tmix. The renderer probes actual tmix lead-in behavior, preserves 60fps output count, and checks random-access determinism and fresh HTML review hashes. For sharp graphic direction or an efficient draft, explicitly choose `--subframes 1`; do not mislabel its blur quality. It captures the canvas losslessly, or falls back to a browser surface for non-Canvas work. Audio must match the film length within 50ms; rebuild/pad measured audio rather than silently truncating it. No `--allow-demo` in a real final export; that flag is for explicit pipeline tests only.

For portable direct-file playback, inline or copy every selected local asset, use relative audio paths, and await image/font readiness. A single HTML file can embed a compressed narration mix if explicitly required; avoid embedding uncompressed stems plus duplicate base64 audio. Keep source WAVs for editing outside the browser payload.

## Final review

```
python3 <skill>/scripts/audit_pacing.py my-film/edit-plan.json --max-shot 5 --max-gap .65
ffprobe -v error -show_streams -show_format -of json my-film/final.mp4
ffmpeg -v error -i my-film/final.mp4 -f null -
```

edit-plan.json has `shots` and measured narration `phrases`, each with start/end. The audit flags metadata holds/gaps; inspect narration-only quiet runs separately. Treat flags according to editorial intent, not as universal laws. Decode the actual file and inspect representative encoded frames, first/last, transitions, captions and audio. Check actual AAC loudness/peaks when needed, and listen when supported. Do not claim subjective listening from ffprobe, waveforms or metadata.

Record source cutoff, asset provenance, voice origin/settings, render sampling and actual review limits. Deliver final.mp4, editable project, narration.txt, captions.srt, SOURCES.md and concise verification. For multi-chapter renders, preserve shared fps/resolution, exact global offsets and original-speed audio; check joins after concatenation rather than assuming separate successful exports imply a correct final film.

If a long render is interrupted before MP4 finalization, keep the incomplete temporary file out of delivery. Recover with bounded frame ranges using the original absolute scene clock and the same temporal sample positions. Preserve font/asset readiness and the review-hash guard for each range. Finalize every segment, concatenate compatible video streams without re-encoding, and encode the complete mixed soundtrack once. Inspect decoded frames immediately before, at and after each join, then verify the complete duration, frame count, decode and audio again. Replace the final master atomically after the complete output passes.
