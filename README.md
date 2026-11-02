# YouTube Video Generation

Documentation for a local workflow that creates narrated educational videos about science, mathematics, technology, and cybersecurity using Duckygen.

## What is shared on GitHub

This repository shares the workflow documentation and `.gitignore`. The following local folders are excluded:

- `duckygen/` — the local skill, scripts, references, and asset library.
- `gitlab-alpine/` and `gitlab-alphine/` — both spellings are ignored.
- `linux-tcp/`
- `php2shell/`
- `bernoulli/`
- `skill-validation/`

Credentials, local agent settings, dependencies, caches, render output, and review frames are also ignored. Keep new private video projects outside the repository or add their folder paths to `.gitignore` before staging files.

**The Duckygen skill is excluded at your request. Cloning this repository alone does not install the skill or provide its scripts and assets.** The usage examples below require a separately available local copy of Duckygen.

## Local requirements

- Python 3 with NumPy for audio processing and helper scripts.
- Node.js with the Playwright package available to the renderer.
- A Chrome/Chromium browser compatible with Playwright.
- FFmpeg and FFprobe available on `PATH`.
- A local narration engine or connected voice generation service for narrated videos.

Reuse installed tools where available. Optional environment overrides are `PLAYWRIGHT_MODULE`, `CHROME_PATH`, `FFMPEG_PATH`, and `FFPROBE_PATH`. Keep API keys and credentials in local environment settings; never commit them.

## Request a video

With Duckygen separately installed in a compatible agent environment, use a prompt such as:

```text
$duckygen

Create a narrated YouTube explainer about how passkeys work.
Audience: everyday technology users.
Duration: approximately 120 seconds.
Format: 16:9, 1920×1080, 60 fps.
Language: English.
Explain the mechanism and its limitations with clear animated examples.
Include the final MP4, editable project, captions, narration, and sources.
```

Provide a target audience, topic, duration, language, voice preference, source material, and any channel branding. For current events, include a reporting cutoff date.

## Local authoring and rendering

These commands assume you are in this workspace and have the private `duckygen/` folder. Create output outside the repository to keep private projects out of GitHub:

```bash
python3 duckygen/scripts/create_project.py \
  --output ../my-film \
  --title 'How Passkeys Work' \
  --duration 120
```

The generated project is a demo scaffold. Replace its sample story and visuals, prepare and measure narration, align captions and shots, and complete its audio plan before rendering. Follow the locally supplied Duckygen documentation for the audio-plan format and authoring details.

```bash
python3 duckygen/scripts/explainer_audio.py build \
  ../my-film/audio-plan.json --out ../my-film/audio

node duckygen/scripts/render_film.cjs \
  ../my-film/film.html --preview --subframes 1
```

Inspect the preview frames and resolve visual or timing issues. After completing the visual review and replacing the demo content, render with the measured audio mix:

```bash
node duckygen/scripts/render_film.cjs \
  ../my-film/film.html --reviewed --subframes 3 \
  --audio ../my-film/audio/soundtrack.wav \
  --output ../my-film/final.mp4
```

Check the final video for complete narration, readable captions, audio synchronization, correct duration, and working playback. Preserve editable sources and attribution alongside the export.

## Expected deliverables

- `final.mp4` with H.264 video and AAC audio.
- Editable HTML/project files and selected assets.
- Narration text, captions, and original audio clips.
- Sources, asset provenance, and license records.
- Shot plan, asset manifest, and verification notes.
- A YouTube title, description, and tags when requested.

## Before pushing to GitHub

Review exactly what Git will publish:

```bash
git status --short
git add README.md .gitignore
git diff --cached --stat
git diff --cached --name-only
```

`.gitignore` only excludes untracked files. If a private folder was already tracked, remove it from Git's index with `git rm -r --cached -- <folder>`; this keeps the local files. Review any existing commit history separately, since ignoring a folder does not remove earlier commits containing it.

Only redistribute assets and third-party components under their applicable licenses. This documentation does not grant rights to separately supplied code, media, trademarks, or voice services.
