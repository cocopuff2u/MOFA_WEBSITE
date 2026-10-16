---
title: Profile Breakdown
---
<div class="mofa-page">

<div class="mofa-page-hero">
  <MofaMark :size="90" />
  <h1>Profile <span class="gradient-title">breakdown</span></h1>
  <p class="mofa-page-sub">What is inside a mobileconfig file, key by key, using a real MOFA profile.</p>
</div>

<p class="mofa-lead">A mobileconfig is a plist with a wrapper. The wrapper tells macOS what the profile is called and who made it. The payload inside carries the preference keys an app reads. Below is the 3-day forced update profile for Microsoft AutoUpdate, trimmed so the structure is easy to follow.</p>

<div class="mofa-legend center">
  <span class="mofa-legend-item"><b>File</b> <code>MOFA_mau_3day_update_v1.mobileconfig</code></span>
  <span class="mofa-legend-item"><b>Payload type</b> <code>com.microsoft.autoupdate2</code></span>
  <span class="mofa-legend-item"><b>Deadline</b> 3 days</span>
</div>

## The example file {.mofa-h2}

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PayloadContent</key>
    <array>
        <dict>
            <!-- Per-app deadlines. Each entry is keyed by the app's install path. -->
            <key>Applications</key>
            <dict>
                <key>/Library/Application Support/Microsoft/MAU2.0/Microsoft AutoUpdate.app</key>
                <dict>
                    <key>Application ID</key>
                    <string>MSau04</string>
                    <key>UpdateDeadline.DaysBeforeForcedQuit</key>
                    <integer>3</integer>
                </dict>
                <key>/Applications/Microsoft Word.app</key>
                <dict>
                    <key>Application ID</key>
                    <string>MSWD2019</string>
                    <key>UpdateDeadline.DaysBeforeForcedQuit</key>
                    <integer>3</integer>
                </dict>
                <!-- Excel, PowerPoint, Outlook, OneNote, OneDrive, Teams and Defender follow the same pattern. -->
            </dict>

            <!-- Global AutoUpdate settings. -->
            <key>ChannelName</key>
            <string>Current</string>
            <key>HowToCheck</key>
            <string>AutomaticDownload</string>
            <key>UpdateCheckInterval</key>
            <integer>240</integer>
            <key>UpdateDeadline.StartAutomaticUpdates</key>
            <integer>3</integer>
            <key>UpdateDeadline.FinalCountDown</key>
            <integer>60</integer>

            <!-- Payload metadata. Every payload needs these. -->
            <key>PayloadType</key>
            <string>com.microsoft.autoupdate2</string>
            <key>PayloadDisplayName</key>
            <string>Microsoft AutoUpdate</string>
            <key>PayloadIdentifier</key>
            <string>com.microsoft.autoupdate2.3daypolicy</string>
            <key>PayloadUUID</key>
            <string>A1B2C3D4-3D3D-3D3D-1234567890CD</string>
            <key>PayloadVersion</key>
            <integer>1</integer>
        </dict>
    </array>

    <!-- Profile metadata. This is what shows in System Settings. -->
    <key>PayloadType</key>
    <string>Configuration</string>
    <key>PayloadDisplayName</key>
    <string>mau_3_day_force_update</string>
    <key>PayloadDescription</key>
    <string>Enforces a 3-day global forced update policy for Microsoft AutoUpdate.</string>
    <key>PayloadOrganization</key>
    <string>Cocolabs - MOFA</string>
    <key>PayloadIdentifier</key>
    <string>dev.cocolabs.mofa.3day</string>
    <key>PayloadUUID</key>
    <string>3DAY-UUID-GLOBAL-9876543210CD</string>
    <key>PayloadVersion</key>
    <integer>1</integer>
