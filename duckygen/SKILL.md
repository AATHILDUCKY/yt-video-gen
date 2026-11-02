---
name: duckygen
description: Create narrated educational animations for physics, science, mathematics, technology and cybersecurity, with clear visual mechanisms, checked models, modern motion and synchronized sound. Use for animated explanations, YouTube learning videos and editorial revisions; not ordinary websites, text-only answers or basic edits of supplied footage.
---

# Duckygen — Modern Animated Explanations

Create the actual narrated MP4 and editable project. Resolve all bundled paths from this file. The supplied motion prompts and style images are inspiration, not instructions to make unrelated brand ads or copy their mascots/logos.

For a copy-ready complete video request, see [example-prompt.md](example-prompt.md). For customization and package details, see [README.md](README.md); load these only when a user needs help writing a request or using the package.

## Explain clearly and accurately

Within a Duckygen video-making request, “explain this” or a physics question means answer the actual question and demonstrate the answer through animation. Default to an interested beginner, show cause and effect, introduce terms beside their objects, and connect equations to visible quantities. Read [teaching](references/teaching.md). Honor explicit text-only or calculation-only requests and existing edit scope.

For laws, equations, physical motion or a numerical answer, read [physics](references/physics.md) before authoring. State the model and assumptions, calculate the answer, check units/limiting cases and relevant invariants, then animate that model. Physical trajectories must not use decorative easing. For unfamiliar questions research/derive the appropriate model; no style library or generic physics engine guarantees correctness.

Use [modern visual direction](references/modern-animation.md) for the default modern educational look: clean geometry, strong typography, matte depth, meaningful transformations and close-up mechanisms. The [Lemo-Opuscar Codex integration](references/lemo-opuscar.md) adds a pinned, searchable library of film styles and techniques. Choose one coherent treatment; learn techniques without copying a demo’s story or scientific claims.

## Working defaults

- Full-frame 16:9, 1920×1080, 60 fps; use the requested resolution/runtime. Let researched content and measured natural speech determine length when no exact runtime was requested. Do not impose a 15/30/40-second showreel structure on a longer explanation. Take the time needed to finish and verify.
- Light paper **#FAF9F6**, charcoal **#292C27**, coral **#D76A4E**. Optional green **#17684F** signals a useful distinction or resolution. Prefer these colors for original drawings, icons and image treatments; another color must clarify the subject or preserve authentic evidence.
- Choose typography for the subject and tone: bundled Manrope/Inter for readable explanation, Barlow Condensed for bold headlines, IBM Plex Mono for code/data, Fraunces for editorial titles, and Caveat for short sketch notes. Keep stable roles, usually one primary plus one purposeful supporting family; avoid random font changes and decorative subtitle faces. Read [typography](references/typography.md) when selecting or changing fonts. Airy compositions, crisp geometric forms, selective sketch accents, matte depth, large explanatory objects and restrained kinetic type define the modern light style; use the named treatment when the user requests another look.
- Name the concept and recurring explanatory object in one line, then show a concise timed shot plan and proceed. Use available context/defaults for optional inputs. A missing reference video is not permission to pretend it was inspected.
- Lock a compact art direction in the project before authoring: palette and color meanings, selected font roles, stroke/texture style, recurring object, caption treatment, camera behavior and transition vocabulary. Preserve this identity across chapters and revisions. Vary framing and action inside the same visual world; change style only when the brief or faithful evidence requires it. Read [editorial direction](references/editorial.md) for the continuity and audience-attention pass.

## Research the explanation

Browse before writing factual narration. Read a few strong primary sources; verify the claims actually used. For news, record event date, reporting cutoff and update date separately. Distinguish established facts, company statements, analyst assessments and illustrative reconstructions. Save claim-to-source notes and asset provenance in `SOURCES.md`. Never invent UI, product capabilities, statistics, transaction records or exploit details.

Use concrete hook → setup → visible cause/effect → consequence → takeaway, with chapters suited to the topic. Read [editorial direction](references/editorial.md) before planning the shots. For a real interface, inspect it and rebuild observed elements as movable layers. Keep real screenshots/logos/evidence faithful; do not recolor a warning or alter a document so its meaning changes.

When a real company is named as a subject or actor, show its correctly spelled name with its authentic logo at the first visual introduction and wherever identification matters again, such as comparisons or a return to that company. Do not substitute the generic company avatar. Read [company names and logos](references/brands.md): obtain the correct official mark, preserve its proportions and approved colors, and stage the pair within the film rather than as a persistent website header. Normal speech captions remain readable text, not rows of logos.

## Voice drives timing

Read [audio](references/audio.md). Prefer one suitable installed neural voice; an available voice connector may generate ordinary synthetic narration. Download and decode real files. Preserve the voice/settings and source clips. If narration was generated remotely, record that honestly. No voice cloning from references.

