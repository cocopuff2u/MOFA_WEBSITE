---
title: Microsoft Office Repair Tools
---
<div class="mofa-page">

<div class="mofa-page-hero">
  <MofaMark :size="90" />
  <h1>Office <span class="gradient-title">repair</span> tools</h1>
  <p class="mofa-page-sub">Reset, repair or remove Microsoft apps on macOS with scripts you can read before you run.</p>
</div>

<p class="mofa-lead">When an Office app will not launch, will not sign in, or will not update, a clean reset usually beats a reinstall. These scripts clear the app's preferences, caches, keychain entries and licensing state in a known order, so the app starts fresh on the next launch. All of them are plain zsh and run from Terminal, Jamf, Intune or any MDM that can run a script.</p>

<div class="mofa-stats">
  <div><b>16 scripts</b><span>maintained by the MOFA community</span></div>
  <div><b>1 unified tool</b><span>Microsoft 365 Reset, by Dan Snelson</span></div>
  <div><b>26 archives</b><span>from Office-Reset.com, preserved as is</span></div>
</div>

<p class="mofa-note">Reset scripts delete app data for the current user, and removal scripts uninstall the app. Read the script first, test it on one Mac, and make sure anything you care about is synced before you run it.</p>

## MOFA community scripts {.mofa-h2}

<p class="mofa-lead">Built on the original Office-Reset.com tools and kept current by the community. Each script targets one app, so you can give users exactly the fix they need.</p>

<div class="mofa-legend center">
  <span class="mofa-legend-item"><b>Maintained by</b> the community</span>
  <span class="mofa-legend-item"><b>Language</b> zsh</span>
  <span class="mofa-legend-item"><b>Source</b> <a href="https://github.com/cocopuff2u/MOFA/tree/main/office_reset_tools/mofa_community_maintained/" target="_blank" rel="noopener">MOFA repo</a></span>
</div>

<table class="mofa-dl">
<thead><tr><th>Tool</th><th>Script</th></tr></thead>
<tbody>
<tr><td><img src="/images/autoupdate.png" alt="" loading="lazy" /><b>AutoUpdate Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_AutoUpdate_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/2025/Excel.webp" alt="" loading="lazy" /><b>Excel Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_Excel_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>License Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_License_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>License Sign-In Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_OfficeLicenseSignIn_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>Office Factory Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_Office_Factory_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>Office Removal</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_Office_Removal.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/2025/OneDrive.webp" alt="" loading="lazy" /><b>OneDrive Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_OneDrive_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/2025/OneNote.webp" alt="" loading="lazy" /><b>OneNote Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_OneNote_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/2025/Outlook.webp" alt="" loading="lazy" /><b>Outlook Data Removal</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_Outlook_Data_Removal.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/2025/Outlook.webp" alt="" loading="lazy" /><b>Outlook Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_Outlook_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/2025/PowerPoint.webp" alt="" loading="lazy" /><b>PowerPoint Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_PowerPoint_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/skype_for_business.png" alt="" loading="lazy" /><b>Skype For Business Removal</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_SkypeForBusiness_Removal.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/2025/Teams.webp" alt="" loading="lazy" /><b>Teams Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_Teams_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/2025/Word.webp" alt="" loading="lazy" /><b>Word Reset</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_Microsoft_Word_Reset.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/script.png" alt="" loading="lazy" /><b>WebExPT Removal</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_WebExPT_Removal.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/script.png" alt="" loading="lazy" /><b>Zoom Plugin Removal</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts/MOFA_Community_ZoomPlugin_Removal.zsh" target="_blank" rel="noopener">View script</a></td></tr>
<tr><td><img src="/images/script.png" alt="" loading="lazy" /><b>Everything</b></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/scripts" target="_blank" rel="noopener">All scripts</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/mofa_community_maintained/packages" target="_blank" rel="noopener">All packages</a></td></tr>
</tbody>
</table>

