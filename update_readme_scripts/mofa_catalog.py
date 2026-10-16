"""App catalog and row renderers for the standalone pages.

Every standalone page (Current / Preview / Beta versions, and their SHA1 / SHA256
pages) is rendered from APPS below. To add an app, add one entry here; to put it
on a channel, add its key to CHANNELS. Nothing else needs editing.

Feeds (repo_raw_data/*.xml):
  current  -> macos_standalone_latest.xml   fields: short_version, min_os, last_updated, full_update_download,
                                             full_update_sha1/256, app_only_update_download, app_update_sha1/256
  preview  -> macos_standalone_preview.xml  fields: short_version, min_os, last_updated, update_download, sha1, sha256
  beta     -> macos_standalone_beta.xml     (same as preview)
  edge     -> macos_standalone_edge_all.xml channels: current, beta, dev, canary
  onedrive -> macos_standalone_onedrive_all.xml rings: 'Production Ring', …
"""
from mofa_common import pkg_anchor, pkg_slug

Y = "(365/2021/2024)"
MAU_NOTE = "<sub>_(Does Not Contain MAU)_</sub>"
RD_ICON = '<img src="/images/microsoft-remote-desktop-logo.png" alt="Remote Desktop" width="15" style="vertical-align: middle; display: inline-block;" />'


def app(key, label, title, data, icon, bundle=None, download=None, link_field="full_update_download",
        notes=(), includes=None, app_only=None, variants=None, min_os=None, source="standalone"):
    return dict(key=key, label=label, title=title, data=data, icon=icon, bundle=bundle, download=download,
                link_field=link_field, notes=list(notes), includes=includes, app_only=app_only,
                variants=variants or {}, min_os=min_os, source=source)


OFFICE_NOTES = [("Release Notes", "https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac")]
DEFENDER_NOTES = [("Release Notes", "https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew")]
INTUNE_NOTES = [("Release Notes", "https://aka.ms/intuneupdates")]
WINAPP_NOTES = [("Release Notes", "https://learn.microsoft.com/en-us/windows-app/whats-new?tabs=macos")]

