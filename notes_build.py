"""
Regenerate notes/posts.json from the markdown files in notes/.

Workflow:
  1. Write a file:  notes/YYYY-MM-DD-some-slug.md
     Start it with a title line:  # My title
  2. Run:           python notes_build.py
The Notes page (notes.html) reads posts.json and renders each note.
No third-party packages required.
"""
import os
import json
import re

NOTES_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "notes")


def title_of(path, slug):
    with open(path, encoding="utf-8") as f:
        for line in f:
            s = line.strip()
            if s.startswith("# "):
                return s[2:].strip()
    return slug.replace("-", " ").strip().capitalize()


def main():
    posts = []
    for name in sorted(os.listdir(NOTES_DIR)):
        if not name.endswith(".md"):
            continue
        m = re.match(r"(\d{4}-\d{2}-\d{2})-(.+)\.md$", name)
        if m:
            date, slug = m.group(1), m.group(2)
        else:
            date, slug = "", name[:-3]
        posts.append({
            "file": name,
            "title": title_of(os.path.join(NOTES_DIR, name), slug),
            "date": date,
        })

    posts.sort(key=lambda p: p["date"], reverse=True)
    out = os.path.join(NOTES_DIR, "posts.json")
    with open(out, "w", encoding="utf-8") as f:
        json.dump(posts, f, ensure_ascii=False, indent=2)
    print("wrote %s with %d note(s)" % (out, len(posts)))


if __name__ == "__main__":
    main()
