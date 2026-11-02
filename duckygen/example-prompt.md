# Duckygen Example Prompt

Copy the prompt below to create the example film. For another video, change the topic, title, audience and duration. Add your script or news brief when available.

```text
$duckygen

Create a complete narrated YouTube explainer about how passkeys work and where
their security benefits and limitations come from. Deliver the actual final video,
not only a script, storyboard, HTML preview or collection of assets.

VIDEO BRIEF
Title: “How Passkeys Work — And Why They’re Replacing Passwords”
Audience: everyday technology users with no security background.
Duration: exactly 120 seconds, including the closing subscribe sentence.
Format: 16:9, 1920×1080, 60fps, H.264/AAC MP4 with fast-start.
Voice: natural, confident male English documentary narration at normal speed.
Goal: make the viewer understand the sign-in mechanism, the useful security
distinctions and the remaining risks without confusing jargon or exaggerated claims.

RESEARCH AND SCRIPT
Research authoritative primary sources before writing the narration. Verify the
claims actually used, distinguish established mechanisms from product-specific
behavior, and save claim-to-source notes in SOURCES.md. Do not invent statistics,
features, interfaces or security guarantees. Explain account recovery and device
access carefully rather than implying that any technology removes every risk.

Open with a concrete question or consequence. Establish the actors, show the causal
steps, deliver small payoffs, then resolve the opening question with a useful
takeaway. For this topic, distinguish the public key from the private key and show
what actually travels during authentication. Verify the details before drawing them.

Draft roughly 250–280 words as a starting point, then adjust to measured natural
speech. Include the CTA in that measurement. Preserve phonetic speech at 1×, keep
phrase joins tight, retain consonants and breaths, and remove unintended long gaps.
Do not accelerate the narrator, truncate the last sentence or pad chapters with
silent holds. Build captions from the final measured clips.

VISUAL IDENTITY
Keep one consistent light sketched world throughout the film:
- Paper #FAF9F6; charcoal #292C27; coral #D76A4E.
- Optional green #17684F only where it communicates a useful distinction.
- Stable sketch outlines, selective fills, subtle depth and large explanatory props.
- Choose a readable primary font and one supporting face when useful. For this
  example, Manrope captions/body with Barlow Condensed short headlines can work;
  use IBM Plex Mono only when technical data genuinely needs it.

Think like a professional motion editor. Aim for about 28–35 meaningful shots,
usually changing composition every 3–5 seconds, with quicker hook inserts and
enough reading time for difficult ideas. Alternate wide context, close-ups,
mechanism diagrams, comparisons and selective kinetic type. Keep one dominant
action per shot and match it to the current spoken idea.

Pick a recurring explanatory object, such as a coral authentication request.
Preserve its role and spatial continuity across related shots. Use purposeful
zooms, pullbacks, masks, clean match cuts and decisive cuts. Shape speed deliberately
and let secondary details follow the main action. Keep captions stable and crisp.

Make it look like a full-frame film, not a website: no persistent mastheads,
navigation, hero sections, card grids, progress bars or repeated title/icon/paragraph
layouts. Avoid arbitrary spinning, constant shake, glow, particles and exaggerated
bounce. Maintain the same palette, typography roles and motion language throughout.

ASSETS AND COMPANY IDENTIFICATION
Search the bundled asset index first and copy only the needed icons, props,
avatars, fonts and sounds into the project. Use the current detailed icon style
and layered hardware props for computers, phones, servers, keys and boundaries.
Use SVGs for close-ups or independently moving parts; use compact PNGs where suited.

When a real company is named as a subject, pair its correct name with its authentic
logo at introduction and wherever identification matters again. Source the proper
official mark, preserve approved colors/proportions and record its source/use terms.
Do not substitute a generic company avatar or an AI-made brand lookalike.

Create missing artwork only when needed. Match the established style, inspect it,
and cache genuinely reusable originals with descriptive names and provenance.
Use public images only after checking their actual redistribution terms. Keep real
evidence faithful and add the required credits to the sources and YouTube description.

FLOW AND OPTIONAL THREE.JS VISUALIZATION
Stage source and destination, reveal the connector from the source, move the request
along that same route, then show the receiver responding on arrival. Point to real
measured targets and keep arrowheads aligned with the path. Do not animate a private
key leaving its protected location merely to make the diagram more dramatic.

At the important mechanism in the middle, use a short Three.js visualization if
depth or separated layers genuinely make the explanation clearer. Adapt Duckygen’s
seekable example rather than inserting its unrelated demo unchanged. Show one
meaningful state change, keep the sketch palette and matte geometry, overlay sharp
2D labels, then return to the next shot using the same recurring object.
Use 2D if it explains the point better. Label illustrative reconstructions; do not
present a teaching model as recorded traffic or a validated security simulation.

AUDIO AND MUSIC
Compose or use appropriately licensed background music. Let it evolve with the
situation: curiosity for the hook, lower complexity for the mechanism, controlled
tension for a risk, and a fitting resolution for the takeaway. Keep a shared sonic
identity. Change arrangements at meaningful turns rather than on every visual cut.

Duck music and effects beneath speech. Use restrained clicks, paper movements,
drawing cues, contacts and impacts at actual actions. Vary cues; do not attach a loud
whoosh to every cut. Reuse cached effects first and cache useful newly generated
generic sounds with their settings/source and reuse terms. Preserve audio stems.

CLOSING SENTENCE AND CHANNEL LOGO
After the takeaway, say:
“For the latest tech news and cybersecurity updates, subscribe to this channel.”

Show the channel logo beside the subscribe prompt throughout that sentence. Use
my actual supplied channel logo, or the sample assets/chanellogo/log.png indexed as
logos/channel-sample. Preserve its proportions and transparency, keep it clear of
captions, and maintain the film’s light sketch style. Do not invent a channel name.
Keep music below the voice and finish with a short natural musical landing within
the 120-second runtime. Avoid a long goodbye or a stack of engagement requests.

BUILD AND REVIEW
Briefly state the concept and recurring object, show the timed shot plan, then build
without asking about routine choices. Use the deterministic HTML/Canvas route or
the documented Hyperframes route as appropriate. Preserve absolute-time seeking,
asset/font readiness and the requested export settings. Use three temporal samples
per output frame for motion blur while keeping reading text sharp.

Inspect actual frames from every shot, key contacts, transitions and peak motion.
For 3D, verify that seeking to the same time after earlier/later frames gives the
same result. Decode the final MP4 and check its exact duration, frame count, first
and last frames, caption bounds, narration presence, synchronization, audio peaks
and the complete final CTA with its logo. Listen when supported and report review
limitations honestly. Use the same final audio mix in the player and export.

DELIVERABLES
- final.mp4: exactly 120 seconds, 1080p60, H.264/AAC, synchronized English captions.
- Editable HTML/project with the selected source assets, manifests and shot plan.
- narration.txt, captions.srt, source voice clips and audio stems.
- SOURCES.md with research, asset provenance and required attribution.
- about-how-passkeys-work.md with the finished title, copy-ready description,
  comma-separated keywords/tags, accurate sources and valid chapter timestamps;
  include relevant hashtags and useful thumbnail/pinned-comment suggestions.
- Editable metadata JSON, concise verification results and a ZIP of the project.

Use assets, scripts and model context efficiently: search a few relevant records,
read only needed references, reuse reviewed unchanged work and generate only missing
material. Finish the actual video and all deliverables before ending the task.
```

For a news video, replace the example topic with the incident brief and add an exact reporting cutoff. Require company statements, preliminary findings and investigator assessments to stay clearly distinguished in narration, visuals and metadata.


## Short educational requests

```text
$duckygen Explain Newton’s second law to a beginner in a modern animated video.
Show net force, mass and acceleration with connected visual quantities. Compare
one variable at a time, solve a worked example with units, and verify the model.
Deliver the narrated MP4, captions, editable project and sources.
```

```text
$duckygen Why does light bend when it enters water? Make an easy-to-follow modern
animated lesson. Label the normal, calculate a Snell-law example, show the ray
from that calculation, and explain the limits of the geometric-optics model.
```

```text
$duckygen Explain how a CPU cache works using a modern Swiss-motion / isometric
visual treatment. Follow one request through a miss and a hit, define terms beside
the objects, and show the actual mechanism rather than animated title cards.
```
