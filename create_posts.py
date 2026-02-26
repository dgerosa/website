import re
import sys
from datetime import date

def slugify(text):
    return re.sub(r'[^a-z0-9\-]+', '', re.sub(r'\s+', '-', text.lower()))

def parse_date(date_str):
    if date_str is None:
        return date.today().isoformat()

    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", date_str):
        raise ValueError("Date must be in YYYY-MM-DD format.")

    try:
        return date.fromisoformat(date_str).isoformat()
    except ValueError as exc:
        raise ValueError("Date must be a valid calendar date in YYYY-MM-DD format.") from exc

def create_post_file(title, post_date=None):
    today = parse_date(post_date)
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
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print('Usage: python create_posts.py "Your Title Here" [YYYY-MM-DD]')
        sys.exit(1)
    try:
        title_input = sys.argv[1]
        date_input = sys.argv[2] if len(sys.argv) == 3 else None
        create_post_file(title_input, date_input)
    except ValueError as err:
        print(f"Error: {err}")
        sys.exit(1)
