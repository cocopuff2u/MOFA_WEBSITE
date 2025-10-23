import xml.etree.ElementTree as ET
from datetime import datetime
import os
import re

# Get the root directory of the project (assuming the script is inside a subfolder like '/update_readme_scripts/')
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the correct paths based on the project root
latest_xml_path = os.path.join(project_root, 'repo_raw_data', 'macos_standalone_latest.xml')
rss_xml_path = os.path.join(project_root, 'docs', 'public', 'rss_feeds', 'mau_rss.xml')
rss_dir = os.path.dirname(rss_xml_path)

# Print the paths to verify if they are correct
print(f"Latest XML Path: {latest_xml_path}")
print(f"RSS Directory Path: {rss_dir}")

def indent(elem, level=0):
    i = "\n" + level * "  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for subelem in elem:
            indent(subelem, level + 1)
        if not subelem.tail or not subelem.tail.strip():
            subelem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

# Create the latest.xml file if it doesn't exist
if not os.path.exists(latest_xml_path):
    root = ET.Element('packages')
    tree = ET.ElementTree(root)
    indent(root)
    tree.write(latest_xml_path, encoding='UTF-8', xml_declaration=True)

# Constants for URLs
SITE_URL = "https://mofa.cocolabs.dev/"
# FEED_URL is now dynamic per package; keep for backward compat but unused for new per-package feeds
# FEED_URL = "https://mofa.cocolabs.dev/rss_feeds/mau_rss.xml"
RELEASE_NOTES_URL = "https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate"

# Helper: get all textual content from an element (text + children text/tails)
def _get_all_text(el: ET.Element) -> str:
    parts = []
    if el.text:
        parts.append(el.text)
    for child in el:
        if child.text:
            parts.append(child.text)
        if child.tail:
            parts.append(child.tail)
    return "".join(parts)

# Build the <description> as escaped HTML text (no child elements, no CDATA)
def _set_description_with_link(desc_el: ET.Element, version: str) -> None:
    desc_el.clear()
    desc_el.text = (
        "Microsoft AutoUpdate"
        "<br>"
        f"Version: {version}"
        "<br>"
        f"Release Notes: <a href=\"{RELEASE_NOTES_URL}\">Release Notes</a>"
    )

# New helpers for multi-package feeds
def _slugify(name: str) -> str:
    return re.sub(r'[^a-z0-9]+', '_', name.lower()).strip('_')

def _is_valid_url(s: str | None) -> bool:
    if not s:
        return False
    s = s.strip()
    if not s or s.lower() in {"n/a", "na"}:
        return False
    return s.startswith("http://") or s.startswith("https://")

def _best_download_url(pkg: ET.Element) -> str:
    app_only = pkg.findtext('app_only_update_download') or ""
    full = pkg.findtext('full_update_download') or ""
    if _is_valid_url(app_only):
        return app_only.strip()
    if _is_valid_url(full):
        return full.strip()
    return SITE_URL

def _to_rfc2822_date(date_str: str | None) -> str:
    # Expecting "October 18, 2025"
    try:
        dt = datetime.strptime((date_str or "").strip(), "%B %d, %Y")
        return dt.strftime("%a, %d %b %Y 00:00:00 +0000")
    except Exception:
        # Fallback: current date at 00:00:00 UTC offset
        return datetime.utcnow().strftime("%a, %d %b %Y 00:00:00 +0000")

def _set_package_description(desc_el: ET.Element, name: str, version: str) -> None:
    # For MAU include Release Notes link; others generic
    desc_el.clear()
    text = f"{name}<br>Version: {version}"
    if name.strip().lower() in {"mau", "microsoft autoupdate", "microsoft autoupdate.app"}:
        text += "<br>" f"Release Notes: <a href=\"{RELEASE_NOTES_URL}\">Release Notes</a>"
    desc_el.text = text

# Ensure rss directory exists
os.makedirs(rss_dir, exist_ok=True)

# Remove single-feed bootstrap; we will create one file per package as needed
# (Previously created docs/public/rss_feeds/mau_rss.xml)

# Parse the latest.xml file
latest_tree = ET.parse(latest_xml_path)
latest_root = latest_tree.getroot()

# Collect all packages
packages = latest_root.findall('package')
if not packages:
    raise ValueError("No package entries found in latest XML")

# Register atom namespace for proper find/create
ET.register_namespace('atom', 'http://www.w3.org/2005/Atom')
ATOM_NS = {'atom': 'http://www.w3.org/2005/Atom'}

