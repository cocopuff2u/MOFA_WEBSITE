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
            "min_os": package.find("min_os").text.strip(),
            "app_only_update_download": package.find("app_only_update_download").text.strip(),
            "app_update_sha256": package.find("app_update_sha256").text.strip(),
            "app_update_sha1": package.find("app_update_sha1").text.strip(),
            "full_update_download": package.find("full_update_download").text.strip(),
            "full_update_sha256": package.find("full_update_sha256").text.strip(),
            "full_update_sha1": package.find("full_update_sha1").text.strip(),
        }
        # logging.debug(f"Extracted package: {packages[name]}") # Uncomment to see all package details

    return global_last_updated, packages

def parse_onedrive_xml(file_path):
    logging.info(f"Parsing OneDrive XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("OneDrive XML file parsed successfully")

    # Extract details for "Upcoming Production Ring"
    onedrive_details = {}
    for package in root.findall("package"):
        name = package.find("name").text.strip()
        if name == "Upcoming Production Ring":
            onedrive_details = {
                "name": name,
                "short_version": package.find("short_version").text.strip(),
                "full_update_download": package.find("full_update_download").text.strip(),
                "full_update_sha256": package.find("full_update_sha256").text.strip(),
                "last_updated": package.find("last_updated").text.strip(),
            }
            logging.info(f"Extracted OneDrive details: {onedrive_details}")
            break

    return onedrive_details

def generate_readme_content(global_last_updated, packages, onedrive_details):
    logging.info("Generating standalone_sha256_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""---
editLink: false
lastUpdated: false
---
# <img src="/images/Microsoft_Logo_512px.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Microsoft Standalone Package & SHA256 Hashes

<span class="extra-small">All links below direct to Microsoft's official Content Delivery Network (CDN).</span>
<span class="extra-small">The links provided will always download the latest version offered by Microsoft. However, the version information listed below reflects the version available at the time of this update.</span>

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{global_last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json)
 (Automatically Updated every 2 hours)_</span>


| **Product Package** | **Link** | **<img src="/images/sha-256.png" alt="image" width="20" style="vertical-align: middle; display: inline-block;" /> SHA256 Hash <img src="/images/sha-256.png" alt="image" width="20" style="vertical-align: middle; display: inline-block;" />** |
|----------------------|----------|------------------|
| **Microsoft** (365/2021/2024) **and Office Suite Installer**<br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, and MAU)_</sub> | <a href="https://go.microsoft.com/fwlink/?linkid=525133"><img src="/images/suite.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'full_update_sha256')}` |
| **Microsoft** (365/2021/2024) **BusinessPro Suite Installer**<br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, Teams, Defender Shim, and MAU)_</sub> | <a href="https://go.microsoft.com/fwlink/?linkid=2009112"><img src="/images/suite.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'full_update_sha256')}` |
| **Word** (365/2021/2024) **Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=525134"><img src="/images/MSWD_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Word', 'full_update_sha256')}` |
| **Excel** (365/2021/2024) **Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=525135"><img src="/images/XCEL_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Excel', 'full_update_sha256')}` |
| **PowerPoint** (365/2021/2024) **Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=525136"><img src="/images/PPT3_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'PowerPoint', 'full_update_sha256')}` |
| **Outlook** (365/2021/2024) **Standalone Installer**| <a href="https://go.microsoft.com/fwlink/?linkid=525137"><img src="/images/Outlook_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Outlook', 'full_update_sha256')}` |
| **OneNote** (365/2021/2024) **Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=820886"><img src="/images/OneNote_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'OneNote', 'full_update_sha256')}` |
| **OneDrive Standalone Installer** | <a href="{onedrive_details['full_update_download']}"><img src="/images/OneDrive_512x512x32.png" alt="Download Image" width="60"></a> | `{onedrive_details['full_update_sha256']}` |
| **Skype for Business Standalone Installer** | <a href="{get_standalone_package_detail(packages, 'Skype', 'app_only_update_download')}"><img src="/images/skype_for_business.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Skype', 'full_update_sha256')}` |
| **Teams Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=2249065"><img src="/images/teams_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Teams', 'full_update_sha256')}` |
| **InTune Company Portal Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=853070"><img src="/images/companyportal.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Intune', 'full_update_sha256')}` |
| **Edge Standalone Installer** <sup>_(Stable Channel)_</sup> | <a href="https://go.microsoft.com/fwlink/?linkid=2093504"><img src="/images/edge_app.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Edge', 'full_update_sha256')}` |
| **Defender For Endpoint Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=2097502"><img src="/images/defender_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Defender For Endpoint', 'full_update_sha256')}` |
| **Defender For Consumer Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=2097001"><img src="/images/defender_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Defender For Consumers', 'full_update_sha256')}` |
| **Defender Shim Installer** | <a href="{get_standalone_package_detail(packages, 'Defender Shim', 'latest_download')}"><img src="/images/defender_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Defender Shim', 'full_update_sha256')}` |
| **Windows App Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=868963"><img src="/images/windowsapp.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Windows App', 'full_update_sha256')}` |
| **Visual Studio Code Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=2156837"><img src="/images/Code_512x512x32.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Visual', 'full_update_sha256')}` |
| **AutoUpdate Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=830196"><img src="/images/autoupdate.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'MAU', 'full_update_sha256')}` |
| **Licensing Helper Tool Installer** | <a href="{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'latest_download')}"><img src="/images/pkg-icon.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'full_update_sha256')}` |
| **Quick Assist Installer** | <a href="{get_standalone_package_detail(packages, 'Quick Assist', 'latest_download')}"><img src="/images/quickassist.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Quick Assist', 'full_update_sha256')}` |
| **Remote Help Installer** | <a href="{get_standalone_package_detail(packages, 'Remote Help', 'latest_download')}"><img src="/images/remotehelp.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Remote Help', 'full_update_sha256')}` |

## SHA256 Hashes Guide

For a detailed guide on how to create/verify SHA256 hashes, please refer to [this guide](/guides/how_to_sha256).

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""
    logging.info("standalone_sha256_hashes content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"standalone_sha256_hashes.md has been overwritten.")

def get_standalone_package_detail(packages, package_name, detail):
    package_name = package_name.lower()
    detail = detail.lower()

    if package_name in packages and detail in packages[package_name]:
        return packages[package_name][detail]
    else:
        return None

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_standalone_latest.xml"  # Update this path if the file is located elsewhere
    onedrive_xml_file_path = "repo_raw_data/macos_standalone_onedrive_all.xml"
    readme_file_path = "docs/standalone_apps/standalone_sha256_hashes_en.md"

    # Parse the XML and generate content
    global_last_updated, packages = parse_latest_xml(xml_file_path)
    onedrive_details = parse_onedrive_xml(onedrive_xml_file_path)

    readme_content = generate_readme_content(global_last_updated, packages, onedrive_details)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)