# Duckygen editorial sketch asset standard

Use `assets/previews/props-v2.png`, `assets/previews/hardware-svg-pack.png` and the actual v2 prop SVGs as the visual reference for new icons and props. Keep the paper/charcoal/coral identity with restrained green where it communicates a real status. Use the existing curated drawing before generating another variant.

Icons use the v3 detailed family shown in `assets/previews/icons-v3-0.jpg` and `icons-v3-48.jpg`. Preserve their stable IDs, named layers and 128×128 coordinate space. Hardware miniatures use the same object language as the props; compact abstract symbols use quieter semantic details and selective coral strokes. Use `scripts/build_detailed_icons.py` only for deliberate maintenance. Avoid adding tiny decorative marks that become noise at delivery size, and prefer a prop or purposeful 3D shot for a complex explanation.

## Shape, stroke and detail

Start with a clear silhouette, correct proportions and one readable idea. Props should look good as large objects on a film stage: selective paper fills, a few coral planes, subtle flat offset depth and clean internal details. Avoid the old single thin path repeated with a noisy offset; do not add random jitter, gradients, glow or a card around every object. Use imperfect outer contours deliberately while keeping screens, repeated slots and structural alignments coherent. The same object should have consistent perspective.

The v2 props use a roughly 320×260 drawing space, main ink strokes around 3.2 units, detail strokes around 2–2.7, rounded caps and joins, and a restrained 12% flat shadow. Icons use a small regular grid with clear strokes around 1.65 units at 24-unit scale. These are starting proportions, not mandatory dimensions: inspect their actual appearance at delivery scale. Avoid isolated details thinner than a pixel at their intended size. Do not mechanically add a shadow or accent if it weakens recognition.

Keep meaningful vector layers in named groups: `shadow`, `body`, `detail`, `accent`; add semantic subgroups when an action needs them. Keep highlights and controls attached to the body during transforms. Use explicit fills/strokes and a padded viewBox with no clipped edges. SVG assets must be self-contained, free of embedded scripts/remote dependencies, and reconstruct identically at any requested time. Avoid faux UI paragraphs or invented dashboards inside device props; abstract screen content is an illustration, not product evidence.

Use filled regions selectively to create hierarchy. Keep real logos, token marks, diagrams and geographic geometry faithful; improve staging and line readability without distorting their meaning. An asset's accent is not automatically a success/failure state. Keep status colors consistent with the film's art direction.

## Motion readiness and review

Inspect at thumbnail size and at the largest planned camera zoom. Check silhouette, contrast, safe margins, inconsistent perspective, loose lines, accidental joins and clipped detail. For a pointing or packet interaction, derive anchors from the visible shape bounds in the active coordinate space; do not rely on an icon's padded viewBox edge as its physical boundary. A flat PNG supports object motion but not separately animated limbs or controls; use layered SVGs when those parts must move.

The curated originals are rebuilt with `scripts/build_refined_props.py`; their indexed `style_revision: 2` prevents the generic maintenance builder from replacing them with the earlier thin-line versions. This is maintenance, not a step on every video job. Do not update already-delivered video assets implicitly; copy reviewed assets into each project and preserve their hashes.

The extended hardware set is authored in `scripts/build_hardware_props.py`. It includes desktop/tower/dual-monitor computers, open and closed laptops, server blades/racks, networking hardware, CPU/GPU/storage, phones and tablets. Generic device screens remain abstract. Named subgroups support screen, fan, port, indicator and other relevant motion. Hardware index entries provide attachment anchors in a 320×260 coordinate space; convert them through the object's transform and camera. Keep each SVG's IDs unique, and prefix IDs when combining multiple inline SVGs into one document.

For new images, choose native SVG/Canvas for precise props, mechanisms and icon families. Use image generation for bitmap artwork that actually benefits from it, then match the established visual language, inspect and cache the useful output. Search indexed assets first, generate one useful candidate rather than many speculative variants, and keep only the needed resolution. Public photos are contextual/evidentiary material with their own credit requirements, not a replacement for this illustration style.
