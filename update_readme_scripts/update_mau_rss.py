import xml.etree.ElementTree as ET
from datetime import datetime
import os

# Paths to the XML files
latest_xml_path = './repo_raw_data/macos_standalone_latest.xml'
rss_xml_path = './docs/public/rss_feeds/mau_rss.xml'

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

# Create the RSS feed file if it doesn't exist
if not os.path.exists(rss_xml_path):
    rss = ET.Element('rss', version='2.0')
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
mau_update_download = mau_package.find('update_download').text
mau_last_updated = mau_package.find('last_updated').text

# Parse the RSS feed
rss_tree = ET.parse(rss_xml_path)
rss_root = rss_tree.getroot()
channel = rss_root.find('channel')

# Initialize channel-level elements
title = channel.find('title')
link = channel.find('link')
description = channel.find('description')
docs = channel.find('docs')

# Add channel-level elements if they do not exist
if title is None:
    title = ET.SubElement(channel, 'title')
    title.text = "MOFA - MAU RSS Feed"
if link is None:
    link = ET.SubElement(channel, 'link')
    link.text = "https://mofa.cocolabs.dev/rss_feeds/mau_rss.xml"
if description is None:
    description = ET.SubElement(channel, 'description')
    description.text = "Microsoft Office Feed for Apple - MAU RSS Feed"
if docs is None:
    docs = ET.SubElement(channel, 'docs')
    docs.text = "http://www.rssboard.org/rss-specification"

# Ensure channel elements are in the specified order
channel_elements = [title, link, description, docs]
for elem in channel_elements:
    if elem is not None:
        channel.remove(elem)
for elem in reversed(channel_elements):
    channel.insert(0, elem)

# Check if the latest MAU version is already in the RSS feed
for item in channel.findall('item'):
    if mau_short_version in item.find('title').text or f"Version {mau_short_version}" in item.find('description').text:
        print("MAU version already in RSS feed")
        exit()

# Create a new RSS item
new_item = ET.Element('item')
title = ET.SubElement(new_item, 'title')
title.text = "New Microsoft AutoUpdate Released"
update_download_link = ET.SubElement(new_item, 'release_notes')
update_download_link.text = "https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate"
description = ET.SubElement(new_item, 'description')
description.text = f"Version {mau_short_version}"
pubDate = ET.SubElement(new_item, 'pubDate')
pubDate.text = datetime.strptime(mau_last_updated, "%B %d, %Y").strftime("%a, %d %b %Y")  # Updated date format
guid = ET.SubElement(new_item, 'update_download')
guid.text = mau_update_download  # Use update_download from latest.xml

# Insert the new item at the top of the channel, below the channel elements
channel.insert(len(channel_elements), new_item)

# Save the updated RSS feed
indent(rss_root)
rss_tree.write(rss_xml_path, encoding='UTF-8', xml_declaration=True)
print("RSS feed updated with new MAU version")
