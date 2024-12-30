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
            "update_download": package.find("update_download").text.strip(),
            "latest_download": package.find("latest_download").text.strip(),
            "sha256": package.find("sha256").text.strip(),
        }
        # logging.debug(f"Extracted package: {packages[name]}") # Uncomment to see all package details

    return global_last_updated, packages

def generate_readme_content(global_last_updated, packages):
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
# <img src="/public/images/Microsoft_Logo_512px.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Microsoft Standalone Packages

<span class="extra-small">All links below direct to Microsoft's official Content Delivery Network (CDN).</span>
<span class="extra-small">The links provided will always download the latest version offered by Microsoft. However, the version information listed below reflects the version available at the time of this update.</span>

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{global_last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json) (Automatically Updated every 4 hours)_</span>

| **Product Package** | **CFBundle Version** | **CFBundle Identifier** | **Download** |
|----------------------|----------------------|--------------------------|--------------|
| **Microsoft** <sup>365/2021/2024</sup> **Office Suite Installer**<br><a href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac" style="text-decoration: none;"><small>_Release Notes_</small></a><br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, and MAU)_</sub> | `{get_standalone_package_detail(packages, 'Microsoft Office Suite', 'short_version')}` | com.microsoft.office | <a href="https://go.microsoft.com/fwlink/?linkid=525133"><img src="/public/images/suite.png" alt="Download Image" width="80"></a> |
| **Microsoft** <sup>365/2021/2024</sup> **BusinessPro Suite Installer**<br><sub>_(Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, Teams, Defender Shim, and MAU)_</sub> | `{get_standalone_package_detail(packages, 'Microsoft BusinessPro Suite', 'short_version')}` | com.microsoft.office | <a href="https://go.microsoft.com/fwlink/?linkid=2009112"><img src="/public/images/suite.png" alt="Download Image" width="80"></a> |
| **Word** <sup>365/2021/2024</sup> **Standalone Installer** | `{get_standalone_package_detail(packages, 'Word', 'short_version')}` | com.microsoft.word | <a href="https://go.microsoft.com/fwlink/?linkid=525134"><img src="/public/images/MSWD_512x512x32.png" alt="Download Image" width="80"></a> |
| **Excel** <sup>365/2021/2024</sup> **Standalone Installer** | `{get_standalone_package_detail(packages, 'Excel', 'short_version')}` | com.microsoft.excel | <a href="https://go.microsoft.com/fwlink/?linkid=525135"><img src="/public/images/XCEL_512x512x32.png" alt="Download Image" width="80"></a> |
| **PowerPoint** <sup>365/2021/2024</sup> **Standalone Installer** | `{get_standalone_package_detail(packages, 'PowerPoint', 'short_version')}` | com.microsoft.powerpoint | <a href="https://go.microsoft.com/fwlink/?linkid=525136"><img src="/public/images/PPT3_512x512x32.png" alt="Download Image" width="80"></a> |
| **Outlook** <sup>365/2021/2024</sup> **Standalone Installer** | `{get_standalone_package_detail(packages, 'Outlook', 'short_version')}` | com.microsoft.outlook | <a href="https://go.microsoft.com/fwlink/?linkid=2228621"><img src="/public/images/Outlook_512x512x32.png" alt="Download Image" width="80"></a>|
| **OneNote** <sup>365/2021/2024</sup> **Standalone Installer** | `{get_standalone_package_detail(packages, 'OneNote', 'short_version')}` | com.microsoft.onenote.mac | <a href="https://go.microsoft.com/fwlink/?linkid=820886"><img src="/public/images/OneNote_512x512x32.png" alt="Download Image" width="80"></a> |
| **OneDrive Standalone Installer**<br><a href="https://support.microsoft.com/en-us/office/onedrive-release-notes-845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{get_standalone_package_detail(packages, 'OneDrive', 'short_version')}` | com.microsoft.OneDrive | <a href="https://go.microsoft.com/fwlink/?linkid=823060"><img src="/public/images/OneDrive_512x512x32.png" alt="Download Image" width="80"></a> |
| **Skype for Business Standalone Installer**<br><a href="https://support.microsoft.com/en-us/office/follow-the-latest-updates-in-skype-for-business-cece9f93-add1-4d93-9a38-56cc598e5781?ui=en-us&rs=en-us&ad=us" style="text-decoration: none;"><small>_Release Notes_</small></a>  | `{get_standalone_package_detail(packages, 'Skype', 'short_version')}` | com.microsoft.SkypeForBusiness | <a href="{get_standalone_package_detail(packages, 'Skype', 'update_download')}"><img src="/public/images/skype_for_business.png" alt="Download Image" width="80"></a> |
| **Teams Standalone Installer**<br><a href="https://support.microsoft.com/en-us/office/what-s-new-in-microsoft-teams-d7092a6d-c896-424c-b362-a472d5f105de" style="text-decoration: none;"><small>_Release Notes_</small></a>  | `{get_standalone_package_detail(packages, 'Teams', 'short_version')}` | com.microsoft.teams2 | <a href="https://go.microsoft.com/fwlink/?linkid=2249065"><img src="/public/images/teams_512x512x32.png" alt="Download Image" width="80"></a> |
| **InTune Company Portal Standalone Installer**<br><a href="https://aka.ms/intuneupdates" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{get_standalone_package_detail(packages, 'Intune', 'short_version')}` | com.microsoft.CompanyPortalMac | <a href="https://go.microsoft.com/fwlink/?linkid=853070"><img src="/public/images/companyportal.png" alt="Download Image" width="80"></a> |
| **Edge Standalone Installer** <sup>_(Stable Channel)_</sup><br><a href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel" style="text-decoration: none;"><small>_Release Notes_</small></a>| `{get_standalone_package_detail(packages, 'Edge', 'short_version')}` | com.microsoft.edgemac | <a href="https://go.microsoft.com/fwlink/?linkid=2093504"><img src="/public/images/edge_app.png" alt="Download Image" width="80"></a>|
| **Defender for Endpoint Installer**<br><a href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{get_standalone_package_detail(packages, 'Defender For Endpoint', 'short_version')}` | com.microsoft.wdav | <a href="https://go.microsoft.com/fwlink/?linkid=2097502"><img src="/public/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Defender for Consumers Installer**<br><a href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{get_standalone_package_detail(packages, 'Defender For Consumers', 'short_version')}` | com.microsoft.wdav | <a href="https://go.microsoft.com/fwlink/?linkid=2247001"><img src="/public/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Defender SHIM Installer** | `{get_standalone_package_detail(packages, 'Defender Shim', 'short_version')}` | com.microsoft.wdav.shim | <a href="{get_standalone_package_detail(packages, 'Defender Shim', 'update_download')}"><img src="/public/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Windows App Standalone Installer** <sup>_(Remote Desktop <img src="/public/images/microsoft-remote-desktop-logo.png" alt="Remote Desktop" width="15" style="vertical-align: middle; display: inline-block;" />)_</sup><br><a href="https://learn.microsoft.com/en-us/windows-app/whats-new?tabs=macos" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{get_standalone_package_detail(packages, 'Windows App', 'short_version')}` | com.microsoft.rdc.macos | <a href="https://go.microsoft.com/fwlink/?linkid=868963"><img src="/public/images/windowsapp.png" alt="Download Image" width="80"></a> |
| **Visual Studio Code Standalone Installer**<br><a href="https://code.visualstudio.com/updates/" style="text-decoration: none;"><small>_Release Notes_</small></a>  | `{get_standalone_package_detail(packages, 'Visual', 'short_version')}` | com.microsoft.VSCode | <a href="https://go.microsoft.com/fwlink/?linkid=2156837"><img src="/public/images/Code_512x512x32.png" alt="Download Image" width="80"></a>|
| **AutoUpdate Standalone Installer**<br><a href="https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate" style="text-decoration: none;"><small>_Release Notes_</small></a>  | `{get_standalone_package_detail(packages, 'MAU', 'short_version')}` | com.microsoft.autoupdate | <a href="https://go.microsoft.com/fwlink/?linkid=830196"><img src="/public/images/autoupdate.png" alt="Download Image" width="80"></a>|
| **Licensing Helper Tool Installer** | `{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'short_version')}` | N/A | <a href="{get_standalone_package_detail(packages, 'Licensing Helper Tool', 'latest_download')}"><img src="/public/images/pkg-icon.png" alt="Download Image" width="80"></a>|
| **Quick Assist Installer** | `{get_standalone_package_detail(packages, 'Quick Assist', 'short_version')}` | com.microsoft.quickassist | <a href="{get_standalone_package_detail(packages, 'Quick Assist', 'latest_download')}"><img src="/public/images/quickassist.png" alt="Download Image" width="80"></a>|
| **Remote Help Installer** | `{get_standalone_package_detail(packages, 'Remote Help', 'short_version')}` | com.microsoft.remotehelp | <a href="{get_standalone_package_detail(packages, 'Remote Help', 'latest_download')}"><img src="/public/images/remotehelp.png" alt="Download Image" width="80"></a>|

