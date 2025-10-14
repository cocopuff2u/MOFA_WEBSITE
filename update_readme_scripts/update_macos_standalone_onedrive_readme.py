import xml.etree.ElementTree as ET
from datetime import datetime
import pytz
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_onedrive_xml(file_path):
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
            "short_version": package.find("short_version").text.strip(),
            "application_id": package.find("application_id").text.strip(),
            "application_name": package.find("application_name").text.strip(),
            "CFBundleVersion": package.find("CFBundleVersion").text.strip(),
            "full_update_download": package.find("full_update_download").text.strip(),
            "full_update_sha1": package.find("full_update_sha1").text.strip(),
            "full_update_sha256": package.find("full_update_sha256").text.strip(),
            "last_updated": package.find("last_updated").text.strip(),
        }
        packages.append(package_info)
        # logging.debug(f"Extracted package: {package_info}") # Uncomment to see all package details

    return last_updated, packages

def generate_onedrive_readme_content(last_updated, packages):
    logging.info("Generating onedrive_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""---
editLink: false
lastUpdated: false
---
# <img src="/images/2025/OneDrive.webp" alt="image" width="40" style="vertical-align: middle; display: inline-block;" /> MacOS Standalone OneDrive Updates

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_onedrive_all.xml)
 (Automatically Updated every 2 hours)_</span>

> [!NOTE]
> I have yet to locate a reliable pull source that is direct from Microsoft, so I pulled from the only sources I could to provide this table. The table is as accurate as the data sources direct from Microsoft. I know there is an API way of pulling data, and I require assistance to set that up. For now, this is as accurate as I can provide. Here is another good source that can provide more information: [Hans Brender's OneDrive Versions](https://hansbrender.com/all-onedrive-versions-mac/).

| Ring Version | Bundle Information  | Download |
|------|---------------------|--------------|
"""
    for package in packages:
        download_image = f"[<img src='/images/2025/OneDrive.webp' alt='Download' width='60' style='vertical-align: middle;' />]({package['full_update_download']})"
        version_and_hash = f"<br>Version: <br> `{package['short_version']}` <br><br> SHA1: <br>`{package['full_update_sha1']}`<br><br> SHA256:<br>`{package['full_update_sha256']}`"

        content += f"| **{package['name']}** <br><br>Last Updated: <br> `{package['last_updated']}` | {version_and_hash} | {download_image} |\n"

    # Add comment section
    content += """
> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    logging.info("onedrive_readme content generated successfully")

    return content

def overwrite_readme(file_path, content):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        file.write(content)
    print(f"macos_standalone_onedrive_readme has been overwritten.")

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_standalone_onedrive_all.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/standalone_apps/macos_standalone_onedrive_readme.md"

    # Parse the XML and generate content
    last_updated, packages = parse_onedrive_xml(xml_file_path)

    readme_content = generate_onedrive_readme_content(last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)