for pkg in packages:
    name = (pkg.findtext('name') or "Unknown").strip()
    slug = _slugify(name)
    feed_filename = f"{slug}_rss.xml"
    feed_path = os.path.join(rss_dir, feed_filename)
    feed_url = SITE_URL + f"rss_feeds/{feed_filename}"

    short_version = (pkg.findtext('short_version') or pkg.findtext('full_version') or "Unknown").strip()
    full_version = (pkg.findtext('full_version') or short_version).strip()
    last_updated = pkg.findtext('last_updated') or ""
    last_build_date_text = _to_rfc2822_date(last_updated)
    best_url = _best_download_url(pkg)
    guid_text = f"{name}:{full_version}"

    # Create the feed file if it doesn't exist or is empty
    if not os.path.exists(feed_path) or os.path.getsize(feed_path) == 0:
        rss = ET.Element('rss', {'version': '2.0', 'xmlns:atom': 'http://www.w3.org/2005/Atom'})
        channel = ET.SubElement(rss, 'channel')
        tree = ET.ElementTree(rss)
        indent(rss)
        tree.write(feed_path, encoding='UTF-8', xml_declaration=True)

    # Parse the per-package RSS feed
    rss_tree = ET.parse(feed_path)
    rss_root = rss_tree.getroot()
    channel = rss_root.find('channel')

    # Initialize channel-level elements per package
    title = channel.find('title')
    link = channel.find('link')
    description = channel.find('description')
    docs = channel.find('docs')

    if title is None:
        title = ET.SubElement(channel, 'title')
    title.text = f"MOFA - {name} RSS Feed"

    if link is None:
        link = ET.SubElement(channel, 'link')
    link.text = SITE_URL  # canonical site link

    if description is None:
        description = ET.SubElement(channel, 'description')
    description.text = f"{name} - RSS Feed"

    if docs is None:
        docs = ET.SubElement(channel, 'docs')
    docs.text = "http://www.rssboard.org/rss-specification"

    # Add/update atom:link rel="self"
    atom_link = channel.find('atom:link', ATOM_NS)
    if atom_link is None:
        atom_link = ET.SubElement(channel, '{http://www.w3.org/2005/Atom}link', {
            'href': feed_url,
            'rel': 'self',
            'type': 'application/rss+xml'
        })
    else:
        atom_link.set('href', feed_url)
        atom_link.set('rel', 'self')
        atom_link.set('type', 'application/rss+xml')

    # Language and ttl
    language = channel.find('language')
    if language is None:
        language = ET.SubElement(channel, 'language')
    language.text = 'en-US'

    ttl = channel.find('ttl')
    if ttl is None:
        ttl = ET.SubElement(channel, 'ttl')
    ttl.text = '60'

    # Channel lastBuildDate (per package)
    last_build_date = channel.find('lastBuildDate')
    if last_build_date is None:
        last_build_date = ET.SubElement(channel, 'lastBuildDate')
    last_build_date.text = last_build_date_text

    # Ensure <image> exists and sits above items
    image = channel.find('image')
    if image is None:
        image = ET.Element('image')
        url_el = ET.SubElement(image, 'url')
        url_el.text = "https://mofa.cocolabs.dev/images/logo_Mofa_NoBackground.png"
        img_title = ET.SubElement(image, 'title')
        img_title.text = f"MOFA - {name} RSS Feed"
        img_link = ET.SubElement(image, 'link')
        img_link.text = SITE_URL
        first_item_index = next((i for i, elem in enumerate(channel) if elem.tag == 'item'), len(channel))
        channel.insert(first_item_index, image)
    else:
        img_link = image.find('link') or ET.SubElement(image, 'link')
        img_link.text = SITE_URL
        img_title = image.find('title') or ET.SubElement(image, 'title')
        img_title.text = f"MOFA - {name} RSS Feed"

    # Remove duplicate non-atom <link> elements at channel level
    links = channel.findall('link')
    if links:
        links[0].text = SITE_URL
        for extra in links[1:]:
            channel.remove(extra)
    else:
        ET.SubElement(channel, 'link').text = SITE_URL

    # Dedupe/update by guid or by name/version in title/description
    existing_items = channel.findall('item')
    guid_map = { (it.findtext('guid') or "").strip(): it for it in existing_items if it.find('guid') is not None }

    def _matches_name_ver(it: ET.Element) -> bool:
        title_el = it.find('title')
        desc_el = it.find('description')
        title_txt = (title_el.text or "") if title_el is not None else ""
        desc_txt = _get_all_text(desc_el) if desc_el is not None else ""
        return (name in title_txt) and (short_version in (title_txt + " " + desc_txt))

    item = guid_map.get(guid_text)
    if item is None:
        # Try fallback matching to convert older items to new guid scheme
        item = next((it for it in existing_items if _matches_name_ver(it)), None)

    if item is not None:
        # Refresh description/link/pubDate and ensure guid is set
        desc_el = item.find('description') or ET.SubElement(item, 'description')
        _set_package_description(desc_el, name, short_version)
        link_el = item.find('link') or ET.SubElement(item, 'link')
        link_el.text = best_url
        pub_el = item.find('pubDate') or ET.SubElement(item, 'pubDate')
        pub_el.text = last_build_date_text
        guid_el = item.find('guid') or ET.SubElement(item, 'guid')
        guid_el.text = guid_text
        guid_el.set('isPermaLink', 'false')
        print(f"Updated existing item for {name} {short_version} in {feed_filename}")
    else:
        # Create a new item at the top
        new_item = ET.Element('item')
        title_el = ET.SubElement(new_item, 'title')
        title_el.text = f"New {name} Released"
        link_el = ET.SubElement(new_item, 'link')
        link_el.text = best_url
        desc_el = ET.SubElement(new_item, 'description')
        _set_package_description(desc_el, name, short_version)
        pub_el = ET.SubElement(new_item, 'pubDate')
        pub_el.text = last_build_date_text
        guid_el = ET.SubElement(new_item, 'guid')
        guid_el.text = guid_text
        guid_el.set('isPermaLink', 'false')
        first_item_index = next((i for i, elem in enumerate(channel) if elem.tag == 'item'), len(channel))
        channel.insert(first_item_index, new_item)
        print(f"Added new item for {name} {short_version} in {feed_filename}")

    # Write per-package feed
    indent(rss_root)
    rss_tree.write(feed_path, encoding='UTF-8', xml_declaration=True)