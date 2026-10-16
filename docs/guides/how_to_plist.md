---
title: How To Plist
---
<div class="mofa-page">

<div class="mofa-page-hero">
  <MofaMark :size="90" />
  <h1>Deploy <span class="gradient-title">plist</span> preferences</h1>
  <p class="mofa-page-sub">Write a preference file for a Microsoft app and ship it with Jamf Pro or Intune.</p>
</div>

<p class="mofa-lead">Microsoft's Mac apps read their settings from property list files. Put the right key in the right plist and the app follows it. Deliver that plist through your MDM as a managed preference and it applies to every Mac you scope, and users cannot change it. This guide uses Outlook as the example.</p>

<div class="mofa-legend center">
  <span class="mofa-legend-item"><b>Example app</b> Outlook</span>
  <span class="mofa-legend-item"><b>Domain</b> <code>com.microsoft.Outlook</code></span>
  <span class="mofa-legend-item"><b>Key</b> <code>PlayMyEmailsEnabled</code></span>
</div>

## Create the file {.mofa-h2}

<p class="mofa-lead">A plist is XML. Open any plain text editor, such as Visual Studio Code or TextEdit in plain text mode, and add the declaration, a root <code>plist</code> element, and a <code>dict</code> holding your keys.</p>

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>PlayMyEmailsEnabled</key>
    <false/>
