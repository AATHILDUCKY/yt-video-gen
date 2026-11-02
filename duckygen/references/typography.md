# Choose typography like an editor

Select type for the video's tone, viewing size and information, rather than changing fonts just to create activity. Use one primary family for captions and explanations, then add a supporting face when it has a clear job. Two families usually suffice; reserve an additional mono or annotation face for a specific need. A user's brand typography takes priority when available and licensed.

| Family ID | Editorial purpose | Use carefully |
| --- | --- | --- |
| `manrope` | Friendly, clear tech explanations; readable captions; geometric figures | Default, not mandatory for every video |
| `inter` | Neutral interface explanations, dense labels and factual narration | Keep label density low enough for phone viewing |
| `barlow-condensed` | Strong news hooks, short headlines, large financial figures | Avoid long sentences or small condensed captions |
| `ibm-plex-mono` | Actual code, commands, identifiers and technical data | Do not make a whole film look like a terminal; never fabricate logs as evidence |
| `fraunces` | Reflective editorial titles, attributed quotations, human consequences | Use sparingly; prefer the primary sans for reading captions |
| `caveat` | Short hand-drawn notes, circles/arrows with a few explanatory words | Not for subtitles, dense labels, precise numeric comparisons or long reading |

Useful pairings: Manrope + Barlow Condensed for an energetic tech-news film; Inter + IBM Plex Mono for a code mechanism; Manrope + Caveat for a sketched walkthrough; Inter + Fraunces for an editorial story. These are examples, not fixed templates. Keep each face's role stable across shots and chapters. Use weight, size, spacing and line breaks before adding another family.

## Timing and legibility

Keep subtitles in a stable, readable primary face. At 1080p, start around 36–46px for captions and 26–32px for essential labels, then inspect at phone viewing size. Limit lines and text volume to actual reading time. Align baselines and margins deliberately. Measure with `ctx.measureText()` after the actual face is ready; wrapping and safe bounds change with the font. Do not stretch letters horizontally to force a fit or use synthetic bold when a real bundled weight is available.

Choose tabular figures for changing counters when supported, or a mono role when aligned technical data needs it. Avoid needless letter animation under a complex spoken explanation. Reveals should expose a readable word, land its emphasis and leave enough time to understand it. Keep directional motion blur on moving graphic layers while preserving readable captions.

## Reuse and embedding

`assets/fonts/families.json` is the small selection catalog. Individual font records are searchable through `asset_tool.py search '<role>' --kind fonts --limit 5`; do not load all font bytes or the complete asset index into context. Use cached fonts instead of downloading them for every film. The selected upstream files are unmodified OFL fonts. The index records hashes, family names, real weight ranges, source revisions and licenses.

The project initializer supports:

```bash
python3 <skill>/scripts/create_project.py --output ./my-film --title 'A clear explanation' --duration 120 --font manrope --heading-font barlow-condensed
python3 <skill>/scripts/create_project.py --output ./code-film --title 'How authorization works' --duration 180 --font inter --accent-font ibm-plex-mono
```

It copies and embeds only the selected families, preserves their licenses and manifest records, saves `typography.json`, and exposes roles through `filmConfig.typography`. Its `type(..., role)` helper defaults to `heading`; captions use `body`, and authors can explicitly use `accent` for a code snippet or annotation. The scaffold remains a demo until the actual story replaces it.

Await selected `FontFace` loads in `window.motionFilmReady` before measuring or capturing frames. A rejected load must fail the render rather than silently changing text metrics through a system fallback. Keep project-local font files and licenses even when their bytes are embedded in HTML. Preserve the chosen family name and real variable/static weight ranges. A new font should be added only when the existing set cannot serve the brief; retain its actual embedding/redistribution license and source, and inspect representative glyphs in the target language.
