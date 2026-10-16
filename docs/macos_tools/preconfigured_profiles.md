---
title: Preconfigured Profiles
---
<div class="mofa-page">

<div class="mofa-page-hero">
  <MofaMark :size="90" />
  <h1>Preconfigured <span class="gradient-title">profiles</span></h1>
  <p class="mofa-page-sub">Ready-to-deploy mobileconfig files for managing Microsoft apps on macOS.</p>
</div>

<p class="mofa-lead">Upload a profile straight to your MDM, or copy the keys into a configuration of your own. Every profile is a plain mobileconfig file, so you can read exactly what it sets before you ship it.</p>

<div class="mofa-stats">
  <div><b>13 profiles</b><span>ready to upload to any MDM</span></div>
  <div><b>Forced updates</b><span>3, 7 or 14 day deadlines for AutoUpdate</span></div>
  <div><b>Privacy</b><span>telemetry off across Office and AutoUpdate</span></div>
</div>

## Microsoft AutoUpdate {.mofa-h2}

<p class="mofa-lead">Enforce a global forced-update deadline for Microsoft AutoUpdate (MAU). Updates download automatically, and once the deadline passes users get a 60 minute countdown before the app is quit and updated.</p>

<figure class="mofa-figure">
  <img src="/images/mau_update_prompt.png" alt="Microsoft AutoUpdate prompt showing a forced update countdown" loading="lazy" />
  <figcaption>What users see once the deadline is reached.</figcaption>
</figure>

<div class="mofa-legend center">
  <span class="mofa-legend-item"><b>Domain</b> <code>com.microsoft.autoupdate2</code></span>
  <span class="mofa-legend-item"><b>Channel</b> Current</span>
  <span class="mofa-legend-item"><b>Downloads</b> Automatic</span>
  <span class="mofa-legend-item"><b>Forced quit</b> 60 minute countdown</span>
  <span class="mofa-legend-item"><b>Check interval</b> Every 4 hours</span>
</div>

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_3day_update_v1.mobileconfig" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></i><div><b>3-day forced update</b><span>Updates are forced three days after release. The tightest policy for fast patching.</span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_7day_update_v1.mobileconfig" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></i><div><b>7-day forced update</b><span>A week to update on their own before AutoUpdate steps in. A good default for most fleets.</span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_14day_update_v1.mobileconfig" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></i><div><b>14-day forced update</b><span>Two weeks of grace. Fits environments that stage updates or need more notice.</span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_3day_update_outlook_daily_v1.mobileconfig" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></i><div><b>3-day, Outlook daily</b><span>Same three day policy, with Outlook forced after one day so mail clients stay current.</span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_7day_update_outlook_daily_v1.mobileconfig" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></i><div><b>7-day, Outlook daily</b><span>Same seven day policy, with Outlook forced after one day.</span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_14day_update_outlook_daily_v1.mobileconfig" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></i><div><b>14-day, Outlook daily</b><span>Same fourteen day policy, with Outlook forced after one day.</span></div></a>
</div>

## Data privacy and telemetry {.mofa-h2}

<p class="mofa-lead">Turn off telemetry collection in each Office app and in AutoUpdate, limiting what is shared with Microsoft. Recommended for <a href="https://learn.microsoft.com/en-us/microsoft-365-apps/deploy/deploy-microsoft-365-apps-gcc-high-dod" target="_blank" rel="noopener">GCC High and DoD environments</a>.</p>

<div class="mofa-legend center">
  <span class="mofa-legend-item"><b>SendAllTelemetryEnabled</b> false</span>
  <span class="mofa-legend-item"><b>SendCriticalTelemetryEnabled</b> false</span>
  <span class="mofa-legend-item"><b>SendASmileEnabled</b> false</span>
  <span class="mofa-legend-item"><b>AcknowledgedDataCollectionPolicy</b> RequiredDataOnly</span>
</div>

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_word_user_privacy.mobileconfig" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>Word</b><span><code>com.microsoft.Word</code></span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_excel_user_privacy.mobileconfig" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>Excel</b><span><code>com.microsoft.Excel</code></span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_powerpoint_user_privacy.mobileconfig" target="_blank" rel="noopener"><i class="ic-bug"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>PowerPoint</b><span><code>com.microsoft.PowerPoint</code></span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_outlook_user_privacy.mobileconfig" target="_blank" rel="noopener"><i class="ic-chat"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>Outlook</b><span><code>com.microsoft.Outlook</code></span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_onenote_user_privacy.mobileconfig" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>OneNote</b><span><code>com.microsoft.OneNote.mac</code></span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_office365servicesv2_user_privacy.mobileconfig" target="_blank" rel="noopener"><i class="ic-mail"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>Office 365 Services</b><span><code>com.microsoft.Office365ServiceV2</code></span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_user_privacy.mobileconfig" target="_blank" rel="noopener"><i class="ic-mail"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>AutoUpdate</b><span><code>com.microsoft.autoupdate2</code></span></div></a>
</div>

<p class="mofa-note">To download a profile, open its link and choose <b>Download raw file</b> on GitHub. Review the payload, then upload it to your MDM or copy the keys into your own profile.</p>

<p class="mofa-foot">New to mobileconfig files? The breakdown page walks through one of these profiles key by key.</p>

<div class="mofa-cta">
  <a class="mofa-btn" href="/macos_tools/profile_breakdown">Profile breakdown</a>
  <a class="mofa-btn alt" href="https://github.com/cocopuff2u/MOFA/tree/main/mobileconfig_profiles" target="_blank" rel="noopener">Browse on GitHub</a>
</div>

<div class="mofa-related"><span>Related</span><a class="mofa-chip outline" href="/macos_tools/profile_breakdown">Profile breakdown</a><a class="mofa-chip outline" href="/standalone_apps/standalone_current_version_en">Current versions</a><a class="mofa-chip outline" href="/about_support/feedback">Feedback</a></div>

</div>
