# Atarax Capital

Website of Atarax Capital, an independent systematic trading practice based in Paris.

Live at **https://www.ataraxcapital.com**.

Atarax is named for *ataraxia*, a lucid calm that turbulence cannot reach. The firm builds rules-based strategies in liquid futures markets, validated out-of-sample and executed automatically, with the aim of compounding a small, protected edge with composure rather than predicting markets or winning every day.

## What this repo is

A standalone static site. No build step, no framework, no dependencies: plain HTML, CSS, and a little vanilla JavaScript, served as-is by GitHub Pages.

```
.
├── index.html        # Homepage
├── notes.html        # "Field Notes" — the journal (renders Markdown from notes/)
├── notes/            # One Markdown file per note, plus posts.json (the index)
│   ├── YYYY-MM-DD-slug.md
│   └── posts.json
├── notes_build.py    # Regenerates notes/posts.json from the Markdown files
├── ac-mark.png       # AC monogram (transparent), used in nav and hero
├── favicon-32.png / favicon-64.png / apple-touch-icon.png
├── assets/           # Original logo source files
└── CNAME             # Custom domain (www.ataraxcapital.com)
```

## Writing a note

1. Create `notes/YYYY-MM-DD-some-slug.md` and start it with a title line:

   ```
   # My title
   ```

2. Regenerate the index:

   ```
   python notes_build.py
   ```

3. Commit and push. The note shows up on the Field Notes page, newest first, each reachable at its own `#slug` link.

Markdown is rendered in the browser, and single line breaks are preserved. English or Korean both render.

## Run locally

```
python -m http.server 8090
```

Then open http://localhost:8090.

## Deploy

GitHub Pages serves the `main` branch root at the custom domain in `CNAME`. Pushing to `main` updates the live site. Keep the `CNAME` file in place, or the custom domain will detach.

---

Established 2025 · Paris. Nothing in this repository is investment advice, or an offer to buy or sell any financial instrument. Trading futures involves substantial risk of loss.
