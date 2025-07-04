import os
import re
from bs4 import BeautifulSoup
from pathlib import Path

SOURCE_DIR = "/Users/dgerosa/Documents/reps/myweb/davidegerosa.com"
OUTPUT_DIR = "/Users/dgerosa/Documents/reps/myweb/converted_markdown"

def slugify(text):
    return re.sub(r'[^a-z0-9\-]+', '', re.sub(r'\s+', '-', text.lower()))

import html2text

import html2text

def extract_content(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    # Extract the <title>
    title_tag = soup.find("title")
    if title_tag:
        title_text = title_tag.text.replace(" – Davide Gerosa", "").strip()
    else:
        title_text = "Untitled"

    # Extract tags from <a> with rel="category tag"
    tags = []
    for a in soup.find_all("a", rel="category tag"):
        text = a.get_text(strip=True)
        if text:
            tags.append(text)

    # Extract and convert paragraphs
    paragraphs = soup.find_all("p")
    combined_html = "\n\n".join(str(p) for p in paragraphs)

    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_images = False
    h.ignore_links = False
    h.ignore_emphasis = False
    h.ignore_tables = False
    h.protect_links = True
    h.use_automatic_links = False

    content_md = h.handle(combined_html).strip()

    return title_text, content_md, tags

def process_html_file(html_path):
    rel_path = os.path.relpath(html_path, SOURCE_DIR)
    parts = Path(rel_path).parts

    try:
        year, month, day, slug = parts[0], parts[1], parts[2], parts[3]
    except IndexError:
        print(f"Skipping malformed path: {html_path}")
        return

    date = f"{year}-{month}-{day}"
    filename = f"{date}-{slug}.md"
    permalink = f"/posts/{year}-{month}-{day}-{slug}"

    title, content, tags = extract_content(html_path)
    tag_lines = "\n".join(f"  - {tag}" for tag in tags)

    md_content = (
        "---\n"
        f"title: '{title}'\n"
        f"date: {date}\n"
        f"permalink: {permalink}\n"
        "tags:\n"
        f"{tag_lines}\n"
        "---\n\n"
        f"{content}\n\n"
    )

    out_path = os.path.join(OUTPUT_DIR, filename)
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"Wrote {out_path}")


def main():
    for root, _, files in os.walk(SOURCE_DIR):
        if "index.html" in files:
            html_path = os.path.join(root, "index.html")
            process_html_file(html_path)

if __name__ == "__main__":
    main()