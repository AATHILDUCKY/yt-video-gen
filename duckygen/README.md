# Duckygen

Create modern narrated educational animations for physics, science, mathematics, technology and cybersecurity, with visible mechanisms, checked models, tight speech, reusable assets and synchronized sound. The skill folder and invocation name are `duckygen`; invoke with `$duckygen`.

## Setup

Use Python 3.10+, Node.js 22+, FFmpeg/FFprobe, and a compatible browser. From this skill folder, install dependencies into your active Python virtual environment and the local Node package:

```bash
python3 -m pip install -r requirements.txt
npm install
npx playwright install chromium
npm run validate
```

The browser download is optional when a compatible browser is already available through `CHROME_PATH`. Register this folder with your agent's skill discovery mechanism or ask the agent to read `SKILL.md` directly. Configure a narration engine or voice service separately; none is bundled. Package validation does not require dependency installation or voice access.

Original code and documentation are currently unlicensed. See [third-party notices](THIRD_PARTY_NOTICES.md) for bundled components and their existing terms.

The default look uses paper `#FAF9F6`, charcoal `#292C27`, coral `#D76A4E`, and optional green `#17684F`. Six bundled open-source font families support different editorial needs. Runtime follows your brief and measured narration; two minutes is an example, not a fixed limit.

## Consistent style, purposeful editing

Keep one recognizable visual identity throughout the film: light sketch backgrounds, stable line quality, consistent color meanings, selected font roles, caption styling and camera behavior. Match new assets to that world. Create variety through framing, scale, action and contrast rather than switching visual styles between scenes. Preserve the established identity when revising a project.

Use the included generic actor PNGs when people, attackers, developers, organizations, companies or bots need a visible role. Public MIT-licensed source geometry is retained with licenses and editable SVG variants. These are illustrative assets, not real people or company logos. Pick only the actors needed by the current explanation.

When a real company is named, show its **company name with its authentic logo** at the first visual introduction and in comparisons or later shots where identification matters. Use an official source and preserve the mark's proportions and approved colors, even when they differ from the sketch palette. Do not substitute the generic company avatar or an AI-made lookalike. Place the pair naturally in the film composition; keep ordinary captions readable and avoid persistent website-style branding. See [company logo guidance](references/brands.md) for sourcing and reuse.

Think about the viewer's next question. Establish stakes quickly, show one causal step at a time, provide small answers along the way and resolve the opening question. Use the recurring explanatory object as a memory anchor. Reduce competing labels and movement when the explanation becomes difficult; a readable pause can be more engaging than another effect. Use honest evidence and meaningful contrasts instead of manufactured urgency.

Compose every scene as a full-frame film shot. Large explanatory objects, close-ups, spatial diagrams, decisive cuts and motivated camera moves should carry the story. Avoid website hero sections, navigation, scrolling-page layouts, card grids and repeated title/icon/paragraph arrangements. Real UI can appear when it is the subject, framed around the relevant interaction.

Music follows the situation. A curious opening, a clear mechanism explanation, a tense consequence and a resolved takeaway can use different beds or arrangements while retaining a shared motif and sonic character. Change at meaningful story turns, not at every cut. Keep voice intelligible, bridge musical changes smoothly and preserve actual stems/cue times. See [editorial direction](references/editorial.md) and [audio direction](references/audio.md).

### Closing sentence and music

End with the real takeaway, then a concise spoken invitation suited to the topic. Default: **“For the latest tech news and cybersecurity updates, subscribe to this channel.”** For a security-focused story: **“For more cybersecurity updates and clear breakdowns of digital threats, subscribe to this channel.”** Keep one relevant CTA, with the same narrator and a suitable musical resolution beneath it. Measure the sentence within the video runtime and let the music land naturally after the final word. See [closing direction and research](references/ending.md) for alternatives, timing and visual treatment.

Show the **channel logo beside the final subscribe prompt** throughout the closing sentence. A transparent sample is included at [assets/chanellogo/log.png](assets/chanellogo/log.png), using an original duck/circuit mark in the channel palette. Use the actual channel logo when supplied. The project initializer copies/embeds the sample by default and exposes `filmConfig.channelLogoAsset`; compose it into the final shot with clear space and stable captions. Use `--channel-logo-asset logos/<your-cached-channel-mark>` to select a different indexed logo. The sample contains no invented channel name.