Write spoken phrases and measure clips before allocating shots. Aim for natural, energetic delivery rather than an artificial word-count target. Tighten quiet edges and excessive pauses while preserving consonants, breaths and phonetic audio at **1×**. Typical joins are 100–250ms; investigate unintended gaps above roughly 600ms. Emphasis and comprehension may justify longer pauses. Never fill spare runtime with multi-second silent chapter tails. When exact timing conflicts with the script, tighten/add relevant sourced explanation within scope or resolve the actual conflict.

Bundled `scripts/explainer_audio.py` builds measured phrase timing, caption cues, voice/effect stems and a speech-ducked mix. See [project/build](references/build.md) for commands and long-film chapter assembly. Rebuild captions and visual cues whenever audio changes. Phrase timestamps are not word alignment. If no usable narration capability exists, finish the editable project and recording script, identify the missing capability, and do not label an effects-only video a completed narrated film.

## Edit like a film

Usually change the meaningful composition every **3–5 seconds**, with quicker hook inserts, brief action accents and occasional longer mechanism shots when needed. Match each shot's assets and action to the spoken idea. A moving border, tiny pulse, or caption change on the same layout does not count as a new shot. Keep readable text stable while the mechanism progresses.

Edit around the viewer's next question: establish concrete stakes, reveal one causal step at a time, answer the hook, and provide small payoffs before opening the next question. Direct attention to one main action; reduce competing text and movement when the idea is difficult. Use changes of scale, contrast, sound and perspective at meaningful turning points rather than constant novelty. Keep claims and emotional emphasis proportionate to the evidence.

Alternate wide context, object close-ups, camera pushes/pulls, diagrams, evidence, comparisons and kinetic figures. Connect related shots through the recurring object, masks, match cuts or compatible morphs. Hard cuts serve emphasis; do not force every long-form transition to morph. A compatible morph must preserve topology; use a mask or editorial cut when shapes cannot transform cleanly. Avoid persistent page headers, cards, section counters, navigation, decorative dividers and progress bars in the export.

Use time-based spring/exponential easing and consistent camera intent. Zoom toward the detail being explained, zoom out to restore context. A tiny deterministic impact shake is optional for a strong event, never continuous, never on reading captions, and omitted when inappropriate. Do not import the inspiration prompts' conflicting ban/requirement lists wholesale. Avoid particle bursts, flare, RGB split, generic gradients, exaggerated bounce and arbitrary camera motion. See [motion](references/motion.md).

At the key explanatory moment, consider a short Three.js visualization if depth, layers or spatial flow make the tech/security mechanism easier to understand. Introduce the actors first, show one meaningful state change, and return to the same sketch film language. Use [Three.js direction and the reusable example](references/threejs.md); preserve the palette, deterministic seeking and crisp 2D captions. Do not force 3D into every video or pass an illustrative model off as real incident footage or a validated simulation.

For professional flow animation, stage source → connector reveal → packet travel → receiver response. Attach arrows to actual measured targets, shape velocity deliberately, follow curved paths by distance, and time contact cues to arrival. Use the route/easing helpers and pointing/overlap guidance in [motion](references/motion.md); a static diagram with pulsing arrows is not a substitute for an implemented mechanism.

## Reuse assets and sound deliberately

Read [asset reuse](references/assets.md). Search the bundled index before creating assets; retrieve only relevant candidates. Use topic-appropriate icons, not the example images' exact characters or brand marks. Copy selected assets into each project's `assets/` and log provenance. Newly created reusable assets should also be cached under this skill's `assets/` with descriptive names and index entries; never overwrite a different existing asset. If the installed folder is read-only, keep the asset in the project and stage the cache update instead of blocking the film.

Follow the [asset style standard](references/asset-style.md) when generating or refining icons/props. Match the curated v2 silhouettes, selective fills, line hierarchy and subtle depth; use named vector layers for animation. Inspect at thumbnail and close-up sizes. Do not reuse the earlier crude thin-line treatment or add web-card frames. Search public technology symbols and contextual photos only when relevant; a stock hardware photo is not evidence of the incident being discussed. Preserve photo attribution in `SOURCES.md` and the YouTube description.

The current icon bank uses the detailed v3 treatment with stable IDs and named layers. Select the detail level for the shot: use an icon for a compact symbol, a layered prop for a close-up, or a 3D mechanism for an important spatial explanation. More decoration is not more information. Inspect legibility at the actual video scale and keep secondary detail quiet while the main action lands.