</dict>
</plist>
```

<p class="mofa-note">Trimmed for clarity. The <a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_3day_update_v1.mobileconfig" target="_blank" rel="noopener">full profile</a> lists every Office app in the Applications dictionary. Each payload and the profile itself need their own PayloadUUID and PayloadIdentifier, and both must be unique on the device.</p>

## Key by key {.mofa-h2}

<p class="mofa-lead">The keys that do the work, with the units Microsoft documents for them. Each card links to the <a href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/mau-preferences" target="_blank" rel="noopener">AutoUpdate preferences reference</a>.</p>

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/mau-preferences" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></svg></i><div><b>HowToCheck</b><span>How updates are fetched. <code>AutomaticDownload</code> downloads and installs them. <code>AutomaticCheck</code> only checks, and <code>Manual</code> leaves it to the user. Setting this locks the choice in the AutoUpdate preferences.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/mau-preferences" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18"/></svg></i><div><b>ChannelName</b><span>Which release channel to follow. <code>Current</code> is production. <code>Preview</code> and <code>Beta</code> get builds earlier, and <code>CurrentThrottle</code> receives production builds on a slower rollout.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/mau-preferences" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/></svg></i><div><b>UpdateCheckInterval</b><span>Minutes between update checks. The profile uses <code>240</code>, four hours. Microsoft's default is 780 and they suggest a multiple of 60. The older <code>UpdateCheckFrequency</code> key is deprecated.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/mau-preferences" target="_blank" rel="noopener"><i class="ic-bug"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="17" rx="2"/><path d="M3 9h18M8 2v4M16 2v4"/></svg></i><div><b>UpdateDeadline.DaysBeforeForcedQuit</b><span>Days a user has before the app is force quit and updated. Set per app inside <code>Applications</code>. The clock starts when the update is detected on that Mac, not when Microsoft releases it.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/mau-preferences" target="_blank" rel="noopener"><i class="ic-chat"><svg viewBox="0 0 24 24"><path d="M4 6h10M4 12h10M4 18h6M15 17l2.5 2.5L22 15"/></svg></i><div><b>UpdateDeadline.StartAutomaticUpdates</b><span>Days before the deadline when AutoUpdate starts treating every update as an automatic download. The minimum is 3 and it cannot exceed the forced quit deadline.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/mau-preferences" target="_blank" rel="noopener"><i class="ic-mail"><svg viewBox="0 0 24 24"><circle cx="12" cy="13" r="8"/><path d="M12 9v4l2.5 2.5M9 2h6M12 2v3"/></svg></i><div><b>UpdateDeadline.FinalCountDown</b><span>Minutes of warning before the forced quit, shown as the countdown dialog. The profile uses <code>60</code>. Microsoft allows 10 to 720.</span></div></a>
</div>

<div class="mofa-figures">
  <figure class="mofa-figure">
    <img src="/images/mau_preferences_example2.png" alt="AutoUpdate preferences with the update method locked by HowToCheck" loading="lazy" />
    <figcaption>HowToCheck locks the update method in AutoUpdate's preferences.</figcaption>
  </figure>
  <figure class="mofa-figure">
    <img src="/images/mau_preferences_example.png" alt="AutoUpdate preferences showing the channel selected by ChannelName" loading="lazy" />
    <figcaption>ChannelName picks the release channel shown here.</figcaption>
  </figure>
</div>

## Make your own {.mofa-h2}

<p class="mofa-lead">An unsigned mobileconfig is plain text, so for a quick change open it in a text editor such as Visual Studio Code and edit the keys directly. To capture settings you have not written out yet, let the app do it for you.</p>

<div class="mofa-rows rows-left">
  <div class="mofa-row"><i class="ic-fork"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg></i><div><b>1. Set it in the app</b><span>Open the app, go to its preferences and make the change you want to deploy. Save or close so the preference is written out.</span></div></div>
  <div class="mofa-row"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M3 6a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></i><div><b>2. Find the plist</b><span>Look in <code>~/Library/Preferences/</code> for the app's domain, for example <code>com.microsoft.autoupdate2.plist</code>. System-wide settings land in <code>/Library/Preferences/</code>.</span></div></div>
  <div class="mofa-row"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6"/></svg></i><div><b>3. Convert to a mobileconfig</b><span>Open the plist in ProfileCreator or iMazing, add the display name and organization, and export a mobileconfig ready for your MDM.</span></div></div>
</div>

## Tools {.mofa-h2}

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://apps.apple.com/us/app/apple-configurator/id1037126344" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><rect x="5" y="2" width="14" height="20" rx="2"/><path d="M11 18h2"/></svg></i><div><b>Apple Configurator</b><span>Apple's own profile editor. Good for building standard payloads and for signing profiles.</span></div></a>
  <a class="mofa-row" href="https://github.com/ProfileCreator/ProfileCreator" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>ProfileCreator</b><span>Free and open source. Built around community manifests, so it knows the keys for Microsoft apps and most other admin tools.</span></div></a>
  <a class="mofa-row" href="https://code.visualstudio.com" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg></i><div><b>Visual Studio Code</b><span>Edit unsigned mobileconfig files directly. Handy for small fixes and for reading what a profile actually sets.</span></div></a>
  <a class="mofa-row" href="https://www.fatcatsoftware.com/plisteditpro/" target="_blank" rel="noopener"><i class="ic-bug"><svg viewBox="0 0 24 24"><path d="M4 6h10M4 12h10M4 18h6M15 17l2.5 2.5L22 15"/></svg></i><div><b>PlistEdit Pro</b><span>A dedicated plist editor. Useful when you are working from an app's preference file before converting it.</span></div></a>
  <a class="mofa-row" href="https://github.com/timsutton/mcxToProfile" target="_blank" rel="noopener"><i class="ic-chat"><svg viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6"/></svg></i><div><b>mcxToProfile</b><span>Command line tool that turns a plist or legacy MCX settings into a configuration profile. Scriptable.</span></div></a>
  <a class="mofa-row" href="https://imazing.com/profile-editor" target="_blank" rel="noopener"><i class="ic-mail"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg></i><div><b>iMazing Profile Editor</b><span>Free editor with a friendly interface. Creates and edits mobileconfig files without needing to know the plist format.</span></div></a>
</div>

## Further reading {.mofa-h2}

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://docs.google.com/spreadsheets/d/1ESX5td0y0OP3jdzZ-C2SItm-TUi-iA_bcHCBvaoCumw/edit?gid=0#gid=0" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M3 19a6 6 0 0 1 12 0M15 18.5a4.5 4.5 0 0 1 6 0"/></svg></i><div><b>Mac Admins preferences list</b><span>Community spreadsheet of every known Office for Mac preference key. The best single reference there is.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/mau-preferences" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></svg></i><div><b>AutoUpdate preferences</b><span>Microsoft's reference for every key AutoUpdate reads, with types, defaults and allowed values.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/deploy-preferences-for-office-for-mac" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M4 6h10M4 12h10M4 18h6M15 17l2.5 2.5L22 15"/></svg></i><div><b>Deploy preferences for Office</b><span>Microsoft's overview of how plist-based preferences work and how to deploy them.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/set-preference-per-app" target="_blank" rel="noopener"><i class="ic-bug"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg></i><div><b>Set preferences per app</b><span>How to target Word, Excel, PowerPoint and the rest individually.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/preferences-outlook" target="_blank" rel="noopener"><i class="ic-chat"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></i><div><b>Outlook preferences</b><span>Keys specific to Outlook for Mac.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/preferences-office" target="_blank" rel="noopener"><i class="ic-mail"><svg viewBox="0 0 24 24"><path d="M3 6a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></i><div><b>Office suite preferences</b><span>Keys shared across the whole suite, such as sign-in and privacy settings.</span></div></a>
</div>

<p class="mofa-foot">Ready to deploy something? The profiles page has forced-update and privacy profiles you can upload as they are.</p>

<div class="mofa-cta">
  <a class="mofa-btn" href="/macos_tools/preconfigured_profiles">Preconfigured profiles</a>
  <a class="mofa-btn alt" href="https://github.com/cocopuff2u/MOFA/tree/main/mobileconfig_profiles" target="_blank" rel="noopener">Browse on GitHub</a>
</div>

<div class="mofa-related"><span>Related</span><a class="mofa-chip outline" href="/macos_tools/preconfigured_profiles">Preconfigured profiles</a><a class="mofa-chip outline" href="/standalone_apps/standalone_current_version_en">Current versions</a><a class="mofa-chip outline" href="/about_support/feedback">Feedback</a></div>

</div>
