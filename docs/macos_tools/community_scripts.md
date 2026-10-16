---
title: Community Scripts
---
<div class="mofa-page">

<div class="mofa-page-hero">
  <MofaMark :size="90" />
  <h1>Community <span class="gradient-title">scripts</span></h1>
  <p class="mofa-page-sub">Scripts from Mac admins for downloading, installing, updating and managing Microsoft apps on macOS.</p>
</div>

<p class="mofa-lead">You do not have to write the deployment script yourself. The ones below are maintained in the open by people who run them in production, and several read the same Microsoft feeds that power this site. Pick one, read it, and wire it into your MDM.</p>

<div class="mofa-stats">
  <div><b>5 scripts</b><span>install, update and remove Office</span></div>
  <div><b>Open source</b><span>every one is readable before you run it</span></div>
  <div><b>Yours next?</b><span>contributions are welcome</span></div>
</div>

## Deploy and manage Office {.mofa-h2}

<div class="mofa-rows rows-left">
  <a class="mofa-row" href="https://gist.github.com/talkingmoose/b6637160b65b751824943ede022daa17" target="_blank" rel="noopener"><i class="ic-fork"><svg viewBox="0 0 24 24"><path d="M12 4v11M7 10l5 5 5-5M4 19h16"/></svg></i><div><b>Download and install Microsoft products</b><span>By TalkingMoose. Fetches the latest installer from Microsoft's direct links and installs it, with optional SHA256 verification.</span></div></a>
  <a class="mofa-row" href="https://github.com/microsoft/shell-intune-samples/blob/master/macOS/Apps/Microsoft%20365%20Apps%20for%20Mac/installM365Apps.sh" target="_blank" rel="noopener"><i class="ic-globe"><svg viewBox="0 0 24 24"><rect x="3" y="4" width="18" height="13" rx="2"/><path d="M8 21h8M12 17v4"/></svg></i><div><b>Install Microsoft 365 Apps</b><span>By Microsoft. From the official Intune shell samples. Downloads and installs the full suite, and works outside Intune too.</span></div></a>
  <a class="mofa-row" href="https://github.com/microsoft/shell-intune-samples/blob/master/macOS/Apps/Microsoft%20365%20Apps%20for%20Mac/uninstallOfficeBusinessPro.sh" target="_blank" rel="noopener"><i class="ic-bug"><svg viewBox="0 0 24 24"><path d="M4 7h16M9 7V4h6v3M6 7l1 13h10l1-13M10 11v6M14 11v6"/></svg></i><div><b>Uninstall Office BusinessPro</b><span>By Microsoft. The matching removal script from the Intune samples. Takes the whole suite off a Mac cleanly.</span></div></a>
  <a class="mofa-row" href="https://github.com/Installomator/Installomator" target="_blank" rel="noopener"><i class="ic-refine"><svg viewBox="0 0 24 24"><path d="M12 3l8 3v6c0 4.5-3.2 8.3-8 9.5C7.2 20.3 4 16.5 4 12V6z"/><path d="M9 12l2 2 4-4"/></svg></i><div><b>Installomator</b><span>One script that installs and updates hundreds of apps, Office included, by label. Verifies signatures and handles updates on a schedule.</span></div></a>
  <a class="mofa-row" href="https://github.com/pbowden-msft" target="_blank" rel="noopener"><i class="ic-chat"><svg viewBox="0 0 24 24"><path d="M8 7l-5 5 5 5M16 7l5 5-5 5M14 4l-4 16"/></svg></i><div><b>Paul Bowden's tools</b><span>A collection of scripts for repairing, configuring and automating Office on macOS, from the person who shaped much of Office for Mac deployment.</span></div></a>
  <a class="mofa-row" href="https://github.com/cocopuff2u/MOFA/pulls" target="_blank" rel="noopener"><i class="ic-mail"><svg viewBox="0 0 24 24"><path d="M12 5v14M5 12h14"/></svg></i><div><b>Add your script</b><span>Got something that saves other admins time? Open a pull request with a link and a line about what it does.</span></div></a>
</div>

<p class="mofa-note">Scripts here are maintained by their authors, not by MOFA. Read a script before you deploy it, and check its repository for the latest version and any open issues.</p>

<p class="mofa-foot">Looking to fix an install rather than deploy one? The repair tools page has reset and removal scripts for every Office app.</p>

<div class="mofa-cta">
  <a class="mofa-btn" href="/macos_tools/microsoft_office_repair_tools">Repair tools</a>
  <a class="mofa-btn alt" href="https://github.com/cocopuff2u/MOFA/discussions" target="_blank" rel="noopener">Start a discussion</a>
</div>

<div class="mofa-related"><span>Related</span><a class="mofa-chip outline" href="/macos_tools/preconfigured_profiles">Preconfigured profiles</a><a class="mofa-chip outline" href="/standalone_apps/standalone_sha256_hashes_en">SHA256 hashes</a><a class="mofa-chip outline" href="/about_support/feedback">Feedback</a></div>

</div>