## Detailed sample prompt

For a complete, ready-to-copy example including Three.js, company logos and the channel-logo outro, open [example-prompt.md](example-prompt.md).

Copy the prompt below and replace the bracketed inputs. Omit optional inputs you do not have; the skill can research sources, choose relevant assets and compose music.

```text
$duckygen

Create the complete narrated YouTube explainer, including the final MP4 and editable project.

Topic: [How passkeys protect accounts—and where risks remain]
Audience: [Curious everyday technology users; no security background]
Working title: [Why Passkeys Are Replacing Passwords]
Core takeaway: [Explain the mechanism and its practical limits clearly]
Duration: exactly 120 seconds
Format: 16:9, 1920×1080, 60fps
Language and voice: English; natural, confident male documentary narration
Optional materials: [Paste a script, source links, brand assets or reference paths]
Reporting cutoff for news: [YYYY-MM-DD; omit for an evergreen explanation]

COMPANY IDENTIFICATION
For any real company named as an actor or subject, show its correctly spelled name
with its authentic official logo at introduction and wherever identification matters
again. Use the correct company/product identity and reporting-period mark. Preserve
approved logo colors and proportions; surrounding illustrations keep Duckygen's
palette. Do not replace a named company's logo with the generic company avatar.
Keep source/use-term records and cache reusable originals only where permitted.

CONSISTENT IDENTITY AND VIEWER ATTENTION
Lock the visual identity before building: palette meanings, stroke/texture style,
font roles, caption treatment, recurring object, camera intent and transitions.
Preserve this identity across all chapters. Vary the composition and action within
the same sketched world; do not change styles just to make the next shot different.

Think like a professional editor about what the viewer understands and wants to
know next. Establish a concrete question and stakes, show visible cause and effect,
offer mini-payoffs, and answer the opening question by the end. Keep one main focus
per shot. Reduce visual and musical complexity during difficult explanations.
Use purposeful changes of scale, perspective and rhythm to renew interest. Do not
invent urgency, evidence or claims about guaranteed audience retention.

PROFESSIONAL FLOW ANIMATION
Stage source and destination before transferring information. Draw the connector
from the source, move the packet along the same route, and change the receiver's
state on arrival. Point to real measured targets; align arrowheads to path tangents.
Shape speed deliberately with smooth acceleration/deceleration, selective
anticipation and secondary follow-through. Avoid generic pulse loops, disconnected
arrows, random movement and motion that implies an unsupported real-world event.
Use Duckygen's deterministic route, flow-state and easing helpers where suitable.

CLOSING CTA
After the takeaway, say one short, topic-relevant subscribe sentence. For a general
tech/cybersecurity film, use: “For the latest tech news and cybersecurity updates,
subscribe to this channel.” Adapt it when the specific subject needs a more relevant
promise. Keep the same narrator and normal speech speed. Measure this line before
locking the runtime; do not append extra seconds or rush the main explanation.
Support it with a fitting resolution arrangement, ducked beneath speech, followed
by a brief natural music landing. Keep the closing shot in the same sketch style.
Show the channel logo next to the subscribe prompt throughout this sentence. Use
my supplied channel logo or the bundled sample assets/chanellogo/log.png; preserve
its proportions and keep it clear of the captions.

RESEARCH AND STORY
Research before drafting narration. Prefer primary sources and verify every factual
claim used. For news, distinguish event dates, reporting dates, company statements,
preliminary findings and investigator assessments. Preserve the specified cutoff.
Document inaccessible sources and reliable corroboration. Do not invent statistics,
product features, real interfaces, transaction records or attack details.

Use the supplied script as the foundation when present. Open with a compelling
question or consequence, explain the mechanism through visible cause and effect,
then end with a clear takeaway. Keep technical terms understandable.

For this two-minute film, start around 250–280 words and adjust to measured natural
speech. Preserve important qualifications. Generate and measure narration before
locking the visual timeline. Keep phonetic speech at 1×; tighten the script rather
than speeding up or truncating sentences. Keep phrase joins generally 100–250ms,
preserve breaths and consonants, and remove unintended long gaps. Do not pad chapters
with silent holds. If a narration capability is unavailable, state the limitation.

VISUAL DIRECTION
Use Duckygen's light sketched palette: #FAF9F6, #292C27, #D76A4E, with #17684F
only when it clarifies a distinction. Choose a readable primary font and a supporting
headline, code or annotation font only when the topic needs it. Think like an editor:
keep each font's role consistent, use stable sans-serif captions and avoid random
font changes. Use original sketch illustrations, large explanatory objects and concise kinetic typography. Preserve
authentic colors and content when showing real evidence or recognizable marks.

Name the concept and choose one recurring explanatory object from the topic. For
the passkey example, a coral authorization request can connect device, challenge,
signature and server verification. Show how the object's role changes as the
explanation advances; avoid suggesting a private key travels to the server.

Aim for roughly 28–35 meaningful shots in this 120-second film. Usually change
composition every 3–5 seconds, with quicker hook inserts and readable mechanism
shots. Alternate wide context, close-ups, diagrams, comparisons and financial or
data figures where relevant. Match the visible action to the spoken idea.

Use purposeful zooms, pullbacks, masks, match cuts, compatible morphs and decisive
cuts. A tiny impact shake is optional for one strong reveal; keep captions stable.
Favor spatial continuity without forcing every transition to morph. Avoid website
cards, persistent headers, navigation, section counters, decorative progress bars,
generic hacker imagery, arbitrary movement and repeated title-plus-icon layouts.

ASSETS AND SOUND
Search the bundled asset bank first. Copy only relevant icons, props, connectors,
fonts and sounds into the project's assets/ folder with provenance. Create missing
original assets with descriptive filenames. Cache reusable originals in Duckygen's
asset bank when writable; otherwise stage the cache update in the project.

Search the compact avatar/illustration library for people, developers, attackers,
organizations, companies, bots and technical systems. Use PNGs for small/medium
actor cutouts and the SVG variants for close-ups or separate vector-layer motion.
Inspect a small candidate contact sheet instead of repeatedly loading every image.
Download public images only after verifying their actual redistribution license;
preserve credits and source records. Generate new bitmap art only when needed.

Compose an evolving electronic bed suited to the explanation and duck it beneath
speech. Map music states to the situation: curiosity, explanation, evidence,
consequence and resolution as appropriate. Change the bed or arrangement at those
turns while preserving a shared sonic identity. Use suitable bridges or audio
crossfades; avoid abrupt volume jumps or restarting a track on every visual cut.
Implement and record the actual music cue times, not only a written intention.
Add restrained clicks, paper movements, drawing cues, transition accents
and impacts at meaningful actions. Vary cues; avoid a loud whoosh on every cut.
Keep source voice clips, voice settings, music/effect stems and the final mix.
Record whether narration was generated locally or through a remote service.

BUILD AND REVIEW
Briefly state the concept, recurring object and timed shot plan, then build without
additional approval questions unless a genuine blocker requires clarification.

Use the installed Hyperframes CLI/core companion when it helps author, inspect or
render the film. Preserve Duckygen's style, measured narration and 60fps contract.
Follow the actual Hyperframes composition/timeline format rather than assuming
an ordinary HTML page is render-ready. Keep the bundled Canvas renderer when it
better satisfies the existing project or required three-sample motion blur.

Build a deterministic editable HTML/Canvas project using window.seek(t). Keep
playback controls outside exported frames. Use 60fps and three temporal samples per
frame for motion blur; keep reading text sharp. Use the same final mix for player
and export. Replace the scaffold's demo story with this actual researched film.

Inspect representative images from every shot, important cuts and peak motion
before rendering the master. Decode and inspect the finished MP4, including its
first/last frames and any render joins. Check exact duration, frame count, captions,
narration presence, synchronization, audio peaks and the final spoken sentence.
Listen through a supported interface when available. Report actual checks and any
review limitations honestly; signal checks do not equal manual listening.

DELIVER
- final.mp4: exactly 120 seconds, H.264/AAC, fast-start, synchronized English captions.
- Editable HTML/project, source assets, shot plan and asset manifest.
- narration.txt, captions.srt, SOURCES.md and a source-attributed YouTube description.
- about-{video-name}.md with the finished video's title, copy-ready description,
  comma-separated keywords/tags, sources, valid chapter timestamps when appropriate,
  relevant hashtags and optional thumbnail/pinned-comment suggestions. Make the
  metadata accurate and search-friendly without keyword stuffing or ranking claims.
- ZIP of the editable project, including concise verification results.

Complete the actual video, not only a storyboard or a collection of assets.
```

