import re
import sys
from datetime import date

def slugify(text):
    return re.sub(r'[^a-z0-9\-]+', '', re.sub(r'\s+', '-', text.lower()))

def create_post_file(title):
    today = date.today().isoformat()  # YYYY-MM-DD
    slug = slugify(title)
    filename = f"{today}-{slug}.md"

    content = f"""---
title: "{title}"
date: {today}
permalink: /posts/{today}-{slug}
tags:
  - 
---
"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"File created: {filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python create_post.py \"Your Title Here\"")
        sys.exit(1)
    title_input = sys.argv[1]
    create_post_file(title_input)