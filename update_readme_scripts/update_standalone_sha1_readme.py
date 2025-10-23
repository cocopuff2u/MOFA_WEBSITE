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
    logging.info(f"Parsing OneDrive-specific XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("OneDrive XML file parsed successfully")

    # Extract the "Upcoming Production Version" package details
    for package in root.findall("package"):
        name = package.find("name").text.strip()
        if name == "Upcoming Production Ring":
            onedrive_details = {
                "name": name,
                "short_version": package.find("short_version").text.strip(),
                "application_id": package.find("application_id").text.strip(),
                "application_name": package.find("application_name").text.strip(),
                "full_update_download": package.find("full_update_download").text.strip(),
                "full_update_sha1": package.find("full_update_sha1").text.strip(),
                "full_update_sha256": package.find("full_update_sha256").text.strip(),
                "last_updated": package.find("last_updated").text.strip(),
            }
            logging.info(f"Extracted OneDrive details: {onedrive_details}")
            return onedrive_details

    logging.warning("No 'Upcoming Production Ring' package found in OneDrive XML")
    return None

def parse_edge_xml(file_path):
    logging.info(f"Parsing Edge-specific XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("Edge XML file parsed successfully")

    # Extract the "current" version details
    for version in root.findall("Version"):
        name = version.find("Name").text.strip()
        if name == "current":
            edge_details = {
                "name": name,
                "version": version.find("Version").text.strip(),
                "application_id": version.find("Application_ID").text.strip(),
                "application_name": version.find("Application_Name").text.strip(),
                "full_update_download": version.find("Full_Update_Download").text.strip(),
                "full_update_sha1": version.find("Full_Update_Sha1").text.strip(),
                "full_update_sha256": version.find("Full_Update_Sha256").text.strip(),
                "last_updated": version.find("Last_Update").text.strip(),
            }
            logging.info(f"Extracted Edge 'current' version details: {edge_details}")
            return edge_details

    logging.warning("No 'current' version found in Edge XML")
    return None

def generate_readme_content(global_last_updated, packages):
    logging.info("Generating standalone_sha1_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""---
editLink: false
lastUpdated: false
---
# <img src="/images/Microsoft_Logo.webp" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Microsoft Standalone Package & SHA1 Hashes

<span class="extra-small">All links below direct to Microsoft's official Content Delivery Network (CDN).</span>
<span class="extra-small">The links provided will always download the latest version offered by Microsoft. However, the version information listed below reflects the version available at the time of this update.</span>

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{global_last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json)
 (Automatically Updated every 2 hours)_</span>

| **Product Package** | **Link** | **<img src="/images/sha-256.png" alt="image" width="20" style="vertical-align: middle; display: inline-block;" /> SHA1 Hash <img src="/images/sha-256.png" alt="image" width="20" style="vertical-align: middle; display: inline-block;" />** |
|----------------------|----------|------------------|
| **Microsoft** (365/2021/2024) **and Office Suite Installer**<br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, and MAU)_</sub> | <a href="https://go.microsoft.com/fwlink/?linkid=525133"><img src="/images/Office_Suite.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'full_update_sha1')}` |
| **Microsoft** (365/2021/2024) **BusinessPro Suite Installer**<br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, Teams, Defender Shim, and MAU)_</sub> | <a href="https://go.microsoft.com/fwlink/?linkid=2009112"><img src="/images/Office_Suite.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'full_update_sha1')}` |
| **Word** (365/2021/2024) **Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=525134"><img src="/images/2025/Word.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Word', 'full_update_sha1')}` |
| **Excel** (365/2021/2024) **Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=525135"><img src="/images/2025/Excel.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Excel', 'full_update_sha1')}` |
| **PowerPoint** (365/2021/2024) **Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=525136"><img src="/images/2025/PowerPoint.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'PowerPoint', 'full_update_sha1')}` |
| **Outlook** (365/2021/2024) **Standalone Installer**| <a href="https://go.microsoft.com/fwlink/?linkid=525137"><img src="/images/2025/Outlook.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Outlook', 'full_update_sha1')}` |
| **OneNote** (365/2021/2024) **Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=820886"><img src="/images/2025/OneNote.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'OneNote', 'full_update_sha1')}` |
| **OneDrive Standalone Installer** | <a href="{get_onedrive_package_detail(onedrive_details, 'full_update_download')}"><img src="/images/2025/OneDrive.webp" alt="Download Image" width="60"></a> | `{get_onedrive_package_detail(onedrive_details, 'full_update_sha1')}` |
| **Skype for Business Standalone Installer** | <a href="{get_standalone_package_detail(packages, 'Skype', 'app_only_update_download')}"><img src="/images/Skype_For_Business.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Skype', 'full_update_sha1')}` |
| **Teams Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=2249065"><img src="/images/2021/Teams.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Teams', 'full_update_sha1')}` |
| **InTune Company Portal Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=853070"><img src="/images/2021/Company_Portal.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Intune', 'full_update_sha1')}` |
| **Edge** <sup>_(Current Channel)_</sup> | <a href="https://go.microsoft.com/fwlink/?linkid=2093504"><img src="/images/edge/edge.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Edge', 'full_update_sha1')}` |
| **Defender For Endpoint Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=2097502"><img src="/images/2025/Defender.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Defender For Endpoint', 'full_update_sha1')}` |
| **Defender For Consumer Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=2097001"><img src="/images/2025/Defender.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Defender For Consumers', 'full_update_sha1')}` |
| **Defender Shim Installer** | <a href="{get_standalone_package_detail(packages, 'Defender Shim', 'latest_download')}"><img src="/images/2025/Defender.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Defender Shim', 'full_update_sha1')}` |
| **Windows App Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=868963"><img src="/images/2025/Windows_App.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Windows App', 'full_update_sha1')}` |
| **Visual Studio Code Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=2156837"><img src="/images/2021/Code.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Visual', 'full_update_sha1')}` |
| **Microsoft Copilot** | <a href="{get_standalone_package_detail(packages, 'Copilot', 'update_download')}"><img src="/images/2025/Copilot.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Copilot', 'full_update_sha1')}` |
| **AutoUpdate Standalone Installer** | <a href="https://go.microsoft.com/fwlink/?linkid=830196"><img src="/images/2019/AutoUpdate.webp" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'MAU', 'full_update_sha1')}` |
| **Licensing Helper Tool Installer** | <a href="{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'latest_download')}"><img src="/images/pkg-icon.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'full_update_sha1')}` |
| **Quick Assist Installer** | <a href="{get_standalone_package_detail(packages, 'Quick Assist', 'latest_download')}"><img src="/images/quickassist.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Quick Assist', 'full_update_sha1')}` |
| **Remote Help Installer** | <a href="{get_standalone_package_detail(packages, 'Remote Help', 'latest_download')}"><img src="/images/remotehelp.png" alt="Download Image" width="60"></a> | `{get_standalone_package_detail(packages, 'Remote Help', 'full_update_sha1')}` |

