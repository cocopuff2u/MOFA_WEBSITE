import xml.etree.ElementTree as ET
import logging
from html import escape

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_appstore_xml(file_path: str):
    """
    Parse the macOS App Store XML and return:
      - global_last_updated (str)
      - packages (list[dict]) with keys:
        name, application_name, currentVersionReleaseDate, icon_image,
        version, app_store_url
    """
    logging.info(f"Parsing App Store XML file: {file_path}")
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("App Store XML parsed successfully")

    def get_text(parent, tag, default=""):
        node = parent.find(tag)
        return (node.text or "").strip() if node is not None and node.text is not None else default

    global_last_updated = get_text(root, "last_updated", "")
    logging.info(f"App Store XML last_updated: {global_last_updated}")

    packages = []
    for pkg in root.findall("package"):
        packages.append({
            "name": get_text(pkg, "name"),
            "application_name": get_text(pkg, "application_name"),
            "currentVersionReleaseDate": get_text(pkg, "currentVersionReleaseDate"),
            "icon_image": get_text(pkg, "icon_image"),
            "version": get_text(pkg, "version"),
            "app_store_url": get_text(pkg, "app_store_url"),
        })
    logging.info(f"Extracted {len(packages)} App Store packages")
    return global_last_updated, packages

def generate_readme_content(global_last_updated: str, packages: list[dict]) -> str:
    """
    Generate minimal page focusing only on macOS App Store data.
    """
    logging.info("Generating App Store minimal page content")

    def render_tile(pkg: dict) -> str:
        title = pkg.get("application_name") or pkg.get("name") or "Unknown App"
        version = pkg.get("version") or "N/A"
        release_date = pkg.get("currentVersionReleaseDate") or "N/A"
        icon = pkg.get("icon_image") or ""
        app_store_url = pkg.get("app_store_url") or "#"

        img_html = f'<img src="{escape(icon)}" alt="{escape(title)}">' if icon else ""

        return f'''
    <div class="tile">
      <div class="tile-card">
        <div class="tile-media">{img_html}</div>
        <div class="tile-title"><b>{escape(title)}</b></div>
        <div class="tile-version"><em><code>{escape(version)}</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>{escape(release_date)}</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="{escape(app_store_url)}">App Store</a>
        </div>
      </div>
    </div>'''.strip()

    tiles_html = "\n".join(render_tile(p) for p in packages)

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
  /* Status bar and links (match standalone) */
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

  /* Inline appearance toggle next to the status line */
  .appearance-toggle-inline {{
    display: inline-flex;
    align-items: center;
    margin-left: 8px;
    vertical-align: middle;
  }}

  /* Theme switch styles (scoped) */
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
  .mofa-minimal .VPSwitch .icon .sun, .mofa-minimal .VPSwitch .icon .moon {{ display: none; }}
  html:not(.dark) .mofa-minimal .VPSwitch .icon .sun {{ display: inline-block; }}
  html.dark .mofa-minimal .VPSwitch .icon .moon {{ display: inline-block; }}

  /* MOFA hero title */
  .brand-hero {{
    display: grid;
    place-items: center;
    min-height: 0;
    padding: 8px 0;
    overflow: visible;
  }}
  .brand-title {{
    display: inline-block;
    text-align: center;
    margin: 0;
    line-height: 1.05;
  }}
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
  .gradient-title-mini {{
    background: -webkit-linear-gradient(120deg, #00BFFF 30%, #FF3B30);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: clamp(32px, 12vmin, 96px);
    color: transparent;
  }}

  /* Page title under hero */
  .page-title {{
    text-align: center;
    margin: 2px 0 10px 0;
    font-weight: 700;
    font-size: clamp(18px, 3.5vmin, 28px);
    opacity: 0.9;
  }}

  /* Existing grid and tiles */
  .grid-wrap {{
    --btn-glass-bg: rgba(142, 142, 147, 0.24);
    --btn-glass-bg-hover: rgba(142, 142, 147, 0.32);
    --btn-glass-border: rgba(60, 60, 67, 0.36);
    --btn-glass-text: #4a4a4d;
  }}
  html.dark .grid-wrap {{
    --btn-glass-bg: rgba(255, 255, 255, 0.12);
    --btn-glass-bg-hover: rgba(255, 255, 255, 0.18);
    --btn-glass-border: rgba(255, 255, 255, 0.24);
    --btn-glass-text: #f2f2f4;
  }}

  .grid {{
    display: grid;
    grid-template-columns: repeat(6, minmax(180px, 1fr));
    gap: 16px;
    width: calc(100% - 32px);
    margin: 0 auto;
    align-items: stretch;
  }}
  @media (max-width: 1400px) {{ .grid {{ grid-template-columns: repeat(5, minmax(180px, 1fr)); }} }}
  @media (max-width: 1200px) {{ .grid {{ grid-template-columns: repeat(4, minmax(180px, 1fr)); }} }}
  @media (max-width: 900px)  {{ .grid {{ grid-template-columns: repeat(3, minmax(180px, 1fr)); }} }}
  @media (max-width: 700px)  {{ .grid {{ grid-template-columns: repeat(2, minmax(160px, 1fr)); gap: 12px; width: calc(100% - 24px); }} }}
  @media (max-width: 420px)  {{ .grid {{ grid-template-columns: repeat(1, minmax(200px, 1fr)); }} }}

  .tile {{ display: flex; justify-content: center; align-items: stretch; }}
  .tile-card {{
    width: 100%; max-width: 220px; display: flex; flex-direction: column; align-items: center;
    gap: 6px; text-align: center; margin: 0 auto; height: 100%;
    background: var(--vp-c-bg, #fff);
    border: 1px solid var(--vp-c-divider, rgba(0,0,0,0.12));
    border-radius: 12px; padding: 10px 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  }}
  .tile-media {{ height: 92px; display: flex; align-items: center; justify-content: center; }}
  .tile-media img {{ max-height: 80px; width: auto; height: auto; }}
  .tile-title {{ min-height: 40px; display: flex; align-items: center; justify-content: center; }}
  .tile-version code {{
    white-space: normal; overflow-wrap: anywhere; word-break: break-word;
    display: inline-block; padding: 2px 6px; border-radius: 6px;
    background: var(--vp-c-bg-soft, rgba(0,0,0,0.04));
  }}
  .tile-spacer {{ flex: 1 1 auto; width: 100%; }}
  .tile-links {{ margin-top: 6px; display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; }}
  .tile-links a {{ text-decoration: none; }}
  .grid-wrap .tile-links a.btn {{
    color: var(--btn-glass-text) !important;
    display: inline-flex; align-items: center; justify-content: center;
    min-height: 34px; min-width: 108px; padding: 6px 12px; border-radius: 12px; cursor: pointer;
    background: var(--btn-glass-bg) !important; background-color: var(--btn-glass-bg) !important;
    border: 1px solid var(--btn-glass-border) !important;
    -webkit-backdrop-filter: saturate(180%) blur(14px); backdrop-filter: saturate(180%) blur(14px);
    font-weight: 600; font-size: 0.95rem; line-height: 1.2; box-shadow: none !important;
    transition: background .2s ease, transform .05s ease, opacity .2s ease, border-color .2s ease;
  }}
  .grid-wrap .tile-links a.btn:hover {{
    background: var(--btn-glass-bg-hover) !important; background-color: var(--btn-glass-bg-hover) !important;
  }}
</style>

<!-- MOFA hero title (match standalone) -->
<div class="brand-hero">
  <a class="brand-title gradient-title-mini" href="/">MOFA</a>
</div>
<h1 class="page-title">MacOS App Store apps</h1>

<!-- Status with last updated, raw links, and theme switch -->
<div class="status-bar">
  <div class="status-line">
    <span>Last Updated: <code class="status-ts">{escape(global_last_updated)}</code></span>
    <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.xml"><strong>Raw XML</strong></a>
    <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.yaml"><strong>Raw YAML</strong></a>
    <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.json"><strong>Raw JSON</strong></a>
    <span class="muted">(Automatically updated every 2 hours)</span>
  </div>
  <span class="appearance-toggle-inline mofa-minimal">
    <button id="appearance-toggle" class="VPSwitch VPSwitchAppearance" type="button" role="switch" title="Switch theme" aria-checked="false">
      <span class="check"><span class="icon"><span class="vpi-sun sun"></span><span class="vpi-moon moon"></span></span></span>
    </button>
  </span>
</div>

<div class="grid-wrap">
  <div class="grid">
{tiles_html}
  </div>
</div>
"""
    logging.info("App Store minimal content generated successfully")
    return content

def overwrite_readme(file_path: str, content: str):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"{file_path} has been overwritten.")

if __name__ == "__main__":
    # Source: macOS App Store XML
    xml_file_path = "repo_raw_data/macos_appstore_latest.xml"
    # Output page
    readme_file_path = "docs/minimal_macos_appstore.md"

    last_updated, packages = parse_appstore_xml(xml_file_path)
    page = generate_readme_content(last_updated, packages)
    overwrite_readme(readme_file_path, page)