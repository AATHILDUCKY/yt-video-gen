# Reusable asset bank

The bank contains original tech/action icons, larger sketch props, connectors, cached procedural cues, selected CC0 third-party sounds, six complementary font families and a motion runtime. Use the index for current counts. `assets/catalog.html` is a visual/audio contact sheet. `assets/index.json` is the machine-readable source/tag/hash index; do not paste the whole index into context. Read only relevant candidates:

Named companies use their authentic logo together with their name, not the generic company avatar. Follow [brands.md](brands.md) for official sourcing, brand colors, film placement and selective logo caching. Generic actors and hardware remain palette-matched illustrations.

```
python3 <skill>/scripts/asset_tool.py search 'browser request security' --limit 6
python3 <skill>/scripts/asset_tool.py search 'paper' --kind sfx
python3 <skill>/scripts/asset_tool.py copy props/browser-window icons/shield connectors/arrow-curve-right sfx/click-soft --project ./my-film
```

The copy command copies selected assets into the project's assets folder and appends source records to `asset-manifest.json`. Hashes detect accidental changes. Assets with different bytes are not overwritten. Read `assets/PROVENANCE.md` and preserve every selected font's OFL through its `license_files` record. Choose families by editorial role using [typography](typography.md) and `assets/fonts/families.json`. The bank includes explicitly licensed contextual photos; it does not include a generic collection of product logos or cloned reference characters.

Sound files live in `assets/soundeffects/cc0/` and `assets/soundeffects/generated/`; their stable IDs remain `sfx/<name>`. The copy command also includes each selected asset's `license_files`, and its manifest preserves origin, reuse terms, source URL and audio metadata when present. Preserve these records when delivering a project. CC0 sounds may be reused, modified and redistributed; check a newly sourced asset's actual terms before caching it. A free preview or download alone does not grant redistribution rights.

Original vector drawings use charcoal on transparent backgrounds. Apply coral or optional green selectively through an SVG stroke treatment or colored drawing layer, preserving readable ink/paper contrast. Keep line irregularity stable at arbitrary timeline times. Recolor original illustrations to the palette; preserve authentic UI/evidence meaning when it needs real brand/status colors. A generated photo cannot be made truthful evidence by adding a sketch filter.

Prefer the prop versions for close-ups; tiny 24-unit icons should not do the explanatory work of a full scene. Select assets for actors and mechanisms. For example, a request may use browser, packet/transfer, boundary and server; a news update may use a dated document, comparison and source excerpt. Do not add all 64 icons as decoration.

For computer/server explanations, search the layered hardware props before creating anything: `desktop-computer`, `computer-tower`, `dual-monitor-workstation`, `laptop-open`, `laptop-closed`, `server-blade`, `data-center-racks`, `network-router`, `network-switch`, `cpu-processor`, `gpu-card`, `external-drive`, `smartphone-device`, `tablet-device`. The original `laptop-workstation` and `server-rack` remain available. Use only the relevant objects, preserve their layer groups for motion, and scale any indexed attachment anchors from their declared coordinate space.

## Persist new reusable assets

When a new asset is genuinely needed, create it once, use it in the project, then cache the reusable original inside this skill. Use descriptive subject/action names, not `image1` or a previous video's title. Save source/license information at creation time. Use the image-generation skill/tool for appropriate raster artwork and inspect the result; use native SVG/Canvas for exact diagrams/icons.

```
python3 <skill>/scripts/asset_tool.py cache ./my-film/assets/semantic-search-index.svg --name semantic-search-index --kind props --tags search index knowledge --source 'Original SVG authored for the project' --license 'Original generated artwork; reusable in generated projects'
```

Cache accepts local SVG, PNG, JPEG, WebP and WAV. It reuses identical hashes and versions a different existing name. Keep brand/customer-specific material in its project unless reuse is authorized. Reject external-script/remote-reference SVGs rather than embedding them blindly. If writing the installed bank requires filesystem permission, follow that environment's access check; stage the update in the project when unavailable. Do not make a future film depend on an inaccessible shared cache path: copy/inline selected assets into the project.

For every new useful generic sound, cache the finished 16-bit mono/stereo PCM WAV after inspection. Record the generator/provider and settings or source recipe in `--source`; retain any provider restrictions in `--license`. Do not relabel generated audio as CC0 unless it was actually released that way. `--source-url` and `--license-file` retain an external source and its license when applicable. Do not cache unusable drafts, private narration or duplicates.

