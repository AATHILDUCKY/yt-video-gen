# Hyperframes integration

Duckygen controls the film's editorial intent, light sketch identity, palette, typography, researched narration, sound direction and delivery requirements. Hyperframes provides an additional authoring, preview, checking and rendering toolchain. Installing a skill is not installing its CLI runtime, dependencies or proving a video render works.

## Companion instructions

Unmodified CLI and core instruction files are bundled under `companions/hyperframes-cli/` and `companions/hyperframes/`, with Apache-2.0 license and pinned provenance. No global skill installation is required to read these files. Read the [core contract](../companions/hyperframes/SKILL.md) and [CLI router](../companions/hyperframes-cli/SKILL.md) only for a Hyperframes job. Then read only the linked format, explainer, audio or command reference actually needed. Do not load all companion files. The external CLI may evolve; verify installed help/version and preserve the project lockfile when using it. The runtime needs Node.js 22+ and FFmpeg; browser availability must also be checked.

## Choose a route, keep the film identity

For a new editable Hyperframes composition, follow its current root/scene/timeline contract. Use stable clip IDs, actual measured timing and paused registered timelines. Copy Duckygen's selected fonts, assets and final audio into the project using relative paths, with licenses. Explicitly preserve 1920×1080 and 60fps when those Duckygen defaults or the user's brief apply; a companion's 30fps default does not change the brief. Its visual examples and registry components do not override the sketch style or authorize web-like cards and navigation. Adapt reusable techniques to the established art direction.

A `window.seek(t)` Canvas film is not automatically a Hyperframes root composition. Use a documented seekable Canvas adapter and readiness contract if supported by the installed runtime; otherwise keep the bundled Canvas renderer. Do not relabel a plain HTML file as Hyperframes-compatible. For Hyperframes authoring, its registered timeline is the source of truth; expose any `window.seek(t)` preview adapter against that same timeline without creating independent state.

Keep existing reviewed projects on their working renderer unless migration has a concrete benefit. Avoid rendering twice through different engines or rewriting unchanged scenes to satisfy a tooling preference. Check whether the selected Hyperframes version actually supports the requested temporal sampling. If three subframes are required and unsupported, use the bundled three-sample renderer for a compatible Canvas project, or a documented equivalent pipeline. Record the actual path and settings; never claim unsupported motion blur.

## Local production loop

From a valid Hyperframes project, consult each command's help and relevant bundled reference before using flags:

```bash
npx hyperframes lint
npx hyperframes check --json
npx hyperframes snapshot --help
npx hyperframes preview --help
npx hyperframes render --help
```

Fix actual check failures and inspect representative snapshots, important cuts, motion peaks, captions and style continuity before export. A successful command or a report with zero samples is not a visual review. For a complete-video request, continue through a verified local MP4 without inserting a new approval gate. Preserve editable files, the measured music cue map, stems and sources. Inspect the actual encoded output as described in build.md.

The companion also documents cloud rendering, publishing, hosted media generation and feedback. Those capabilities are outside the default local-film route; installing the skill alone does not authorize publication, paid service use or sending project content elsewhere. Use only capabilities within the user's task and existing authorization. Missing optional companions can be installed/read when genuinely needed; their absence does not require abandoning the working local pipeline.

Upstream: https://github.com/heygen-com/hyperframes
Bundled revision and hashes: `companions/hyperframes-provenance.json`.