## Adapt the request

- For another length, change the duration and shot budget together. Let measured delivery determine narration length; do not stretch a two-minute script across a longer runtime.
- For tech news, supply the incident brief and a reporting cutoff. Keep uncertainty visible and distinguish reported losses, frozen funds, recovered assets and company-funded replacements when relevant.
- For product explanations, supply the real site or inspected interface. Reconstruct only observed features; references guide style rather than supply fictional product evidence.
- For revisions, point to the existing project and describe the desired editorial changes. Preserve usable media and reviewed unchanged sections.

## Package and tools

### Detailed icons and explanatory 3D

The existing **88 icon IDs** now use a refined v3 treatment: selected hardware symbols become layered miniature illustrations, and the remaining symbols gain clearer stroke hierarchy and selective internal accents. IDs and filenames remain stable. [Preview icons 1–48](assets/previews/icons-v3-0.jpg) and [icons 49–88](assets/previews/icons-v3-48.jpg). Keep essential shapes legible; detailed props serve close-ups better than enlarging a tiny symbol. `scripts/build_detailed_icons.py` maintains the icon family without changing delivered projects.

Use Three.js where it clarifies an important mechanism, often after the setup in the middle of the explanation. Show packet routing, authorization boundaries, hidden hardware layers or staged data movement with one clear cause-and-effect action. Carry the same sketch palette and recurring object into 3D, keep labels/captions sharp, and return smoothly to the next scene. Avoid decorative spinning objects, neon style changes or presenting a teaching model as real attack footage.

