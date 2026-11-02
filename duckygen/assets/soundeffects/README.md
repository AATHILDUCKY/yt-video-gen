# Reusable sound library

- `cc0/`: 65 selected Kenney effects: 50 interface cues, 12 tactile impacts, and 3 sci-fi/computer textures, decoded from Ogg Vorbis to 48 kHz, 16-bit PCM WAV without gain or timing changes.
- `generated/`: original procedural cues and future reusable generated effects. These have their own source/reuse records; do not assume generated assets are CC0.
- `licenses/`: preserved upstream licenses.

Kenney's source page lists Interface Sounds under CC0: https://kenney.nl/assets/interface-sounds
License: https://creativecommons.org/publicdomain/zero/1.0/
The original CC0 license is in `licenses/kenney-interface-sounds.txt`. Attribution is optional; credit Kenney when useful. Commercial use, adaptation and redistribution are allowed under CC0.

The original direct download returned HTML and the current download-link endpoint was inaccessible. Interface files and their license were retrieved from https://github.com/GeorgeQLe/assets-sfx-ui at revision `760afd035e8fc3cd7fb5bc58d49a967649875e3e`. Additional impact/scifi sources use pinned public mirrors at https://github.com/npmiaman/game-forge and https://github.com/shoemoney/commander-in-chief. Original Kenney pack licenses are retained in `licenses/`; official source pages are https://kenney.nl/assets/impact-sounds and https://kenney.nl/assets/sci-fi-sounds. Retrieved November 1, 2026. `../index.json` records each original filename, pinned download URL, original and converted SHA-256, duration, channels and sample rate.

Use `scripts/asset_tool.py search '<action>' --kind sfx --limit 5` from the skill root. Asset IDs remain `sfx/<name>`. Copy selected files with the tool so their license and source manifest travel into the project. Listen to candidates when supported; filename tags are suggestions, not a claim of subjective audio review.

When a new generic effect is needed, generate it once and cache a usable 16-bit PCM WAV with a descriptive name, action tags, source/settings and reuse terms. `asset_tool.py cache ... --kind sfx` writes to `generated/`, records audio metadata and reuses identical hashes. Supply an external license with `--license-file` when applicable. Keep project-specific narration and private/brand material in their project. If the installed library is not writable, stage the cache update in the project and continue the film.

Only search and load relevant records. Avoid downloading the same packs again, resynthesizing existing cues, loading all audio into a film, or treating every cut as a reason to add sound.
