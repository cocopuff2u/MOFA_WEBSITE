import xml.etree.ElementTree as ET
from datetime import datetime
import pytz
import logging
import os

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_other_xml(file_path):
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
            "application_id": package.find("application_id").text.strip(),
            "application_name": package.find("application_name").text.strip(),
            "CFBundleVersion": package.find("CFBundleVersion").text.strip(),
            "short_version": package.find("short_version").text.strip(),
            "full_version": package.find("full_version").text.strip(),
            "last_updated": package.find("last_updated").text.strip(),
            "min_os": package.find("min_os").text.strip() if package.find("min_os") is not None else "N/A",
            "update_download": package.find("update_download").text.strip(),
            "latest_download": package.find("latest_download").text.strip(),
            "sha1": package.find("sha1").text.strip(),
            "sha256": package.find("sha256").text.strip(),
        }
        packages.append(package_info)
        # logging.debug(f"Extracted package: {package_info}") # Uncomment to see all package details

    return last_updated, packages

def get_other_package_icon(package_name):
    """
    Map an "other" tools package name to its logo under docs/public/images.
    """
    name = package_name.lower()
    if "powershell" in name:
        return "/images/2025/PowerShell.png"
    elif ".net sdk" in name:
        return "/images/2025/DotNet.png"
    elif "bicep" in name:
        return "/images/2025/Bicep.png"
    elif "sqlcmd" in name:
        return "/images/2025/Sqlcmd.png"
    elif name.startswith("az") or "azure" in name:
        return "/images/2025/Azure.png"
    else:
        return "/images/Microsoft_Logo.webp"

def generate_other_readme_content(last_updated, packages):
    logging.info("Generating other_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""---
editLink: false
lastUpdated: false
---
# <img src="/images/Microsoft_Logo.webp" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> Other Microsoft Apps

<span class="extra-small">All links below direct to Microsoft's official release sources (GitHub releases, Microsoft CDN, or Homebrew).</span>
<span class="extra-small">The version information listed below reflects the version available at the time of this update.</span>

<span class="extra-small">_Last Updated: <code style="color : dodgerblue">{last_updated}</code> [**_Raw XML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_other_latest.xml) [**_Raw YAML_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_other_latest.yaml) [**_Raw JSON_**](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_other_latest.json) (Automatically Updated every 4 hours)_</span>

| **Product Package** | **Bundle Information** | **Download** |
|----------------------|----------------------|--------------|
"""

    # Direct downloads first, Homebrew-only packages grouped at the bottom
    direct_packages = [p for p in packages if p["latest_download"].startswith("http")]
    brew_packages = [p for p in packages if not p["latest_download"].startswith("http")]

    for package in direct_packages + brew_packages:
        name = package["name"]
        icon = get_other_package_icon(name)
        download = package["latest_download"]

        if download.startswith("http"):
            download_cell = f"<a href=\"{download}\"><img src=\"{icon}\" alt=\"Download Image\" width=\"80\"></a>"
        else:
            # Not a direct download (e.g. installed via Homebrew)
            download_cell = f"<img src=\"{icon}\" alt=\"{name}\" width=\"80\"><br>`{download}`"

        content += (
            f"| **{name}**<br><br>_**Last Update:** `{package['last_updated']}`_<br> "
            f"| **Version:**<br>`{package['short_version']}` "
            f"| {download_cell} |\n"
        )

    # SHA256 table for packages with direct downloads
    content += """
## <img src="/images/Microsoft_Logo.webp" alt="image" width="25" style="vertical-align: middle; display: inline-block;" /> SHA256 Information

| **Product Package** | **Download** | **SHA256** |
|----------------------|-----------------|------------|
"""

    for package in direct_packages:
        name = package["name"]
        icon = get_other_package_icon(name)
        content += (
            f"| **{name}** "
            f"| <a href=\"{package['latest_download']}\"><img src=\"{icon}\" alt=\"Download Image\" width=\"80\"></a> "
            f"| `{package['sha256']}` |\n"
        )

    # Add comment section
    content += """
> [!IMPORTANT]
> This page is fully automated and updated through a script. To modify the content, the script itself must be updated. The information presented here is generated automatically based on the most recent data available from Microsoft. Please note that it may not always reflect complete accuracy. To access and edit the scripts, please visit the [scripts folder here](https://github.com/cocopuff2u/MOFA_WEBSITE/tree/main/update_readme_scripts).
"""

    logging.info("other_readme content generated successfully")

    return content

def overwrite_readme(file_path, content):
    # Ensure the directory exists
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        file.write(content)
    print(f"macos_standalone_other_readme has been overwritten.")

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_other_latest.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/standalone_apps/macos_standalone_other_readme.md"

    # Parse the XML and generate content
    last_updated, packages = parse_other_xml(xml_file_path)

    readme_content = generate_other_readme_content(last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)
