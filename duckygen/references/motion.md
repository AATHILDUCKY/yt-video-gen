# Motion that explains

Use bundled `assets/runtime/motion.js` for time-based exponential easing, small-overshoot springs, camera transforms, masks, compatible point morphs and brief impact offsets. Choose motion from the spoken action. An object has an anchor, destination and timing; a camera zoom has an explanatory target. Moving the entire scene continuously does not substitute for meaningful shots.

At narration scale, maintain a 3–5 second visual rhythm without making reading frantic. A close-up can begin as a wide diagram finishes its relation. Carry a request, document, key or value through the handoff. A camera pull-out restores the larger system after a close-up. Preserve spatial continuity when it helps, and use a purposeful hard cut when a new context is clearer. Keep type crisp during readable holds.

For actual vector morphs, use matched point counts/order and corresponding topology. Measure runtime layout/text bounds for match cuts. When shapes differ, transform through a shared intermediate, use a mask, or cut; do not crossfade and call it a morph. A filling mask must cover the furthest corner, not merely half the frame width. Separate outgoing/incoming text windows to prevent accidental letter overlap. Avoid will-change on camera-scaled DOM/text.

Directional blur comes from temporal samples at neighboring actual times, blended in disjoint triplets by the renderer. The object's time-based velocity/direction determines the result. An isotropic CSS blur is not equivalent. Use fewer samples intentionally for a sharp graphic treatment or draft and report that choice. Never blur small reading text merely to look cinematic.

A purposeful impact can use `Motion.impact(localTime, pixels)`; this returns a tiny damped translation and settles quickly. The user allows selective shake, despite an inspiration prompt banning it. Do not apply that prompt's ban globally, and do not add shake to calm explanations. No random state or evolving simulation may drive the export.

## Professional flow and motion craft

Aim for the craft of a deliberate motion-graphics edit: staging, controlled velocity, clean contact, overlap and readable settling. This HTML workflow does not create an Adobe After Effects project or reproduce its engine. Adobe's Graph Editor guidance is useful for shaping speed rather than applying one preset ease everywhere: https://www.adobe.com/learn/after-effects/web/adjusting-keyframes-dynamic-movement (researched November 1, 2026).

Use `Motion.bezierEase(t,x1,y1,x2,y2)` for a deliberate speed profile. Anticipation should prepare an action, not delay every entrance; use a small pre-move only when it helps. Let secondary details follow the main object by a few frames, then settle. Keep parent/child anchors and rotation pivots intentional. Avoid arbitrary elastic bounce, uniform stagger on every letter, all objects moving at once, and mechanical stop-start timing unrelated to narration.

For a pointing gesture, reveal the actor or cursor, move toward the actual target, land at its boundary, then emphasize the target and attach any contact sound. Measure the target in the active coordinate space. Do not point into empty space or let a camera move detach an arrow from its object.

For information flow, establish source and destination first. Reveal the connector from the source, move a packet along that same route, then change the receiver's state on arrival. Keep direction unambiguous. A decorative arrow that appears after the transfer does not explain it. Route paths around text/actors; attach endpoints at shape edges rather than through an avatar's face. A return acknowledgement needs a visibly reversed or separate return path. Show a blocked request stopping at its boundary; do not let it ghost through and label it blocked.

The bundled route helper builds an approximate arc-length table once, so equal progress steps follow equal path distances instead of accelerating unpredictably around bends. Create immutable geometry outside `seek()`; every visible state still comes from the requested time. Example:

```js
const requestRoute = Motion.route([[340,540],[600,360],[1200,360],[1460,540]]);
// Inside drawFilm(t); durations are examples to match to measured narration.
const state = Motion.flowState(t, {start: 4.2, draw: .28, travel: .85, settle: .16});
Motion.drawFlow(ctx, requestRoute, {progress: state.line, stroke: '#D76A4E'});
if (state.packetVisible) {
  const p = requestRoute.at(Motion.bezierEase(state.packet, .3, 0, .3, 1));
  ctx.save(); ctx.translate(p.x,p.y); ctx.rotate(p.angle);
  // Draw the selected transaction/message asset around its own center here.
  ctx.restore();
}
// Use state.arrival for the receiver's acknowledgement; it begins on arrival.
```

Do not loop packets indefinitely unless ongoing activity is actually being explained. For multiple packets, stagger by the story's real units; avoid random swarms. Label illustrative flows and never invent transaction paths as real evidence. Inspect source contact, curve midpoint, arrival and the next shot at full speed and in sampled frames. Use a large enough SVG or PNG for the shot; tiny pixelated avatars and cheap isotropic blur will not produce polished motion.

## Optional short beat-led mode

Only for a requested short showreel/ad/chapter bumper: use its specified tempo, defaulting to 120 BPM if absent. One beat is 0.5 seconds and one four-beat bar is 2 seconds. Fifteen seconds is 30 beats, or seven full bars plus two beats—not eight full bars.

Equal technique shares and a full-bar structure can conflict. State a concrete allocation before building; preserve the user's chosen priority instead of pretending both hold. A useful 15-second allocation is 0–2 hook; 2–4 kinetic type; 4–6 compatible shape morph; 6–8 dimensional moment; 8–10 data/UI; 10–12 synthesis; 12–14 strongest payoff; 14–15 end. This is an example to adapt, not a stock sequence for tech news.

Write a concise per-beat action/anchor/camera/cue plan and make something meaningful change on each beat. For a requested seamless loop, plan the return and compare the first and final *output* frames, including type, cursor, camera and object state. Do not force a loop or Claude logo onto a normal long-form explainer. Actual product UI/brand evidence is required before a product film; absent supplied product references are not reusable permission to invent it.
