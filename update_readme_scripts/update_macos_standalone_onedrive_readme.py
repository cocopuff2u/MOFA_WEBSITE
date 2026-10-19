"""OneDrive versions page, from MOFA's macos_standalone_onedrive_all feed.

The feed carries one <package> per update-ring manifest Microsoft publishes, plus the
official download link, the legacy standalone-updater manifests and the last build for
each older macOS range. Rings are grouped into sections here by name; anything new that
MOFA adds lands under "Other update feeds" rather than disappearing.
"""
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

# (feed name, label on the page, one-line meaning). Order is display order.
RELEASE = [
    ("Production Ring",                          "Production",            "The default ring. New builds every 1 to 2 weeks."),
    ("Upcoming Production Ring",                 "Upcoming Production",   "Staged to become the next Production build."),
    ("Production Ring (Official Download Link)", "Official download",     "What Microsoft's public <em>Download OneDrive for Mac</em> link serves."),
    ("Production Ring (Legacy Manifest)",        "Legacy manifest",       "The old generic Production manifest. Current clients no longer read it."),
    ("Deferred Ring",                            "Deferred",              "Enterprise ring. Gets a build after 60 days in Production, every 2 to 3 months."),
    ("Upcoming Deferred Ring",                   "Upcoming Deferred",     "Staged to become the next Deferred build."),
    ("Insider Ring",                             "Insider",               "First public ring. New builds 1 to 2 times a week."),
    ("Upcoming Insider Ring",                    "Upcoming Insider",      "Staged to become the next Insider build."),
]
INTERNAL = [
    ("MSIT Slow Ring (Preview)",          "MSIT Slow",          "Microsoft's own IT ring, ahead of Insider."),
    ("Upcoming MSIT Slow Ring (Preview)", "Upcoming MSIT Slow", "Staged to become the next MSIT Slow build."),
    ("MSIT Fast Ring (Preview)",          "MSIT Fast",          "Microsoft's earliest ring. Builds land here first."),
    ("Upcoming MSIT Fast Ring (Preview)", "Upcoming MSIT Fast", "Staged to become the next MSIT Fast build."),
]
STANDALONE = [
    ("Production Ring (Standalone Updater)", "Production", ""),
    ("Deferred Ring (Standalone Updater)",   "Deferred",   ""),
    ("Insider Ring (Standalone Updater)",    "Insider",    ""),
    ("MSIT Slow Ring (Standalone Updater)",  "MSIT Slow",  ""),
    ("MSIT Fast Ring (Standalone Updater)",  "MSIT Fast",  ""),
]
OTHER_KNOWN = {
    "Rolling Out (Unknown Use)": ("Rolling Out", "Purpose not documented by Microsoft. Historically trails Production by about a week."),
}
LEGACY_OS_RE = re.compile(r"^Last Build for (macOS .+)$", re.I)


def norm(name):
    return " ".join(name.split())


def val(ring, key):
    v = (ring.get(key) or "").strip()
    return "" if v in ("", "N/A", "None") else v


MONTHS = ["January", "February", "March", "April", "May", "June", "July", "August",
          "September", "October", "November", "December"]


def build_date(version):
    """OneDrive versions encode the build date: 26.173.0906 -> September 6, 2026."""
    m = re.match(r"^(\d{2})\.\d{3}\.(\d{2})(\d{2})", version or "")
    if not m:
        return ""
    yy, mm, dd = (int(x) for x in m.groups())
    if not 1 <= mm <= 12 or not 1 <= dd <= 31:
        return ""
    return f"{MONTHS[mm - 1]} {dd}, 20{yy:02d}"


def date_cell(ring):
    """Microsoft's date for the build: the release-notes date when they list one,
    otherwise the build date from the version number, shown muted."""
    rd = val(ring, "release_date")
    if rd:
        m = re.match(r"(?i)target date:\s*(.+)", rd)
        if m:
            return f'<td title="Microsoft\'s target date for this ring">Target {html.escape(m.group(1))}</td>'
        return f"<td>{html.escape(rd)}</td>"
    bd = build_date(val(ring, "short_version"))
    if bd:
        return (f'<td><span class="built" title="Microsoft lists no release date for this build. '
                f'This is the build date encoded in the version number.">{bd}</span></td>')
    return "<td>—</td>"


def version_cell(ring, label, versions):
    build = val(ring, "build") or val(ring, "short_version")
    tags = ""
    if label.startswith("Upcoming "):
        target = label[len("Upcoming "):]
        if target in versions and versions[target] == val(ring, "short_version"):
            tags += f'<span class="mofa-chip outline tag">same as {html.escape(target)}</span>'
    pct = val(ring, "rollout_percent")
    if pct.isdigit() and int(pct) < 100:
        tags += f'<span class="mofa-chip outline tag">{pct}% rollout</span>'
    return f"<code>{html.escape(build)}</code>{tags}"


def download_cell(ring):
    uni = val(ring, "full_update_download")
    intel = val(ring, "intel_update_download")
    out = f'<a class="mofa-chip" href="{html.escape(uni)}">Download<span class="ext"> .pkg</span></a>' if uni else ""
    if intel and intel != uni:
        out += f'<a class="mofa-chip outline" href="{html.escape(intel)}" title="Intel-only package">Intel</a>'
    return out


def ring_row(section, label, meaning, ring, versions):
    sub = f'<span class="sub">{meaning}</span>' if meaning else ""
    return (
        "<tr>"
        f"<td>{pkg_anchor(label, pkg_slug(section + '-' + label))}<img src=\"{ICON}\" alt=\"\" loading=\"lazy\" /><b>{html.escape(label)}</b>{sub}</td>"
        f"<td>{version_cell(ring, label, versions)}</td>"
        f"{date_cell(ring)}"
        f"<td>{download_cell(ring)}</td>"
        "</tr>\n"
    )


