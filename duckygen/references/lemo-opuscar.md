# Lemo-Opuscar integration and Codex adaptations

Use when a Lemo style, modern animated explanation, style exploration or a useful Lemo production technique is requested. The [Codex adapter](../companions/lemo-opuscar/SKILL.md) is the entrypoint. The library is pinned to `bebbbe1aa92a3cb4bb6f83500e61b23a17d1aa00`; `upstream.json` retains source hashes. The published catalog has 66 styles plus an upstream authoring template; gallery videos, stills, demo voices, sample instruments and models are excluded.

Search locally with `python3 <skill>/scripts/lemo_library.py list <query>`. Read the chosen STYLE.md and only the directing/technical sections relevant to the work. For a user's custom look, adapt a compatible style's grammar rather than claiming an altered palette/material is an exact reproduction. A prompt is inspiration and instruction, not evidence of successful reproduction by Codex.

## What changes for this workflow

| Upstream convention | Codex / Duckygen adaptation |
| --- | --- |
| Claude plugin commands and AskUserQuestion | Use available Codex tools. Existing requests/defaults answer routine choices; clarify only material missing information. |
| Setup clone, automatic fetch/reset and eager installs | Use the bundled pinned library. Reuse local tools; add a scoped dependency only when the chosen implementation needs it. Never run upstream bootstrap implicitly. |
| 30–60s and generally 24fps | Preserve the user's brief. Duckygen defaults remain 16:9, 1080p60; measured narration determines unspecified duration. |
| Fixed style invariants and extensive choice gates | Keep the requested art direction; the user explicitly wants a modern educational adaptation. State a chosen treatment and proceed. |
| Score grid drives all cues | Measured speech and learning events lead educational timing; music supports them. Keep a single synchronized timeline. |
| Sound on every action, camera/silence quotas, fixed reading holds | Use purposeful foley, framing and reading time appropriate to the mechanism. Do not fill quotas or drown the voice. |
| Simplified motion/springs in visual demos | Use aesthetic easing only for editorial motion. Quantitative physical motion comes from checked laws and initial conditions. |
| Frame contract READY/render/DUR | Keep seek/motionFilmReady/filmConfig for the bundled renderer, or adapt all readiness/clock/canvas contracts explicitly. Never merely rename globals and assume a valid render. |
| Lemo Three.js r170 and post effects | Preserve compatible runtime versions per project. Duckygen's bundled engine is a separate version; do not mix post-pass imports across versions without checking APIs and output. |
| Mux may pad/cut audio to picture | Measure the full final narration and CTA first. Do not truncate speech to satisfy runtime. Keep identical mix sources for preview/export. |
| Full playback/listening review | Perform supported checks and clearly record what was actually viewed/heard. ASR does not prove pronunciation or mix quality. |

The upstream source documents are kept unchanged with renamed instruction entrypoints so they do not silently govern unrelated workspace work. Updates require choosing a new revision and reviewing adapter compatibility; no automatic update runs on a film request. Custom project assets and user styles are never reset by this integration.

## Technique reuse and rights

Plan the learner's question and original treatment first. STYLE.md supplies visual grammar; demo code supplies implementation ideas, not the story, scientific answer or proof. `lemo_library.py fetch-demo` downloads a selected demo's source at the pinned revision into `<project>/lemo-reference/<slug>/`; inspect it before running or copying it. It excludes media/binary assets, preserves a license notice and provenance, and refuses to replace differing files.

Code/docs: MIT, copyright LemoLab. Demo films/stills: CC BY 4.0 with LemoLab attribution and change notice; several demo voice tracks are excluded and must not be reused. Individual assets keep their own terms. The default integration downloads none of those media. A new film made using original content and library techniques does not require a Lemo watermark. Retain the MIT notice for copied code and record actual third-party assets in SOURCES.md.

Source and license details: https://github.com/lemomo-ai/lemo-opuscar . This adaptation is bundled with Duckygen; it does not install or publish a Claude plugin.
