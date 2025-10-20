import xml.etree.ElementTree as ET
from datetime import datetime
import os

# Get the root directory of the project (assuming the script is inside a subfolder like '/update_readme_scripts/')
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Define the correct paths based on the project root
latest_xml_path = os.path.join(project_root, 'repo_raw_data', 'macos_standalone_latest.xml')
rss_xml_path = os.path.join(project_root, 'docs', 'public', 'rss_feeds', 'mau_rss.xml')

# Print the paths to verify if they are correct
print(f"Latest XML Path: {latest_xml_path}")
print(f"RSS XML Path: {rss_xml_path}")

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
FEED_URL = "https://mofa.cocolabs.dev/rss_feeds/mau_rss.xml"
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

# Create the RSS feed file if it doesn't exist or is empty
if not os.path.exists(rss_xml_path) or os.path.getsize(rss_xml_path) == 0:
    rss = ET.Element('rss', {'version': '2.0', 'xmlns:atom': 'http://www.w3.org/2005/Atom'})
    channel = ET.SubElement(rss, 'channel')
    tree = ET.ElementTree(rss)
    indent(rss)
    tree.write(rss_xml_path, encoding='UTF-8', xml_declaration=True)

# Parse the latest.xml file
latest_tree = ET.parse(latest_xml_path)
latest_root = latest_tree.getroot()

# Extract MAU package details
mau_package = None
for package in latest_root.findall('package'):
    if package.find('name').text == 'MAU':
        mau_package = package
        break

if mau_package is None:
    raise ValueError("MAU package not found in latest.xml")

mau_short_version = mau_package.find('short_version').text
mau_update_download = mau_package.find('app_only_update_download').text
mau_last_updated = mau_package.find('last_updated').text

# Parse the RSS feed
rss_tree = ET.parse(rss_xml_path)
rss_root = rss_tree.getroot()
channel = rss_root.find('channel')

# Register atom namespace for proper find/create
ET.register_namespace('atom', 'http://www.w3.org/2005/Atom')
ATOM_NS = {'atom': 'http://www.w3.org/2005/Atom'}

# Initialize channel-level elements if they do not exist
title = channel.find('title')
link = channel.find('link')
description = channel.find('description')
docs = channel.find('docs')

if title is None:
    title = ET.SubElement(channel, 'title')
    title.text = "MOFA - MAU RSS Feed"
if link is None:
    link = ET.SubElement(channel, 'link')
# Always ensure canonical channel link points to the site (not the feed URL)
link.text = SITE_URL
if description is None:
    description = ET.SubElement(channel, 'description')
    description.text = "Microsoft Office Feed for Apple - MAU RSS Feed"
if docs is None:
    docs = ET.SubElement(channel, 'docs')
    docs.text = "http://www.rssboard.org/rss-specification"

# Add/update atom:link rel="self" for the feed URL
atom_link = channel.find('atom:link', ATOM_NS)
if atom_link is None:
    atom_link = ET.SubElement(channel, '{http://www.w3.org/2005/Atom}link', {
        'href': FEED_URL,
        'rel': 'self',
        'type': 'application/rss+xml'
    })
else:
    atom_link.set('href', FEED_URL)
    atom_link.set('rel', 'self')
    atom_link.set('type', 'application/rss+xml')

# Add/ensure language, ttl, and lastBuildDate
language = channel.find('language')
if language is None:
    language = ET.SubElement(channel, 'language')
    language.text = 'en-US'

ttl = channel.find('ttl')
if ttl is None:
    ttl = ET.SubElement(channel, 'ttl')
    ttl.text = '60'

# Use MAU last_updated as channel lastBuildDate
last_build_date_text = datetime.strptime(mau_last_updated, "%B %d, %Y").strftime("%a, %d %b %Y 00:00:00 +0000")
last_build_date = channel.find('lastBuildDate')
if last_build_date is None:
    last_build_date = ET.SubElement(channel, 'lastBuildDate')
last_build_date.text = last_build_date_text

# Add the <image> element above the <item> elements
image = channel.find('image')
if image is None:
    image = ET.Element('image')
    url = ET.SubElement(image, 'url')
    url.text = "https://mofa.cocolabs.dev/images/logo_Mofa_NoBackground.png"
    img_title = ET.SubElement(image, 'title')
    img_title.text = "MOFA - MAU RSS Feed"
    img_link = ET.SubElement(image, 'link')
    img_link.text = SITE_URL
    first_item_index = next((i for i, elem in enumerate(channel) if elem.tag == 'item'), len(channel))
    channel.insert(first_item_index, image)
else:
    # Ensure image link points to the site URL
    img_link = image.find('link')
    if img_link is None:
        img_link = ET.SubElement(image, 'link')
    img_link.text = SITE_URL

# Remove duplicate non-atom channel <link> elements (keep the first one as canonical)
links = channel.findall('link')
if links:
    links[0].text = SITE_URL
    for extra in links[1:]:
        channel.remove(extra)
else:
    ET.SubElement(channel, 'link').text = SITE_URL

# Check if the MAU version already exists in the RSS feed
existing_version = False
for item in channel.findall('item'):
    title_el = item.find('title')
    desc_el = item.find('description')
    if not (title_el is None or desc_el is None):
        desc_text = _get_all_text(desc_el)
        if (mau_short_version in (title_el.text or "")) or (mau_short_version in desc_text):
            _set_description_with_link(desc_el, mau_short_version)
            existing_version = True
            print("MAU version already in RSS feed")
            break

# If the version is not already in the feed, add it
if not existing_version:
    new_item = ET.Element('item')
    title_el = ET.SubElement(new_item, 'title')
    title_el.text = "New Microsoft AutoUpdate Released"
    link_el = ET.SubElement(new_item, 'link')
    link_el.text = mau_update_download
    desc_el = ET.SubElement(new_item, 'description')
    _set_description_with_link(desc_el, mau_short_version)
    pubDate = ET.SubElement(new_item, 'pubDate')
    pubDate.text = last_build_date_text
    guid = ET.SubElement(new_item, 'guid')
    guid.text = mau_update_download
    guid.set('isPermaLink', 'false')

    # Insert the new item into the RSS feed
    first_item_index = next((i for i, elem in enumerate(channel) if elem.tag == 'item'), len(channel))
    channel.insert(first_item_index, new_item)
    print("RSS feed updated with new MAU version")

# Always write updates (even if only header normalization happened)
indent(rss_root)
rss_tree.write(rss_xml_path, encoding='UTF-8', xml_declaration=True)