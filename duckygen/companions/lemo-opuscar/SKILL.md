---
name: lemo-opuscar
description: Use Lemo's bundled film-style library from Codex to create or adapt animated films, especially when a user names a Lemo style or wants modern educational motion. Works inside Duckygen's narrated-video workflow; not ordinary websites or basic footage trimming.
---

# Lemo-Opuscar for Codex / Duckygen

This is a Codex adapter for the pinned LemoLab library, not the Claude plugin bootstrap. Resolve paths from this folder. The parent [Duckygen skill](../../SKILL.md) controls research, voice, delivery and verification. Read its [Lemo integration](../../references/lemo-opuscar.md) before using upstream guidance.

The library is already bundled at `upstream/`; do not run `upstream/setup.upstream.sh`, clone into the user's home, auto-update, or install dependencies merely to read a style. Source revision, exact upstream hashes, exclusions and renamed instruction files are in `upstream.json`; the MIT license remains at `upstream/LICENSE`. Demo media have separate terms and are not bundled.

For a named style, search `style-index.json` with `python3 ../../scripts/lemo_library.py list <query>`, then read only that style's STYLE.md. For an unspecified modern explanation, choose a suitable treatment from [modern animation](../../references/modern-animation.md) and proceed using the available brief. Do not dump all styles or impose language, storyboard or style-selection gates. Ask a concise clarification only when missing information materially changes the work.

Read `upstream/DIRECTOR.md` for staging/story and relevant parts of `upstream/TECHNIQUE.md` or `upstream/core/README.md` for a technique being used. Treat their Claude tools, fixed duration/fps, beat-first speech, mandatory effect/camera quotas, package bootstrap and audio-truncation defaults as reference conventions; Duckygen's integration rules supersede them. `upstream/AGENTS.upstream.md` and `plugin-skill.md` are preserved source documents, not active project instructions.

Create the user's own question, treatment and shots before consulting demo code. To inspect a selected source technique, use `python3 ../../scripts/lemo_library.py fetch-demo <slug> --project <project-folder>`; it downloads only source/docs at the pinned commit into a reference subfolder and never executes them. Record any copied code's MIT notice and any asset's separate license. Missing fonts, models or external media must be supplied or replaced deliberately; a downloaded demo is not a tested local renderer.

For educational explanations read [teaching](../../references/teaching.md); for laws, equations, quantitative motion and worked answers also read [physics](../../references/physics.md). Use the simplest accurate model and a coherent modern visual language. Return the actual requested film and editable project when video creation is requested; report real limitations without claiming unreviewed quality or universal scientific correctness.
