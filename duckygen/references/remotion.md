# Remotion route for Duckygen documentaries

Use Remotion for a requested React/Remotion project, an existing Remotion composition, or when its reusable components materially help the film. Keep an existing working Canvas/Three.js project on its current renderer unless the user requests migration. Installing guidance does not install the video runtime.

The pinned upstream bundle is in [companions/remotion-best-practices](../companions/remotion-best-practices/). Its router is [remotion-best-practices/SKILL.md](../companions/remotion-best-practices/remotion-best-practices/SKILL.md). Load only the focused creation, markup, captions, rendering or interactivity reference needed. Upstream source revision and file hashes are in `upstream.json`; retain original instruction files and notices.

Duckygen controls research, factual qualifications, the established sketch identity, measured narration, source credits and delivery. A brief explicitly requesting a finished MP4 authorizes rendering: the companion's preview-first default must not leave that request unfinished. Studio is useful for review, not a replacement for export.

For Remotion, use `useCurrentFrame()` and `useVideoConfig()` as the sole visual time source. Express local scene timing in frame offsets, retain absolute-time resets for Three.js, and avoid advancing clocks, CSS animations or accumulating simulation state. Await fonts and images through Remotion's documented readiness APIs; keep captions as crisp 2D overlays.

Set `fps`, dimensions and `durationInFrames = round(seconds * fps)` from the brief. Measure narration first, edit the script or quiet joins as needed, and retain speech at 1×. Use the final measured caption times and the same mixed soundtrack in preview and export. Copy only selected assets, fonts and licenses into the project; do not depend on paths inside an installed skill.

Use installed compatible Remotion packages before adding dependencies. Keep package versions consistent and retain a lockfile. Do not migrate active productions or add a framework merely because a companion is available. Verify actual temporal sampling support before claiming motion blur: a 60fps export alone is not a three-sample master.

Inspect actual stills and motion, then export locally through the project's documented Remotion render command. Verify H.264/AAC, requested frame count and runtime, full decode, audio levels and browser playback. Deliver the MP4, editable project, narration, captions, audio stems, sources, metadata and honest review limits. Reuse reviewed unchanged media for scoped revisions, and use atomic output replacement so a failed render cannot destroy the previous master.
