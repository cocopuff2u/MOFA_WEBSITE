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
# <img src="/images/Microsoft_Logo.webp" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Microsoft Standalone Preview Packages

<span class="extra-small">All links below point to Microsoft's official Content Delivery Network (CDN).</span>
<span class="extra-small">The links always provide the latest version available from Microsoft as of the last update. However, the version details listed below reflect the specific version available at the time this information was last updated. This information is pulled directly from Microsoft, so if no updates are available, it may show an older or current version.</span>

<div style="text-align: center;">

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{global_last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_preview.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_preview.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_preview.json) (Automatically Updated every 2 hours)_</span>

</div>

<div style="display: flex; justify-content: center;">

| **Product Package** | **Version Info** | **Download** |
|----------------------|----------------------|--------------|
| **Word** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Word', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Word', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Word', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.word` | <a href="{get_standalone_package_detail(packages, 'Word', 'update_download')}"><img src="/images/2025/Word.webp" alt="Download Image" width="80"></a> |
| **Excel** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Excel', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Excel', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Excel', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.excel` | <a href="{get_standalone_package_detail(packages, 'Excel', 'update_download')}"><img src="/images/2025/Excel.webp" alt="Download Image" width="80"></a> |
| **PowerPoint** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'PowerPoint', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'PowerPoint', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.powerpoint` | <a href="{get_standalone_package_detail(packages, 'PowerPoint', 'update_download')}"><img src="/images/2025/PowerPoint.webp" alt="Download Image" width="80"></a> |
| **Outlook** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Outlook', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Outlook', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.outlook` | <a href="{get_standalone_package_detail(packages, 'Outlook', 'update_download')}"><img src="/images/2025/Outlook.webp" alt="Download Image" width="80"></a>|
| **OneNote** (365/2021/2024) **Standalone Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'OneNote', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'OneNote', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.onenote.mac` | <a href="{get_standalone_package_detail(packages, 'OneNote', 'update_download')}"><img src="/images/2025/OneNote.webp" alt="Download Image" width="80"></a> |
| **Teams Standalone Installer**<br><a href="https://support.microsoft.com/en-us/office/what-s-new-in-microsoft-teams-d7092a6d-c896-424c-b362-a472d5f105de" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Teams', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Teams', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Teams', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.teams2` | <a href="{get_standalone_package_detail(packages, 'Teams', 'update_download')}"><img src="/images/2025/Teams.webp" alt="Download Image" width="80"></a> |
| **InTune Company Portal Standalone Installer**<br><a href="https://aka.ms/intuneupdates" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Intune', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Intune', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Intune', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.CompanyPortalMac` | <a href="{get_standalone_package_detail(packages, 'Intune', 'update_download')}"><img src="/images/companyportal.png" alt="Download Image" width="80"></a> |
| **Edge Standalone Installer** <sup>_(Stable Channel)_</sup><br><a href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Edge', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Edge', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Edge', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.edgemac` | <a href="{get_standalone_package_detail(packages, 'Edge', 'update_download')}"><img src="/images/edge_app.png" alt="Download Image" width="80"></a>|
| **Defender for Endpoint Installer**<br><a href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Defender For Endpoint', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Defender For Endpoint', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Defender For Endpoint', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.wdav` | <a href="{get_standalone_package_detail(packages, 'Defender For Endpoint', 'update_download')}"><img src="/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Defender for Consumers Installer**<br><a href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Defender For Consumers', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Defender For Consumers', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Defender For Consumers', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.wdav` | <a href="{get_standalone_package_detail(packages, 'Defender For Consumers', 'update_download')}"><img src="/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Defender SHIM Installer**<br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Defender Shim', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Defender Shim', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Defender Shim', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.wdav.shim` | <a href="{get_standalone_package_detail(packages, 'Defender Shim', 'update_download')}"><img src="/images/defender_512x512x32.png" alt="Download Image" width="80"></a> |
| **Visual Studio Code Insider Standalone Installer**<br><a href="https://github.com/microsoft/vscode/labels/iteration-plan" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'Visual', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'Visual', 'full_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'Visual', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.VSCodeInsider` | <a href="{get_standalone_package_detail(packages, 'Visual', 'update_download')}"><img src="/images/2021/Code_Insider.webp" alt="Download Image" width="80"></a>|
| **AutoUpdate Standalone Installer**<br><a href="https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate" style="text-decoration: none;"><small>_Release Notes_</small></a><br><br>_**Last Update:** `{get_standalone_package_detail(packages, 'MAU', 'last_updated')}`_<br> | **Version:**<br>`{get_standalone_package_detail(packages, 'MAU', 'short_version')}`<br><br>**Min OS:**<br>`{get_standalone_package_detail(packages, 'MAU', 'min_os')}`<br><br>**CFBundle ID:**<br>`com.microsoft.autoupdate` | <a href="{get_standalone_package_detail(packages, 'MAU', 'update_download')}"><img src="/images/autoupdate.png" alt="Download Image" width="80"></a>|

</div>

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

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_standalone_preview.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/standalone_apps/standalone_preview_version_en.md"

    # Parse the XML and generate content
    global_last_updated, packages = parse_latest_xml(xml_file_path)

    readme_content = generate_readme_content(global_last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)