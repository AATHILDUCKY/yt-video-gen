# YouTube metadata after the film

For every completed video, deliver `about-{video-name}.md` beside final.mp4 and include it in the editable ZIP. Use a short lowercase hyphenated filename, such as `about-how-passkeys-work.md`. This is authored for the actual final cut, not copied from a previous video's SEO text. Never publish or upload merely because metadata was requested.

Include a clear, accurate video title, a copy-ready natural-language description, and one comma-separated keyword/tag line. Lead the description with the actual topic and value to the viewer; mention one or two relevant search phrases naturally. Add sources, reporting cutoff and necessary uncertainty for news; preserve attribution and credit requirements. Do not repeat the keyword list in the description, invent search volumes, promise rankings, use unrelated trending names or exaggerate claims for clicks.

Useful additional items: actual chapter timestamps, up to a few relevant hashtags, a concise thumbnail-text suggestion, a pinned-comment suggestion, language and a suggested category. Do not fabricate channel links, handles or a sponsor. Keep optional audience-setting notes content-specific; an animated style alone does not determine whether a film is made for kids. Describe synthetic media accurately where needed; do not claim an upload disclosure setting has been selected.

## Reusable formatter

Write the film-specific content once in `youtube-metadata.json`, then format with:

```bash
python3 <skill>/scripts/write_youtube_about.py my-film/youtube-metadata.json --project my-film --name how-passkeys-work
```

Required fields: `title` (string), `description` (string) and `keywords` (array of individual strings). Optional: `duration` in seconds, `chapters` as `{start, label}` objects, `sources` as `{title, url}`, `credits`, `disclosure`, `hashtags` (strings with #), `thumbnail_text`, `pinned_comment`, `language`, `category`, `audience_note`. The formatter never invents missing content or uploads anything. Use `--replace` only when intentionally updating an existing file. Preserve the JSON as editable source.

Keep the title within 100 characters and the assembled description within the upload limit; the helper conservatively enforces 5,000 UTF-8 bytes for API compatibility. Keep tag text within its budget; choose focused relevant terms, including useful spelling variants. YouTube says title, thumbnail and description matter more for discovery than tags. Chapters must match the encoded film: begin at 00:00, include at least three timestamps in ascending order, and keep each chapter at least 10 seconds long. Omit invalid chapters rather than inventing extra runtime. Refresh metadata if narration, facts or chapter timing changes.

Primary references, researched November 1, 2026:
- https://support.google.com/youtube/answer/12948449 — description guidance.
- https://support.google.com/youtube/answer/146402 — tags and their limited discovery role.
- https://support.google.com/youtube/answer/9884579 — chapter requirements.
- https://developers.google.com/youtube/data/reference/rest/v3/videos — upload metadata limits; verify current API documentation before integration.
