"""OneDrive versions page: one row per OneDrive update ring, from MOFA's macos_standalone_onedrive_all feed."""
import html
import logging
import re

from mofa_common import (feed_header, frontmatter, legend, overwrite_readme, parse_onedrive_xml,
                         pkg_anchor, pkg_slug, related, verify_note)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

XML_PATH = "repo_raw_data/macos_standalone_onedrive_all.xml"
PAGE_PATH = "docs/standalone_apps/macos_standalone_onedrive_readme.md"
ICON = "/images/2025/OneDrive.webp"

RELEASE_NOTES = "https://support.microsoft.com/en-us/office/onedrive-release-notes-845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac"
RING_DOCS = "https://learn.microsoft.com/en-us/sharepoint/sync-client-update-process"
HANS_BRENDER = "https://hansbrender.com/all-onedrive-versions-mac/"

# Display order and one-line meaning for each ring MOFA tracks. Anything else in the feed
# lands under "Other update feeds" so a new ring never silently disappears.
RINGS = [
    ("Production Ring",          "Production",          "The default ring. New builds every 1 to 2 weeks."),
    ("Upcoming Production Ring", "Upcoming Production", "Staged to become the next Production build."),
    ("Deferred Ring",            "Deferred",            "Enterprise ring. Gets a build after 60 days in Production, every 2 to 3 months."),
    ("Upcoming Deferred Ring",   "Upcoming Deferred",   "Staged to become the next Deferred build."),
    ("Insider Ring",             "Insider",             "First public ring. New builds 1 to 2 times a week."),
]
OTHER_LABELS = {
    "Rolling Out (Unknown Use)":     ("Rolling Out",     "Microsoft update endpoint. Purpose not documented."),
    "App New Version (Unknown Use)": ("App New Version", "Microsoft update endpoint. Purpose not documented."),
}


def norm(name):
    return " ".join(name.split())


def date_only(stamp):
    """'October 14, 2026 08:16 PM EDT' -> 'October 14, 2026'. Full stamp goes in the cell's title."""
    m = re.match(r"([A-Za-z]+ \d{1,2}, \d{4})", stamp)
    return m.group(1) if m else stamp


def ring_row(label, meaning, ring, baseline=None):
    """One <tr> of the ring table. `baseline` is (label, version) of the ring an Upcoming row feeds."""
    version = ring.get("short_version", "")
    same = ""
    if baseline and baseline[1] == version:
        same = f' <span class="mofa-chip outline same">same as {html.escape(baseline[0])}</span>'
    stamp = ring.get("last_updated", "")
    url = ring.get("full_update_download", "")
    return (
        f"<tr>"
        f"<td>{pkg_anchor(label, pkg_slug(label))}<img src=\"{ICON}\" alt=\"\" loading=\"lazy\" /><b>{html.escape(label)}</b>"
        f"<span class=\"sub\">{meaning}</span></td>"
        f"<td><code>{html.escape(version)}</code>{same}</td>"
        f"<td title=\"{html.escape(stamp)}\">{html.escape(date_only(stamp))}</td>"
        f"<td><a class=\"mofa-chip\" href=\"{html.escape(url)}\">Download<span class=\"ext\"> .pkg</span></a></td>"
        f"</tr>\n"
    )


def ring_table(rows):
    return (
        '<table class="mofa-dl mofa-rings">\n'
        "<thead><tr><th>Ring</th><th>Version</th><th>Updated</th><th>Download</th></tr></thead>\n"
        f"<tbody>\n{''.join(rows)}</tbody>\n</table>\n"
    )


def hash_table(entries):
    rows = "".join(
        f"<tr><td><b>{html.escape(label)}</b></td>"
        f"<td><code>{ring.get('full_update_sha256', '')}</code></td>"
        f"<td><code>{ring.get('full_update_sha1', '')}</code></td></tr>\n"
        for label, ring in entries
    )
    return (
        '<table class="mofa-dl mofa-hashes">\n'
        "<thead><tr><th>Ring</th><th>SHA256</th><th>SHA1</th></tr></thead>\n"
        f"<tbody>\n{rows}</tbody>\n</table>\n"
    )


def generate(last_updated, rings_by_name):
    rings = {norm(k): v for k, v in rings_by_name.items()}

    known, used = [], set()
    for feed_name, label, meaning in RINGS:
        if feed_name in rings:
            known.append((label, meaning, rings[feed_name]))
            used.add(feed_name)
    other = []
    for feed_name, ring in rings.items():
        if feed_name in used:
            continue
        label, meaning = OTHER_LABELS.get(feed_name, (feed_name.replace(" (Unknown Use)", ""), "Microsoft update endpoint. Purpose not documented."))
        other.append((label, meaning, ring))

    versions = {label: ring.get("short_version", "") for label, _, ring in known}
    main_rows = []
    for label, meaning, ring in known:
        base = None
        if label.startswith("Upcoming "):
            target = label[len("Upcoming "):]
            if target in versions:
                base = (target, versions[target])
        main_rows.append(ring_row(label, meaning, ring, base))
    other_rows = [ring_row(label, meaning, ring) for label, meaning, ring in other]

    subtitle = ("Every OneDrive for Mac update ring, with the build each one serves right now. "
                "Downloads are the universal <code>.pkg</code> straight from Microsoft.")
    head = feed_header("OneDrive versions", subtitle, last_updated, raw="macos_standalone_onedrive_all",
                       icon=ICON, tile=True,
                       source=[("Release notes", RELEASE_NOTES), ("How rings work", RING_DOCS)])

    body = f"""{frontmatter('OneDrive versions', editLink=False, lastUpdated=False, outline=False, packageOutline=True)}
{head}
{legend([('Upcoming', 'the build staged to roll into that ring next'), ('same as …', 'the upcoming build has already reached the ring')])}

## Release rings

{ring_table(main_rows)}
"""
    if other_rows:
        body += f"""
## Other update feeds

<p class="mofa-note">Microsoft's installer also checks these endpoints. MOFA tracks them so a new build shows up here first, but Microsoft does not document which clients they serve.</p>

{ring_table(other_rows)}
"""
    body += f"""
## Checksums

{verify_note('SHA256')}

{hash_table([(l, r) for l, _, r in known + other])}
<p class="mofa-note">Microsoft does not publish one feed that covers every OneDrive ring, so MOFA reads the per-ring update endpoints the OneDrive installer itself uses. Dates are when each endpoint last changed. For a full version history, see <a href="{HANS_BRENDER}" target="_blank" rel="noopener">Hans Brender's OneDrive versions list</a>.</p>

{related([('Current versions', '/standalone_apps/standalone_current_version_en'),
          ('SHA256 hashes', '/standalone_apps/standalone_sha256_hashes_en'),
          ('Office update history', '/standalone_apps/standalone_update_history_en'),
          ('Config profiles', '/macos_tools/preconfigured_profiles'),
          ('Raw feeds', '/standalone_apps/standalone_raw_feeds_en')])}
"""
    return body


if __name__ == "__main__":
    last_updated, rings = parse_onedrive_xml(XML_PATH)
    logging.info("OneDrive feed updated %s, %d rings", last_updated, len(rings))
    overwrite_readme(PAGE_PATH, generate(last_updated, rings))