<p class="mofa-note">Help wanted: the community set still needs the remaining Office-Reset.com scripts reviewed and folded in, and the separate removal scripts combined into one removal tool. <a href="https://github.com/cocopuff2u/MOFA" target="_blank" rel="noopener">Join in on GitHub</a>.</p>

## Microsoft 365 Reset {.mofa-h2}

<div class="mofa-os">
  <img src="/images/Microsoft_365_Reset.png" alt="Microsoft 365 Reset" />
  <div><b>One script for everything</b><span>Maintained by Dan Snelson. The successor to the per-app reset tools.</span></div>
</div>

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://github.com/dan-snelson/Microsoft-365-Reset" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg></i><div><b>Interactive mode</b><span>A swiftDialog interface lets users pick what to repair, reset or remove. Built for Self Service.</span></div></a>
  <a class="mofa-row" href="https://github.com/dan-snelson/Microsoft-365-Reset" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6"/></svg></i><div><b>Silent mode</b><span>Pass parameters and it runs without prompts, for Jamf Pro policies and other MDM deployments.</span></div></a>
  <a class="mofa-row" href="https://github.com/dan-snelson/Microsoft-365-Reset" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M4 6h10M4 12h10M4 18h6M15 17l2.5 2.5L22 15"/></svg></i><div><b>Dependencies and logging</b><span>Handles the order things must happen in and writes a log you can hand to support.</span></div></a>
</div>

<div class="mofa-cta">
  <a class="mofa-btn" href="https://github.com/dan-snelson/Microsoft-365-Reset" target="_blank" rel="noopener">Microsoft 365 Reset on GitHub</a>
</div>

## Office-Reset.com archives {.mofa-h2}

<div class="mofa-os">
  <img src="/images/Office_Reset_512x512.png" alt="Office-Reset.com" />
  <div><b>The originals, preserved</b><span>Office-Reset.com is offline and these tools are no longer maintained.</span></div>
</div>

<div class="mofa-legend center">
  <span class="mofa-legend-item"><b>Status</b> Offline, no longer maintained</span>
  <span class="mofa-legend-item"><b>Source</b> <a href="https://github.com/cocopuff2u/MOFA/tree/main/office_reset_tools/office_reset_archived/" target="_blank" rel="noopener">MOFA repo</a></span>
</div>

<p class="mofa-note">Kept for reference and for anyone who still depends on a specific version. They receive no updates or support. For current fixes use the community scripts or Microsoft 365 Reset above. Packages download directly. Scripts open on GitHub.</p>