The package includes a pinned local Three.js module/core build with its MIT license, an original seekable authorization visualization and a self-contained demo builder. [Preview the 3D mechanism](assets/previews/threejs-mechanism.jpg):

```bash
python3 scripts/create_three_demo.py --output ./three-mechanism-study
```

This is a silent authoring example, not a completed video. Copy the engine only when using 3D; normal 2D projects remain lightweight. [Three.js integration guidance](references/threejs.md) covers timing, deterministic rendering, WebGL checks and review. Prefer the clearest 2D/3D choice for the actual tech or cybersecurity story.

### Refined props and expanded public library

The 30 files in `assets/props/` use the refined editorial sketch treatment: clearer silhouettes, stronger stroke hierarchy, selective coral fills, subtle depth and named animation layers. The original 16 asset IDs remain stable, and 14 additional hardware SVGs extend the set. Future icons and props should follow the [asset style standard](references/asset-style.md), rather than the earlier thin-line sketches. [Preview the refined originals](assets/previews/props-v2.png) or [the hardware set](assets/previews/hardware-svg-pack.png).

The hardware set includes desktop computers, tower PCs, dual-monitor workstations, open/closed laptops, server blades, data-center racks, routers, network switches, CPU processors, GPU cards, external drives, smartphones and tablets. Each uses the Duckygen palette and named vector layers; relevant details such as fans, screens and ports are grouped for animation. Index records include optional attachment anchors in the asset's 320×260 coordinate space. Transform these anchors with the object/camera before attaching an arrow or packet.

```bash
python3 scripts/asset_tool.py search 'server computer laptop' --kind props --limit 6
python3 scripts/asset_tool.py copy props/desktop-computer props/laptop-open props/server-blade props/network-router --project ./my-film
```

Use these as generic explanatory hardware, not as an invented real product interface. `scripts/build_hardware_props.py` is the editable authoring source for deliberate maintenance; normal video jobs copy the cached SVGs.

The expanded library also includes 24 additional MIT-licensed technology symbols covering processors, AI, APIs, networks, connectivity, devices, security, coding, automation, cloud transfers and data. Five compact technology photographs provide optional real-world context, with individual source/author/license records. Preserve the actual subject of these photographs: a historical CPU collection is not a current-chip benchmark image, and a generic server photo is not evidence of a specific incident.

Use the light sketch style for explanatory scenes; introduce real photography only when it serves context or evidence. Keep authentic photo content faithful, fit it into the established film framing, and include required credits in `SOURCES.md` and `about-{video-name}.md`. Search `--kind photos` for the photos and `tech-` for the additional vector symbols. Download only a genuinely missing subject after checking its license, rather than collecting unrelated images.

```bash
python3 scripts/asset_tool.py search 'cpu security network' --kind icons --limit 6
python3 scripts/asset_tool.py search 'server' --kind photos --limit 3
python3 scripts/build_catalog.py
```

