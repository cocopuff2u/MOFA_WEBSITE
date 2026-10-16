"""Builds the nine standalone pages (Current / Preview / Beta versions and their SHA1 / SHA256 pages)
from the app catalog in mofa_catalog.py. Run from the repository root."""
import logging

from mofa_common import (feed_header, frontmatter, related, verify_note, overwrite_readme,
                         parse_latest_xml, parse_edge_xml, parse_onedrive_xml)
from mofa_catalog import PAGE_TEXT, SHA_TEXT, version_table, sha_table

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

FEEDS = {
    "current": "repo_raw_data/macos_standalone_latest.xml",
    "preview": "repo_raw_data/macos_standalone_preview.xml",
    "beta": "repo_raw_data/macos_standalone_beta.xml",
}
OUT = {
    ("current", None): "docs/standalone_apps/standalone_current_version_en.md",
    ("preview", None): "docs/standalone_apps/standalone_preview_version_en.md",
    ("beta", None): "docs/standalone_apps/standalone_beta_version_en.md",
    ("current", "SHA1"): "docs/standalone_apps/standalone_sha1_hashes_en.md",
    ("current", "SHA256"): "docs/standalone_apps/standalone_sha256_hashes_en.md",
    ("preview", "SHA1"): "docs/standalone_apps/standalone_preview_sha1_hashes_en.md",
    ("preview", "SHA256"): "docs/standalone_apps/standalone_preview_sha256_hashes_en.md",
    ("beta", "SHA1"): "docs/standalone_apps/standalone_beta_sha1_hashes_en.md",
    ("beta", "SHA256"): "docs/standalone_apps/standalone_beta_sha256_hashes_en.md",
}
APP_ONLY_NOTE = ("\n*Note that App-Only installers may download a newer package compared to standalone installers, "
                 "which are the recommended choice. Standalone installers are hardlinks and are typically updated within "
                 "48 hours after a release. For items without specific release notes, please refer to the release notes "
                 "for the entire suite.*\n")


def load():
    data, updated = {}, {}
    for ch, path in FEEDS.items():
        updated[ch], data[ch] = parse_latest_xml(path)
    _, data["edge"] = parse_edge_xml("repo_raw_data/macos_standalone_edge_all.xml")
    _, data["onedrive"] = parse_onedrive_xml("repo_raw_data/macos_standalone_onedrive_all.xml")
    return data, updated


def version_page(channel, data, updated):
    title, subtitle, raw = PAGE_TEXT[channel]
    body = (frontmatter(title, editLink=False, lastUpdated=False, outline=False, packageOutline=True) + "\n"
            + feed_header(title, subtitle, updated[channel], raw=raw) + "\n"
            + version_table(channel, data))
    if channel == "current":
        body += APP_ONLY_NOTE
    return body + "\n" + related(exclude=title) + "\n"


def sha_page(channel, algo, data, updated):
    title, subtitle = SHA_TEXT[(channel, algo)]
    raw = PAGE_TEXT[channel][2]
    return (frontmatter(title, editLink=False, lastUpdated=False, outline=False, packageOutline=True) + "\n"
            + feed_header(title, subtitle, updated[channel], raw=raw) + "\n"
            + verify_note(algo) + "\n\n"
            + sha_table(channel, data, algo)
            + "\n" + related(exclude=title) + "\n")


if __name__ == "__main__":
    data, updated = load()
    for (channel, algo), path in OUT.items():
        content = version_page(channel, data, updated) if algo is None else sha_page(channel, algo, data, updated)
        overwrite_readme(path, content)
    logging.info("standalone pages generated")
