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

    content = f"""---
editLink: false
lastUpdated: false
layout: doc
navbar: true
sidebar: false
footer: true
aside: false
---
<div style="text-align: center;">

_Last Updated: <code style="color : dodgerblue">{global_last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json) (Automatically Updated every 2 hours)_
</div>
<div style="display: flex; justify-content: center;">

| **Product Package** | **Bundle Information** | **Download** |
|----------------------|----------------------|--------------|
| **Microsoft** (365/2021/2024) **Office Suite Installer**<br><a href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac" style="text-decoration: none;"><small>_Release Notes_</small></a><br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, and MAU)_</sub><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.office` | <a href="https://go.microsoft.com/fwlink/?linkid=525133"><img src="/images/suite.png" alt="Download Image" width="80"></a> |
| **Microsoft** (365/2021/2024) **BusinessPro Suite Installer**<br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, Teams, Defender Shim, and MAU)_</sub><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.office` | <a href="https://go.microsoft.com/fwlink/?linkid=2009112"><img src="/images/suite.png" alt="Download Image" width="80"></a> |
| **Word** (365/2021/2024) **Standalone Installer**<br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Word', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Word', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Word', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Word', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.word` | <a href="https://go.microsoft.com/fwlink/?linkid=525134"><img src="/images/MSWD_512x512x32.png" alt="Download Image" width="80"></a> |
| **Word** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Word', 'app_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Word', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Word', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Word', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.word` | <a href="{get_standalone_package_detail(packages, 'Word', 'app_only_update_download')}"><img src="/images/MSWD_512x512x32.png" alt="Download Image" width="80"></a> |
| **Excel** (365/2021/2024) **Standalone Installer**<br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Excel', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Excel', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Excel', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Excel', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.excel` | <a href="https://go.microsoft.com/fwlink/?linkid=525135"><img src="/images/XCEL_512x512x32.png" alt="Download Image" width="80"></a> |
| **Excel** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Excel', 'app_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Excel', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Excel', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Excel', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.excel` | <a href="{get_standalone_package_detail(packages, 'Excel', 'app_only_update_download')}"><img src="/images/XCEL_512x512x32.png" alt="Download Image" width="80"></a> |
| **PowerPoint** (365/2021/2024) **Standalone Installer**<br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'PowerPoint', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.powerpoint` | <a href="https://go.microsoft.com/fwlink/?linkid=525136"><img src="/images/PPT3_512x512x32.png" alt="Download Image" width="80"></a> |
| **PowerPoint** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'app_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'PowerPoint', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.powerpoint` | <a href="{get_standalone_package_detail(packages, 'PowerPoint', 'app_only_update_download')}"><img src="/images/PPT3_512x512x32.png" alt="Download Image" width="80"></a> |
| **Outlook** (365/2021/2024) **Standalone Installer**<br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Outlook', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.outlook` | <a href="https://go.microsoft.com/fwlink/?linkid=2228621"><img src="/images/Outlook_512x512x32.png" alt="Download Image" width="80"></a>|
| **Outlook** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'app_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Outlook', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.outlook` | <a href="{get_standalone_package_detail(packages, 'Outlook', 'app_only_update_download')}"><img src="/images/Outlook_512x512x32.png" alt="Download Image" width="80"></a>|
| **OneNote** (365/2021/2024) **Standalone Installer**<br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'OneNote', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.onenote.mac` | <a href="https://go.microsoft.com/fwlink/?linkid=820886"><img src="/images/OneNote_512x512x32.png" alt="Download Image" width="80"></a> |
| **OneNote** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'app_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'OneNote', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.onenote.mac` | <a href="{get_standalone_package_detail(packages, 'OneNote', 'app_only_update_download')}"><img src="/images/OneNote_512x512x32.png" alt="Download Image" width="80"></a> |
| **OneDrive Standalone Installer** <sup>(Production Ring)</sup> <br><a href="https://support.microsoft.com/en-us/office/onedrive-release-notes-845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'last_updated')}`_<br> | **Version:**<br>`{get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'short_version')}`<br><br>**Min OS:**<br>`13.0`<br><br>**CFBundle ID:**<br>`{get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'CFBundleVersion')}` | <a href="{get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'full_update_download')}"><img src="/images/OneDrive_512x512x32.png" alt="Download Image" width="80"></a> |
| **Skype for Business Standalone Installer**<br><a href="https://support.microsoft.com/en-us/office/follow-the-latest-updates-in-skype-for-business-cece9f93-add1-4d93-9a38-56cc598e5781?ui=en-us&rs=en-us&ad=us" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Skype', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Skype', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Skype', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Skype', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.SkypeForBusiness` | <a href="{get_standalone_package_detail(packages, 'Skype', 'app_only_update_download')}"><img src="/images/skype_for_business.png" alt="Download Image" width="80"></a> |
| **Teams Standalone Installer**<br><a href="https://support.microsoft.com/en-us/office/what-s-new-in-microsoft-teams-d7092a6d-c896-424c-b362-a472d5f105de" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Teams', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Teams', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Teams', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Teams', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.teams2` | <a href="https://go.microsoft.com/fwlink/?linkid=2249065"><img src="/images/teams_512x512x32.png" alt="Download Image" width="80"></a> |
| **InTune Company Portal Standalone Installer**<br><a href="https://aka.ms/intuneupdates" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Intune', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Intune', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Intune', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Intune', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.CompanyPortalMac` | <a href="https://go.microsoft.com/fwlink/?linkid=853070"><img src="/images/companyportal.png" alt="Download Image" width="80"></a> |
| **InTune Company Portal App Only Installer**<br><a href="https://aka.ms/intuneupdates" style="text-decoration: none;"><small>_Release Notes_</small></a> <sub>_(Does Not Contain MAU)_</sub><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Intune', 'app_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Intune', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Intune', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Intune', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.CompanyPortalMac` | <a href="{get_standalone_package_detail(packages, 'Intune', 'app_only_update_download')}"><img src="/images/companyportal.png" alt="Download Image" width="80"></a> |
| **Edge** <sup>_(Current Channel)_</sup><br><a href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{edge_current_version.get('full_update_sha256', 'N/A')}`<br><br>_**Last Update:** `{edge_current_version.get('last_updated', 'N/A')}`_<br> | **Version:**<br>`{edge_current_version.get('version', 'N/A')}`<br><br>**Min OS:**<br>`11.0`<br><br>**CFBundle ID:**<br>`{edge_current_version.get('cf_bundle_version', 'N/A')}` | <a href="{edge_current_version.get('full_update_download', '#')}"><img src="/images/edge_app.png" alt="Download Image" width="80"></a>|
| **Defender for Endpoint Installer**<br><a href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Defender For Endpoint', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Defender For Endpoint', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Defender For Endpoint', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Defender For Endpoint', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.wdav` | <a href="https://go.microsoft.com/fwlink/?linkid=2097502"><img src="/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Defender for Consumers Installer**<br><a href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Defender For Consumers', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Defender For Consumers', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Defender For Consumers', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Defender For Consumers', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.wdav` | <a href="https://go.microsoft.com/fwlink/?linkid=2247001"><img src="/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Defender SHIM Installer**<br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Defender Shim', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Defender Shim', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Defender Shim', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Defender Shim', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.wdav.shim` | <a href="{get_standalone_package_detail(packages, 'Defender Shim', 'app_only_update_download')}"><img src="/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Windows App Standalone Installer** <sup>_(Remote Desktop <img src="/images/microsoft-remote-desktop-logo.png" alt="Remote Desktop" width="15" style="vertical-align: middle; display: inline-block;" />)_</sup><br><a href="https://learn.microsoft.com/en-us/windows-app/whats-new?tabs=macos" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Windows App', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.rdc.macos` | <a href="https://go.microsoft.com/fwlink/?linkid=868963"><img src="/images/windowsapp.png" alt="Download Image" width="80"></a> |
| **Windows App Only Installer** <sup>_(Remote Desktop <img src="/images/microsoft-remote-desktop-logo.png" alt="Remote Desktop" width="15" style="vertical-align: middle; display: inline-block;" />)_</sup><br><a href="https://learn.microsoft.com/en-us/windows-app/whats-new?tabs=macos" style="text-decoration: none;"><small>_Release Notes_</small></a> <sub>_(Does Not Contain MAU)_</sub><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'app_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Windows App', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.rdc.macos` | <a href="{get_standalone_package_detail(packages, 'Windows App', 'app_only_update_download')}"><img src="/images/windowsapp.png" alt="Download Image" width="80"></a> |
| **Visual Studio Code Standalone Installer**<br><a href="https://code.visualstudio.com/updates/" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Visual', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Visual', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Visual', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Visual', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.VSCode` | <a href="https://go.microsoft.com/fwlink/?linkid=2156837"><img src="/images/Code_512x512x32.png" alt="Download Image" width="80"></a>|
| **AutoUpdate Standalone Installer**<br><a href="https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'MAU', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'MAU', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'MAU', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'MAU', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.autoupdate` | <a href="https://go.microsoft.com/fwlink/?linkid=830196"><img src="/images/autoupdate.png" alt="Download Image" width="80"></a>|
| **Licensing Helper Tool Installer**<br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.licensinghelper` | <a href="{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'full_update_download')}"><img src="/images/pkg-icon.png" alt="Download Image" width="80"></a>|
| **Quick Assist Installer**<br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Quick Assist', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Quick Assist', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Quick Assist', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Quick Assist', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.quickassist` | <a href="{get_standalone_package_detail(packages, 'Quick Assist', 'full_update_download')}"><img src="/images/quickassist.png" alt="Download Image" width="80"></a>|
| **Remote Help Installer**<br><br>**sha256:**<br>`{get_standalone_package_detail(packages, 'Remote Help', 'full_update_sha256')}`<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Remote Help', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Remote Help', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Remote Help', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.remotehelp` | <a href="{get_standalone_package_detail(packages, 'Remote Help', 'full_update_download')}"><img src="/images/remotehelp.png" alt="Download Image" width="80"></a>|

</div>
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
    readme_file_path = "docs/simple.md"

    # Parse the XML and generate content
    global_last_updated, packages = parse_latest_xml(xml_file_path)

    readme_content = generate_readme_content(global_last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)