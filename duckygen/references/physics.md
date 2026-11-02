# Physics and mathematical explanations

Use with [teaching](teaching.md). The goal is an understandable, checked explanation of the user's question. A beautiful trajectory is not proof of a correct law. Choose the model before styling or timing the action.

## Define the model

Record in the existing project notes or `model.json`: the question, expected quantity/units, governing equations, assumptions, initial/boundary conditions, coordinate system, parameters and source references. Keep physical time separate from scene time. Distinguish a quantitative simulation, a conceptual mechanism and measured evidence on screen when the distinction matters.

Verify the laws actually used with authoritative sources: primary research or standards for specialized claims; established textbooks, official educational sources or original technical documentation for fundamentals. Preserve source/edition/section and the applicable approximation. A demo's scientific claim is not a source for a new question. For a new field, derive an appropriate model rather than forcing it into the helper's example formulas.

If a question is underdetermined, answer symbolically or demonstrate a labeled assumption. Correct a false premise with a comparison. Ask only for information that materially changes the requested answer and cannot reasonably be assumed. Do not promise that an arbitrary question has a single exact numerical answer.

Use SI internally, explicit unit conversions at input/output, radians for trig, and a declared sign convention. Distinguish mass from weight, force from velocity, and position from displacement. Model constants have scope: 9.81 m/s² is an approximate local near-Earth gravitational acceleration, not gravity everywhere. Keep precision proportionate to the input and approximation.

## Make motion obey the law

Prefer an analytic solution when available. Otherwise choose an appropriate solver, fixed physical step, meaningful error tolerance and event handling. Precompute a deterministic trajectory or reconstruct it from fixed initial conditions. Absolute-time seeking must sample that same model; never advance physics from the previously rendered frame. Render fps and solver step are independent.

A slow-motion teaching view may use `physicalTime = speed * (sceneTime - start)` with a stated speed. Compare experiments on the same physical clock. Avoid arbitrary easing of physical time, forces or measured quantities. One world-to-screen transform maps positions, arrows and labels. Label exaggerated geometry, unequal axis scales or schematic distances; do not compute the answer from distorted screen pixels.

Handle impacts, contacts, constraints, boundaries and regime changes explicitly. Stop free-flight at first ground contact or switch to a justified collision/contact model; do not let a ball tunnel below the floor and clamp its y-coordinate while retaining a fictitious velocity. During a teaching freeze, label the freeze and preserve the sampled state. Reset trails and graphs deterministically on a backward seek.

Some common interpretation traps:

- Newton's second law uses **net** force. Rest or constant speed can have balanced forces. Action/reaction forces act on different bodies.
- Free fall without air resistance gives equal acceleration for different test masses in a uniform field; real drag depends on the object and environment. An arrow proportional to weight gets longer with mass; an acceleration arrow does not in that model.
- Conservation depends on the system. Elastic collisions conserve kinetic energy and momentum for an isolated system; inelastic collisions convert some kinetic energy into internal energy. Friction/damping needs an energy sink, not disappearing energy.
- Pendulum `T ≈ 2π√(L/g)` assumes small angles. An undamped spring's angular frequency is `√(k/m)`; damping and driving change behavior.
- A sound wave in air is a longitudinal pressure/displacement pattern. A sine graph is a representation, not a literal sideways path of air molecules. Quantum states and spacetime diagrams also require clear limits to classical visual analogies.
- Refraction angles are measured from the surface **normal**. Include total internal reflection where the indices/angle require it; do not draw a transmitted ray for an impossible real angle.
- Electrons, conventional current, fields and signal propagation are different. Do not animate a DC circuit as water physically filling a wire or an atom as an exact classical planetary system.

## Verify before rendering

Check dimensions, signs, initial conditions, a limiting case, and the result against an independent analytic calculation or trusted reference. Evaluate the actual model outputs used by the scene. Inspect conserved quantities only where the assumptions imply conservation; check dissipative trends otherwise. For numerical trajectories, halve the step and compare the answer/event time against a declared tolerance. Plot position/velocity/energy or constraint residuals when they can expose an error.

Check an actual worked example with numbers and units. For a 20 m drop from rest with uniform g=9.81 m/s² and no drag, first ground contact is `sqrt(2h/g) ≈ 2.019 s`, with downward speed `sqrt(2gh) ≈ 19.809 m/s`. Different test masses share that contact time. Near the apex of an ideal projectile, vertical velocity is zero while downward acceleration remains g.

Bundled `assets/runtime/physics-models.mjs` contains small checked analytic models for uniform-gravity flight/first contact, a linear undamped spring, one-dimensional isolated collisions and Snell refraction. Read its parameter contracts before reuse; these are examples, not a general physics engine. `node scripts/check_physics_models.mjs` checks meaningful invariants and edge cases. For other topics add a project-specific model with the same discipline. `scripts/create_physics_demo.py` generates a silent seekable free-fall authoring example to inspect the model-to-visual mapping; it is not a finished narrated lesson.

Save a concise `model-verification.json` for the film: inputs, equations/assumptions, computed answer, units, checks/tolerances and any limitations. Tests of these helpers do not validate a different model, real hardware or an engineering design. For high-stakes engineering/medical/legal topics, keep the explanation within validated evidence and the user's requested scope.

## Trusted starting references

- NASA, free fall without air resistance: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/free-fall-without-air-resistance/
- NASA, weight equation: https://www1.grc.nasa.gov/beginners-guide-to-aeronautics/weight-gravitational-force/
- OpenStax University Physics Vol. 1, projectile motion: https://openstax.org/books/university-physics-volume-1/pages/4-3-projectile-motion
- OpenStax University Physics Vol. 1, simple harmonic motion: https://openstax.org/books/university-physics-volume-1/pages/15-1-simple-harmonic-motion
- OpenStax University Physics Vol. 1, one-dimensional collisions: https://openstax.org/books/university-physics-volume-1/pages/9-4-types-of-collisions
- OpenStax University Physics Vol. 3, total internal reflection: https://openstax.org/books/university-physics-volume-3/pages/1-4-total-internal-reflection

These sources support the named introductory models; research the actual requested topic as needed.