APPS = {a["key"]: a for a in [
    app("office-suite", "Office Suite", f"**Microsoft** {Y} **Office Suite Installer**", "Microsoft Office Suite",
        "/images/Office_Suite.webp", "com.microsoft.office", "https://go.microsoft.com/fwlink/?linkid=525133",
        notes=OFFICE_NOTES, includes="Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, Defender Shim, and MAU"),
    app("businesspro-suite", "BusinessPro Suite", f"**Microsoft** {Y} **BusinessPro Suite Installer**", "Microsoft BusinessPro Suite",
        "/images/Office_Suite.webp", "com.microsoft.office", "https://go.microsoft.com/fwlink/?linkid=2009112",
        includes="Includes Word, Excel, PowerPoint, Outlook, OneNote, OneDrive, Teams, Defender Shim, and MAU"),
    app("word", "Word", f"**Word** {Y} **Standalone Installer**", "Word", "/images/2025/Word.webp", "com.microsoft.word",
        "https://go.microsoft.com/fwlink/?linkid=525134", app_only=f"**Word** {Y} **App Only Installer**"),
    app("excel", "Excel", f"**Excel** {Y} **Standalone Installer**", "Excel", "/images/2025/Excel.webp", "com.microsoft.excel",
        "https://go.microsoft.com/fwlink/?linkid=525135", app_only=f"**Excel** {Y} **App Only Installer**"),
    app("powerpoint", "PowerPoint", f"**PowerPoint** {Y} **Standalone Installer**", "PowerPoint", "/images/2025/PowerPoint.webp",
        "com.microsoft.powerpoint", "https://go.microsoft.com/fwlink/?linkid=525136", app_only=f"**PowerPoint** {Y} **App Only Installer**"),
    app("outlook", "Outlook", f"**Outlook** {Y} **Standalone Installer**", "Outlook", "/images/2025/Outlook.webp", "com.microsoft.outlook",
        "https://go.microsoft.com/fwlink/?linkid=525137", app_only=f"**Outlook** {Y} **App Only Installer**"),
    app("onenote", "OneNote", f"**OneNote** {Y} **Standalone Installer**", "OneNote", "/images/2025/OneNote.webp", "com.microsoft.onenote.mac",
        "https://go.microsoft.com/fwlink/?linkid=820886", app_only=f"**OneNote** {Y} **App Only Installer**"),
    app("onedrive", "OneDrive", "**OneDrive Standalone Installer** <sup>(Production Ring)</sup>", "Production Ring",
        "/images/2025/OneDrive.webp", "com.microsoft.OneDrive", "https://go.microsoft.com/fwlink/?linkid=823060", min_os="13.0", source="onedrive",
        notes=[("Release Notes", "https://support.microsoft.com/en-us/office/onedrive-release-notes-845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac")]),
    app("skype", "Skype for Business", "**Skype for Business Standalone Installer**", "Skype", "/images/Skype_For_Business.webp",
        "com.microsoft.SkypeForBusiness", link_field="app_only_update_download",
        notes=[("Release Notes", "https://support.microsoft.com/en-us/office/follow-the-latest-updates-in-skype-for-business-cece9f93-add1-4d93-9a38-56cc598e5781"),
               ("Retired Notes", "https://support.microsoft.com/en-us/skype/skype-is-retiring-in-may-2025-what-you-need-to-know-2a7d2501-427f-485e-8be0-2068a9f90472")]),
    app("teams", "Teams", "**Teams Standalone Installer**", "Teams", "/images/2025/Teams.webp", "com.microsoft.teams2",
        "https://go.microsoft.com/fwlink/?linkid=2249065",
        notes=[("Release Notes", "https://support.microsoft.com/en-us/office/what-s-new-in-microsoft-teams-d7092a6d-c896-424c-b362-a472d5f105de"),
               ("Version History", "https://learn.microsoft.com/en-us/officeupdates/teams-app-versioning")]),
    app("intune", "Intune Company Portal", "**InTune Company Portal Standalone Installer**", "Intune", "/images/2021/Company_Portal.webp",
        "com.microsoft.CompanyPortalMac", "https://go.microsoft.com/fwlink/?linkid=853070", notes=INTUNE_NOTES,
        app_only="**InTune Company Portal App Only Installer**"),
    app("edge", "Edge", "**Edge** <sup>_(Current Channel)_</sup>", "current", "/images/edge/edge.webp", None, min_os="11.0", source="edge",
        notes=[("Release Notes", "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel")],
        variants={"preview": dict(title="**Edge Standalone Installer** <sup>_(Stable Channel)_</sup>", data="Edge", source="standalone", min_os=None, bundle="com.microsoft.edgemac")}),
    app("edge-beta", "Edge (Beta Channel)", "**Edge** <sup>_(Beta Channel)_</sup>", "beta", "/images/edge/edge_beta.webp", None, min_os="11.0", source="edge",
        notes=[("Release Notes", "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-beta-channel")]),
    app("edge-dev", "Edge (Dev Channel)", "**Edge** <sup>_(Dev Channel)_</sup>", "dev", "/images/edge/edge_dev.webp", None, min_os="11.0", source="edge"),
    app("edge-canary", "Edge (Canary Channel)", "**Edge** <sup>_(Canary Channel)_</sup>", "canary", "/images/edge/edge_canary.webp", None, min_os="11.0", source="edge"),
    app("defender-endpoint", "Defender for Endpoint", "**Defender for Endpoint Installer**", "Defender For Endpoint", "/images/2025/Defender.webp",
        "com.microsoft.wdav", "https://go.microsoft.com/fwlink/?linkid=2097502", notes=DEFENDER_NOTES),
    app("defender-consumers", "Defender for Consumers", "**Defender for Consumers Installer**", "Defender For Consumers", "/images/2025/Defender.webp",
        "com.microsoft.wdav", "https://go.microsoft.com/fwlink/?linkid=2247001", notes=DEFENDER_NOTES),
    app("defender-shim", "Defender Shim", "**Defender SHIM Installer**", "Defender Shim", "/images/2025/Defender.webp", "com.microsoft.wdav.shim",
        link_field="app_only_update_download"),
    app("windows-app", "Windows App", f"**Windows App Standalone Installer** <sup>_(Remote Desktop {RD_ICON})_</sup>", "Windows App",
        "/images/2025/Windows_App.webp", "com.microsoft.rdc.macos", "https://go.microsoft.com/fwlink/?linkid=868963", notes=WINAPP_NOTES,
        app_only=f"**Windows App Only Installer** <sup>_(Remote Desktop {RD_ICON})_</sup>"),
    app("windows-app-beta", "Windows App Beta", f"**Windows App Beta Standalone Installer** <sup>_(Remote Desktop {RD_ICON})_</sup>", "Windows App Beta",
        "/images/2025/Windows_App.webp", "com.microsoft.rdc.macos.beta", notes=WINAPP_NOTES,
        variants={"beta": dict(download="https://install.appcenter.ms/orgs/rdmacios-k2vy/apps/microsoft-remote-desktop-for-mac/distribution_groups/all-users-of-microsoft-remote-desktop-for-mac")}),
    app("vscode", "Visual Studio Code", "**Visual Studio Code Standalone Installer**", "Visual", "/images/2021/Code.webp", "com.microsoft.VSCode",
        "https://code.visualstudio.com/sha/download?build=stable&os=darwin-universal-dmg",
        notes=[("Release Notes", "https://code.visualstudio.com/updates/")],
        variants={"preview": dict(label="Visual Studio Code Insider", title="**Visual Studio Code Insider Standalone Installer**", icon="/images/2021/Code_Insider.webp", bundle="com.microsoft.VSCodeInsiders", version_field="full_version"),
                  "beta": dict(label="Visual Studio Code Insider", title="**Visual Studio Code Insider Standalone Installer**", icon="/images/2021/Code_Insider.webp", bundle="com.microsoft.VSCodeInsiders", version_field="full_version")}),
    app("m365-copilot", "Microsoft 365 Copilot", "**Microsoft 365 Copilot**", "Copilot", "/images/2025/Copilot.webp", "com.microsoft.m365copilot",
        "https://go.microsoft.com/fwlink/?linkid=2325438",
        notes=[("Release Notes", "https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes?tabs=mac")],
        includes="Transitioning into the Copilot app below",
        variants={"preview": dict(label="Microsoft Copilot", title="**Microsoft Copilot**", includes=None, version_field="full_version"), "beta": dict(label="Microsoft Copilot", title="**Microsoft Copilot**", includes=None)}),
    app("copilot-app", "Copilot App", "**Microsoft Copilot** <sup>_(Copilot App)_</sup>", "Copilot App", "/images/2026/Copilot_App.webp", "com.microsoft.m365copilot",
        "https://go.microsoft.com/fwlink/?linkid=2325114",
        notes=[("Transition Notes", "https://support.microsoft.com/en-us/microsoft-365-copilot/the-microsoft-365-app-transition-to-the-microsoft-365-copilot-app")],
        includes="Replaces Microsoft 365 Copilot; updated by EdgeUpdater, not MAU"),
    app("autoupdate", "AutoUpdate", "**AutoUpdate Standalone Installer**", "MAU", "/images/2019/AutoUpdate.webp", "com.microsoft.autoupdate",
        "https://go.microsoft.com/fwlink/?linkid=830196",
        notes=[("Release Notes", "https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate")]),
    app("licensing-helper", "Licensing Helper", "**Licensing Helper Tool Installer**", "Licensing Helper Tool", "/images/pkg-icon.png", None),
    app("quick-assist", "Quick Assist", "**Quick Assist Installer**", "Quick Assist", "/images/quickassist.png", "com.microsoft.quickassist"),
    app("remote-help", "Remote Help", "**Remote Help Installer**", "Remote Help", "/images/remotehelp.png", "com.microsoft.remotehelp"),
]}

