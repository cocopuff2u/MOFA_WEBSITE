import xml.etree.ElementTree as ET
from collections import Counter
import logging
import re

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

SEVERITY_ORDER = {"Critical": 0, "Important": 1, "Moderate": 2, "Low": 3}
SEVERITY_BADGES = {"Critical": "danger", "Important": "warning", "Moderate": "info", "Low": "info"}

def parse_cve_history_xml(file_path):
    logging.info(f"Parsing XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("XML file parsed successfully")

    # Extract last_scan_date
    last_scan_date = root.find("last_scan_date").text.strip()
    logging.info(f"XML last_scan_date: {last_scan_date}")

    # Extract update details
    updates = []
    for update in root.findall("Update"):
        version = update.find("Version").text.strip().replace("Version ", "")
        update_info = {
            "date": update.find("Date").text.strip(),
            "version": version,
            "cves": []
        }
        for app in update.find("SecurityUpdates").findall("Application"):
            app_name = app.find("Name").text.strip()
            for cve in app.findall("CVE"):
                cve_name = cve.text.strip()
                if not cve_name.startswith("CVE-"):
                    continue
                update_info["cves"].append({
                    "cve": cve_name,
                    "app": app_name,
                    "severity": cve.get("severity"),
                    "impact": cve.get("impact"),
                    "exploited": cve.get("exploited"),
                })
        updates.append(update_info)

    return last_scan_date, updates

def app_tag(app_name):
    # Colored dot per app; colors live in style.css as .app-<name>
    css_name = re.sub(r'[^a-z0-9]+', '-', app_name.lower()).strip('-')
    return f'<span class="app-tag app-{css_name}">{app_name}</span>'

def cve_url(cve_name):
    return f"https://msrc.microsoft.com/update-guide/vulnerability/{cve_name}"

def severity_badge(cve):
    if not cve["severity"]:
        return "N/A"
    badge = f'<Badge type="{SEVERITY_BADGES.get(cve["severity"], "info")}" text="{cve["severity"]}" />'
    if cve["exploited"] == "Yes":
        badge += ' <Badge type="danger" text="Exploited" />'
    return badge

def count_summary(cves):
    # "23 CVEs · 5 Critical"
    critical = sum(1 for c in cves if c["severity"] == "Critical")
    summary = f"{len(cves)} CVE{'s' if len(cves) != 1 else ''}"
    if critical:
        summary += f" · {critical} Critical"
    exploited = sum(1 for c in cves if c["exploited"] == "Yes")
    if exploited:
        summary += f" · {exploited} Exploited"
    return summary

def render_glance(year, updates):
    cves = [c for u in updates for c in u["cves"]]
    by_app = Counter(c["app"] for c in cves)
    critical_by_app = Counter(c["app"] for c in cves if c["severity"] == "Critical")

    content = f"""
::: tip At a glance ({year})
**{count_summary(cves)}** across {len(updates)} security release{'s' if len(updates) != 1 else ''}

| Application | CVEs | Critical |
|-------------|------|----------|
"""
    for app, count in by_app.most_common():
        content += f"| {app_tag(app)} | {count} | {critical_by_app.get(app, 0)} |\n"
    content += ":::\n"
    return content

def render_release(update):
    cves = sorted(update["cves"], key=lambda c: (SEVERITY_ORDER.get(c["severity"], 9), c["app"], c["cve"]))
    by_app = Counter(c["app"] for c in update["cves"])
    app_summary = " ".join(f"{app_tag(app)} {count}" for app, count in by_app.most_common())

    content = f"""
### {update['version']}

<span class="extra-small">**{update['date']}** · {count_summary(cves)} · {app_summary}</span>

::: details View {len(cves)} CVE{'s' if len(cves) != 1 else ''}
| CVE | Application | Severity | Impact |
|-----|-------------|----------|--------|
"""
    for cve in cves:
        content += f"| [{cve['cve']}]({cve_url(cve['cve'])}) | {app_tag(cve['app'])} | {severity_badge(cve)} | {cve['impact'] or 'N/A'} |\n"
    content += ":::\n"
    return content

def generate_readme_content(last_scan_date, updates):
    logging.info("Generating standalone_cve_history_readme content")

    # Only releases that fixed CVEs; the rest are counted per year
    security_updates = [u for u in updates if u["cves"]]
    updates_by_year = {}
    for update in updates:
        year_match = re.search(r'(\d{4})\s*$', update['date'])
        updates_by_year.setdefault(year_match.group(1) if year_match else "Other", []).append(update)

    content = f"""---
editLink: false
lastUpdated: false
outline: [2, 2]
---
# <img src="/images/Microsoft_Logo.webp" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Office CVE History

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{last_scan_date}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/mac_standalone_cve_history.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/mac_standalone_cve_history.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/mac_standalone_cve_history.json)
 (Automatically Updated every 2 hours)_</span>

Every security vulnerability (CVE) Microsoft has fixed in Microsoft 365 and Office for Mac, grouped by the release that fixed it, newest first. Only releases with security fixes are listed. Sources: [Release notes for Office for Mac](https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac) and the [Microsoft Security Response Center](https://msrc.microsoft.com/update-guide).

<span class="extra-small"><Badge type="danger" text="Critical" /> — can be exploited without user interaction, such as remote code execution<br><Badge type="warning" text="Important" /> — could compromise data or availability, usually requiring user action<br><Badge type="danger" text="Exploited" /> — Microsoft reports active exploitation</span>
"""
    if security_updates:
        latest_year = next(iter(updates_by_year))
        content += render_glance(latest_year, [u for u in updates_by_year[latest_year] if u["cves"]])

    for year, year_updates in updates_by_year.items():
        year_security = [u for u in year_updates if u["cves"]]
        if not year_security:
            continue
        year_cves = [c for u in year_security for c in u["cves"]]
        skipped = len(year_updates) - len(year_security)
        content += f"""
## <span class="year-title">{year}</span> <span class="year-meta ignore-header">{len(year_security)} security release{'s' if len(year_security) != 1 else ''} · {count_summary(year_cves)}</span> {{#year-{year}}}
"""
        if skipped:
            content += f"\n<span class=\"extra-small\">{skipped} other release{'s' if skipped != 1 else ''} this year had no security fixes.</span>\n"
        for update in year_security:
            content += render_release(update)

    content += """
> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    logging.info("standalone_cve_history content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"standalone_cve_history.md has been overwritten.")

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/mac_standalone_cve_history.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/standalone_apps/standalone_cve_history_en.md"

    # Parse the XML and generate content
    last_scan_date, updates = parse_cve_history_xml(xml_file_path)

    readme_content = generate_readme_content(last_scan_date, updates)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)
