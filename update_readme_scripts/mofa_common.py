"""Shared pieces for the page generators.

Every generated page gets the same header (feed_header) and, where it has a
package table, the same right-hand package list (add_pkg_anchors). Change the
look in one place here and every generator picks it up on its next run.
"""
import html
import os
import re
import xml.etree.ElementTree as ET
from datetime import datetime

import pytz

AUTOMATION_NOTE = "> [!IMPORTANT]\n> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).\n"


def now_eastern():
    """Current time as 'October 16, 2026 06:35 AM EDT' (US/Eastern), the format every page uses."""
    eastern = pytz.timezone("US/Eastern")
    return datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")


def verify_note(algo):
    """'Compare the hash…' note shown under the header of every hash page."""
    return (f'<p class="mofa-note">Compare the {algo} of your download to the value listed here. '
            f'If they differ, the file was changed in transit. '
            f'<a href="/guides/how_to_{algo.lower()}">How to check {algo} on macOS →</a></p>')


def overwrite_readme(file_path, content, note=True):
    """Write a generated page: add package anchors, append the automation notice (unless note=False), create dirs."""
    content = add_pkg_anchors(content)
    if note and "> [!IMPORTANT]" not in content:
        content = content.rstrip("\n") + "\n\n" + AUTOMATION_NOTE
    os.makedirs(os.path.dirname(file_path) or ".", exist_ok=True)
    with open(file_path, "w") as f:
        f.write(content)
    print(f"{os.path.basename(file_path)} written")


def parse_latest_xml(file_path):
    """Standalone feed (macos_standalone_*.xml): (last_updated, {lowercase name: {every child tag: text}}).
    A superset of what each page needs, so one parser serves them all. min_os defaults to 'N/A'."""
    root = ET.parse(file_path).getroot()
    last_updated = root.find("last_updated").text.strip()
    packages = {}
    for pkg in root.findall("package"):
        d = {c.tag: (c.text or "").strip() for c in pkg}
        d["name"] = d.get("name", "").lower()
        d.setdefault("min_os", "N/A")
        packages[d["name"]] = d
    return last_updated, packages


def parse_edge_xml(file_path):
    """Edge feed (macos_standalone_edge_all.xml): (last_updated, {channel: {snake_case field: text}}).
    Keys are lowercased tag names (Application_ID -> application_id). Aliases: last_updated, cf_bundle_version, cfbundle_version."""
    root = ET.parse(file_path).getroot()
    last_updated = root.find("last_updated").text.strip()
    versions = {}
    for v in root.findall("Version"):
        d = {c.tag.lower(): (c.text or "").strip() for c in v}
        d["last_updated"] = d.get("last_update", "")
        d["cf_bundle_version"] = d["cfbundle_version"] = d.get("cfbundleversion", "")
        versions[d.get("name", "").lower()] = d
    return last_updated, versions


def parse_onedrive_xml(file_path):
    """OneDrive feed (macos_standalone_onedrive_all.xml): (last_updated, {ring name: {field: text}})."""
    root = ET.parse(file_path).getroot()
    last_updated = root.find("last_updated").text.strip()
    rings = {}
    for pkg in root.findall("package"):
        d = {c.tag: (c.text or "").strip() for c in pkg}
        rings[d.get("name", "")] = d
    return last_updated, rings


def get_standalone_package_detail(packages, package_name, detail):
    """Case-insensitive lookup into the dict from parse_latest_xml; None when missing."""
    package_name, detail = package_name.lower(), detail.lower()
    return packages.get(package_name, {}).get(detail)


RAW_BASE = "https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/"
# Feeds that are built in this repository rather than pulled from MOFA
SITE_RAW_BASE = "https://github.com/cocopuff2u/MOFA_WEBSITE/blob/main/repo_raw_data/"


def frontmatter(title=None, **fields):
    """VitePress frontmatter block. Booleans become true/false, lists become [a, b]."""
    lines = ["---"]
    if title:
        lines.append(f"title: {title}")
    for k, v in fields.items():
        if isinstance(v, bool):
            v = "true" if v else "false"
        elif isinstance(v, (list, tuple)):
            v = "[" + ", ".join(str(x) for x in v) + "]"
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def raw_chips(raw, formats=("xml", "yaml", "json"), raw_base=None):
    """Pill links to the raw feed files, or '' when there is no raw file."""
    if not raw:
        return ""
    base = raw_base or RAW_BASE
    return "".join(
        f'<a class="mofa-chip" href="{base}{raw}.{f}" target="_blank" rel="noopener">{f.upper()}</a>'
        for f in formats
    )


def status_line(updated, raw=None, formats=("xml", "yaml", "json"), raw_base=None):
    """Compact 'Updated …' line with raw-feed chips. Used inside the Minimal views' status bar."""
    chips = raw_chips(raw, formats, raw_base)
    raw_html = f'<span class="mofa-feed-raw">Raw feed: {chips}</span>' if chips else ""
    return f'<span class="mofa-feed-updated"><i></i>Updated {updated}</span>{raw_html}'


RELATED_STANDALONE = [
    ('Current versions', '/standalone_apps/standalone_current_version_en'),
    ('Preview versions', '/standalone_apps/standalone_preview_version_en'),
    ('Beta versions', '/standalone_apps/standalone_beta_version_en'),
    ('SHA1 hashes', '/standalone_apps/standalone_sha1_hashes_en'),
    ('SHA256 hashes', '/standalone_apps/standalone_sha256_hashes_en'),
    ('Preview SHA1 hashes', '/standalone_apps/standalone_preview_sha1_hashes_en'),
    ('Preview SHA256 hashes', '/standalone_apps/standalone_preview_sha256_hashes_en'),
    ('Beta SHA1 hashes', '/standalone_apps/standalone_beta_sha1_hashes_en'),
    ('Beta SHA256 hashes', '/standalone_apps/standalone_beta_sha256_hashes_en'),
    ('Mac App Store', '/macos_appstore/macos_appstore_current_version'),
    ('iOS App Store', '/ios_appstore/ios_appstore_current_version'),
    ('Config profiles', '/macos_tools/preconfigured_profiles'),
    ('Repair tools', '/macos_tools/microsoft_office_repair_tools'),
    ('Scripts', '/macos_tools/community_scripts'),
    ('Feedback', '/about_support/feedback'),
]


