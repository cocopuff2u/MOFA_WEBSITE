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
        # Use button-styled links instead of a text separator
        links_html = f'<a class="btn" href="{primary_href}">Installer</a>'
        if secondary_dl:
            links_html += f' <a class="btn" href="{secondary_dl}">App Only</a>'
        cell = f'''
    <div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="{primary_href}"><img src="{img_src}" alt="{img_alt}"></a>
        </div>
        <div class="tile-title"><b>{name_html}</b></div>
        <div class="tile-version"><em><code>{version_html}</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>{last_updated_html}</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="{rel_notes_url}"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">{links_html}</div>
      </div>
    </div>'''.strip()
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
        name="Microsoft Business Pro Suite",
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
        name="OneDrive",
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
        name="Company Portal",
        version=get_standalone_package_detail(packages, 'Intune', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Intune', 'last_updated'),
        img_src="/images/2021/Company_Portal.webp",
        rel_notes_url="https://aka.ms/intuneupdates",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=853070",
        secondary_dl=get_standalone_package_detail(packages, 'Intune', 'app_only_update_download')
    ))

    # Edge (Current channel)
    tiles.append(render_tile(
        name="Edge",
        version=edge_current_version.get('version', 'N/A'),
        last_updated=edge_current_version.get('last_updated', 'N/A'),
        img_src="/images/edge/edge.webp",
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
        img_src="/images/2025/Defender.webp",
        rel_notes_url="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=2097502",
        secondary_dl=None
    ))
    tiles.append(render_tile(
        name="Defender for Consumers",
        version=get_standalone_package_detail(packages, 'Defender For Consumers', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Defender For Consumers', 'last_updated'),
        img_src="/images/2025/Defender.webp",
        rel_notes_url="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=2247001",
        secondary_dl=None
    ))
    tiles.append(render_tile(
        name="Defender Shim",
        version=get_standalone_package_detail(packages, 'Defender Shim', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Defender Shim', 'last_updated'),
        img_src="/images/2025/Defender.webp",
        rel_notes_url="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew",
        primary_dl=get_standalone_package_detail(packages, 'Defender Shim', 'full_update_download') or get_standalone_package_detail(packages, 'Defender Shim', 'app_only_update_download'),
        secondary_dl=None
    ))

    # Windows App (Remote Desktop)
    tiles.append(render_tile(
        name="Windows App",
        version=get_standalone_package_detail(packages, 'Windows App', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Windows App', 'last_updated'),
        img_src="/images/2025/Windows_App.webp",
        rel_notes_url="https://learn.microsoft.com/en-us/windows-app/whats-new?tabs=macos",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=868963",
        secondary_dl=get_standalone_package_detail(packages, 'Windows App', 'app_only_update_download')
    ))

    # VS Code
    tiles.append(render_tile(
        name="Visual Studio Code",
        version=get_standalone_package_detail(packages, 'Visual', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'Visual', 'last_updated'),
        img_src="/images/2021/Code.webp",
        rel_notes_url="https://code.visualstudio.com/updates/",
        primary_dl="https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal-dmg",
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
        name="Microsoft AutoUpdate",
        version=get_standalone_package_detail(packages, 'MAU', 'short_version'),
        last_updated=get_standalone_package_detail(packages, 'MAU', 'last_updated'),
        img_src="/images/2019/AutoUpdate.webp",
        rel_notes_url="https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate",
        primary_dl="https://go.microsoft.com/fwlink/?linkid=830196",
        secondary_dl=None
    ))

    # Build responsive grid (max 6 columns; fewer on smaller screens)
    grid_items_html = "\n".join(tiles)
    grid_html = (
        '<div class="grid-wrap">'
        '<div class="grid">'
        + grid_items_html +
        '</div></div>'
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
  /* NEW: Status bar styles (fix Markdown-in-HTML issue and wrapping) */
  .status-bar {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    text-align: center;
    margin-bottom: 8px;
  }}
  .status-line {{
    display: inline-flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 8px;
    max-width: 100%;
  }}
  .status-line code.status-ts {{
    color: dodgerblue;
  }}
  .status-line a {{
    text-decoration: none;
    font-weight: 600;
    opacity: 0.9;
  }}
  .status-line a:hover {{
    text-decoration: underline;
    opacity: 1;
  }}
  .status-line .muted {{
    opacity: 0.8;
  }}

  /* If color-mix is supported, derive palette from theme vars for better theming */
  @supports (color: color-mix(in oklab, white 50%, black)) {{
    .grid-wrap {{
      --btn-bg1: color-mix(in oklab, var(--vp-c-bg, #ffffff) 90%, white);
      --btn-bg2: color-mix(in oklab, var(--vp-c-bg, #ffffff) 70%, #d8dde7);
      --btn-bg1-hover: color-mix(in oklab, var(--btn-bg1) 88%, white);
      --btn-bg2-hover: color-mix(in oklab, var(--btn-bg2) 88%, white);
      --btn-border: color-mix(in oklab, var(--vp-c-text, #111) 28%, transparent);
      --btn-text: color-mix(in oklab, var(--vp-c-text, #111) 98%, black);
    }}
    @media (prefers-color-scheme: dark) {{
      .grid-wrap {{
        --btn-bg1: color-mix(in oklab, var(--vp-c-bg, #1e1e20) 85%, #3a3a3c);
        --btn-bg2: color-mix(in oklab, var(--vp-c-bg, #1e1e20) 70%, #2a2a2d);
        --btn-bg1-hover: color-mix(in oklab, var(--btn-bg1) 88%, #4a4a4d);
        --btn-bg2-hover: color-mix(in oklab, var(--btn-bg2) 88%, #36363a);
        --btn-border: color-mix(in oklab, var(--vp-c-text, #ddd) 22%, transparent);
        --btn-text: color-mix(in oklab, var(--vp-c-text, #ddd) 96%, white);
      }}
    }}
  }}

  /* Inline appearance toggle next to the status line */
  .appearance-toggle-inline {{
    display: inline-flex;
    align-items: center;
    margin-left: 8px;
    vertical-align: middle;
  }}

  /* SCOPE SWITCH STYLES to this page only to avoid leaking to other pages */
  .mofa-minimal .VPSwitch {{
    position: relative;
    width: 46px;
    height: 26px;
    border-radius: 999px;
    border: 1px solid var(--vp-c-divider, rgba(0,0,0,0.12));
    background: var(--vp-c-bg-soft, rgba(0,0,0,0.06));
    cursor: pointer;
    transition: background .2s ease, border-color .2s ease;
    pointer-events: auto;
  }}
  .mofa-minimal .VPSwitch .check {{
    position: absolute;
    top: 2px;
    left: 2px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: var(--vp-c-bg, #ffffff);
    box-shadow: 0 1px 2px rgba(0,0,0,0.15);
    transition: transform .2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .mofa-minimal .VPSwitch[aria-checked="true"] .check {{
    transform: translateX(20px);
  }}

  /* Show sun in light, moon in dark (scoped) */
  .mofa-minimal .VPSwitch .icon .sun, .mofa-minimal .VPSwitch .icon .moon {{ display: none; }}
  html:not(.dark) .mofa-minimal .VPSwitch .icon .sun {{ display: inline-block; }}
  html.dark .mofa-minimal .VPSwitch .icon .moon {{ display: inline-block; }}

  /* Center wrapper for the MOFA hero title */
  .brand-hero {{
    display: grid;
    place-items: center;
    min-height: 0;
    padding: 8px 0;
    overflow: visible;
  }}
  @supports (height: 100svh) {{
    .brand-hero {{ min-height: 0; }}
  }}

  /* Ensure the link itself centers and only the text is clickable */
  .brand-title {{
    display: inline-block;    /* was block – limit clickable area to text */
    text-align: center;
    margin: 0;                /* remove auto margins that add width */
    line-height: 1.05;
  }}

  /* Remove underline/highlight for the MOFA link in all states */
  a.brand-title,
  a.brand-title:link,
  a.brand-title:visited,
  a.brand-title:hover,
  a.brand-title:active,
  a.brand-title:focus {{
    text-decoration: none !important;
    border-bottom: 0 !important;
    box-shadow: none !important;
    -webkit-tap-highlight-color: transparent;
  }}

  /* Ensure gradient text doesn't fall back to a theme color */
  .gradient-title-mini {{
    background: -webkit-linear-gradient(120deg, #00BFFF 30%, #FF3B30);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: clamp(32px, 12vmin, 96px); /* scales with smallest viewport side */
    color: transparent; /* keep text transparent; gradient provides color */
  }}

  /* Responsive grid: max 6 columns; step down on smaller screens */
  .grid {{
    display: grid;
    grid-template-columns: repeat(6, minmax(180px, 1fr));
    gap: 16px;
    width: calc(100% - 32px);
    margin: 0 auto;
    align-items: stretch;       /* ensure items stretch to equal height */
  }}

  .tile {{
    display: flex;
    justify-content: center;
    align-items: stretch;
  }}

  .tile-card {{
    width: 100%;
    max-width: 200px;
    display: flex;
    flex-direction: column;     /* column layout for spacer technique */
    align-items: center;
    gap: 6px;
    text-align: center;
    margin: 0 auto;
    height: 100%;

    background: var(--vp-c-bg, #fff);
    border: 1px solid var(--vp-c-divider, rgba(0,0,0,0.12));
    border-radius: 12px;
    padding: 10px 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  }}

  .tile-media {{
    height: 92px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .tile-media img {{
    max-height: 80px;
    width: auto;
    height: auto;
  }}

  .tile-title {{
    min-height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .tile-version {{
    min-height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 8px;
  }}
  .tile-version code {{
    white-space: normal;
    overflow-wrap: anywhere;
    word-break: break-word;
    display: inline-block;
    padding: 2px 6px;
    border-radius: 6px;
    background: var(--vp-c-bg-soft, rgba(0,0,0,0.04));
  }}
  .tile-updated {{
    min-height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}

  /* Keep Release Notes height consistent */
  .tile-relnotes {{
    min-height: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
  }}
  .tile-relnotes a.relnotes {{
    text-decoration: none;
    opacity: 0.9;
  }}
  .tile-relnotes a.relnotes:hover {{
    opacity: 1;
    text-decoration: underline;
  }}

  /* Flexible spacer pushes buttons to the bottom, aligning rows visually */
  .tile-spacer {{
    flex: 1 1 auto;
    width: 100%;
  }}

  .tile-links {{
    margin-top: 6px;
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
  }}
  .tile-links a {{
    text-decoration: none;
  }}

  /* Glass button palette (visible on white in light mode) */
  .grid-wrap {{
    /* Neutral gray so it stands out on white */
    --btn-glass-bg: rgba(142, 142, 147, 0.24);
    --btn-glass-bg-hover: rgba(142, 142, 147, 0.32);
    --btn-glass-border: rgba(60, 60, 67, 0.36);
    /* CHANGED: slightly lighter dark gray for light-mode button text */
    --btn-glass-text: #4a4a4d;
  }}
  /* Use .dark class from your toggle (not OS media query) */
  html.dark .grid-wrap {{
    --btn-glass-bg: rgba(255, 255, 255, 0.12);
    --btn-glass-bg-hover: rgba(255, 255, 255, 0.18);
    --btn-glass-border: rgba(255, 255, 255, 0.24);
    --btn-glass-text: #f2f2f4;
  }}

  /* iOS-like glass buttons: translucent, blurred, no shadows */
  .grid-wrap .tile-links a.btn {{
    /* color is driven by --btn-glass-text */
    color: var(--btn-glass-text) !important;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    min-height: 34px;
    min-width: 108px;
    padding: 6px 12px;
    border-radius: 12px;
    cursor: pointer;

    /* Flat translucent fill + clear border (no gradient) */
    background: var(--btn-glass-bg) !important;
    background-color: var(--btn-glass-bg) !important; /* ensure visible on white */
    border: 1px solid var(--btn-glass-border) !important;

    /* frosted glass */
    -webkit-backdrop-filter: saturate(180%) blur(14px);
    backdrop-filter: saturate(180%) blur(14px);

    font-weight: 600;
    font-size: 0.95rem;
    line-height: 1.2;

    /* ensure visible and crisp */
    opacity: 1 !important;

    /* no shadows */
    box-shadow: none !important;
    text-shadow: none !important;

    transition: background 0.2s ease, transform 0.05s ease, opacity 0.2s ease, border-color 0.2s ease;
  }}
  .grid-wrap .tile-links a.btn:hover {{
    background: var(--btn-glass-bg-hover) !important;
    background-color: var(--btn-glass-bg-hover) !important;
    border-color: var(--btn-glass-border) !important;
    text-decoration: none;
    opacity: 1 !important;
    box-shadow: none !important;
  }}
  .grid-wrap .tile-links a.btn:active {{
    transform: translateY(1px);
    background: var(--btn-glass-bg-hover) !important;
    opacity: 1 !important;
    box-shadow: none !important;
  }}
  .grid-wrap .tile-links a.btn:focus-visible {{
    outline: 2px solid color-mix(in oklab, var(--btn-glass-text) 45%, dodgerblue);
    outline-offset: 2px;
    box-shadow: none !important;
  }}

  /* Force light mode edge/text */
  html:not(.dark) .tile-links a.btn {{
    color: var(--btn-glass-text) !important;
    border-color: var(--btn-glass-border) !important;
    opacity: 1 !important;
  }}

  /* Breakpoints */
  @media (max-width: 1400px) {{
    .grid {{ grid-template-columns: repeat(5, minmax(180px, 1fr)); }}
  }}
  @media (max-width: 1200px) {{
    .grid {{ grid-template-columns: repeat(4, minmax(180px, 1fr)); }}
  }}
  @media (max-width: 900px) {{
    .grid {{ grid-template-columns: repeat(3, minmax(180px, 1fr)); }}
  }}
  @media (max-width: 700px) {{
    .grid {{ grid-template-columns: repeat(2, minmax(160px, 1fr)); gap: 12px; width: calc(100% - 24px); }}
    .tile-media {{ height: 84px; }}
    .tile-media img {{ max-height: 72px; }}
  }}
  @media (max-width: 420px) {{
    .grid {{ grid-template-columns: repeat(1, minmax(200px, 1fr)); }}
  }}
</style>

<!-- Centered hero wrapper to prevent cut-off on short screens -->
<div class="brand-hero">
  <a class="brand-title gradient-title-mini" href="/">MOFA</a>
</div>

<div class="status-bar">
      <div class="status-line">
        <span>Last Updated: <code class="status-ts">{global_last_updated}</code></span>
        <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml"><strong>Raw XML</strong></a>
        <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml"><strong>Raw YAML</strong></a>
        <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json"><strong>Raw JSON</strong></a>
        <span class="muted">(Automatically updated every 2 hours)</span>
      </div>
      <span class="appearance-toggle-inline mofa-minimal">
        <button id="appearance-toggle" class="VPSwitch VPSwitchAppearance" type="button" role="switch" title="Switch theme" aria-checked="false">
          <span class="check"><span class="icon"><span class="vpi-sun sun"></span><span class="vpi-moon moon"></span></span></span>
        </button>
      </span>
    </div>

{grid_html}
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
    readme_file_path = "docs/minimal.md"

    # Parse the XML and generate content
    global_last_updated, packages = parse_latest_xml(xml_file_path)

    readme_content = generate_readme_content(global_last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)