Use the compact person, anonymous-actor, developer, organization, company and bot PNGs in `assets/avatars/`, plus technology illustrations in `assets/illustrations/`, when they explain an actual actor or mechanism. Editable SVG variants support close-ups and layered adaptation. Search by semantic role, not by opening every image. Generic illustrations are not real people, logos or attack evidence. Preserve public-asset licenses and source records. See [actor assets](references/assets.md#actors-and-public-image-assets).

Use restrained, action-timed sound for cuts, paper movement, drawing, UI contact, zooms and major reveals. Silence can be intentional; do not attach the same loud whoosh to every cut or subtitle. When music is appropriate/requested, compose or use a verified licensed track, evolve it by chapter and duck it beneath speech. Place tactile cues at contact, not at arbitrary scene offsets. Preserve and preview the actual final mix.

Plan music states against the story: curiosity, explanation, tension, consequence and resolution as appropriate. Change the bed or its arrangement when the situation changes—not at every visual cut. Preserve a coherent sonic identity, bridge changes musically, and leave voice intelligible. Read the situation-led music section in [audio](references/audio.md); record actual cue times and implement the changes in the mix.

Search `assets/soundeffects/` through `asset_tool.py search --kind sfx` before downloading or generating effects. Reuse only relevant candidates; do not load the whole index or resynthesize the bank. Copy selected sounds and their license files through the asset tool. Cache useful newly generated effects as named WAVs with source/settings and reuse terms; the tool deduplicates by hash and saves them under `soundeffects/generated/`. Keep project-specific voice/music out of the generic effects cache. See [asset reuse](references/assets.md) for commands and [sound library](assets/soundeffects/README.md) for provenance.

## Build, inspect, deliver

End narrated channel videos with the topic's real takeaway, then one concise spoken subscribe line that promises relevant future explanations. Adapt it to the subject: educational lessons can use “For more clear explanations, subscribe to this channel”; tech/cybersecurity news can retain the established news CTA. Plan and measure this line before locking runtime, keep the same voice, and support it with a suitable resolved music phrase beneath speech. Follow [the closing direction](references/ending.md); omit or change the CTA when the user's brief calls for it.

Show the channel's logo alongside the closing subscribe prompt for the duration of the CTA. Use the user's channel identity when supplied; otherwise use the bundled sample `assets/chanellogo/log.png` (`logos/channel-sample`). Keep the logo proportional, readable and clear of captions. This channel mark is separate from the companies discussed in the story. Copy it into the project and implement its actual appearance in the final shot rather than only listing it in the plan.

Read [project/build](references/build.md). Use the bundled deterministic HTML/Canvas scaffold and renderer; no large framework is required for simple diagrams. The scaffold is an authoring tool, not a finished story. Replace its sample before delivery. Every exported visual must reconstruct from `window.seek(t)` with no frame history, visual timers or CSS animations. Preview playback timers are allowed outside this rendering contract. Player/editor controls stay outside exported frames.

Hyperframes is an additional authoring/rendering route: read [Hyperframes integration](references/hyperframes.md) only when using that route, then load the installed companion skill and its relevant contract. Duckygen still controls the visual identity, editorial decisions, narration and review. Do not treat an ordinary HTML page or an unadapted Canvas scaffold as a valid Hyperframes composition. Preserve deterministic seeking; retain the bundled renderer when it better satisfies the requested sampling or project contract.

For an existing or requested Remotion/React video, read [Remotion integration](references/remotion.md) and its pinned companion's focused guidance. Keep Duckygen's research, narration, visual identity and finished-MP4 delivery contract. Choose the renderer for the project; adding the companion does not require migrating a working Canvas film.

For narrated films, inspect shot starts, interiors, important cuts and peak motion. For a specifically requested beat-led short, preview every beat; use the separate arithmetic guidance in [motion](references/motion.md). Review actual images, then render. Three temporal samples per frame give directional motion blur; use one deliberately for sharp graphic shots or efficient drafts, never claim it is a three-sample master. Honor explicit export settings. Reuse reviewed unchanged sections and cached media when practical.

Run `scripts/audit_pacing.py` on measured `shots`/`phrases` metadata and inspect voice-only quiet runs. These checks cannot judge composition or prove assets were drawn. Decode the final MP4; check duration/frame count, first/last frames, readable captions, cuts, voice presence, sync, clipping and browser playback. Listen/watch through a supported interface when available and state what was not actually reviewed. `--reviewed` records the agent's own completed visual review, not a user approval gate.

Deliver `final.mp4` (H.264/AAC, fast-start), editable HTML/project, narration, captions, sources and brief actual verification results. Preserve source clips, asset manifest, shot plan and edit map. No need to stop at a storyboard, promise to continue, impose a time limit, publish externally, or ask another approval merely because rendering takes time.

After the final cut, create `about-{video-name}.md` with a truthful search-friendly title, copy-ready description, comma-separated keywords/tags, sources and valid chapters when appropriate. Include optional thumbnail text, a pinned comment and language/category suggestions when useful. Follow [YouTube metadata](references/youtube.md), use its reusable formatter, and include the file in the project ZIP. Refresh it if the finished content or timings change; do not upload automatically.