def ring_table(rows, first_col="Ring"):
    return (
        '<table class="mofa-dl mofa-rings">\n'
        f"<thead><tr><th>{first_col}</th><th>Version</th><th>Released</th><th>Download</th></tr></thead>\n"
        f"<tbody>\n{''.join(rows)}</tbody>\n</table>\n"
    )


def hash_table(entries):
    rows = ""
    for section, label, ring in entries:
        sha256 = val(ring, "full_update_sha256") or "—"
        sha1 = val(ring, "full_update_sha1") or "—"
        where = f'<span class="sub">{html.escape(section)}</span>' if section else ""
        rows += (f"<tr><td><b>{html.escape(label)}</b>{where}</td>"
                 f"<td><code>{sha256}</code></td><td><code>{sha1}</code></td></tr>\n")
    return (
        '<table class="mofa-dl mofa-hashes">\n'
        "<thead><tr><th>Ring</th><th>SHA256</th><th>SHA1</th></tr></thead>\n"
        f"<tbody>\n{rows}</tbody>\n</table>\n"
    )


def pick(rings, spec, used):
    """Rows for a section, in spec order, only for rings present in the feed."""
    out = []
    for feed_name, label, meaning in spec:
        if feed_name in rings:
            out.append((label, meaning, rings[feed_name]))
            used.add(feed_name)
    return out


def section(title, key, rows, versions, note=None, first_col="Ring"):
    if not rows:
        return ""
    body = f"\n## {title}\n\n"
    if note:
        body += f'<p class="mofa-note">{note}</p>\n\n'
    body += ring_table([ring_row(key, l, m, r, versions) for l, m, r in rows], first_col)
    return body


def generate(last_updated, rings_by_name):
    rings = {norm(k): v for k, v in rings_by_name.items()}
    used = set()

    release = pick(rings, RELEASE, used)
    internal = pick(rings, INTERNAL, used)
    standalone = pick(rings, STANDALONE, used)

    legacy = []
    for feed_name, ring in rings.items():
        m = LEGACY_OS_RE.match(feed_name)
        if m:
            legacy.append((m.group(1), "", ring))
            used.add(feed_name)
    legacy.sort(key=lambda t: [int(x) for x in re.findall(r"\d+", t[0])])

    other = []
    for feed_name, ring in rings.items():
        if feed_name in used:
            continue
        label, meaning = OTHER_KNOWN.get(feed_name, (feed_name, val(ring, "note") or "Not documented by Microsoft."))
        other.append((label, meaning, ring))

    # "same as …" compares an Upcoming row with the ring it feeds, within the same section.
    rel_versions = {l: val(r, "short_version") for l, _, r in release}
    int_versions = {l: val(r, "short_version") for l, _, r in internal}

    subtitle = ("Every OneDrive for Mac update ring, with the build each one serves right now. "
                "Downloads are the universal <code>.pkg</code> straight from Microsoft's CDN.")
    head = feed_header("OneDrive versions", subtitle, last_updated, raw="macos_standalone_onedrive_all",
                       icon=ICON, tile=True,
                       source=[("Release notes", RELEASE_NOTES), ("How rings work", RING_DOCS)])

    body = f"""{frontmatter('OneDrive versions', editLink=False, lastUpdated=False, outline=False, packageOutline=True)}
{head}
{legend([('Upcoming', 'the build staged to roll into that ring next'),
         ('% rollout', 'Microsoft is still throttling that build to a share of devices'),
         ('<span class="built">grey date</span>', 'Microsoft lists no release date, so this is the build date from the version number'),
         ('Intel', 'an Intel-only package exists alongside the universal one')])}
"""
    body += section("Release rings", "release", release, rel_versions)
    body += section("Microsoft internal rings", "internal", internal, int_versions,
                    note="Rings Microsoft's own IT department runs before a build reaches Insiders. "
                         "Not selectable in the app. Useful as an early look at what's coming.")
    body += section("Standalone updater", "standalone", standalone, {},
                    note="Manifests read by the legacy <code>OneDriveStandaloneUpdater</code> LaunchAgent, which older "
                         "installs still use. Current installs update from inside OneDrive.app and follow the release rings above.")
    body += section("Last builds for older macOS", "legacy", legacy, {},
                    note="The final build Microsoft offers to Macs that cannot run the current release. "
                         "A Mac reads the manifest for the highest range it falls in, so each row is the newest "
                         "OneDrive that still installs on that macOS range.",
                    first_col="macOS")
    body += section("Other update feeds", "other", other, {},
                    note="Endpoints the OneDrive installer checks that Microsoft does not document. "
                         "MOFA tracks them so a new build shows up here first.")

    hashes = ([("", l, r) for l, _, r in release]
              + [("Internal", l, r) for l, _, r in internal]
              + [("Standalone updater", l, r) for l, _, r in standalone]
              + [("Older macOS", l, r) for l, _, r in legacy]
              + [("", l, r) for l, _, r in other])
    body += f"""
## Checksums

{verify_note('SHA256')}

{hash_table(hashes)}
<p class="mofa-note">Microsoft does not publish one feed that covers every OneDrive ring, so MOFA reads the per-ring update manifests the OneDrive updater itself uses, plus the public download link. Hashes come from Microsoft's manifests. For a full version history, see <a href="{HANS_BRENDER}" target="_blank" rel="noopener">Hans Brender's OneDrive versions list</a>.</p>

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