def related(links=RELATED_STANDALONE, exclude=None):
    """One-line strip of related-page chips for the bottom of a page. `exclude` drops the current page's own entry."""
    chips = "".join(f'<a class="mofa-chip outline" href="{u}">{l}</a>' for l, u in links if l != exclude)
    return f'<div class="mofa-related"><span>Related</span>{chips}</div>'


def legend(items):
    """Key/meaning pairs shown as a compact inline legend under the header.
    items – list of (key_html, meaning). key_html can be plain text or a <Badge …/>."""
    spans = "".join(f'<span class="mofa-legend-item"><b>{k}</b>{m}</span>' for k, m in items)
    return f'<div class="mofa-legend">{spans}</div>'


def feed_header(title, subtitle, updated, raw=None, formats=("xml", "yaml", "json"),
                icon="/images/Microsoft_Logo.webp", tile=False, source=None, raw_base=None):
    """Page header: icon, title, one-line description, then the 'Updated …' row with raw-feed chips.

    raw      – basename of the file in MOFA/latest_raw_files (e.g. 'macos_standalone_latest'), or None for no chips
    tile     – True renders the icon as a rounded app tile (App Store / Teams / OneDrive); False keeps it plain (Microsoft logo)
    source   – optional list of (label, url) pairs shown as "Source: …" in the meta row
    raw_base – where the raw files live; defaults to the MOFA repo, SITE_RAW_BASE for feeds built here
    """
    icon_cls = "mofa-feed-icon" + ("" if tile else " plain")
    links = raw_chips(raw, formats, raw_base)
    chips = f'\n  <span class="mofa-feed-raw">Raw feed:\n    {links}\n  </span>' if links else ""
    src = ""
    if source:
        anchors = "".join(f'<a class="mofa-chip outline" href="{u}" target="_blank" rel="noopener">{html.escape(l, quote=False)}</a>' for l, u in source)
        src = f'\n  <span class="mofa-feed-source">Source: {anchors}</span>'
    return (
        f'<div class="mofa-feed-head">\n'
        f'  <img class="{icon_cls}" src="{icon}" alt="" />\n'
        f'  <div class="mofa-feed-text">\n'
        f'    <h1>{html.escape(title, quote=False)}</h1>\n'
        f'    <p>{subtitle}</p>\n'
        f'  </div>\n'
        f'</div>\n'
        f'<div class="mofa-feed-meta">\n'
        f'  <span class="mofa-feed-updated"><i></i>Updated {updated}</span>{src}{chips}\n'
        f'</div>\n'
    )


# --- Package outline anchors -------------------------------------------------
# The right-hand "On this page" list (docs/.vitepress/theme/components/PackageJump.vue)
# reads <a class="pkg-anchor" id="pkg-…" data-label="…"> from each product row.
# Rows may carry one by hand; any row that does not gets one here, so adding or
# removing a row in a table never breaks the sidebar.

_LABEL_FIX = {
    'Microsoft and Office Suite': 'Office Suite', 'Microsoft Office Suite': 'Office Suite',
    'Microsoft BusinessPro Suite': 'BusinessPro Suite', 'Defender For Consumer': 'Defender for Consumers',
    'Defender for Consumer': 'Defender for Consumers', 'Defender For Endpoint': 'Defender for Endpoint',
    'Defender SHIM': 'Defender Shim', 'Licensing Helper Tool': 'Licensing Helper',
    'Microsoft Copilot (Copilot App)': 'Copilot App', 'Windows App Beta (Remote Desktop)': 'Windows App Beta',
}


def pkg_label(cell):
    t = re.sub(r'<sup>(.*?)</sup>', r' \1 ', cell)
    t = re.sub(r'<[^>]+>', ' ', t)
    t = t.replace('**', '').replace('_', '').replace('`', '')
    t = re.sub(r'\(365/2021/2024\)', '', t)
    t = re.sub(r'\b(Standalone Installer|Installer|Standalone)\b', '', t)
    t = re.sub(r'\s+', ' ', t).strip(' -|').replace('( ', '(').replace(' )', ')')
    return _LABEL_FIX.get(t, t)


def pkg_slug(label, fallback='row'):
    return 'pkg-' + (re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-') or fallback)


def pkg_anchor(label, slug):
    return f'<a id="{slug}" class="pkg-anchor" data-label="{html.escape(label, quote=True)}"></a>'


def add_pkg_anchors(markdown):
    out, used = [], set()
    for line in markdown.split('\n'):
        if line.startswith('| **') and 'Product Package' not in line and 'pkg-anchor' not in line:
            cell = line[2:].split(' | ')[0].split('<br>')[0]
            label = pkg_label(cell)
            if label and 'App Only' not in label:
                slug = base = pkg_slug(label)
                n = 2
                while slug in used:
                    slug, n = f"{base}-{n}", n + 1
                used.add(slug)
                line = '| ' + pkg_anchor(label, slug) + line[2:]
        else:
            m = re.search(r'id="([^"]+)" class="pkg-anchor"', line)
            if m:
                used.add(m.group(1))
        out.append(line)
    return '\n'.join(out)