<span class="extra-small">_**For items without specific release notes, please refer to the release notes for the entire suite.**_</span>

<span class="extra-small">_**All apps above include MAU with installation, except for Skype for Business, OneDrive, Defender SHIM, Licensing Helper Tool, Quick Assist, and Remote Help.**_</span>

# <img src="/public/images/Microsoft_Logo_512px.png" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Microsoft Standalone Packages without MAU

| **Product Package** | **CFBundle Version** | **CFBundle Identifier** | **Download** |
|----------------------|----------------------|--------------------------|--------------|
| **Word** <sup>365/2021/2024</sup> **Standalone Installer** | `{get_standalone_package_detail(packages, 'Word', 'short_version')}` | com.microsoft.word | <a href="{get_standalone_package_detail(packages, 'Word', 'update_download')}"><img src="/public/images/MSWD_512x512x32.png" alt="Download Image" width="80"></a> |
| **Excel** <sup>365/2021/2024</sup> **Standalone Installer** | `{get_standalone_package_detail(packages, 'Excel', 'short_version')}` | com.microsoft.excel | <a href="{get_standalone_package_detail(packages, 'Excel', 'update_download')}"><img src="/public/images/XCEL_512x512x32.png" alt="Download Image" width="80"></a> |
| **PowerPoint** <sup>365/2021/2024</sup> **Standalone Installer** | `{get_standalone_package_detail(packages, 'PowerPoint', 'short_version')}` | com.microsoft.powerpoint | <a href="{get_standalone_package_detail(packages, 'PowerPoint', 'update_download')}"><img src="/public/images/PPT3_512x512x32.png" alt="Download Image" width="80"></a> |
| **Outlook** <sup>365/2021/2024</sup> **Standalone Installer**<sup>_(Weekly Channel)_</sup>| `{get_standalone_package_detail(packages, 'Outlook', 'short_version')}` | com.microsoft.outlook  | <a href="{get_standalone_package_detail(packages, 'Outlook', 'update_download')}"><img src="/public/images/Outlook_512x512x32.png" alt="Download Image" width="80"></a>|
| **OneNote** <sup>365/2021/2024</sup> **Standalone Installer** | `{get_standalone_package_detail(packages, 'OneNote', 'short_version')}` | com.microsoft.onenote.mac | <a href="{get_standalone_package_detail(packages, 'OneNote', 'update_download')}"><img src="/public/images/OneNote_512x512x32.png" alt="Download Image" width="80"></a> |
| **InTune Company Portal Standalone Installer**<br><a href="https://aka.ms/intuneupdates" style="text-decoration: none;"><small>_Release Notes_</small></a> | `{get_standalone_package_detail(packages, 'Intune', 'short_version')}` | com.microsoft.CompanyPortalMac | <a href="{get_standalone_package_detail(packages, 'Intune', 'update_download')}"><img src="/public/images/companyportal.png" alt="Download Image" width="80"></a> |


> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from the Microsoft. Please note that it may not always reflect complete accuracy.
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

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_standalone_latest.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/standalone_current_version.md"

    # Parse the XML and generate content
    global_last_updated, packages = parse_latest_xml(xml_file_path)

    readme_content = generate_readme_content(global_last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)