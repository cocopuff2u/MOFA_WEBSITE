import xml.etree.ElementTree as ET
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Heading and intro for each cloud, keyed by the cloud attribute in the XML
CLOUD_SECTIONS = {
    "Public": ("Public Cloud", "Commercial and education tenants."),
    "Government": ("Government Cloud", "US Government tenants (GCC, GCC High and DoD). These clouds receive builds on their own schedule, separate from the public cloud."),
}

# Short headings so the page outline doesn't truncate, keyed by platform id in the XML
PLATFORM_HEADINGS = {
    "mac": "New Teams",
    "ios": "Teams for iOS",
    "classic_mac": "Classic Teams",
    "mac_gcc": "New Teams (GCC)",
    "mac_gcch": "New Teams (GCCH)",
    "mac_dod": "New Teams (DoD)",
    "classic_mac_gcc": "Classic Teams (GCC)",
    "classic_mac_gcch": "Classic Teams (GCCH)",
    "classic_mac_dod": "Classic Teams (DoD)",
}

# Intro shown above each platform table, keyed by platform id in the XML
PLATFORM_NOTES = {
    "mac": "The current Teams client for macOS (bundle ID `com.microsoft.teams2`). Each build links to its full installer package.",
    "ios": "Teams for iPhone and iPad. Updates are delivered through the App Store, so there are no installer packages.",
    "classic_mac": "Classic Teams (bundle ID `com.microsoft.teams`) is retired and no longer receives updates. Kept here for reference.",
}

def parse_teams_history_xml(file_path):
    logging.info(f"Parsing XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("XML file parsed successfully")

    # Extract last_scan_date
    last_scan_date = root.find("last_scan_date").text.strip()
    logging.info(f"XML last_scan_date: {last_scan_date}")

    # Extract release details per platform
    platforms = []
    for platform in root.findall("platform"):
        releases = []
        for release in platform.findall("release"):
            releases.append({child.tag: (child.text or "").strip() for child in release})
        platforms.append({
            "id": platform.get("id"),
            "name": platform.get("name"),
            "cloud": platform.get("cloud", "Public"),
            "releases": releases,
        })
        logging.info(f"Extracted {len(releases)} releases for {platform.get('name')}")

    return last_scan_date, platforms

def cell(release, field):
    # Blank or "NA" values from the scraper show as N/A
    value = release.get(field, "")
    return value if value not in ("", "NA") else "N/A"

def render_platform_table(platform):
    releases = platform["releases"]
    has_installer = any("archive" in r for r in releases)
    has_electron = any("electron_version" in r for r in releases)

    content = f"\n### {PLATFORM_HEADINGS.get(platform['id'], platform['name'])}\n"
    if platform["id"] in PLATFORM_NOTES:
        content += f"\n{PLATFORM_NOTES[platform['id']]}\n"

    if not releases:
        return content + "\n_No releases listed._\n"

    # Latest build stays visible while the full history is collapsed
    latest = releases[0]
    latest_rolling_out = " (rolling out)" if latest.get("rolling_out") == "true" else ""
    content += f"\n**Latest:** `{latest['version']}` <span class='extra-small'>{latest['date']}{latest_rolling_out}</span>\n"

    content += f"""
::: details Version history ({len(releases)} builds)
<table class="shrink-table">
  <thead>
    <tr>
      <th>Release year</th>
      <th>Release date</th>
      <th>Teams version</th>
      <th>SlimCore version</th>
"""
    if has_electron:
        content += "      <th>Electron version</th>\n"
    if has_installer:
        content += "      <th>Installer</th>\n"
    content += """    </tr>
  </thead>
  <tbody>
"""
    for release in releases:
        # Split "October 01, 2026" back into Microsoft's year and date columns
        month_day, _, year = release['date'].rpartition(", ")
        rolling_out = " (rolling out)" if release.get("rolling_out") == "true" else ""
        content += f"    <tr>\n"
        content += f"      <td>{year}</td>\n"
        content += f"      <td>{month_day}{rolling_out}</td>\n"
        content += f"      <td>{release['version']}</td>\n"
        content += f"      <td>{cell(release, 'slimcore_version')}</td>\n"
        if has_electron:
            content += f"      <td>{cell(release, 'electron_version')}</td>\n"
        if has_installer:
            if release.get("archive") == "true":
                content += f"      <td>archived</td>\n"
            elif release.get("installer_download"):
                content += f"      <td><a href=\"{release['installer_download']}\">Installer</a></td>\n"
            else:
                content += f"      <td>N/A</td>\n"
        content += f"    </tr>\n"

    content += """  </tbody>
</table>
:::
"""
    return content

def generate_readme_content(last_scan_date, platforms):
    logging.info("Generating teams_update_history_readme content")

    content = f"""---
editLink: false
lastUpdated: false
outline: [2, 3]
---
# <img src="/images/2025/Teams.webp" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Teams Update History

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{last_scan_date}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/teams_update_history.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/teams_update_history.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/teams_update_history.json)
 (Automatically Updated every 2 hours)_</span>

Every Teams build Microsoft has released for Apple platforms, newest first. Source: [Microsoft Teams app versioning](https://learn.microsoft.com/en-us/officeupdates/teams-app-versioning).
"""
    for cloud, (heading, intro) in CLOUD_SECTIONS.items():
        cloud_platforms = [p for p in platforms if p["cloud"] == cloud]
        if not cloud_platforms:
            continue
        content += f"\n## {heading}\n\n{intro}\n"
        for platform in cloud_platforms:
            content += render_platform_table(platform)

    content += """
> [!NOTE]
> Microsoft notes that builds can be replaced while they roll out, so a version shown in your Teams client may not appear here. Builds marked **(rolling out)** have not yet reached every user.

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    logging.info("teams_update_history content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"teams_update_history_en.md has been overwritten.")

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/teams_update_history.xml"
    readme_file_path = "docs/standalone_apps/teams_update_history_en.md"

    # Parse the XML and generate content
    last_scan_date, platforms = parse_teams_history_xml(xml_file_path)

    readme_content = generate_readme_content(last_scan_date, platforms)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)
