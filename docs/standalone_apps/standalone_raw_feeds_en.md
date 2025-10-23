# 📂 MOFA Standalone RAW Feeds

This directory `https://github.com/cocopuff2u/MOFA/tree/main/latest_raw_files` contains raw output information related to Microsoft Standalone Applications and Mac/iOS App Store applications. These outputs are generated automatically using scripts, providing MacAdmins with the latest information in various formats. This setup simplifies the process of accessing and managing app-related data provided by Microsoft.

## 🛠️ Repository Overview

- **Scripts Location**: All scripts used to retrieve and process the data are located in the `https://github.com/cocopuff2u/MOFA/tree/main/.github/actions` directory of the repository. These scripts automate the fetching and formatting of app data from Microsoft-provided feeds. The raw data is automatically updated every 2 hours using a GitHub Action, which is triggered by workflows located in the `https://github.com/cocopuff2u/MOFA/tree/main/.github/actions` directory.
- **Purpose**: The scripts collect app metadata, convert it into multiple formats, and ensure the information remains current.

## 📄 File Outputs  

This directory provides app-related data in four widely-used formats: RSS, XML, JSON, and YAML. Each format contains the same set of files for easy comparison and integration into various workflows. Below is a breakdown of the available files by format:

### 📰 RSS Feeds
**Description**: RSS feeds provide syndicated update notifications for macOS standalone apps. They are rebuilt every 2 hours and published to the MOFA website, with source feeds available on GitHub.

- **[macOS Standalone All RSS Feeds](https://github.com/cocopuff2u/MOFA/tree/main/latest_raw_files/macos_standalone_rss)**
  Contains all the generated RSS feeds that are pushed to the MOFA website.

- **[macOS Standalone Office Suite RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/office_suite_rss.xml)**
  Contains the RSS feed for Office Suite. K

- **[macOS Standalone Word RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/word_rss.xml)**
  Contains the RSS feed for Word.

- **[macOS Standalone Excel RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/excel_rss.xml)**
  Contains the RSS feed for Excel.

- **[macOS Standalone OneNote RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/onenote_rss.xml)**
  Contains the RSS feed for OneNote.

- **[macOS Standalone OneNote RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/onenote_rss.xml)**
  Contains the RSS feed for OneNote.

- **[macOS Standalone Outlook RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/outlook_rss.xml)**
  Contains the RSS feed for Outlook.

- **[macOS Standalone PowerPoint RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/powerpoint_rss.xml)**
  Contains the RSS feed for PowerPoint.

- **[macOS Standalone Teams RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/teams_rss.xml)**
  Contains the RSS feed for Teams.

- **[macOS Standalone Windows App RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/windows_app_rss.xml)**
  Contains the RSS feed for Windows App.

- **[macOS Standalone Company Portal RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/company_portal_rss.xml)**
  Contains the RSS feed for Company Portal.

- **[macOS Standalone Defender RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/defender_for_endpoint_rss.xml)**
  Contains the RSS feed for Defender.

- **[macOS Standalone Microsoft AutoUpdater RSS Feeds](https://mofa.cocolabs.dev/rss_feeds/mau_rss.xml)**
  Contains the RSS feed for Microsoft AutoUpdater.

### 🧩 XML Files  
**Description**: XML provides structured app data, ideal for systems requiring hierarchical data representation.  

- **[macOS Standalone Update History](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_update_history.xml)**  
  Contains the update history for standalone macOS apps.  

- **[macOS Standalone Latest](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml)**  
  Provides the latest details about macOS standalone apps.  

- **[macOS Standalone Preview](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_preview.xml)**  
  Provides the preview details about macOS standalone apps.  

- **[macOS Standalone Beta](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_beta.xml)**  
  Provides the beta details about macOS standalone apps.  

- **[macOS Standalone CVE History](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/mac_standalone_cve_history.xml)**  
  Documents CVE (Common Vulnerabilities and Exposures) history for macOS standalone apps.  

### 🌐 JSON Files  
**Description**: JSON offers lightweight and easy-to-parse data, commonly used in modern development environments.  

- **[macOS Standalone Update History](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_update_history.json)**  
  Contains the update history for standalone macOS apps.  

- **[macOS Standalone Latest](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json)**  
  Provides the latest details about macOS standalone apps.  

- **[macOS Standalone Preview](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_preview.jsonl)**  
  Provides the preview details about macOS standalone apps.  

- **[macOS Standalone Beta](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_beta.json)**  
  Provides the beta details about macOS standalone apps.  

- **[macOS Standalone CVE History](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/mac_standalone_cve_history.json)**  
  Documents CVE history for macOS standalone apps.  

### ✍️ YAML Files  
**Description**: YAML offers a human-readable format, ideal for configurations and manual edits.  

- **[macOS Standalone Update History](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_update_history.yaml)**  
  Contains the update history for standalone macOS apps.  

- **[macOS Standalone Latest](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml)**  
  Provides the latest details about macOS standalone apps.  

- **[macOS Standalone Preview](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_preview.yaml)**  
  Provides the preview details about macOS standalone apps.  

- **[macOS Standalone Beta](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_beta.yaml)**  
  Provides the beta details about macOS standalone apps.  

- **[macOS Standalone CVE History](https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/mac_standalone_cve_history.yaml)**  
  Documents CVE history for macOS standalone apps.  

## 🌟 Why Multiple Formats?

The choice to provide XML, JSON, and YAML outputs ensures compatibility with a wide range of tools and systems. By supporting multiple formats, we accommodate diverse user needs:

- **XML**: Designed for enterprise applications and legacy systems.
- **JSON**: Suitable for modern development environments and APIs.
- **YAML**: Ideal for user-friendly configuration and quick manual edits.

## 📌 Usage Instructions

1. Locate the required output file in this directory.
2. Refer to the scripts in the `https://github.com/cocopuff2u/MOFA/tree/main/.github/actions` directory to understand or customize how the data is fetched and formatted.
3. Choose the format that best fits your application or integration needs.

## 🔗 Access the Latest Raw Files

You can access all the latest raw files [here](https://github.com/cocopuff2u/MOFA/tree/main/latest_raw_files).

