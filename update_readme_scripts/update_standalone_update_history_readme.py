import xml.etree.ElementTree as ET
from datetime import datetime
import pytz
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def parse_update_history_xml(file_path):
    logging.info(f"Parsing XML file: {file_path}")

    # Parse the XML file
    tree = ET.parse(file_path)
    root = tree.getroot()
    logging.debug("XML file parsed successfully")

    # Extract last_scan_date
    last_scan_date = root.find("last_scan_date").text.strip()
    logging.info(f"XML last_scan_date: {last_scan_date}")

    # Extract release details
    releases = []
    for release in root.findall("release"):
        if release.find("archive").text.strip().lower() == "true":
            release_info = {
                "date": release.find("date").text.strip(),
                "version": release.find("version").text.strip(),
                "businesspro_suite_download": "archived",
                "suite_download": "archived",
                "word_update": "archived",
                "excel_update": "archived",
                "powerpoint_update": "archived",
                "outlook_update": "archived",
                "onenote_update": "archived",
            }
        else:
            release_info = {
                "date": release.find("date").text.strip(),
                "version": release.find("version").text.strip(),
                "businesspro_suite_download": release.find("businesspro_suite_download").text.strip() if release.find("businesspro_suite_download") is not None else "",
                "suite_download": release.find("suite_download").text.strip() if release.find("suite_download") is not None else "",
                "word_update": release.find("word_update").text.strip() if release.find("word_update") is not None else "",
                "excel_update": release.find("excel_update").text.strip() if release.find("excel_update") is not None else "",
                "powerpoint_update": release.find("powerpoint_update").text.strip() if release.find("powerpoint_update") is not None else "",
                "outlook_update": release.find("outlook_update").text.strip() if release.find("outlook_update") is not None else "",
                "onenote_update": release.find("onenote_update").text.strip() if release.find("onenote_update") is not None else "",
            }
        releases.append(release_info)
        # logging.debug(f"Extracted release: {release_info}") # Uncomment to see all release details

    return last_scan_date, releases

def generate_readme_content(last_scan_date, releases):
    logging.info("Generating standalone_update_history_readme content")

    # Set timezone to US/Eastern (EST/EDT)
    eastern = pytz.timezone('US/Eastern')

    # Get the current time in UTC and convert to EST
    current_time = datetime.now(pytz.utc).astimezone(eastern).strftime("%B %d, %Y %I:%M %p %Z")
    logging.debug(f"Current time (EST): {current_time}")

    content = f"""
# Standalone Update History

<sup>_Last Updated: <code style="color : mediumseagreen">{last_scan_date}_</code>

| Version | Date | BusinessPro | Suite | Word | Excel | PowerPoint | Outlook | OneNote |
|---------|------|-------------|-------|------|-------|------------|---------|---------|
"""
    for release in releases:
        content += f"| {release['version']} | {release['date']} | "
        content += f"archived | " if release['businesspro_suite_download'] == "archived" else f"[BusinessPro]({release['businesspro_suite_download']}) | " if release['businesspro_suite_download'] else " | "
        content += f"archived | " if release['suite_download'] == "archived" else f"[Suite]({release['suite_download']}) | " if release['suite_download'] else " | "
        content += f"archived | " if release['word_update'] == "archived" else f"[Word]({release['word_update']}) | " if release['word_update'] else " | "
        content += f"archived | " if release['excel_update'] == "archived" else f"[Excel]({release['excel_update']}) | " if release['excel_update'] else " | "
        content += f"archived | " if release['powerpoint_update'] == "archived" else f"[PowerPoint]({release['powerpoint_update']}) | " if release['powerpoint_update'] else " | "
        content += f"archived | " if release['outlook_update'] == "archived" else f"[Outlook]({release['outlook_update']}) | " if release['outlook_update'] else " | "
        content += f"archived | " if release['onenote_update'] == "archived" else f"[OneNote]({release['onenote_update']}) | " if release['onenote_update'] else " | "
        content += "\n"

    logging.info("standalone_update_history_readme content generated successfully")

    return content

def overwrite_readme(file_path, content):
    with open(file_path, "w") as file:
        file.write(content)
    print(f"standalone_update_history_readme.md has been overwritten.")

if __name__ == "__main__":
    # Define file paths
    xml_file_path = "repo_raw_data/macos_standalone_update_history.xml"  # Update this path if the file is located elsewhere
    readme_file_path = "standalone_update_history_readme.md"

    # Parse the XML and generate content
    last_scan_date, releases = parse_update_history_xml(xml_file_path)

    readme_content = generate_readme_content(last_scan_date, releases)

    # Overwrite the README file
    overwrite_readme(readme_file_path, readme_content)