# Duckygen — Educational Video Skill

A reusable skill that helps an AI coding agent turn a topic into a narrated educational video. Use it for science lessons, animated technical explanations, and YouTube videos about technology or cybersecurity.

Tell the agent what to explain, who the audience is, and how long the video should be. Duckygen guides research, scripting, animation, narration timing, rendering, and review. A completed narrated project includes an MP4, editable files, captions, narration, and sources.

**You need an AI agent such as Codex to use the skill.** The included command-line tools also support manual authoring. Narration requires a separately available voice engine or service.

[Installation](#installation) · [First video](#create-your-first-video) · [Troubleshooting](#troubleshooting) · [Detailed guide](duckygen/README.md) · [Full example prompt](duckygen/example-prompt.md)

## Before you start

The commands below use a Bash-compatible terminal on Linux or macOS.

| Requirement | Why it is needed |
| --- | --- |
| An AI agent that can read skills and run local commands | Uses Duckygen to plan and build your video |
| Python 3.10 or newer | Project tools and audio processing |
| Node.js 22 or newer, with npm | Browser-based preview and rendering |
| FFmpeg and FFprobe | Audio mixing, video encoding, and output checks |
| A narration engine or voice service | Spoken audio for narrated videos |

Playwright, NumPy, and Chromium are installed in the steps below. No voice model, service subscription, or API credentials are bundled. You can validate the package and create a demo without a narration service.

## Installation

### 1. Download the repository

On this GitHub page, select **Code → Download ZIP**, extract it, and open a terminal in the extracted folder. You can also clone the URL shown under **Code** with Git.

You should see `README.md` and a `duckygen/` folder. Run all commands from this repository folder unless a step says otherwise.

### 2. Check your system tools

```bash
python3 --version
node --version
npm --version
ffmpeg -version
ffprobe -version
```

If a command is missing, install that tool before continuing. Check that Python is at least 3.10 and Node is at least 22. Install FFmpeg through your operating system's package manager; FFprobe normally comes with it.

### 3. Install the Python and Node dependencies

```bash
python3 -m venv .venv
. .venv/bin/activate
python3 -m pip install -r duckygen/requirements.txt
npm install --prefix duckygen
```

Keep this terminal open with the virtual environment active while using the tools. The `.venv/` folder keeps Python dependencies local to this checkout.

### 4. Install the rendering browser

```bash
cd duckygen
npx playwright install chromium
cd ..
```

This downloads the Chromium version used by the installed Playwright package. If you already have a compatible browser, you can use its executable path through `CHROME_PATH` instead.

On Linux, if Playwright reports missing system libraries, run its suggested dependency installation command and retry. Installing operating system packages may require administrator access.

### 5. Make the skill available to your agent

Codex discovers user skills in `~/.agents/skills`. On Linux or macOS, link this checkout from the repository root:

```bash
mkdir -p "$HOME/.agents/skills"
ln -s "$PWD/duckygen" "$HOME/.agents/skills/duckygen"
```

Run those commands from the repository root. They link the inner `duckygen/` skill folder, which contains `SKILL.md`. Keep the checkout in place while using this link. If the destination already exists, inspect it before replacing it.

Start a new Codex session if the skill does not appear. Launch your agent from the terminal with `.venv` active so its Python commands can access the installed dependencies. See [official OpenAI skill documentation](https://learn.chatgpt.com/docs/build-skills) for discovery details.

**Other agents:** use the agent's supported skill installation mechanism, or ask it to read `duckygen/SKILL.md` from this checkout and follow the linked references. The direct-file method also lets you try the workflow before registering the skill.

### 6. Check that the package is ready

```bash
npm --prefix duckygen run validate
```

The command should finish successfully, with `valid: true` or `passed: true` in the check reports. It checks documentation links, Python syntax, assets, companion files, and introductory physics helpers. It runs without a browser, voice service, or API credentials; it does not render a video.

## Create your first video

Paste this into your agent's chat after installation:

```text
$duckygen

Create a narrated educational video explaining why objects fall at the same
acceleration in a vacuum.
Audience: beginners.
Duration: approximately 60 seconds.
Format: 16:9, 1920×1080, 60 fps.
Language: English.
Use clear animated examples and explain the assumptions.
Save the project outside this repository in ../my-first-video.
Use an available narration engine or voice service. If none is available,
tell me what is missing and prepare the editable project and narration script.
Include the final MP4, editable project, captions, narration, and sources.
```

Replace the topic, audience, duration, and output folder for your own video. Add a script, trusted source links, voice preference, language, and channel logo when available. For current events, include a reporting cutoff date.

The agent researches and scripts the explanation, measures narration, builds the visuals, reviews frames, and renders the final video when the required tools are available. Ask for changes to the same project to revise wording, timing, visuals, or music.

See the [full example prompt](duckygen/example-prompt.md) for more control over style, sound, and delivery.

## Try the tools without generating narration

From the repository root, with `.venv` active:

```bash
python3 duckygen/scripts/create_project.py \
  --output ../duckygen-demo \
  --title 'My first Duckygen project' \
  --duration 10
```

Open `../duckygen-demo/watch.html` in your browser. This is an editable visual demo with sample content, not a finished narrated explanation. Choose a new output folder if that folder already exists and contains files.

## Manual authoring and rendering

This section is for users who want to edit the project directly. You can let your agent handle these steps for an ordinary video request.

Run these commands from the repository root. Create output outside the repository to keep private projects out of GitHub:

```bash
python3 duckygen/scripts/create_project.py \
  --output ../my-film \
  --title 'How Passkeys Work' \
  --duration 120
```

The generated project is a demo scaffold. Replace its sample story and visuals, prepare and measure narration, align captions and shots, and complete its audio plan before rendering. See the [build workflow](duckygen/references/build.md) and [audio guide](duckygen/references/audio.md) for the audio-plan format and authoring details.

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

## Troubleshooting

| Problem | What to do |
| --- | --- |
| `$duckygen` is unavailable | Check that `~/.agents/skills/duckygen/SKILL.md` exists and start a new agent session. You can also ask the agent to read the skill file directly. |
| `No module named numpy` | Run `. .venv/bin/activate`, then `python3 -m pip install -r duckygen/requirements.txt` from the repository root. |
| `Cannot find module 'playwright'` | Run `npm install --prefix duckygen` from the repository root. |
| Playwright cannot find its browser | Run `npx playwright install chromium` from inside `duckygen/`. |
| Chromium reports missing Linux libraries | Follow Playwright's system-dependency installation instructions, then retry. |
| `ffmpeg` or `ffprobe` is missing | Install FFmpeg and confirm both commands are available in the terminal used by your agent. |
| The agent cannot generate narration | Configure a local narration engine or connected voice service, or supply your own voice recordings. |
| The renderer says the project is a demo | Replace the sample story, visuals, and audio before marking it as a real project; see the build guide. |
| The skill link stops working after moving the repository | Update the symlink to point to the checkout's new location. |

To continue in a new terminal, open the repository folder and run `. .venv/bin/activate` again. Advanced tool overrides are `PLAYWRIGHT_MODULE`, `CHROME_PATH`, `FFMPEG_PATH`, and `FFPROBE_PATH`.

## Package contents

| Path | Purpose |
| --- | --- |
| [duckygen/SKILL.md](duckygen/SKILL.md) | Agent instructions |
| [duckygen/example-prompt.md](duckygen/example-prompt.md) | Detailed, copy-ready request |
| `duckygen/scripts/` | Project creation, audio, rendering, and validation |
| `duckygen/assets/` | Visual assets, fonts, sounds, and runtime helpers |
| `duckygen/references/` | Focused production guides |
| `duckygen/companions/` | Optional companion workflows and attribution |

## Keeping personal projects private

The shared skill is `duckygen/`. The existing local folders `gitlab-alpine/`, `gitlab-alphine/`, `linux-tcp/`, `php2shell/`, `bernoulli/`, and `skill-validation/` are ignored by Git, along with credentials, local settings, dependencies, and caches.

Create new video projects outside the repository, as the examples do. If you create a private project inside it, add that folder to `.gitignore` before staging files. New project folder names are not automatically ignored.

## Before pushing to GitHub

Review exactly what Git will publish:

```bash
git status --short
git add README.md .gitignore .gitattributes .github/ duckygen/
git diff --cached --stat
git diff --cached --name-only
```

`.gitignore` only excludes untracked files. If a private folder was already tracked, remove it from Git's index with `git rm -r --cached -- <folder>`; this keeps the local files. Review any existing commit history separately, since ignoring a folder does not remove earlier commits containing it.

## Licensing and third-party materials

No open-source license has been assigned to Duckygen's original code or documentation. Third-party components keep their existing licenses; see [third-party notices](duckygen/THIRD_PARTY_NOTICES.md) and [asset provenance](duckygen/assets/PROVENANCE.md). The package does not grant rights to separately supplied media, trademarks, or voice services.
