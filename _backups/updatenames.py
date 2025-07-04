import os
import re

print("This script updates the dates in filenames and content of posts in the _posts directory based on the correct dates from the _oldposts directory.")
# Directories
posts_dir = "_posts"
oldposts_dir = "_oldposts"

# Regex to extract date and title from filenames
filename_pattern = re.compile(r"(\d{4}-\d{2}-\d{2})-(.+)\.md")

# Build a map from title to date for files in _oldposts
oldposts_map = {}
for fname in os.listdir(oldposts_dir):
    match = filename_pattern.match(fname)
    if match:
        date, title = match.groups()
        oldposts_map[title] = date

# Process files in _posts
for fname in os.listdir(posts_dir):
    match = filename_pattern.match(fname)
    if not match:
        continue
    current_date, title = match.groups()

    if title in oldposts_map:
        correct_date = oldposts_map[title]

        if correct_date != current_date:
            old_path = os.path.join(posts_dir, fname)
            new_fname = f"{correct_date}-{title}.md"
            new_path = os.path.join(posts_dir, new_fname)

            # Read the file
            with open(old_path, "r", encoding="utf-8") as f:
                content = f.read()

            # Replace all instances of the current date with the correct one
            updated_content = content.replace(current_date, correct_date)

            # Write back the updated content
            with open(old_path, "w", encoding="utf-8") as f:
                f.write(updated_content)

            # Rename the file
            os.rename(old_path, new_path)
            print(f"Fixed: {fname} -> {new_fname}")