# Which apps appear on each channel, in order. "+appOnly" rows follow their parent on the current channel.
CHANNELS = {
    "current": ["office-suite", "businesspro-suite", "word", "excel", "powerpoint", "outlook", "onenote", "onedrive", "skype",
                "teams", "intune", "edge", "defender-endpoint", "defender-consumers", "defender-shim", "windows-app", "vscode",
                "m365-copilot", "copilot-app", "autoupdate", "licensing-helper", "quick-assist", "remote-help"],
    "preview": ["word", "excel", "powerpoint", "outlook", "onenote", "teams", "intune", "edge", "defender-endpoint",
                "defender-consumers", "defender-shim", "m365-copilot", "vscode", "autoupdate"],
    "beta":    ["word", "excel", "powerpoint", "outlook", "onenote", "teams", "intune", "edge-beta", "edge-dev", "edge-canary",
                "defender-endpoint", "defender-consumers", "defender-shim", "vscode", "m365-copilot", "autoupdate", "windows-app-beta"],
}

PAGE_TEXT = {
    "current": ("Standalone packages", "Current production versions of Microsoft’s standalone macOS installers. Links go straight to Microsoft’s CDN and always download the newest build. Versions shown are as of the last update.", "macos_standalone_latest"),
    "preview": ("Preview packages", "Preview channel builds of Microsoft’s standalone macOS installers. Links go straight to Microsoft’s CDN and always download the newest build. Versions shown are as of the last update.", "macos_standalone_preview"),
    "beta":    ("Beta packages", "Beta channel builds of Microsoft’s standalone macOS installers. Links go straight to Microsoft’s CDN and always download the newest build. Versions shown are as of the last update.", "macos_standalone_beta"),
}
SHA_TEXT = {
    ("current", "SHA1"):   ("SHA1 hashes", "SHA1 checksums for the current standalone installers, so you can verify what you downloaded."),
    ("current", "SHA256"): ("SHA256 hashes", "SHA256 checksums for the current standalone installers, so you can verify what you downloaded."),
    ("preview", "SHA1"):   ("Preview SHA1 hashes", "SHA1 checksums for the preview channel installers."),
    ("preview", "SHA256"): ("Preview SHA256 hashes", "SHA256 checksums for the preview channel installers."),
    ("beta", "SHA1"):      ("Beta SHA1 hashes", "SHA1 checksums for the beta channel installers."),
    ("beta", "SHA256"):    ("Beta SHA256 hashes", "SHA256 checksums for the beta channel installers."),
}