```
python3 <skill>/scripts/asset_tool.py search 'zoom reveal' --kind sfx --limit 5
python3 <skill>/scripts/asset_tool.py copy sfx/kenney-maximize-001 --project ./my-film
python3 <skill>/scripts/asset_tool.py cache ./my-film/assets/soft-page-fold.wav --name soft-page-fold --kind sfx --tags paper fold transition soft --source 'Original procedural effect; record synthesis recipe/settings here' --license 'Original procedural audio; reusable in generated projects'
```

Sound caching measures duration, sample rate and channels, deduplicates by content hash, and stores new files in `soundeffects/generated/`. Search a handful of candidates first; only fetch or generate when no cached effect fits. This saves tokens, downloads and synthesis work without adding unnecessary sounds to the film.

`build_asset_bank.py` is a maintenance/recovery script for the original bundled bank, not a normal generation step. Custom indexed assets are retained. Do not regenerate unused drawings/cues or download a new icon package on every run.

After changing the shared bank, run `python3 <skill>/scripts/validate_assets.py`. It checks file integrity/provenance and XML/WAV structure, not artistic quality. Refresh the catalog with `scripts/build_catalog.py` only when its contents change; this does not regenerate any asset. Curated v2 props are preserved by the generic bank builder. Their dedicated source is `scripts/build_refined_props.py`; follow [asset-style.md](asset-style.md) for new artwork.

## Actors and public image assets

`assets/avatars/` contains generic person, anonymous hacker/attacker, developer, organization, company and bot illustrations. `assets/illustrations/` contains team, security, cloud, server, database and laptop artwork. Each has a compact transparent 512×512 PNG and editable `-vector` asset ID. These use Duckygen's palette and organic sketch backplates, incorporating MIT-licensed Tabler icon geometry. Upstream SVGs are retained in `assets/sources/tabler/`; license and import revision/hashes are recorded locally. They are role illustrations, not photographs of real people or authentic company logos. Avoid implying a real person's guilt through a generic attacker illustration.

```
python3 <skill>/scripts/asset_tool.py search 'developer bot company' --limit 5
python3 <skill>/scripts/asset_tool.py copy avatars/developer-coder avatars/bot-assistant illustrations/server-infrastructure --project ./my-film
```

Use PNGs for small/medium actor cutouts; prefer the indexed SVG variant for a large zoom or when its vector layers need separate animation. A PNG is a single image, not a rigged character. Keep selected actors visually consistent; avoid filling a shot with avatar tiles or adding generic faces as decoration. Crop/position them on the film stage rather than building a website-like card grid.

For genuinely missing artwork, reuse a matching vector when exact geometry matters; use image generation for appropriate new bitmap illustrations. Generate only the needed size/variants, inspect once, optimize file size, and cache the reusable result with descriptive tags and actual source/license. `--kind avatars` is available for actor PNG/SVGs. Copy selected files into the project rather than embedding the entire bank. A file's small byte size does not reduce its model image-input token cost: search tags first and inspect a small contact sheet of candidates instead of repeatedly opening full-resolution art.

When researching public images, follow the source to its actual license; public availability or a Google Images result is not permission to redistribute. Prefer explicit public-domain/CC0/MIT/OFL or other compatible licensed sources, retain attribution and modification notices when required, and cache only where redistribution permits it. Avoid bulk downloading stock images, brand marks or photos unrelated to the current explanation. Original source: https://github.com/tabler/tabler-icons ; license: `assets/licenses/tabler-icons-MIT.txt`.

## Context photographs

The `photos/` records include real author/source/license information and copy their credit files with the selected image. Use `attribution_text` plus the license URL and any actual edit note in the film's source ledger and YouTube credits. Photo resizing/cropping does not make a real setting evidence of a specific event. Keep photos as optional context within the light sketch film, not a competing random visual style. For a newly cached public photo, use `--kind photos`, `--source-url`, `--license-file` and `--attribution` with the actual terms. Do not infer public-domain status merely because an image is downloadable.

## Model and context efficiency

Use the available capable model to make the story, asset and motion decisions; use deterministic scripts for copying, hashing, timing, mixing, formatting and encoding. Do not make speculative claims about model prices or silently select paid services. Reuse measured audio, reviewed unchanged scenes and indexed artwork. Keep one authoritative shot/cue plan, read only relevant references and a handful of asset results, and patch affected sections rather than rewriting the whole film. A larger model or more generated variants does not replace actual visual review.
