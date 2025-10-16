import xml.etree.ElementTree as ET
from datetime import datetime
import pytz
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_latest_xml(file_path):
    logging.info(f"Parsing XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("XML file parsed successfully")

    # Extract global last_updated
    global_last_updated = root.find("last_updated").text.strip()
    logging.info(f"XML last_updated: {global_last_updated}")

    # Extract package details
    packages = {}
    for package in root.findall("package"):
        name = package.find("name").text.strip().lower()  # Store by lowercase name for easy access
        packages[name] = {
            "name": name,
            "application_id": package.find("application_id").text.strip(),
            "application_name": package.find("application_name").text.strip(),
            "short_version": package.find("short_version").text.strip(),
            "full_version": package.find("full_version").text.strip(),
            "last_updated": package.find("last_updated").text.strip(),
            "full_update_sha1": package.find("full_update_sha1").text.strip(),
            "app_only_update_download": package.find("app_only_update_download").text.strip(),
            "app_update_sha256": package.find("app_update_sha256").text.strip(),
            "app_update_sha1": package.find("app_update_sha1").text.strip(),
            "full_update_download": package.find("full_update_download").text.strip(),
            "full_update_sha256": package.find("full_update_sha256").text.strip(),
            "full_update_sha1": package.find("full_update_sha1").text.strip(),
            "min_os": package.find("min_os").text.strip() if package.find("min_os") is not None else "N/A",
        }
        # logging.debug(f"Extracted package: {packages[name]}") # Uncomment to see all package details

    return global_last_updated, packages

def parse_onedrive_xml(file_path):
    logging.info(f"Parsing OneDrive XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("OneDrive XML file parsed successfully")

    # Extract global last_updated
    global_last_updated = root.find("last_updated").text.strip()
    logging.info(f"OneDrive XML last_updated: {global_last_updated}")

    # Extract package details
    onedrive_packages = {}
    for package in root.findall("package"):
        name = package.find("name").text.strip()
        onedrive_packages[name] = {
            "name": name,
            "short_version": package.find("short_version").text.strip(),
            "application_id": package.find("application_id").text.strip(),
            "application_name": package.find("application_name").text.strip(),
            "CFBundleVersion": package.find("CFBundleVersion").text.strip(),
            "full_update_download": package.find("full_update_download").text.strip(),
            "full_update_sha1": package.find("full_update_sha1").text.strip(),
            "full_update_sha256": package.find("full_update_sha256").text.strip(),
            "last_updated": package.find("last_updated").text.strip(),
        }
        # logging.debug(f"Extracted OneDrive package: {onedrive_packages[name]}") # Uncomment for debugging

    return global_last_updated, onedrive_packages

def parse_edge_xml(file_path):
    logging.info(f"Parsing Edge XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("Edge XML file parsed successfully")

    # Extract global last_updated
    global_last_updated = root.find("last_updated").text.strip()
    logging.info(f"Edge XML last_updated: {global_last_updated}")

    # Extract "current" version details
    edge_current_version = {}
    for version in root.findall("Version"):
        if version.find("Name").text.strip().lower() == "current":
            edge_current_version = {
                "name": version.find("Name").text.strip(),
                "version": version.find("Version").text.strip(),
                "application_id": version.find("Application_ID").text.strip(),
                "application_name": version.find("Application_Name").text.strip(),
                "cf_bundle_version": version.find("CFBundleVersion").text.strip(),
                "full_update_download": version.find("Full_Update_Download").text.strip(),
                "full_update_sha1": version.find("Full_Update_Sha1").text.strip(),
                "full_update_sha256": version.find("Full_Update_Sha256").text.strip(),
                "last_updated": version.find("Last_Update").text.strip(),
            }
            break

    return global_last_updated, edge_current_version

def generate_readme_content(global_last_updated, packages):
    logging.info("Generating standalone_main_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    # Parse OneDrive XML
    onedrive_xml_file_path = "repo_raw_data/macos_standalone_onedrive_all.xml"
    onedrive_last_updated, onedrive_packages = parse_onedrive_xml(onedrive_xml_file_path)

    # Parse Edge XML
    edge_xml_file_path = "repo_raw_data/macos_standalone_edge_all.xml"
    edge_last_updated, edge_current_version = parse_edge_xml(edge_xml_file_path)

    def nz(v, default="N/A"):
        return v if v not in (None, "", "N/A") else default

    # Helper to generate a single tile cell
    def render_tile(name, version, last_updated, img_src, rel_notes_url, primary_dl, secondary_dl=None, img_alt=None):
        name_html = name
        version_html = nz(version)
        last_updated_html = nz(last_updated)
        img_alt = img_alt or name_html
        primary_href = primary_dl or "#"
        links_html = f'<a href="{primary_href}">Installer</a>'
        if secondary_dl:
            links_html += f' | <a href="{secondary_dl}">App Only</a>'
        cell = f'''
    <td align="center" class="tile-td">
      <div class="tile-card">
        <div class="tile-media">
          <a href="{primary_href}"><img src="{img_src}" alt="{img_alt or name_html}"></a>
        </div>
        <div class="tile-title"><b>{name_html}</b></div>
        <div class="tile-version"><em><code>{version_html}</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>{last_updated_html}</code></em></small></div>
        <a href="{rel_notes_url}" style="text-decoration: none;"><small>Release Notes</small></a>
        <div class="tile-links">{links_html}</div>
      </div>
    </td>'''.strip()
        return cell

    # Build list of tiles. Primary download favors known FWLinks where used previously; App Only from package when available.
    tiles = []

    # Common Office release notes
    office_rel_notes = "https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac"

    # Suites
    tiles.append(render_tile(
        name="Microsoft Office Suite",
        version=get_standalone_package_detail(packages, 'Microsoft Office Suite', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Microsoft Office Suite', 'last_updated'),
        img_src="/images/Office_Suite.webp",
        rel_notes_url=office_rel_notes,
        primary_dl="https://go.microsoft.com/fwlink/?linkid=525133",
        secondary_dl=None
    ))
    tiles.append(render_tile(
        name="Microsoft BusinessPro Suite",
        version=get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'last_updated'),
        img_src="/images/Office_Suite.webp",
        rel_notes_url=office_rel_notes,
        primary_dl="https://go.microsoft.com/fwlink/?linkid=2009112",
        secondary_dl=None
    ))

    # Core Office apps
    tiles.append(render_tile(
        name="Word",
        version=get_standalone_package_detail(packages, 'Word', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Word', 'last_updated'),
        img_src="/images/2025/Word.webp",
        rel_notes_url=office_rel_notes,
        primary_dl="https://go.microsoft.com/fwlink/?linkid=525134",
        secondary_dl=get_standalone_package_detail(packages, 'Word', 'app_only_update_download')
    ))
    tiles.append(render_tile(
        name="Excel",
        version=get_standalone_package_detail(packages, 'Excel', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Excel', 'last_updated'),
        img_src="/images/2025/Excel.webp",
        rel_notes_url=office_rel_notes,
        primary_dl="https://go.microsoft.com/fwlink/?linkid=525135",
        secondary_dl=get_standalone_package_detail(packages, 'Excel', 'app_only_update_download')
    ))
    tiles.append(render_tile(
        name="PowerPoint",
        version=get_standalone_package_detail(packages, 'PowerPoint', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'PowerPoint', 'last_updated'),
        img_src="/images/2025/PowerPoint.webp",
        rel_notes_url=office_rel_notes,
        primary_dl="https://go.microsoft.com/fwlink/?linkid=525136",
        secondary_dl=get_standalone_package_detail(packages, 'PowerPoint', 'app_only_update_download')
    ))
    tiles.append(render_tile(
        name="Outlook",
        version=get_standalone_package_detail(packages, 'Outlook', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Outlook', 'last_updated'),
        img_src="/images/2025/Outlook.webp",
        rel_notes_url=office_rel_notes,
        primary_dl="https://go.microsoft.com/fwlink/?linkid=525137",
        secondary_dl=get_standalone_package_detail(packages, 'Outlook', 'app_only_update_download')
    ))
    tiles.append(render_tile(
        name="OneNote",
        version=get_standalone_package_detail(packages, 'OneNote', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'OneNote', 'last_updated'),
        img_src="/images/2025/OneNote.webp",
        rel_notes_url=office_rel_notes,
        primary_dl="https://go.microsoft.com/fwlink/?linkid=820886",
        secondary_dl=get_standalone_package_detail(packages, 'OneNote', 'app_only_update_download')
    ))

    # OneDrive (Production Ring)
    tiles.append(render_tile(
        name="OneDrive (Production)",
        version=get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'short_version'),
        last_updated=get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'last_updated'),
        img_src="/images/2025/OneDrive.webp",
        rel_notes_url="https://support.microsoft.com/en-us/office/onedrive-release-notes-845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac",
        primary_dl=get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'full_update_download'),
        secondary_dl=None
    ))

    # Teams
    tiles.append(render_tile(
        name="Teams",
        version=get_standalone_package_detail(packages, 'Teams', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Teams', 'last_updated'),
        img_src="/images/2025/Teams.webp",
        rel_notes_url="https://support.microsoft.com/en-us/office/what-s-new-in-microsoft-teams-d7092a6d-c896-424c-b362-a472d5f105de",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=2249065",
        secondary_dl=None
    ))

    # Intune Company Portal
    tiles.append(render_tile(
        name="Intune Company Portal",
        version=get_standalone_package_detail(packages, 'Intune', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Intune', 'last_updated'),
        img_src="/images/companyportal.png",
        rel_notes_url="https://aka.ms/intuneupdates",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=853070",
        secondary_dl=get_standalone_package_detail(packages, 'Intune', 'app_only_update_download')
    ))

    # Edge (Current channel)
    tiles.append(render_tile(
        name="Edge (Current)",
        version=edge_current_version.get('version', 'N/A'),
        last_updated=edge_current_version.get('last_updated', 'N/A'),
        img_src="/images/edge_app.png",
        rel_notes_url="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel",
        primary_dl=edge_current_version.get('full_update_download'),
        secondary_dl=None,
        img_alt="Edge"
    ))

    # Defender
    tiles.append(render_tile(
        name="Defender for Endpoint",
        version=get_standalone_package_detail(packages, 'Defender For Endpoint', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Defender For Endpoint', 'last_updated'),
        img_src="/images/defender_512x512x32.png",
        rel_notes_url="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=2097502",
        secondary_dl=None
    ))
    tiles.append(render_tile(
        name="Defender for Consumers",
        version=get_standalone_package_detail(packages, 'Defender For Consumers', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Defender For Consumers', 'last_updated'),
        img_src="/images/defender_512x512x32.png",
        rel_notes_url="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=2247001",
        secondary_dl=None
    ))
    tiles.append(render_tile(
        name="Defender Shim",
        version=get_standalone_package_detail(packages, 'Defender Shim', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Defender Shim', 'last_updated'),
        img_src="/images/defender_512x512x32.png",
        rel_notes_url="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew",
        primary_dl=get_standalone_package_detail(packages, 'Defender Shim', 'full_update_download') or get_standalone_package_detail(packages, 'Defender Shim', 'app_only_update_download'),
        secondary_dl=get_standalone_package_detail(packages, 'Defender Shim', 'app_only_update_download')
    ))

    # Windows App (Remote Desktop)
    tiles.append(render_tile(
        name="Windows App (Remote Desktop)",
        version=get_standalone_package_detail(packages, 'Windows App', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Windows App', 'last_updated'),
        img_src="/images/windowsapp.png",
        rel_notes_url="https://learn.microsoft.com/en-us/windows-app/whats-new?tabs=macos",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=868963",
        secondary_dl=get_standalone_package_detail(packages, 'Windows App', 'app_only_update_download')
    ))

    # VS Code
    tiles.append(render_tile(
        name="Visual Studio Code",
        version=get_standalone_package_detail(packages, 'Visual', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Visual', 'last_updated'),
        img_src="/images/Code_512x512x32.png",
        rel_notes_url="https://code.visualstudio.com/updates/",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=2156837",
        secondary_dl=None
    ))

    # Copilot
    tiles.append(render_tile(
        name="Microsoft Copilot",
        version=get_standalone_package_detail(packages, 'Copilot', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Copilot', 'last_updated'),
        img_src="/images/2025/Copilot.webp",
        rel_notes_url="https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes?tabs=mac",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=2325438",
        secondary_dl=None
    ))

    # MAU
    tiles.append(render_tile(
        name="Microsoft AutoUpdate (MAU)",
        version=get_standalone_package_detail(packages, 'MAU', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'MAU', 'last_updated'),
        img_src="/images/autoupdate.png",
        rel_notes_url="https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=830196",
        secondary_dl=None
    ))

    # Build table with 6 items per row
    rows_html = []
    for i in range(0, len(tiles), 6):
        row_cells = "\n".join(tiles[i:i+6])
        rows_html.append(f"<tr>\n{row_cells}\n</tr>")
    # Use a simple 100% width wrapper to avoid horizontal overflow
    table_html = (
        '<div class="grid-wrap">'
        '<table class="grid-table">'
        + "\n".join(rows_html) +
        "</table></div>"
    )

    content = f"""---
editLink: false
lastUpdated: false
layout: doc
navbar: false
sidebar: false
footer: true
aside: false
prev: false
next: false 
---
<style>
  /* Prevent page horizontal scroll */
  html, body {{
    overflow-x: hidden;
  }}

  /* 100% width grid wrapper (no 100vw to avoid overflow) */
  .grid-wrap {{
    width: 100%;
    margin: 0 auto;
    overflow-x: hidden;
  }}

  /* Table sizing: subtract outer border-spacing to avoid overflow */
  .grid-table {{
    width: calc(100% - 32px);    /* accounts for left+right border-spacing (16px each) */
    margin: 0 auto;
    table-layout: fixed;         /* equal column widths */
    border-collapse: separate;
    border-spacing: 16px 16px;   /* gaps between tiles */
  }}

  /* Equal-height tile layout */
  .tile-td {{
    padding: 12px 10px;
    vertical-align: top;
  }}
  .tile-card {{
    width: 100%;                 /* flexible width, fits the column */
    max-width: 200px;            /* cap tile width for consistency */
    display: flex;
    flex-direction: column;
    align-items: center;
    gap: 6px;
    text-align: center;
    margin: 0 auto;              /* center card in its cell */
  }}
  .tile-media {{
    height: 92px;                /* fixed icon block height */
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .tile-media img {{
    max-height: 80px;            /* constrain icon size */
    width: auto;
    height: auto;
  }}
  .tile-title {{
    min-height: 44px;            /* fixed title block height for 1-2 lines */
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .tile-version {{
    min-height: 28px;            /* version block height */
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .tile-updated {{
    min-height: 44px;            /* ensure consistent space for dates */
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .tile-links {{
    margin-top: 6px;
  }}

  /* Optional: slightly tighter at smaller widths */
  @media (max-width: 1100px) {{
    .grid-table {{ border-spacing: 12px 12px; width: calc(100% - 24px); }}
    .tile-media {{ height: 84px; }}
    .tile-media img {{ max-height: 72px; }}
  }}
</style>

<div style="text-align: center;">

_Last Updated: <code style="color : dodgerblue">{global_last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json) (Automatically Updated every 2 hours)_
</div>

<<<<<<< HEAD:update_readme_scripts/update_standalone_current_version_minimal.py
<div class="status-bar">
      <div class="status-line">
        <span>Last Updated: <code class="status-ts">{global_last_updated}</code></span>
        <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml"><strong>Raw XML</strong></a>
        <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml"><strong>Raw YAML</strong></a>
        <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json"><strong>Raw JSON</strong></a>
        <span class="muted">(Automatically updated every 2 hours)</span>
      </div>
      <span class="appearance-toggle-inline">
        <button id="appearance-toggle" class="VPSwitch VPSwitchAppearance" type="button" role="switch" title="Switch theme" aria-checked="false">
          <span class="check"><span class="icon"><span class="vpi-sun sun"></span><span class="vpi-moon moon"></span></span></span>
        </button>
      </span>
    </div>

{grid_html}
=======
{table_html}
>>>>>>> parent of 1cde9ec42d (add minimal page):update_readme_scripts/update_standalone_current_version_mininum.py
"""
    logging.info("standalone_current_version content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"standalone_current_version.md has been overwritten.")

def get_standalone_package_detail(packages, package_name, detail):
    package_name = package_name.lower()
    detail = detail.lower()

    if package_name in packages and detail in packages[package_name]:
        return packages[package_name][detail]
    else:
        return None

def get_onedrive_package_detail(onedrive_packages, package_name, detail):
    package_name = package_name.strip()
    detail = detail.strip()

    if package_name in onedrive_packages and detail in onedrive_packages[package_name]:
        return onedrive_packages[package_name][detail]
    else:
        return None

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_standalone_latest.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/mininum.md"

    # Parse the XML and generate content
    global_last_updated, packages = parse_latest_xml(xml_file_path)

    readme_content = generate_readme_content(global_last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)