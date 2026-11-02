# Three.js for the important explanatory moment

Use a short Three.js visualization when spatial relationships, hidden layers, routing or staged state changes explain something more clearly than a 2D diagram. Place it where the audience reaches the key mechanism, often in the middle of the film after the actors/problem are established. It is a storytelling tool, not a required decorative interlude. If a simple diagram communicates the point better, keep it 2D.

Good tech/cybersecurity uses: a request crossing an authorization boundary; a packet traversing network segments; a key unlocking the correct layer; storage or hardware layers separating to reveal their roles; a queue moving through compute stages. Show one main cause and consequence at a time. A simplified teaching visualization is not a validated simulation, exploit replay, real traffic capture or evidence of an incident. Label illustrative reconstructions and preserve uncertainty.

## Keep the Duckygen look

Carry the same packet, key or other through-line object from the sketch scene into 3D, then back to the next shot. Preserve paper `#FAF9F6`, charcoal `#292C27`, coral `#D76A4E` and purposeful green `#17684F`. Prefer orthographic/controlled perspective, matte or flat-shaded geometry and clear silhouette edges. Avoid a glossy neon style change, arbitrary spins, particles and dramatic camera orbits. Move the camera only to reveal the relation being explained.

Use simple geometry and a few objects. Establish source, boundary and destination, then animate the causal step. Reveal layers selectively instead of exploding everything at once. Freeze or simplify secondary activity while the important change lands. Labels and speech-timed captions remain sharp 2D overlays with stable reading positions. Synchronize contact sounds and musical intensity to actual changes; do not add a whoosh to every camera move.

## Reusable local implementation

The package caches Three.js 0.187.0 module/core files and its MIT license in `assets/runtime/vendor/three/`; pinned source and hashes are in `provenance.json`. Only copy these files when a project uses 3D. Do not download/install Three.js repeatedly or embed the full engine into ordinary 2D videos.

`assets/runtime/three-visualizer.mjs` exports `createAuthorizationVisualization(THREE, options)`, returning `canvas`, `seek(t)`, `dispose()`, `scene` and `camera`. It is a small original teaching example: an unapproved request stops, authorization changes, and that request proceeds to the server. Adapt the mechanism and labels to the researched subject; do not treat its gate as a literal depiction of every security system.

Create a self-contained silent authoring demo with:

```bash
python3 <skill>/scripts/create_three_demo.py --output ./three-mechanism-study
```

The demo is marked `isDemo:true`, has no narration/music and is not a completed explainer. It embeds the pinned modules with blob-module imports so the offline HTML does not depend on a CDN. It exposes `window.motionFilmReady` and `window.seek(t)` and composites an offscreen WebGL canvas into `canvas#film`, which the bundled renderer captures. Preserve Three.js/font licenses in delivered projects.

## Deterministic integration

Create geometry/materials once, await required modules/assets, then calculate every transform, visibility, state and camera property from the requested absolute shot time. Do not use Clock/Timer, animation loops, accumulated deltas, unseeded randomness or advancing physics during export. For animated models, use a documented absolute-time sampling/reset strategy and verify random access; ordinary `mixer.update(delta)` playback alone is not a deterministic export contract. Dispose geometry, materials, textures and renderer when finished.

For synchronous Canvas export, render the WebGL scene inside `seek(t)` before copying it to the 2D film canvas. Use a capture-compatible drawing buffer and pixel ratio 1 for exact export dimensions; preserve the buffer only where this integration requires it. Wait for fonts/media before capture. In a Hyperframes composition, adapt the scene to its registered seekable timeline rather than running a separate live loop. The selected runtime must still satisfy the requested fps and motion-blur sampling.

WebGL availability varies by browser/GPU. Test the target environment. The sample was checked with headless Chrome using its software WebGL support; do not claim GPU acceleration from that test. If 3D is unavailable, make a clear equivalent 2D mechanism or report the actual blocker instead of delivering blank frames.

## Review

Inspect setup, action, boundary contact, state change, arrival, peak camera motion and the return to 2D. Compare the same timestamp after earlier and later seeks; capture results must match. Check 3D labels against actual projected positions, prevent geometry from obscuring key information, and inspect at phone size. Then review the actual encoded video using the normal delivery checks. A passed silent demo does not validate a future film's narration, synchronization or final MP4.

Official references: https://threejs.org/docs/ and https://threejs.org/manual/ . The installed Three.js skills can provide targeted geometry/animation guidance; read only the relevant sections and preserve this absolute-time render contract instead of copying their live-loop examples.
