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
            "last_updated": package.find("last_updated").text.strip(),
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
    """
    Parse the OneDrive-specific XML file and extract package details.
    """
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
        # logging.debug(f"Extracted OneDrive package: {onedrive_packages[name]}") # Uncomment to debug

    return global_last_updated, onedrive_packages

def parse_edge_xml(file_path):
    """
    Parse the Edge-specific XML file and extract the 'current' version details.
    """
    logging.info(f"Parsing Edge XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("Edge XML file parsed successfully")

    # Extract global last_updated
    global_last_updated = root.find("last_updated").text.strip()
    logging.info(f"Edge XML last_updated: {global_last_updated}")

    # Extract 'current' version details
    edge_details = {}
    for version in root.findall("Version"):
        name = version.find("Name").text.strip().lower()
        if name == "current":
            edge_details = {
                "name": name,
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

    return global_last_updated, edge_details

def generate_readme_content(global_last_updated, packages, onedrive_global_last_updated, onedrive_packages, edge_details):
    logging.info("Generating standalone_main_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""---
editLink: false
lastUpdated: false
---
# <img src="/images/Microsoft_Logo_512px.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Microsoft Standalone Packages

## <img src="/images/Microsoft_Logo_512px.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Microsoft Package Links

<span class="extra-small">All links below direct to Microsoft's official Content Delivery Network (CDN).</span>
<span class="extra-small">The links provided will always download the latest version offered by Microsoft. However, the version information listed below reflects the version available at the time of this update.</span>

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{global_last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json) (Automatically Updated every 2 hours)_</span>

| **Product Package** | **Version Info** | **Download** |
|----------------------|------------------|--------------|
| **Microsoft** (365/2021/2024) **Office Suite Installer**<br><a href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac" style="text-decoration: none;"><small>_Release Notes_</small></a><br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, and MAU)_</sub><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.office` | <a href="https://go.microsoft.com/fwlink/?linkid=525133"><img src="/images/suite.png" alt="Download Image" width="80"></a> |
| **Microsoft** (365/2021/2024) **BusinessPro Suite Installer**<br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, Teams, Defender Shim, and MAU)_</sub><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.office` | <a href="https://go.microsoft.com/fwlink/?linkid=2009112"><img src="/images/suite.png" alt="Download Image" width="80"></a> |
| **Word** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Word', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Word', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Word', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.word` | <a href="https://go.microsoft.com/fwlink/?linkid=525134"><img src="/images/MSWD_512x512x32.png" alt="Download Image" width="80"></a> |
| **Word** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Word', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Word', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Word', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.word` | <a href="{get_standalone_package_detail(packages, 'Word', 'app_only_update_download')}"><img src="/images/MSWD_512x512x32.png" alt="Download Image" width="80"></a> |
| **Excel** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Excel', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Excel', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Excel', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.excel` | <a href="https://go.microsoft.com/fwlink/?linkid=525135"><img src="/images/XCEL_512x512x32.png" alt="Download Image" width="80"></a> |
| **Excel** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Excel', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Excel', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Excel', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.excel` | <a href="{get_standalone_package_detail(packages, 'Excel', 'app_only_update_download')}"><img src="/images/XCEL_512x512x32.png" alt="Download Image" width="80"></a> |
| **PowerPoint** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'PowerPoint', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.powerpoint` | <a href="https://go.microsoft.com/fwlink/?linkid=525136"><img src="/images/PPT3_512x512x32.png" alt="Download Image" width="80"></a> |
| **PowerPoint** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'PowerPoint', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.powerpoint` | <a href="{get_standalone_package_detail(packages, 'PowerPoint', 'app_only_update_download')}"><img src="/images/PPT3_512x512x32.png" alt="Download Image" width="80"></a> |
| **Outlook** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Outlook', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.outlook` | <a href="https://go.microsoft.com/fwlink/?linkid=2228621"><img src="/images/Outlook_512x512x32.png" alt="Download Image" width="80"></a>|
| **Outlook** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Outlook', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.outlook` | <a href="{get_standalone_package_detail(packages, 'Outlook', 'app_only_update_download')}"><img src="/images/Outlook_512x512x32.png" alt="Download Image" width="80"></a>|
| **OneNote** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'OneNote', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.onenote.mac` | <a href="https://go.microsoft.com/fwlink/?linkid=820886"><img src="/images/OneNote_512x512x32.png" alt="Download Image" width="80"></a> |
| **OneNote** (365/2021/2024) **App Only Installer** <br><sub>_(Does Not Contain MAU)_</sub><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'OneNote', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.onenote.mac` | <a href="{get_standalone_package_detail(packages, 'OneNote', 'app_only_update_download')}"><img src="/images/OneNote_512x512x32.png" alt="Download Image" width="80"></a> |
| **OneDrive Standalone Installer** <sup>(Production Ring)</sup> <br><a href="https://support.microsoft.com/en-us/office/onedrive-release-notes-845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'last_updated')}`_<br> | **Version:**<br>`{get_onedrive_package_detail(onedrive_packages, 'Production Ring', 'short_version')}`<br><br>**Min OS:**<br>`13.0`<br><br>**CFBundle ID:**<br>`com.microsoft.OneDrive` | <a href="https://go.microsoft.com/fwlink/?linkid=823060"><img src="/images/OneDrive_512x512x32.png" alt="Download Image" width="80"></a> |
| **Skype for Business Standalone Installer**<br><a href="https://support.microsoft.com/en-us/office/follow-the-latest-updates-in-skype-for-business-cece9f93-add1-4d93-9a38-56cc598e5781?ui=en-us&rs=en-us&ad=us" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Skype', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Skype', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Skype', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.SkypeForBusiness` | <a href="{get_standalone_package_detail(packages, 'Skype', 'app_only_update_download')}"><img src="/images/skype_for_business.png" alt="Download Image" width="80"></a> |
| **Teams Standalone Installer**<br><a href="https://support.microsoft.com/en-us/office/what-s-new-in-microsoft-teams-d7092a6d-c896-424c-b362-a472d5f105de" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Teams', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Teams', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Teams', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.teams2` | <a href="https://go.microsoft.com/fwlink/?linkid=2249065"><img src="/images/teams_512x512x32.png" alt="Download Image" width="80"></a> |
| **InTune Company Portal Standalone Installer**<br><a href="https://aka.ms/intuneupdates" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Intune', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Intune', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Intune', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.CompanyPortalMac` | <a href="https://go.microsoft.com/fwlink/?linkid=853070"><img src="/images/companyportal.png" alt="Download Image" width="80"></a> |
| **InTune Company Portal App Only Installer**<br><a href="https://aka.ms/intuneupdates" style="text-decoration: none;"><small>_Release Notes_</small></a> <sub>_(Does Not Contain MAU)_</sub><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Intune', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Intune', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Intune', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.CompanyPortalMac` | <a href="{get_standalone_package_detail(packages, 'Intune', 'app_only_update_download')}"><img src="/images/companyportal.png" alt="Download Image" width="80"></a> |
| **Edge** <sup>_(Current Channel)_</sup><br><a href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{edge_details['last_updated']}`_<br> | **Version:**<br>`{edge_details['version']}`<br><br>**Min OS:**<br>`11.0`<br><br>**CFBundle ID:**<br>`{edge_details['cf_bundle_version']}` | <a href="{edge_details['full_update_download']}"><img src="/images/edge_app.png" alt="Download Image" width="80"></a>|
| **Defender for Endpoint Installer**<br><a href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Defender For Endpoint', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Defender For Endpoint', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Defender For Endpoint', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.wdav` | <a href="https://go.microsoft.com/fwlink/?linkid=2097502"><img src="/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Defender for Consumers Installer**<br><a href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Defender For Consumers', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Defender For Consumers', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Defender For Consumers', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.wdav` | <a href="https://go.microsoft.com/fwlink/?linkid=2247001"><img src="/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Defender SHIM Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Defender Shim', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Defender Shim', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Defender Shim', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.wdav.shim` | <a href="{get_standalone_package_detail(packages, 'Defender Shim', 'app_only_update_download')}"><img src="/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Windows App Standalone Installer** <sup>_(Remote Desktop <img src="/images/microsoft-remote-desktop-logo.png" alt="Remote Desktop" width="15" style="vertical-align: middle; display: inline-block;" />)_</sup><br><a href="https://learn.microsoft.com/en-us/windows-app/whats-new?tabs=macos" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Windows App', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.rdc.macos` | <a href="https://go.microsoft.com/fwlink/?linkid=868963"><img src="/images/windowsapp.png" alt="Download Image" width="80"></a> |
| **Windows App Only Installer** <sup>_(Remote Desktop <img src="/images/microsoft-remote-desktop-logo.png" alt="Remote Desktop" width="15" style="vertical-align: middle; display: inline-block;" />)_</sup><br><a href="https://learn.microsoft.com/en-us/windows-app/whats-new?tabs=macos" style="text-decoration: none;"><small>_Release Notes_</small></a> <sub>_(Does Not Contain MAU)_</sub><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Windows App', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Windows App', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.rdc.macos` | <a href="{get_standalone_package_detail(packages, 'Windows App', 'app_only_update_download')}"><img src="/images/windowsapp.png" alt="Download Image" width="80"></a> |
| **Visual Studio Code Standalone Installer**<br><a href="https://code.visualstudio.com/updates/" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Visual', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Visual', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Visual', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.VSCode` | <a href="https://go.microsoft.com/fwlink/?linkid=2156837"><img src="/images/Code_512x512x32.png" alt="Download Image" width="80"></a>|
| **AutoUpdate Standalone Installer**<br><a href="https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'MAU', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'MAU', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'MAU', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.autoupdate` | <a href="https://go.microsoft.com/fwlink/?linkid=830196"><img src="/images/autoupdate.png" alt="Download Image" width="80"></a>|
| **Licensing Helper Tool Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'min_os')}`<br><br>**CFBundle ID:**<br>N/A | <a href="{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'full_update_download')}"><img src="/images/pkg-icon.png" alt="Download Image" width="80"></a>|
| **Quick Assist Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Quick Assist', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Quick Assist', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Quick Assist', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.quickassist` | <a href="{get_standalone_package_detail(packages, 'Quick Assist', 'full_update_download')}"><img src="/images/quickassist.png" alt="Download Image" width="80"></a>|
| **Remote Help Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Remote Help', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Remote Help', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Remote Help', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.remotehelp` | <a href="{get_standalone_package_detail(packages, 'Remote Help', 'full_update_download')}"><img src="/images/remotehelp.png" alt="Download Image" width="80"></a>|