## SHA1 Hashes Guide

For a detailed guide on how to create/verify SHA1 hashes, please refer to [this guide](/guides/how_to_sha1).

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""
    logging.info("standalone_sha1_hashes content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"standalone_sha1_hashes.md has been overwritten.")

def get_standalone_package_detail(packages, package_name, detail):
    package_name = package_name.lower()
    detail = detail.lower()

    if package_name in packages and detail in packages[package_name]:
        return packages[package_name][detail]
    else:
        return None

def get_onedrive_package_detail(onedrive_details, detail):
    detail = detail.lower()
    if detail in onedrive_details:
        return onedrive_details[detail]
    else:
        return None

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_standalone_latest.xml"  # Update this path if the file is located elsewhere
    onedrive_xml_file_path = "repo_raw_data/macos_standalone_onedrive_all.xml"
    edge_xml_file_path = "repo_raw_data/macos_standalone_edge_all.xml"
    readme_file_path = "docs/standalone_apps/standalone_sha1_hashes_en.md"

    # Parse the XML files
    global_last_updated, packages = parse_latest_xml(xml_file_path)
    onedrive_details = parse_onedrive_xml(onedrive_xml_file_path)
    edge_details = parse_edge_xml(edge_xml_file_path)

    # Update OneDrive details in the packages dictionary
    if onedrive_details:
        packages["onedrive"] = {
            "name": "onedrive",
            "full_update_download": get_onedrive_package_detail(onedrive_details, "full_update_download"),
            "full_update_sha1": get_onedrive_package_detail(onedrive_details, "full_update_sha1"),
        }

    # Update Edge details in the packages dictionary
    if edge_details:
        packages["edge"] = {
            "name": "edge",
            "full_update_download": edge_details["full_update_download"],
            "full_update_sha1": edge_details["full_update_sha1"],
        }

    # Generate content and overwrite the README file
    readme_content = generate_readme_content(global_last_updated, packages)
    overwrite_readme(readme_file_path, readme_content)