</dict>
</plist>
```

<p class="mofa-note">This turns off the Play My Emails feature in Outlook. Save it as <code>com.microsoft.Outlook.plist</code>. The file name is the app's preference domain, and each app or suite has its own. Add as many keys as you need to the same <code>dict</code>.</p>

## Where plist files live {.mofa-h2}

<p class="mofa-lead">macOS reads preferences from three places. Which one you use decides who the setting applies to and whether users can override it.</p>

<div class="mofa-rows rows-left">
  <div class="mofa-row"><i class="ic-fork"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg></i><div><b>User</b><span><code>~/Library/Preferences/</code><br>One local account only. The app writes here when the user changes a setting.</span></div></div>
  <div class="mofa-row"><i class="ic-globe"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg></i><div><b>Computer</b><span><code>/Library/Preferences/</code><br>Every account on the Mac. Set by scripts or by hand. User preferences take priority over it.</span></div></div>
  <div class="mofa-row"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>Managed</b><span><code>/Library/Managed Preferences/</code><br>Written by your MDM. Applies to every account and overrides both of the others. This is where a deployed plist ends up.</span></div></div>
</div>

## Deploy with Jamf Pro {.mofa-h2}

<div class="mofa-rows rows-left">
  <div class="mofa-row"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></svg></i><div><b>1. Create a configuration profile</b><span>Go to Configuration Profiles, New, and add the Application &amp; Custom Settings payload. Upload the plist, or paste its XML, with <code>com.microsoft.Outlook</code> as the preference domain.</span></div></div>
  <div class="mofa-row"><i class="ic-globe"><svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M3 19a6 6 0 0 1 12 0M15 18.5a4.5 4.5 0 0 1 6 0"/></svg></i><div><b>2. Scope it</b><span>Assign the profile to the Smart Groups or Static Groups that should receive it.</span></div></div>
  <div class="mofa-row"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M4 12h16M14 6l6 6-6 6"/></svg></i><div><b>3. Save</b><span>Devices pick it up on their next MDM check-in. Check the profile's status tab to watch it land.</span></div></div>
</div>

## Deploy with Intune {.mofa-h2}

<p class="mofa-lead">Intune gives you three ways in. Pick the one that fits. Whichever you choose, go to Devices, macOS, Configuration profiles, Create profile in the Intune admin center.</p>

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/mem/intune/configuration/settings-catalog" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M4 6h10M4 12h10M4 18h6M15 17l2.5 2.5L22 15"/></svg></i><div><b>Settings catalog <span class="mofa-chip">Recommended</span></b><span>No plist needed. Choose Settings catalog, search for the setting, and tick it. Nearly every Microsoft app key is in there.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/mem/intune/configuration/preference-file-settings-macos" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg></i><div><b>Preference file</b><span>For keys the catalog does not have yet. Choose Templates, Preference file, enter the domain, and upload a stripped plist. See the example below. Intune wraps it into a mobileconfig for you.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/mem/intune/configuration/custom-settings-macos" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M3 6a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></i><div><b>Custom profile</b><span>Wrap the plist into a mobileconfig yourself with ProfileCreator or iMazing, then choose Templates, Custom, and upload it. Most control, most work.</span></div></a>
</div>

<p class="mofa-lead">A preference file is the plist with its wrapper removed. Keep only what sits inside the <code>dict</code>, and save it as <code>.xml</code>.</p>

```xml
<key>PlayMyEmailsEnabled</key>
<false/>
<key>DefaultEmailAddressOrDomain</key>
<string>example.com</string>
```

<p class="mofa-note">Not sure whether a key is in the settings catalog? The <a href="https://github.com/IntunePMFiles/DeviceConfig" target="_blank" rel="noopener">DeviceConfig repo</a> lists every key it supports, for Mac and iOS. If you use the settings catalog and a preference file together, do not set the same key in both. Keys must be unique across the profiles that reach a device. After any of the three options, assign the profile to your user or device groups and save. Devices apply it on their next sync.</p>

## Test and validate {.mofa-h2}

<div class="mofa-rows rows-left">
  <div class="mofa-row"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M3 6a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></i><div><b>1. Look for the file</b><span>On a scoped Mac, confirm the plist landed in <code>/Library/Managed Preferences/</code>. If it is not there, the profile has not arrived yet.</span></div></div>
  <div class="mofa-row"><i class="ic-globe"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7 9l3 3-3 3M12 15h5"/></svg></i><div><b>2. Read it back</b><span>Ask the preferences system what value the app will actually see. The command below should print <code>0</code>.</span></div></div>
  <div class="mofa-row"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M4 6h10M4 12h10M4 18h6M15 17l2.5 2.5L22 15"/></svg></i><div><b>3. Check the console</b><span>Jamf Pro shows status per device on the profile. Intune has device status under the profile's monitoring reports.</span></div></div>
</div>

```bash
ls "/Library/Managed Preferences/"
defaults read com.microsoft.Outlook PlayMyEmailsEnabled
```

<p class="mofa-note">Before rolling out widely, scope to a small test group and open the app. A wrong key name fails silently, so the only real test is seeing the setting change. Double check the bundle identifier too. Outlook is <code>com.microsoft.Outlook</code>, with a capital O.</p>

## Troubleshooting {.mofa-h2}

<div class="mofa-rows rows-left">
  <div class="mofa-row"><i class="ic-bug"><svg viewBox="0 0 24 24"><path d="M8 9a4 4 0 0 1 8 0v6a4 4 0 0 1-8 0zM9 5l-2-2M15 5l2-2M4 12h4M16 12h4M5 18l3-2M19 18l-3-2M5 7l3 2M19 7l-3 2"/></svg></i><div><b>Profile never arrives</b><span>Check the device is in scope and has checked in. Force a sync from the console, or run <code>sudo jamf policy</code> on Jamf, and watch the profile list in System Settings.</span></div></div>
  <div class="mofa-row"><i class="ic-chat"><svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M12 8v5M12 16h.01"/></svg></i><div><b>Setting does not change</b><span>Run the <code>defaults read</code> check. If the value is right but the app ignores it, the key name or type is wrong. Compare against Microsoft's reference for that app.</span></div></div>
  <div class="mofa-row"><i class="ic-mail"><svg viewBox="0 0 24 24"><circle cx="12" cy="8" r="4"/><path d="M4 21a8 8 0 0 1 16 0"/></svg></i><div><b>Works for some users only</b><span>Managed preferences win over user preferences, so if a user's copy still differs the profile is not applying to that account. Check scope and whether the profile is user or device level.</span></div></div>
</div>

## Further reading {.mofa-h2}

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://docs.google.com/spreadsheets/d/1ESX5td0y0OP3jdzZ-C2SItm-TUi-iA_bcHCBvaoCumw/edit?gid=0#gid=0" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><circle cx="9" cy="8" r="3.5"/><circle cx="17" cy="9" r="2.5"/><path d="M3 19a6 6 0 0 1 12 0M15 18.5a4.5 4.5 0 0 1 6 0"/></svg></i><div><b>Mac Admins preferences list</b><span>Community spreadsheet of every known Office for Mac preference key. Start here.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/deploy-preferences-for-office-for-mac" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></svg></i><div><b>Deploy preferences for Office</b><span>Microsoft's overview of plist-based preferences for the Mac apps.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/set-preference-per-app" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg></i><div><b>Set preferences per app</b><span>How to target Word, Excel, PowerPoint and the rest individually.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/preferences-outlook" target="_blank" rel="noopener"><i class="ic-bug"><svg viewBox="0 0 24 24"><rect x="3" y="5" width="18" height="14" rx="2"/><path d="M3 7l9 6 9-6"/></svg></i><div><b>Outlook preferences</b><span>Every key Outlook for Mac reads, including the one used in this guide.</span></div></a>
  <a class="mofa-row" href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/preferences-office" target="_blank" rel="noopener"><i class="ic-chat"><svg viewBox="0 0 24 24"><path d="M3 6a2 2 0 0 1 2-2h5l2 2h7a2 2 0 0 1 2 2v10a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/></svg></i><div><b>Office suite preferences</b><span>Keys shared across the whole suite, such as sign-in and privacy.</span></div></a>
  <a class="mofa-row" href="https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html" target="_blank" rel="noopener"><i class="ic-mail"><svg viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg></i><div><b>Property List Programming Guide</b><span>Apple's reference for the plist format itself, types and all.</span></div></a>
</div>

<p class="mofa-foot">Want to see a finished profile before writing your own? The breakdown page walks through a real MOFA mobileconfig key by key.</p>

<div class="mofa-cta">
  <a class="mofa-btn" href="/macos_tools/profile_breakdown">Profile breakdown</a>
  <a class="mofa-btn alt" href="/macos_tools/preconfigured_profiles">Preconfigured profiles</a>
</div>

<div class="mofa-related"><span>Related</span><a class="mofa-chip outline" href="/guides/how_to_sha256">How To SHA256</a><a class="mofa-chip outline" href="/guides/how_to_sha1">How To SHA1</a><a class="mofa-chip outline" href="/about_support/feedback">Feedback</a></div>

</div>