<span class="extra-small">_**Note that App-Only installers may download a newer package compared to standalone installers, which are the recommended choice. Standalone installers are hardlinks and are typically updated within 48 hours after a release. For items without specific release notes, please refer to the release notes for the entire suite.**_</span>

## <img src="/images/sha-256.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> SHA1 & SHA256 Checksums  

A checksum is a unique string 🔑 derived from a file’s contents, used to verify its integrity and authenticity.  

### ✅ Why Checking SHA Is Important  
It's important to verify the integrity of downloaded installers by comparing the checksum (SHA1/SHA256). This ensures that the installer is **authentic** and has not been tampered with 🛡️ during the download process.  

- **SHA1** 🔗: [Link to SHA1 checksums](/standalone_apps/standalone_sha1_hashes_en)  
- **SHA256** 🔗: [Link to SHA256 checksums](/standalone_apps/standalone_sha256_hashes_en)  

📖 For a guide on how to verify checksums on macOS, follow this [📜 step-by-step guide for SHA1](/guides/how_to_sha1) or [📜 step-by-step guide for SHA256](/guides/how_to_sha256).  

## <img src="/images/Microsoft_Logo_512px.png" alt="Microsoft Logo" width="25" style="vertical-align: middle; display: inline-block;" /> Office Updates & Settings  