# ---------------------------------------------------------------------------
def resolve(key, channel):
    """App entry with the channel's overrides applied."""
    a = dict(APPS[key])
    v = a["variants"].get(channel, {})
    a.update(v)
    a["channel_download"] = v.get("download")   # a fixed link that applies on this channel only
    return a


def record(a, channel, data):
    """The feed record for this app on this channel (dict of fields), or {}."""
    if a["source"] == "edge":
        return data["edge"].get(a["data"], {})
    if a["source"] == "onedrive":
        return data["onedrive"].get(a["data"], {})
    return data[channel].get(a["data"].lower(), {})


def download_link(a, channel, rec, app_only=False, for_hash=False):
    """Download URL for a row. Hash pages (for_hash) link to the exact file the hash describes,
    so they ignore channel-level fixed links and use the feed's file URL where one exists."""
    if app_only:
        return rec.get("app_only_update_download", "")
    if a["source"] == "edge":
        return rec.get("full_update_download", "")
    if a["source"] == "onedrive":
        return rec.get("full_update_download", "") if for_hash else a["download"]
    if channel == "current":
        return a["download"] or rec.get(a["link_field"], "")
    if for_hash:
        return rec.get("update_download", "")
    return a.get("channel_download") or rec.get("update_download", "")


def hash_value(a, channel, rec, algo):
    algo = algo.lower()
    if channel == "current" or a["source"] in ("edge", "onedrive"):
        return rec.get(f"full_update_{algo}", "")
    return rec.get(algo, "")


def title_cell(a, title, notes, includes, extra=None):
    parts = [title]
    if notes:
        parts.append("<br>" + " &#124; ".join(f'<a href="{u}" style="text-decoration: none;"><small>_{l}_</small></a>' for l, u in notes))
    if includes:
        parts.append(f"<br><sub>_({includes})_</sub>")
    if extra:
        parts.append(extra)
    return "".join(parts)


def version_row(a, channel, data, app_only=False):
    rec = record(a, channel, data)
    title = a["app_only"] if app_only else a["title"]
    extra = f" {MAU_NOTE}" if app_only else None
    label = a["label"] + (" (App Only)" if app_only else "")
    anchor = "" if app_only else pkg_anchor(a["label"], pkg_slug(a["label"]))
    bundle = a["bundle"] or rec.get("cf_bundle_version") or rec.get("CFBundleVersion") or "—"
    min_os = a["min_os"] or rec.get("min_os", "N/A")
    first = f"{anchor}{title_cell(a, title, a['notes'], a['includes'], extra)}<br><br>_**Last Update:** `{rec.get('last_updated', 'N/A')}`_<br>"
    vfield = a.get("version_field", "short_version")
    second = f"**Version:**<br>`{rec.get(vfield) or rec.get('short_version') or rec.get('version', 'N/A')}`<br><br>**Min OS:**<br>`{min_os}`<br><br>**CFBundle ID:**<br>`{bundle}`"
    third = f'<a href="{download_link(a, channel, rec, app_only)}"><img src="{a["icon"]}" alt="Download Image" width="80"></a>'
    return f"| {first} | {second} | {third} |"


def sha_row(a, channel, data, algo):
    rec = record(a, channel, data)
    anchor = pkg_anchor(a["label"], pkg_slug(a["label"]))
    return (f'| {anchor}{a["title"]} '
            f'| <a href="{download_link(a, channel, rec, for_hash=True)}"><img src="{a["icon"]}" alt="Download Image" width="60"></a> '
            f'| `{hash_value(a, channel, rec, algo)}` |')


def version_table(channel, data):
    out = ["| **Product Package** | **Version Info** | **Download** |", "|----------------------|------------------|--------------|"]
    for key in CHANNELS[channel]:
        a = resolve(key, channel)
        out.append(version_row(a, channel, data))
        if channel == "current" and a["app_only"]:
            out.append(version_row(a, channel, data, app_only=True))
    return "\n".join(out) + "\n"


def sha_table(channel, data, algo):
    badge = '<img src="/images/sha-256.png" alt="image" width="20" style="vertical-align: middle; display: inline-block;" />'
    out = [f"| **Product Package** | **Link** | **{badge} {algo} Hash {badge}** |", "|----------------------|-----------------|------------|"]
    for key in CHANNELS[channel]:
        out.append(sha_row(resolve(key, channel), channel, data, algo))
    return "\n".join(out) + "\n"
