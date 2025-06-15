import requests
import re
from pathlib import Path

# Configuration
username = "dgerosa"
repo_prefixes = {
    "astrostatistics": "astrostatistics_bicocca_",
    "scientificcomputing": "scientificcomputing_bicocca_",
    "machinelearning4physics": "machinelearning4physics_bicocca_"
}
base_path = Path("../_pages")
max_year = 2100

# Function to check the latest existing repo for a course
def find_latest_year(prefix, current_year):
    latest_year = current_year
    for year in range(current_year + 1, max_year):
        repo_name = f"{prefix}{year}"
        url = f"https://api.github.com/repos/{username}/{repo_name}"
        response = requests.get(url)
        if response.status_code == 200:
            latest_year = year
        else:
            break
    return latest_year

# Main loop over all course files
for course, prefix in repo_prefixes.items():
    redirect_file = base_path / f"{course}.md"
    if not redirect_file.exists():
        print(f"⚠️ File not found: {redirect_file}")
        continue

    content = redirect_file.read_text()
    match = re.search(r"https://github\.com/{}/{}(\d+)".format(username, prefix), content)
    if not match:
        print(f"⚠️ Could not find GitHub link in: {redirect_file}")
        continue

    current_year = int(match.group(1))
    latest_year = find_latest_year(prefix, current_year)

    if latest_year > current_year:
        new_url = f"https://github.com/{username}/{prefix}{latest_year}"
        new_content = re.sub(
            r"https://github\.com/{}/{}(\d+)".format(username, prefix),
            new_url,
            content
        )
        redirect_file.write_text(new_content)
        print(f"✅ Updated {course} redirect to {new_url}")
    else:
        print(f"⏩ No update needed for {course} (latest: {current_year})")