### 📄 Prebuilt Configuration Profiles  
Easily manage Office updates with **prebuilt configuration profiles** provided by MOFA. A **MobileConfig file** (`.mobileconfig`) is a **plist-based XML file** 📝 used to automate settings on macOS and iOS devices, ensuring seamless policy enforcement and configuration.  

- **📥 Download Prebuilt Configuration Files:** [Access preconfigured profiles](/macos_tools/preconfigured_profiles)  

### 🛠️ Building a Configuration Profile  
- **📝 Create Your Own Configuration File:** [Step-by-step guide](/macos_tools/profile_breakdown)  

### 🔹 Mac Admin Community-Driven Preferences List *(Highly Recommended!)*  
📄 **[🔍 View Google Doc](https://docs.google.com/spreadsheets/d/1ESX5td0y0OP3jdzZ-C2SItm-TUi-iA_bcHCBvaoCumw/edit?gid=0#gid=0)**  

### 📘 Official Microsoft Documentation  
- **📄 [General PLIST Preferences](https://learn.microsoft.com/en-us/microsoft-365-apps/mac/deploy-preferences-for-office-for-mac)**  
- **📄 [App-Specific Preferences](https://learn.microsoft.com/en-us/microsoft-365-apps/mac/set-preference-per-app)**  
- **📄 [Outlook Preferences](https://learn.microsoft.com/en-us/microsoft-365-apps/mac/preferences-outlook)**  
- **📄 [Office Suite Preferences](https://learn.microsoft.com/en-us/microsoft-365-apps/mac/preferences-office)**  

## <img src="/images/Microsoft_Logo_512px.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Other Microsoft Versions  

If you're looking for other Office versions such as **Preview, Beta, or App Store versions**, please check the following links:  

- **🚀 Office Preview**: [🔗 Link to Preview Version](/standalone_apps/standalone_preview_version_en)  
- **🧪 Office Beta**: [🔗 Link to Beta Version](/standalone_apps/standalone_beta_version_en)  
- **🛍️ MacOS App Store Version**: [🔗 Link to App Store Version](/macos_appstore/macos_appstore_current_version)  
- **📱 iOS App Store Version**: [🔗 Link to App Store Version](/ios_appstore/ios_appstore_current_version)  

## <img src="/images/Microsoft_Logo_512px.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Office Repair Tools/Scripts  

If you're looking to **deploy or troubleshoot Office installations or updates**, you can use the following guides and tools:  

- **🛠️ Office Repair Tools for macOS**: [🔗 Link to Office Repair Tools](/macos_tools/microsoft_office_repair_tools)  
- **📜 Office Scripts for macOS**: [🔗 Link to Community Scripts](https://mofa.cocolabs.dev/macos_tools/community_scripts.html)  

These tools can help resolve common installation or update errors and restore Office to a working state ⚙️.  

## 💬 **Got a Need? Let Us Know!**  

If you need something, here are a few ways to reach out:  

💭 **[Start a Discussion](https://github.com/cocopuff2u/MOFA/discussions)**  
Use this to ask **questions, share ideas, or have conversations** with the community. It's a great place to get feedback or advice!  

🐛 **[Open an Issue](https://github.com/cocopuff2u/MOFA/issues)**  
If you're experiencing a problem, encountering a **bug**, or need help with something specific, create an issue here to bring it to our attention.  

🔧 **[Submit a Pull Request](https://github.com/cocopuff2u/MOFA/pulls)**  
If you have **improvements, bug fixes, or new features** to contribute, submit a pull request and help make the project better!  

📬 **[Contact Us](https://mofa.cocolabs.dev/about_support/report_issue.html)**  
If you're not familiar with GitHub or need assistance outside of the platform, feel free to **reach out through our contact page**!  

> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
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
    """
    Retrieve specific details for a given OneDrive package.
    """
    if package_name in onedrive_packages and detail in onedrive_packages[package_name]:
        return onedrive_packages[package_name][detail]
    else:
        return None

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_standalone_latest.xml"
    onedrive_xml_file_path = "repo_raw_data/macos_standalone_onedrive_all.xml"
    edge_xml_file_path = "repo_raw_data/macos_standalone_edge_all.xml"
    readme_file_path = "docs/standalone_apps/standalone_current_version_en.md"

    # Parse the XML files and generate content
    global_last_updated, packages = parse_latest_xml(xml_file_path)
    onedrive_global_last_updated, onedrive_packages = parse_onedrive_xml(onedrive_xml_file_path)
    edge_global_last_updated, edge_details = parse_edge_xml(edge_xml_file_path)

    readme_content = generate_readme_content(global_last_updated, packages, onedrive_global_last_updated, onedrive_packages, edge_details)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)