The catalog refreshes without regenerating artwork or sounds and lazy-loads its previews. Only selected assets enter a video project. The generic bank maintenance script preserves reviewed v2 props; use `build_refined_props.py` only for deliberate prop maintenance.

### Compact actors and public image assets

The package includes **12 transparent 512px PNGs** with matching editable SVGs:

- Actors: person, anonymous hacker/attacker, developer, organization, company and bot.
- Technical context: team, security, cloud service, server, database and laptop.

The images use the paper/charcoal/coral theme. Their source geometry comes from [Tabler Icons](https://github.com/tabler/tabler-icons), under its included MIT license, with original Duckygen palette/backplate compositions. Upstream sources, pinned revision and hashes are retained. Search by role, copy the selected assets with their license records, and reuse them instead of downloading or generating the same artwork again. These generic symbols do not replace verified real product logos or evidence.

```bash
python3 scripts/asset_tool.py search 'developer bot server' --limit 5
python3 scripts/asset_tool.py copy avatars/developer-coder avatars/bot-assistant illustrations/server-infrastructure --project ./my-film
```

For large zooms, use the corresponding `-vector` IDs. Avoid enlarging a 512px PNG beyond its useful resolution. A full-resolution image's small compressed file size does not imply a small model token cost; search text first and inspect only a few candidates. Read [asset guidance](references/assets.md) for provenance, caching and model/context efficiency.

### Motion and YouTube delivery

The motion runtime includes adjustable Bézier easing, curved routes with approximate distance-based sampling, progressive arrow drawing and timed packet/arrival states. These help implement deliberate motion-graphics craft in the HTML pipeline; they do not create an Adobe After Effects project. See [motion examples](references/motion.md) for clean pointing, packet flow, anchors, follow-through and review.

After each finished film, create `about-{video-name}.md`. Use the actual final content and timings for a truthful title, natural description, comma-separated keywords, sources and valid chapters. Prioritize useful titles/descriptions and an accurate thumbnail over tag stuffing. The optional formatter keeps this repeatable:

```bash
python3 scripts/write_youtube_about.py ./my-film/youtube-metadata.json --project ./my-film --name how-passkeys-work
```

The JSON supplies `title`, `description` and `keywords` (array), with optional chapters, sources, credits, hashtags, thumbnail text and a pinned comment. See [YouTube metadata](references/youtube.md) for the complete fields, platform references and limits. The helper formats authored content; it does not invent SEO claims or upload the video. Include the generated Markdown and editable JSON in the project ZIP.

### Hyperframes companion

The package includes unmodified core and CLI instruction files in `companions/hyperframes/` and `companions/hyperframes-cli/`, with the upstream Apache-2.0 license, pinned revision and hashes. This keeps the references available offline; it does not install or bundle the Hyperframes runtime, Chrome or Node dependencies. The integration keeps Duckygen's art direction and local renderer available.

For a Hyperframes job, read the [integration guide](references/hyperframes.md), then only the relevant companion sections. Use its lint/check/snapshot/preview/render workflow on a valid composition; inspect the actual frames and final MP4. Installing the skill is not a completed render test. Preserve 60fps explicitly and verify whether the selected runtime supports the requested temporal sampling. Local generation remains the default; hosted publishing and paid services require task-specific authorization.

Source: [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes).

### Fonts chosen for the situation

| Font | Best use |
| --- | --- |
| Manrope | Friendly tech explanations and stable captions |
| Inter | Neutral factual copy, interface labels and captions |
| Barlow Condensed | Short bold headlines, hooks and large figures |
| IBM Plex Mono | Code, commands and aligned technical data |
| Fraunces | Editorial titles and attributed quotations |
| Caveat | Short handwritten sketch notes |

Use one primary family and add a supporting face only when it adds meaning. Avoid handwriting for subtitles and condensed display type for dense reading. Prefer hierarchy through weight, scale and spacing before adding fonts. Read the [typography guide](references/typography.md) for pairings, caption sizing, font readiness and licenses.

```bash
python3 scripts/create_project.py --output ./my-film --title 'How passkeys work' --duration 120 --font manrope --heading-font barlow-condensed
python3 scripts/asset_tool.py search 'code data' --kind fonts --limit 3
```

Only selected families are copied/embedded; their OFL licenses travel with the project. `typography.json` records the roles. Omit `--heading-font` to use the primary family throughout, or use `--accent-font ibm-plex-mono` for code/data. The small selection catalog is `assets/fonts/families.json`. Reuse cached fonts to save downloads and tokens.

### Reusable sound effects

`assets/soundeffects/` includes **75 effects**: 50 Kenney CC0 interface sounds, 12 CC0 tactile impacts, 3 CC0 sci-fi/computer textures, and 10 original procedural cues. Select clicks, confirmations, errors, opening/closing, zoom-related expand/shrink cues, paper/drawing cues, gentle contacts and restrained reveals according to the action. Electronic textures are optional accents, not a reason to turn every explanation into a sci-fi scene. Source/license records travel with selected assets; third-party CC0 sounds are distinct from generated originals. Original downloads were unavailable, so the CC0 files were retrieved from pinned public mirrors with the original Kenney licenses. See [sound library](assets/soundeffects/README.md).

Search a few tagged candidates, copy only what the video needs, then generate a new effect only when none fits. Cache useful new generic sounds once for future projects; avoid re-downloading packs or regenerating the bank. The cache checks hashes to reuse identical content and saves duration/sample-rate metadata for WAVs.

```bash
python3 scripts/asset_tool.py search 'click confirm' --kind sfx --limit 5
python3 scripts/asset_tool.py copy sfx/kenney-confirmation-001 --project ./my-film
python3 scripts/asset_tool.py cache ./my-film/assets/soft-page-fold.wav --name soft-page-fold --kind sfx --tags paper fold transition soft --source 'Original procedural audio; include synthesis settings' --license 'Original audio; reusable in generated projects'
```

Run these commands from the skill folder, or use the absolute script path. Cache downloaded sounds only when their terms permit redistribution, with `--source-url` and `--license-file` where applicable. Keep generated provider restrictions intact. Use `assets/index.json` through search instead of loading the entire catalog into model context.

Install dependencies as described above and register the `duckygen/` folder, then invoke `$duckygen`. The package includes reusable drawings, synthetic sound cues, fonts and licenses, deterministic motion helpers, audio/timing utilities and a Playwright/FFmpeg renderer. It does not bundle a browser, voice model or Node dependencies.

- [SKILL.md](SKILL.md): core workflow and reference routing.
- [Asset catalog](assets/catalog.html): preview reusable illustrations and cues.
- [Asset guidance](references/assets.md): search, copying and cache provenance.
- [Build workflow](references/build.md): authoring, rendering and verification commands.
- [Audio guidance](references/audio.md): measured narration and mixing.

Inspect available Python/NumPy, Node/Playwright, Chrome, FFmpeg and narration tools before installing dependencies. Voice generation uses an available local engine or remote connector; record the actual source. The authoring scaffold is a demo until its story, narration and visuals are replaced.


### Codex-ready Lemo styles and educational explanations

The pinned Lemo-Opuscar companion is in `companions/lemo-opuscar/`, with a Codex-specific entrypoint, 66 published style prompts, directing/technical guides, selected core tools, provenance and the upstream MIT notice. It does not run the Claude bootstrap, auto-update a home-directory clone, install voice models or download demo media. Use [Lemo integration](references/lemo-opuscar.md) for the exact adaptations and licenses.

```bash
python3 scripts/lemo_library.py list swiss
python3 scripts/lemo_library.py list infographic
python3 scripts/lemo_library.py verify
```

For a Duckygen explanation, the workflow answers the question through a visible mechanism, progressive labels, a worked example and a clear takeaway. Physics/equation questions use stated assumptions, checked units and model-driven motion. [Teaching](references/teaching.md), [physics](references/physics.md) and [modern animation](references/modern-animation.md) provide the focused guidance. This improves the workflow; it does not guarantee that every arbitrary scientific question has an exact answer.

```text
$duckygen Explain why heavier objects do not fall faster in a vacuum.
Make a modern narrated beginner video. Show weight versus acceleration,
calculate a 20 m drop with units, and animate the checked result.
```

```bash
node scripts/check_physics_models.mjs
python3 scripts/create_physics_demo.py --output ./free-fall-study
```

The generated study is silent authoring material, not a completed narrated film. It demonstrates an accurate model-to-image mapping and deterministic seeking. For other laws, derive and verify the appropriate project model rather than reusing an unrelated example.
