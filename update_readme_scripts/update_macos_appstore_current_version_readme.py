import html
import re
import xml.etree.ElementTree as ET
from datetime import datetime
import pytz
import logging
from mofa_common import feed_header, add_pkg_anchors, frontmatter, status_line, legend, related, overwrite_readme, verify_note, now_eastern

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_latest_xml(file_path):
    logging.info(f"Parsing XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("XML file parsed successfully")

    # Extract last_updated
    last_updated = root.find("last_updated").text.strip()
    logging.info(f"XML last_updated: {last_updated}")

    # Extract package details
    packages = []
    for package in root.findall("package"):
        package_info = {
            "name": package.find("name").text.strip(),
            "application_name": package.find("application_name").text.strip(),
            "bundleId": package.find("bundleId").text.strip(),
            "currentVersionReleaseDate": package.find("currentVersionReleaseDate").text.strip(),
            "icon_image": package.find("icon_image").text.strip(),
            "minimumOsVersion": package.find("minimumOsVersion").text.strip(),
            "releaseNotes": package.find("releaseNotes").text.strip(),
            "version": package.find("version").text.strip(),
            "app_store_url": package.find("app_store_url").text.strip(),  # NEW: link target for clickable icon
        }
        packages.append(package_info)
        # logging.debug(f"Extracted package: {package_info}") # Uncomment to see all package details

    return last_updated, packages

def generate_readme_content(last_updated, packages):
    logging.info("Generating appstore_latest_readme content")

    current_time = now_eastern()
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""{frontmatter('Mac App Store', editLink=False, lastUpdated=False, outline=False, packageOutline=True)}
{feed_header('Mac App Store', 'Latest versions of Microsoft apps on the Mac App Store, pulled from Apple every two hours.', last_updated, raw='macos_appstore_latest', icon='/images/App_Store_logo.webp', tile=True)}

| **Product Package** | **Version Info** | **Link** |
|---------------------|------------------|:--------:|
"""
    used_slugs = {}
    for package in packages:
        # Anchor + label for the right-hand "On this page" package list (see theme/components/PackageJump.vue)
        label = str(package.get('application_name') or package.get('bundleId') or 'app')
        slug = 'pkg-' + (re.sub(r'[^a-z0-9]+', '-', label.lower()).strip('-')
                         or re.sub(r'[^a-z0-9]+', '-', str(package.get('bundleId', 'app')).lower()).strip('-'))
        used_slugs[slug] = used_slugs.get(slug, 0) + 1
        if used_slugs[slug] > 1:
            slug = f"{slug}-{used_slugs[slug]}"
        anchor = f'<a id="{slug}" class="pkg-anchor" data-label="{html.escape(label, quote=True)}"></a>'
        # Icon in the last column; wrap with link if app_store_url is available
        if package['icon_image'] != 'NA':
            if package.get('app_store_url') and package['app_store_url'] != 'NA':
                icon_html = f"<a href='{package['app_store_url']}' target='_blank' rel='noopener'><img src='{package['icon_image']}' alt='{package['application_name']} icon' width='80'></a>"
            else:
                icon_html = f"<img src='{package['icon_image']}' alt='{package['application_name']} icon' width='80'>"
        else:
            icon_html = ''

        # Column 1: Product Package with Last Update
        product_package_col = (
            f"{anchor}**{package['application_name']}**"
            f"<br><br>_**Last Update:**_ `{package['currentVersionReleaseDate']}`"
        )

        # Column 2: Version Info (Version, Min OS, CFBundle ID)
        version_info_col = (
            f"**Version:**<br>`{package['version']}`"
            f"<br><br>**Min OS:**<br>`{package['minimumOsVersion']}`"
            f"<br><br>**CFBundle ID:**<br>`{package['bundleId']}`"
        )

        content += f"| {product_package_col} | {version_info_col} | {icon_html} |\n"

    # Add comment section
    content += """
"""

    logging.info("appstore_latest_readme content generated successfully")

    return content

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_appstore_latest.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/macos_appstore/macos_appstore_current_version.md"

    # Parse the XML and generate content
    last_updated, packages = parse_latest_xml(xml_file_path)

    readme_content = generate_readme_content(last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)