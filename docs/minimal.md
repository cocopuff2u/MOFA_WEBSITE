---
editLink: false
lastUpdated: false
layout: doc
navbar: false
sidebar: false
footer: true
aside: false
prev: false
next: false 
---
<style>
  /* NEW: Status bar styles (fix Markdown-in-HTML issue and wrapping) */
  .status-bar {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    text-align: center;
    margin-bottom: 8px;
  }
  .status-line {
    display: inline-flex;
    flex-wrap: wrap;
    align-items: center;
    justify-content: center;
    gap: 8px;
    max-width: 100%;
  }
  .status-line code.status-ts {
    color: dodgerblue;
  }
  .status-line a {
    text-decoration: none;
    font-weight: 600;
    opacity: 0.9;
  }
  .status-line a:hover {
    text-decoration: underline;
    opacity: 1;
  }
  .status-line .muted {
    opacity: 0.8;
  }

  /* If color-mix is supported, derive palette from theme vars for better theming */
  @supports (color: color-mix(in oklab, white 50%, black)) {
    .grid-wrap {
      --btn-bg1: color-mix(in oklab, var(--vp-c-bg, #ffffff) 90%, white);
      --btn-bg2: color-mix(in oklab, var(--vp-c-bg, #ffffff) 70%, #d8dde7);
      --btn-bg1-hover: color-mix(in oklab, var(--btn-bg1) 88%, white);
      --btn-bg2-hover: color-mix(in oklab, var(--btn-bg2) 88%, white);
      --btn-border: color-mix(in oklab, var(--vp-c-text, #111) 28%, transparent);
      --btn-text: color-mix(in oklab, var(--vp-c-text, #111) 98%, black);
    }
    @media (prefers-color-scheme: dark) {
      .grid-wrap {
        --btn-bg1: color-mix(in oklab, var(--vp-c-bg, #1e1e20) 85%, #3a3a3c);
        --btn-bg2: color-mix(in oklab, var(--vp-c-bg, #1e1e20) 70%, #2a2a2d);
        --btn-bg1-hover: color-mix(in oklab, var(--btn-bg1) 88%, #4a4a4d);
        --btn-bg2-hover: color-mix(in oklab, var(--btn-bg2) 88%, #36363a);
        --btn-border: color-mix(in oklab, var(--vp-c-text, #ddd) 22%, transparent);
        --btn-text: color-mix(in oklab, var(--vp-c-text, #ddd) 96%, white);
      }
    }
  }

  /* Inline appearance toggle next to the status line */
  .appearance-toggle-inline {
    display: inline-flex;
    align-items: center;
    margin-left: 8px;
    vertical-align: middle;
  }

  /* SCOPE SWITCH STYLES to this page only to avoid leaking to other pages */
  .mofa-minimal .VPSwitch {
    position: relative;
    width: 46px;
    height: 26px;
    border-radius: 999px;
    border: 1px solid var(--vp-c-divider, rgba(0,0,0,0.12));
    background: var(--vp-c-bg-soft, rgba(0,0,0,0.06));
    cursor: pointer;
    transition: background .2s ease, border-color .2s ease;
    pointer-events: auto;
  }
  .mofa-minimal .VPSwitch .check {
    position: absolute;
    top: 2px;
    left: 2px;
    width: 22px;
    height: 22px;
    border-radius: 50%;
    background: var(--vp-c-bg, #ffffff);
    box-shadow: 0 1px 2px rgba(0,0,0,0.15);
    transition: transform .2s ease;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .mofa-minimal .VPSwitch[aria-checked="true"] .check {
    transform: translateX(20px);
  }

  /* Show sun in light, moon in dark (scoped) */
  .mofa-minimal .VPSwitch .icon .sun, .mofa-minimal .VPSwitch .icon .moon { display: none; }
  html:not(.dark) .mofa-minimal .VPSwitch .icon .sun { display: inline-block; }
  html.dark .mofa-minimal .VPSwitch .icon .moon { display: inline-block; }

  /* Center wrapper for the MOFA hero title */
  .brand-hero {
    display: grid;
    place-items: center;
    min-height: 0;
    padding: 8px 0;
    overflow: visible;
  }
  @supports (height: 100svh) {
    .brand-hero { min-height: 0; }
  }

  /* Ensure the link itself centers and only the text is clickable */
  .brand-title {
    display: inline-block;    /* was block – limit clickable area to text */
    text-align: center;
    margin: 0;                /* remove auto margins that add width */
    line-height: 1.05;
  }

  /* Remove underline/highlight for the MOFA link in all states */
  a.brand-title,
  a.brand-title:link,
  a.brand-title:visited,
  a.brand-title:hover,
  a.brand-title:active,
  a.brand-title:focus {
    text-decoration: none !important;
    border-bottom: 0 !important;
    box-shadow: none !important;
    -webkit-tap-highlight-color: transparent;
  }

  /* Ensure gradient text doesn't fall back to a theme color */
  .gradient-title-mini {
    background: -webkit-linear-gradient(120deg, #00BFFF 30%, #FF3B30);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: clamp(32px, 12vmin, 96px); /* scales with smallest viewport side */
    color: transparent; /* keep text transparent; gradient provides color */
  }

  /* Responsive grid: max 6 columns; step down on smaller screens */
  .grid {
    display: grid;
    grid-template-columns: repeat(6, minmax(180px, 1fr));
    gap: 16px;
    width: calc(100% - 32px);
    margin: 0 auto;
    align-items: stretch;       /* ensure items stretch to equal height */
  }

  .tile {
    display: flex;
    justify-content: center;
    align-items: stretch;
  }

  .tile-card {
    width: 100%;
    max-width: 200px;
    display: flex;
    flex-direction: column;     /* column layout for spacer technique */
    align-items: center;
    gap: 6px;
    text-align: center;
    margin: 0 auto;
    height: 100%;

    background: var(--vp-c-bg, #fff);
    border: 1px solid var(--vp-c-divider, rgba(0,0,0,0.12));
    border-radius: 12px;
    padding: 10px 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  }

  .tile-media {
    height: 92px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .tile-media img {
    max-height: 80px;
    width: auto;
    height: auto;
  }

  .tile-title {
    min-height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .tile-version {
    min-height: 28px;
    display: flex;
    align-items: center;
    justify-content: center;
    padding: 0 8px;
  }
  .tile-version code {
    white-space: normal;
    overflow-wrap: anywhere;
    word-break: break-word;
    display: inline-block;
    padding: 2px 6px;
    border-radius: 6px;
    background: var(--vp-c-bg-soft, rgba(0,0,0,0.04));
  }
  .tile-updated {
    min-height: 44px;
    display: flex;
    align-items: center;
    justify-content: center;
  }

  /* Keep Release Notes height consistent */
  .tile-relnotes {
    min-height: 22px;
    display: flex;
    align-items: center;
    justify-content: center;
  }
  .tile-relnotes a.relnotes {
    text-decoration: none;
    opacity: 0.9;
  }
  .tile-relnotes a.relnotes:hover {
    opacity: 1;
    text-decoration: underline;
  }

  /* Flexible spacer pushes buttons to the bottom, aligning rows visually */
  .tile-spacer {
    flex: 1 1 auto;
    width: 100%;
  }

  .tile-links {
    margin-top: 6px;
    display: flex;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
  }
  .tile-links a {
    text-decoration: none;
  }

  /* Glass button palette (visible on white in light mode) */
  .grid-wrap {
    /* Neutral gray so it stands out on white */
    --btn-glass-bg: rgba(142, 142, 147, 0.24);
    --btn-glass-bg-hover: rgba(142, 142, 147, 0.32);
    --btn-glass-border: rgba(60, 60, 67, 0.36);
    /* CHANGED: slightly lighter dark gray for light-mode button text */
    --btn-glass-text: #4a4a4d;
  }
  /* Use .dark class from your toggle (not OS media query) */
  html.dark .grid-wrap {
    --btn-glass-bg: rgba(255, 255, 255, 0.12);
    --btn-glass-bg-hover: rgba(255, 255, 255, 0.18);
    --btn-glass-border: rgba(255, 255, 255, 0.24);
    --btn-glass-text: #f2f2f4;
  }

  /* iOS-like glass buttons: translucent, blurred, no shadows */
  .grid-wrap .tile-links a.btn {
    /* color is driven by --btn-glass-text */
    color: var(--btn-glass-text) !important;
    display: inline-flex;
    align-items: center;
    justify-content: center;
    box-sizing: border-box;
    min-height: 34px;
    min-width: 108px;
    padding: 6px 12px;
    border-radius: 12px;
    cursor: pointer;

    /* Flat translucent fill + clear border (no gradient) */
    background: var(--btn-glass-bg) !important;
    background-color: var(--btn-glass-bg) !important; /* ensure visible on white */
    border: 1px solid var(--btn-glass-border) !important;

    /* frosted glass */
    -webkit-backdrop-filter: saturate(180%) blur(14px);
    backdrop-filter: saturate(180%) blur(14px);

    font-weight: 600;
    font-size: 0.95rem;
    line-height: 1.2;

    /* ensure visible and crisp */
    opacity: 1 !important;

    /* no shadows */
    box-shadow: none !important;
    text-shadow: none !important;

    transition: background 0.2s ease, transform 0.05s ease, opacity 0.2s ease, border-color 0.2s ease;
  }
  .grid-wrap .tile-links a.btn:hover {
    background: var(--btn-glass-bg-hover) !important;
    background-color: var(--btn-glass-bg-hover) !important;
    border-color: var(--btn-glass-border) !important;
    text-decoration: none;
    opacity: 1 !important;
    box-shadow: none !important;
  }
  .grid-wrap .tile-links a.btn:active {
    transform: translateY(1px);
    background: var(--btn-glass-bg-hover) !important;
    opacity: 1 !important;
    box-shadow: none !important;
  }
  .grid-wrap .tile-links a.btn:focus-visible {
    outline: 2px solid color-mix(in oklab, var(--btn-glass-text) 45%, dodgerblue);
    outline-offset: 2px;
    box-shadow: none !important;
  }

  /* Force light mode edge/text */
  html:not(.dark) .tile-links a.btn {
    color: var(--btn-glass-text) !important;
    border-color: var(--btn-glass-border) !important;
    opacity: 1 !important;
  }

  /* Breakpoints */
  @media (max-width: 1400px) {
    .grid { grid-template-columns: repeat(5, minmax(180px, 1fr)); }
  }
  @media (max-width: 1200px) {
    .grid { grid-template-columns: repeat(4, minmax(180px, 1fr)); }
  }
  @media (max-width: 900px) {
    .grid { grid-template-columns: repeat(3, minmax(180px, 1fr)); }
  }
  @media (max-width: 700px) {
    .grid { grid-template-columns: repeat(2, minmax(160px, 1fr)); gap: 12px; width: calc(100% - 24px); }
    .tile-media { height: 84px; }
    .tile-media img { max-height: 72px; }
  }
  @media (max-width: 420px) {
    .grid { grid-template-columns: repeat(1, minmax(200px, 1fr)); }
  }
</style>

<!-- Centered hero wrapper to prevent cut-off on short screens -->
<div class="brand-hero">
  <a class="brand-title gradient-title-mini" href="/">MOFA</a>
</div>

<div class="status-bar">
      <div class="status-line">
        <span>Last Updated: <code class="status-ts">November 16, 2025 05:06 AM EST</code></span>
        <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.xml"><strong>Raw XML</strong></a>
        <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.yaml"><strong>Raw YAML</strong></a>
        <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_standalone_latest.json"><strong>Raw JSON</strong></a>
        <span class="muted">(Automatically updated every 2 hours)</span>
      </div>
      <span class="appearance-toggle-inline mofa-minimal">
        <button id="appearance-toggle" class="VPSwitch VPSwitchAppearance" type="button" role="switch" title="Switch theme" aria-checked="false">
          <span class="check"><span class="icon"><span class="vpi-sun sun"></span><span class="vpi-moon moon"></span></span></span>
        </button>
      </span>
    </div>

<div class="grid-wrap"><div class="grid"><div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=525133"><img src="/images/Office_Suite.webp" alt="Microsoft Office Suite"></a>
        </div>
        <div class="tile-title"><b>Microsoft Office Suite</b></div>
        <div class="tile-version"><em><code>16.103.0 (25110922)</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 09, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=525133">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=2009112"><img src="/images/Office_Suite.webp" alt="Microsoft Business Pro Suite"></a>
        </div>
        <div class="tile-title"><b>Microsoft Business Pro Suite</b></div>
        <div class="tile-version"><em><code>16.103.0 (25110922)</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 09, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=2009112">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=525134"><img src="/images/2025/Word.webp" alt="Word"></a>
        </div>
        <div class="tile-title"><b>Word</b></div>
        <div class="tile-version"><em><code>16.103.1 (25111410)</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 14, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=525134">Installer</a> <a class="btn" href="https://res.public.onecdn.static.microsoft/mro1cdnstorage/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Word_16.103.25111410_Updater.pkg">App Only</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=525135"><img src="/images/2025/Excel.webp" alt="Excel"></a>
        </div>
        <div class="tile-title"><b>Excel</b></div>
        <div class="tile-version"><em><code>16.103.0 (25110922)</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 09, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=525135">Installer</a> <a class="btn" href="https://res.public.onecdn.static.microsoft/mro1cdnstorage/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Excel_16.103.25110922_Updater.pkg">App Only</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=525136"><img src="/images/2025/PowerPoint.webp" alt="PowerPoint"></a>
        </div>
        <div class="tile-title"><b>PowerPoint</b></div>
        <div class="tile-version"><em><code>16.103.0 (25110922)</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 09, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=525136">Installer</a> <a class="btn" href="https://res.public.onecdn.static.microsoft/mro1cdnstorage/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_PowerPoint_16.103.25110922_Updater.pkg">App Only</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=525137"><img src="/images/2025/Outlook.webp" alt="Outlook"></a>
        </div>
        <div class="tile-title"><b>Outlook</b></div>
        <div class="tile-version"><em><code>16.103.0 (25110922)</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 09, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=525137">Installer</a> <a class="btn" href="https://res.public.onecdn.static.microsoft/mro1cdnstorage/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Outlook_16.103.25110922_Updater.pkg">App Only</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=820886"><img src="/images/2025/OneNote.webp" alt="OneNote"></a>
        </div>
        <div class="tile-title"><b>OneNote</b></div>
        <div class="tile-version"><em><code>16.103.0 (25110922)</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 09, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/officeupdates/release-notes-office-for-mac"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=820886">Installer</a> <a class="btn" href="https://res.public.onecdn.static.microsoft/mro1cdnstorage/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_OneNote_16.103.25110922_Updater.pkg">App Only</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://oneclient.sfx.ms/Mac/Installers/25.209.1026.0002/universal/OneDrive.pkg"><img src="/images/2025/OneDrive.webp" alt="OneDrive"></a>
        </div>
        <div class="tile-title"><b>OneDrive</b></div>
        <div class="tile-version"><em><code>25.209.1026</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 14, 2025 02:07 PM EST</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://support.microsoft.com/en-us/office/onedrive-release-notes-845dcf18-f921-435e-bf28-4e24b95e5fc0#OSVersion=Mac"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://oneclient.sfx.ms/Mac/Installers/25.209.1026.0002/universal/OneDrive.pkg">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=2249065"><img src="/images/2025/Teams.webp" alt="Teams"></a>
        </div>
        <div class="tile-title"><b>Teams</b></div>
        <div class="tile-version"><em><code>25306.805.4102.7211</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 11, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://support.microsoft.com/en-us/office/what-s-new-in-microsoft-teams-d7092a6d-c896-424c-b362-a472d5f105de"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=2249065">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=853070"><img src="/images/2021/Company_Portal.webp" alt="Company Portal"></a>
        </div>
        <div class="tile-title"><b>Company Portal</b></div>
        <div class="tile-version"><em><code>5.2510.0</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>October 22, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://aka.ms/intuneupdates"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=853070">Installer</a> <a class="btn" href="https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/CompanyPortal_5.2510.0-Upgrade.pkg">App Only</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/f46834c6-c739-468a-a1ca-90453d0743e5/MicrosoftEdge-142.0.3595.80.pkg"><img src="/images/edge/edge.webp" alt="Edge"></a>
        </div>
        <div class="tile-title"><b>Edge</b></div>
        <div class="tile-version"><em><code>142.0.3595.80</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 15, 2025 03:34 AM EST</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/deployedge/microsoft-edge-relnote-stable-channel"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://msedge.sf.dl.delivery.mp.microsoft.com/filestreamingservice/files/f46834c6-c739-468a-a1ca-90453d0743e5/MicrosoftEdge-142.0.3595.80.pkg">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=2097502"><img src="/images/2025/Defender.webp" alt="Defender for Endpoint"></a>
        </div>
        <div class="tile-title"><b>Defender for Endpoint</b></div>
        <div class="tile-version"><em><code>101.25082.0006</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>September 30, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=2097502">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=2247001"><img src="/images/2025/Defender.webp" alt="Defender for Consumers"></a>
        </div>
        <div class="tile-title"><b>Defender for Consumers</b></div>
        <div class="tile-version"><em><code>101.25082.0006</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>September 30, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=2247001">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Defender_101.24080.0001_Individuals_Shim_Installer.pkg"><img src="/images/2025/Defender.webp" alt="Defender Shim"></a>
        </div>
        <div class="tile-title"><b>Defender Shim</b></div>
        <div class="tile-version"><em><code>101.24080.0001</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>October 16, 2024</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/microsoft-365/security/defender-endpoint/mac-whatsnew"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Microsoft_Defender_101.24080.0001_Individuals_Shim_Installer.pkg">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=868963"><img src="/images/2025/Windows_App.webp" alt="Windows App"></a>
        </div>
        <div class="tile-title"><b>Windows App</b></div>
        <div class="tile-version"><em><code>11.2.7</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 03, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/windows-app/whats-new?tabs=macos"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=868963">Installer</a> <a class="btn" href="https://officecdnmac.microsoft.com/pr/C1297A47-86C4-4C1F-97FA-950631F94777/MacAutoupdate/Windows_App_11.2.7_updater.pkg">App Only</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=2156837"><img src="/images/2021/Code.webp" alt="Visual Studio Code"></a>
        </div>
        <div class="tile-title"><b>Visual Studio Code</b></div>
        <div class="tile-version"><em><code>1.106.0</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 11, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://code.visualstudio.com/updates/"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=2156837">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=2325438"><img src="/images/2025/Copilot.webp" alt="Microsoft Copilot"></a>
        </div>
        <div class="tile-title"><b>Microsoft Copilot</b></div>
        <div class="tile-version"><em><code>1.2511 (1001)</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 11, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/copilot/microsoft-365/release-notes?tabs=mac"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=2325438">Installer</a></div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media">
          <a href="https://go.microsoft.com/fwlink/?linkid=830196"><img src="/images/2019/AutoUpdate.webp" alt="Microsoft AutoUpdate"></a>
        </div>
        <div class="tile-title"><b>Microsoft AutoUpdate</b></div>
        <div class="tile-version"><em><code>4.81 (25111027)</code></em></div>
        <div class="tile-updated"><small>Last Update:<br><em><code>November 10, 2025</code></em></small></div>
        <div class="tile-relnotes"><a class="relnotes" href="https://learn.microsoft.com/en-us/officeupdates/release-history-microsoft-autoupdate"><small>Release Notes</small></a></div>
        <div class="tile-spacer"></div>
        <div class="tile-links"><a class="btn" href="https://go.microsoft.com/fwlink/?linkid=830196">Installer</a></div>
      </div>
    </div></div></div>
