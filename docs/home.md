---
title: Get Started
---
<div class="mofa-page">

<div class="mofa-page-hero">
  <MofaMark :size="120" />
  <h1>Welcome to <span class="gradient-title">MOFA</span></h1>
  <p class="mofa-page-sub">Microsoft Overview Feed for Apple</p>
</div>

<p class="mofa-lead"><span class="gradient-title">MOFA</span> tracks every Microsoft app that runs on a Mac, iPhone or iPad, and turns what Microsoft publishes into pages you can read in seconds and feeds you can script against. Versions, download links, hashes, release notes and security history, refreshed automatically, with no sign-in.</p>

<div class="mofa-stats">
  <div><b>4 sources</b><span>standalone installers, two App Stores, and other Microsoft apps</span></div>
  <div><b>Every 2 hours</b><span>pulled straight from Microsoft</span></div>
  <div><b>XML · JSON · YAML · RSS</b><span>every page is also a feed</span></div>
</div>

## Start here {.mofa-h2}

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="/standalone_apps/standalone_current_version_en"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></svg></i><div><b>Grab the current installer</b><span>Every Office app, Teams, OneDrive, Defender and more, with direct links to Microsoft's CDN and the minimum macOS each needs.</span></div></a>
  <a class="mofa-row" href="/guides/how_to_sha256"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>Verify what you downloaded</b><span>Check a package against its published SHA256 in one Terminal command. Takes a minute the first time.</span></div></a>
  <a class="mofa-row" href="/standalone_apps/standalone_raw_feeds_en"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg></i><div><b>Wire it into your tooling</b><span>The same data as XML, JSON, YAML and RSS, for Munki, Jamf, Intune, a dashboard or a script.</span></div></a>
</div>

## What's tracked {.mofa-h2}

<div class="mofa-rows rows-left">
  <div class="mofa-row"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M3 7l9-4 9 4-9 4zM3 7v10l9 4 9-4V7M12 11v10"/></svg></i><div><b><a href="/standalone_apps/standalone_current_version_en">Standalone installers</a></b><span>Direct from Microsoft's CDN, no App Store needed. <a href="/standalone_apps/standalone_current_version_en">Current</a>, <a href="/standalone_apps/standalone_preview_version_en">Preview</a> and <a href="/standalone_apps/standalone_beta_version_en">Beta</a> channels, each with <a href="/standalone_apps/standalone_sha1_hashes_en">SHA1</a> and <a href="/standalone_apps/standalone_sha256_hashes_en">SHA256</a> hashes.</span></div></div>
  <a class="mofa-row" href="/macos_appstore/macos_appstore_current_version"><i class="ic-globe"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg></i><div><b>Mac App Store</b><span>Microsoft apps distributed through the App Store, for centrally managed installs with VPP.</span></div></a>
  <a class="mofa-row" href="/ios_appstore/ios_appstore_current_version"><i class="ic-refine"><svg viewBox="0 0 24 24"><rect x="7" y="2" width="10" height="20" rx="2"/><path d="M11 18h2"/></svg></i><div><b>iOS App Store</b><span>Microsoft apps for iPhone and iPad, with versions, release notes and minimum iOS.</span></div></a>
  <div class="mofa-row"><i class="ic-chat"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></i><div><b><a href="/standalone_apps/standalone_update_history_en">History and security</a></b><span><a href="/standalone_apps/standalone_update_history_en">Office update history</a>, <a href="/standalone_apps/teams_update_history_en">Teams update history</a> and <a href="/standalone_apps/standalone_cve_history_en">Office CVE history</a>, so "are we patched?" has a quick answer.</span></div></div>
  <div class="mofa-row"><i class="ic-bug"><svg viewBox="0 0 24 24"><path d="M3 6a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></i><div><b><a href="/standalone_apps/macos_standalone_other_readme">Other Microsoft apps</a></b><span>PowerShell, .NET, Azure CLI, VS Code and the rest, plus <a href="/standalone_apps/macos_standalone_onedrive_readme">every OneDrive build</a>.</span></div></div>
  <a class="mofa-row" href="/standalone_apps/standalone_last_supported_versions_en"><i class="ic-mail"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg></i><div><b>Last supported versions</b><span>The final Office build for each macOS release Microsoft no longer updates, for the Macs you cannot upgrade yet.</span></div></a>
</div>

## Tools {.mofa-h2}

<div class="mofa-rows rows-left">
  <div class="mofa-row"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M4 6h10M4 12h10M4 18h6M15 17l2.5 2.5L22 15"/></svg></i><div><b><a href="/macos_tools/preconfigured_profiles">Configuration profiles</a></b><span>Ready-made profiles for AutoUpdate deadlines and telemetry, and a <a href="/macos_tools/profile_breakdown">breakdown</a> if you want to build your own.</span></div></div>
  <a class="mofa-row" href="/macos_tools/microsoft_office_repair_tools"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M14.5 4.5a4 4 0 0 0-5 5L4 15v5h5l5.5-5.5a4 4 0 0 0 5-5l-2.5 2.5-2-2z"/></svg></i><div><b>Repair tools</b><span>Reset and removal scripts for every Office app, plus Microsoft 365 Reset for everything at once.</span></div></a>
  <a class="mofa-row" href="/macos_tools/community_scripts"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg></i><div><b>Community scripts</b><span>Install, update and remove Office with scripts other Mac admins run in production.</span></div></a>
  <a class="mofa-row" href="/macos_tools/app_icons"><i class="ic-chat"><svg viewBox="0 0 24 24"><rect x="4" y="4" width="16" height="16" rx="4"/><circle cx="12" cy="12" r="3"/></svg></i><div><b>App icons</b><span>High-resolution icons for every Microsoft app, in WEBP and PNG, for Self Service and Company Portal.</span></div></a>
  <div class="mofa-row"><i class="ic-bug"><svg viewBox="0 0 24 24"><path d="M6 3h9l5 5v13H6z"/><path d="M14 3v6h6M9 13h6M9 17h6"/></svg></i><div><b><a href="/guides/how_to_plist">How-to guides</a></b><span>Deploy a <a href="/guides/how_to_plist">plist</a> with Jamf or Intune, and verify downloads with <a href="/guides/how_to_sha256">SHA256</a> or <a href="/guides/how_to_sha1">SHA1</a>.</span></div></div>
  <a class="mofa-row" href="/about_support/feedback"><i class="ic-mail"><svg viewBox="0 0 24 24"><path d="M9 18h6M10 21h4M12 3a6 6 0 0 0-3.5 10.9c.6.5.9 1.1 1 1.9h5c.1-.8.4-1.4 1-1.9A6 6 0 0 0 12 3z"/></svg></i><div><b>Something missing?</b><span>Ask for an app, a feed or a guide. Most of what is here started as a request.</span></div></a>
</div>

## How it works {.mofa-h2}

<p class="mofa-lead">Scripts pull from Microsoft's own update feeds and the App Store every two hours, then rebuild every page and feed on this site. Nothing is edited by hand, so the data is only as late as Microsoft's last publish. All of it is open source, inspired by the work of <a href="https://macadmins.software" target="_blank" rel="noopener">MacAdmins.software</a>.</p>

<div class="mofa-cta">
  <a class="mofa-btn" href="/about_support/about">About the project</a>
  <a class="mofa-btn alt" href="https://github.com/cocopuff2u/mofa" target="_blank" rel="noopener">Data on GitHub</a>
  <a class="mofa-btn alt" href="https://github.com/cocopuff2u/mofa_website" target="_blank" rel="noopener">Site on GitHub</a>
</div>

</div>
