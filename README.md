# sebastianschoenen.github.io

Personal landing page, English (`/`) and German (`/de/`), served by GitHub Pages.

## Editing content

All text lives in `content.py`, once per language (`T["en"]`, `T["de"]`).
`build.py` renders both pages plus `sitemap.xml` and `robots.txt`.

```bash
# edit content.py, then
python3 build.py
git add -A && git commit -m "Update content" && git push
```

`index.html` and `de/index.html` are generated. Do not edit them by hand; edits are lost on the next build.

## Files

| File | Purpose |
|---|---|
| `content.py` | All page content, EN and DE |
| `build.py` | Template, structured data (JSON-LD), sitemap, robots |
| `style.css`, `main.js` | Shared styling and behaviour (tabs, menu, reveal, active nav) |
| `SebastianSchoenen.jpg` | Hero photo, referenced from both pages |
| `og-image.png` | 1200×630 preview image for LinkedIn and other link previews |
| `favicon.svg`, `apple-touch-icon.png` | Icons |

## Frequently changed fields

| What | Where in `content.py` |
|---|---|
| Citation count | `hero_stats`, `pub_note` |
| Team size | `hero_stats`, `about_p[0]`, first entry of `exp` |
| New talk | `talks` (cards, current year) or `talks_more` (compact list) |
| New publication | `pub_groups` |
| Research project status | last field of each `research` entry: `"ongoing"`, `"done"` or `""` |
| Award | `awards`, and the count in `tabs` |

`sitemap.xml` lastmod, the `dateModified` in the structured data and the footer year are set automatically on each build.

## After deploying

Google Search Console: property `https://sebastianschoenen.github.io/` (URL prefix), sitemap `sitemap.xml`.
To refresh the LinkedIn link preview after a change: https://www.linkedin.com/post-inspector/