<table class="mofa-dl">
<thead><tr><th>Tool</th><th>Version</th><th>Download</th></tr></thead>
<tbody>
<tr><td><img src="/images/2025/Outlook.webp" alt="" loading="lazy" /><b>Mail To Outlook</b></td><td><code>2.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_MailToOutlook_2.1.pkg">Package</a></td></tr>
<tr><td><img src="/images/autoupdate.png" alt="" loading="lazy" /><b>AutoUpdate Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_AutoUpdate_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_AutoUpdate_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/Excel.webp" alt="" loading="lazy" /><b>Excel Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Excel_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Excel_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/Excel.webp" alt="" loading="lazy" /><b>Excel Reset</b></td><td><code>2.0.0</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Excel_Reset_2.0.0.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Excel_Reset_2.0.0.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>License Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_License_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_License_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>License Sign-In Reset</b></td><td><code>2.0.0</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_OfficeLicenseSignIn_Reset_2.0.0.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_OfficeLicenseSignIn_Reset_2.0.0.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>Factory Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Office_Factory_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Office_Factory_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>Office Removal</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Office_Removal_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Office_Removal_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>Office Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Office_Reset_1.9.1.pkg">Package</a></td></tr>
<tr><td><img src="/images/Office_Suite.webp" alt="" loading="lazy" /><b>Office Reset</b></td><td><code>2.0.0</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Office_Reset_2.0.0.pkg">Package</a></td></tr>
<tr><td><img src="/images/2025/OneDrive.webp" alt="" loading="lazy" /><b>OneDrive Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_OneDrive_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_OneDrive_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/OneDrive.webp" alt="" loading="lazy" /><b>OneDrive Reset</b></td><td><code>2.0.0</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_OneDrive_Reset_2.0.0.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_OneDrive_Reset_2.0.0.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/OneNote.webp" alt="" loading="lazy" /><b>OneNote Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_OneNote_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_OneNote_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/OneNote.webp" alt="" loading="lazy" /><b>OneNote Reset</b></td><td><code>2.0.0</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_OneNote_Reset_2.0.0.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_OneNote_Reset_2.0.0.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/Outlook.webp" alt="" loading="lazy" /><b>Outlook Data Removal</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Outlook_Data_Removal_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Outlook_Data_Removal_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/Outlook.webp" alt="" loading="lazy" /><b>Outlook Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Outlook_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Outlook_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/Outlook.webp" alt="" loading="lazy" /><b>Outlook Reset</b></td><td><code>2.0.0</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Outlook_Reset_2.0.0.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Outlook_Reset_2.0.0.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/PowerPoint.webp" alt="" loading="lazy" /><b>PowerPoint Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_PowerPoint_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_PowerPoint_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/PowerPoint.webp" alt="" loading="lazy" /><b>PowerPoint Reset</b></td><td><code>2.0.0</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_PowerPoint_Reset_2.0.0.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_PowerPoint_Reset_2.0.0.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/skype_for_business.png" alt="" loading="lazy" /><b>Skype For Business Removal</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_SkypeForBusiness_Removal_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_SkypeForBusiness_Removal_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/Teams.webp" alt="" loading="lazy" /><b>Teams Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Teams_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Teams_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/Teams.webp" alt="" loading="lazy" /><b>Teams Reset</b></td><td><code>2.0.0</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Teams_Reset_2.0.0.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Teams_Reset_2.0.0.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/Word.webp" alt="" loading="lazy" /><b>Word Reset</b></td><td><code>1.9.1</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Word_Reset_1.9.1.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Word_Reset_1.9.1.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/2025/Word.webp" alt="" loading="lazy" /><b>Word Reset</b></td><td><code>2.0.0</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_Microsoft_Word_Reset_2.0.0.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_Microsoft_Word_Reset_2.0.0.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/script.png" alt="" loading="lazy" /><b>WebExPT Removal</b></td><td><code>1.9</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_WebExPT_Removal_1.9.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_WebExPT_Removal_1.9.zsh" target="_blank" rel="noopener">Script</a></td></tr>
<tr><td><img src="/images/script.png" alt="" loading="lazy" /><b>Zoom Plugin Removal</b></td><td><code>1.9</code></td><td><a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/raw/refs/heads/main/office_reset_tools/office_reset_archived/packages/Office-Reset.com_ZoomPlugin_Removal_1.9.pkg">Package</a> <a class="mofa-chip" href="https://github.com/cocopuff2u/MOFA/blob/main/office_reset_tools/office_reset_archived/scripts/Office-Reset.com_ZoomPlugin_Removal_1.9.zsh" target="_blank" rel="noopener">Script</a></td></tr>
</tbody>
</table>

<p class="mofa-foot">Have a fix that is not here, or found a script that no longer works? Open an issue or send a pull request and it gets looked at.</p>

<div class="mofa-cta">
  <a class="mofa-btn" href="https://github.com/cocopuff2u/MOFA/issues" target="_blank" rel="noopener">Open an issue</a>
  <a class="mofa-btn alt" href="https://github.com/cocopuff2u/MOFA/discussions" target="_blank" rel="noopener">Start a discussion</a>
</div>

<div class="mofa-related"><span>Related</span><a class="mofa-chip outline" href="/macos_tools/community_scripts">Community scripts</a><a class="mofa-chip outline" href="/macos_tools/preconfigured_profiles">Preconfigured profiles</a><a class="mofa-chip outline" href="/about_support/report_issue">Report an issue</a></div>

</div>
