import xml.etree.ElementTree as ET
from datetime import datetime
import pytz
import logging
import os
from mofa_common import feed_header, add_pkg_anchors, frontmatter, status_line, legend, related, overwrite_readme, verify_note, now_eastern

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

    current_time = now_eastern()
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""{frontmatter('Other Microsoft apps', editLink=False, lastUpdated=False, outline=False, packageOutline=True)}
{feed_header('Other Microsoft apps', 'Microsoft tools outside the Office suite, from GitHub releases, Microsoft’s CDN or Homebrew. Versions shown are as of the last update.', last_updated, raw='macos_other_latest')}

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

    content += "\n{related}\n".replace("{related}", related([('Other apps SHA256', '/standalone_apps/macos_standalone_other_sha256'), ('Current versions', '/standalone_apps/standalone_current_version_en'), ('Raw feeds', '/standalone_apps/standalone_raw_feeds_en')]))

    # Add comment section
    content += """
"""

    logging.info("other_readme content generated successfully")

    return content


def generate_other_sha256_content(last_updated, packages):
    direct_packages = [p for p in packages if p["latest_download"].startswith("http")]
    content = f"""{frontmatter('Other apps SHA256', editLink=False, lastUpdated=False, outline=False, packageOutline=True)}
{feed_header('Other apps SHA256 hashes', 'SHA256 checksums for the Microsoft tools outside the Office suite, so you can verify what you downloaded.', last_updated, raw='macos_other_latest')}
{verify_note('SHA256')}

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
    content += "\n" + related([('Other Microsoft apps', '/standalone_apps/macos_standalone_other_readme'), ('SHA256 hashes', '/standalone_apps/standalone_sha256_hashes_en'), ('Raw feeds', '/standalone_apps/standalone_raw_feeds_en')]) + "\n"
    content += """
"""

    return content

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_other_latest.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "docs/standalone_apps/macos_standalone_other_readme.md"

    # Parse the XML and generate content
    last_updated, packages = parse_other_xml(xml_file_path)

    readme_content = generate_other_readme_content(last_updated, packages)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)
    overwrite_readme("docs/standalone_apps/macos_standalone_other_sha256.md", generate_other_sha256_content(last_updated, packages))
