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
  /* Status bar and links (match standalone) */
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

  /* Inline appearance toggle next to the status line */
  .appearance-toggle-inline {
    display: inline-flex;
    align-items: center;
    margin-left: 8px;
    vertical-align: middle;
  }

  /* Theme switch styles (scoped) */
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
  .mofa-minimal .VPSwitch .icon .sun, .mofa-minimal .VPSwitch .icon .moon { display: none; }
  html:not(.dark) .mofa-minimal .VPSwitch .icon .sun { display: inline-block; }
  html.dark .mofa-minimal .VPSwitch .icon .moon { display: inline-block; }

  /* MOFA hero title */
  .brand-hero {
    display: grid;
    place-items: center;
    min-height: 0;
    padding: 8px 0;
    overflow: visible;
  }
  .brand-title {
    display: inline-block;
    text-align: center;
    margin: 0;
    line-height: 1.05;
  }
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
  .gradient-title-mini {
    background: -webkit-linear-gradient(120deg, #00BFFF 30%, #FF3B30);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-weight: 800;
    font-size: clamp(32px, 12vmin, 96px);
    color: transparent;
  }

  /* Page title under hero */
  .page-title {
    text-align: center;
    margin: 2px 0 10px 0;
    font-weight: 700;
    font-size: clamp(18px, 3.5vmin, 28px);
    opacity: 0.9;
  }

  /* Existing grid and tiles */
  .grid-wrap {
    --btn-glass-bg: rgba(142, 142, 147, 0.24);
    --btn-glass-bg-hover: rgba(142, 142, 147, 0.32);
    --btn-glass-border: rgba(60, 60, 67, 0.36);
    --btn-glass-text: #4a4a4d;
  }
  html.dark .grid-wrap {
    --btn-glass-bg: rgba(255, 255, 255, 0.12);
    --btn-glass-bg-hover: rgba(255, 255, 255, 0.18);
    --btn-glass-border: rgba(255, 255, 255, 0.24);
    --btn-glass-text: #f2f2f4;
  }

  .grid {
    display: grid;
    grid-template-columns: repeat(6, minmax(180px, 1fr));
    gap: 16px;
    width: calc(100% - 32px);
    margin: 0 auto;
    align-items: stretch;
  }
  @media (max-width: 1400px) { .grid { grid-template-columns: repeat(5, minmax(180px, 1fr)); } }
  @media (max-width: 1200px) { .grid { grid-template-columns: repeat(4, minmax(180px, 1fr)); } }
  @media (max-width: 900px)  { .grid { grid-template-columns: repeat(3, minmax(180px, 1fr)); } }
  @media (max-width: 700px)  { .grid { grid-template-columns: repeat(2, minmax(160px, 1fr)); gap: 12px; width: calc(100% - 24px); } }
  @media (max-width: 420px)  { .grid { grid-template-columns: repeat(1, minmax(200px, 1fr)); } }

  .tile { display: flex; justify-content: center; align-items: stretch; }
  .tile-card {
    width: 100%; max-width: 220px; display: flex; flex-direction: column; align-items: center;
    gap: 6px; text-align: center; margin: 0 auto; height: 100%;
    background: var(--vp-c-bg, #fff);
    border: 1px solid var(--vp-c-divider, rgba(0,0,0,0.12));
    border-radius: 12px; padding: 10px 12px;
    box-shadow: 0 2px 6px rgba(0,0,0,0.06);
  }
  .tile-media { height: 92px; display: flex; align-items: center; justify-content: center; }
  .tile-media img { max-height: 80px; width: auto; height: auto; }
  .tile-title { min-height: 40px; display: flex; align-items: center; justify-content: center; }
  .tile-version code {
    white-space: normal; overflow-wrap: anywhere; word-break: break-word;
    display: inline-block; padding: 2px 6px; border-radius: 6px;
    background: var(--vp-c-bg-soft, rgba(0,0,0,0.04));
  }
  .tile-spacer { flex: 1 1 auto; width: 100%; }
  .tile-links { margin-top: 6px; display: flex; gap: 8px; flex-wrap: wrap; justify-content: center; }
  .tile-links a { text-decoration: none; }
  .grid-wrap .tile-links a.btn {
    color: var(--btn-glass-text) !important;
    display: inline-flex; align-items: center; justify-content: center;
    min-height: 34px; min-width: 108px; padding: 6px 12px; border-radius: 12px; cursor: pointer;
    background: var(--btn-glass-bg) !important; background-color: var(--btn-glass-bg) !important;
    border: 1px solid var(--btn-glass-border) !important;
    -webkit-backdrop-filter: saturate(180%) blur(14px); backdrop-filter: saturate(180%) blur(14px);
    font-weight: 600; font-size: 0.95rem; line-height: 1.2; box-shadow: none !important;
    transition: background .2s ease, transform .05s ease, opacity .2s ease, border-color .2s ease;
  }
  .grid-wrap .tile-links a.btn:hover {
    background: var(--btn-glass-bg-hover) !important; background-color: var(--btn-glass-bg-hover) !important;
  }
</style>

<!-- MOFA hero title (match standalone) -->
<div class="brand-hero">
  <a class="brand-title gradient-title-mini" href="/">MOFA</a>
</div>
<h1 class="page-title">MacOS App Store apps</h1>

<!-- Status with last updated, raw links, and theme switch -->
<div class="status-bar">
  <div class="status-line">
    <span>Last Updated: <code class="status-ts">February 10, 2026 08:40 PM EST</code></span>
    <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.xml"><strong>Raw XML</strong></a>
    <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.yaml"><strong>Raw YAML</strong></a>
    <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/macos_appstore_latest.json"><strong>Raw JSON</strong></a>
    <span class="muted">(Automatically updated every 2 hours)</span>
  </div>
  <span class="appearance-toggle-inline mofa-minimal">
    <button id="appearance-toggle" class="VPSwitch VPSwitchAppearance" type="button" role="switch" title="Switch theme" aria-checked="false">
      <span class="check"><span class="icon"><span class="vpi-sun sun"></span><span class="vpi-moon moon"></span></span></span>
    </button>
  </span>
</div>

<div class="grid-wrap">
  <div class="grid">
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/1c/e7/65/1ce765cb-02a9-b01b-c38a-12a625569f71/Word_macOS-0-0-85-220-0-0-0-6-0-2x.png/512x512bb.png" alt="Microsoft Word"></div>
        <div class="tile-title"><b>Microsoft Word</b></div>
        <div class="tile-version"><em><code>16.105.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 03, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-word/id462054704?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/0e/69/42/0e694298-162b-b2f6-3a44-2e50c58be2ad/Excel_macOS-0-0-85-220-0-0-0-6-0-2x.png/512x512bb.png" alt="Microsoft Excel"></div>
        <div class="tile-title"><b>Microsoft Excel</b></div>
        <div class="tile-version"><em><code>16.105.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 03, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-excel/id462058435?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/a2/ed/af/a2edaf10-75ab-2f57-8420-62cf17693dbf/Powerpoint_macOS-0-0-85-220-0-0-0-6-0-2x.png/512x512bb.png" alt="Microsoft PowerPoint"></div>
        <div class="tile-title"><b>Microsoft PowerPoint</b></div>
        <div class="tile-version"><em><code>16.105.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 03, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-powerpoint/id462062816?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/d9/7d/39/d97d3994-c763-6f07-433d-18a936529631/Outlook_macOS-0-0-85-220-0-0-0-6-0-2x.png/512x512bb.png" alt="Microsoft Outlook"></div>
        <div class="tile-title"><b>Microsoft Outlook</b></div>
        <div class="tile-version"><em><code>16.105.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 03, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-outlook/id985367838?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/64/42/9f/64429f2f-b39b-ad64-ddfd-a5ea65d7e0fa/OneNote_macOS-0-0-85-220-0-0-0-6-0-2x.png/512x512bb.png" alt="Microsoft OneNote"></div>
        <div class="tile-title"><b>Microsoft OneNote</b></div>
        <div class="tile-version"><em><code>16.105.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 03, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-onenote/id784801555?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/69/8b/05/698b050b-306a-a0e2-5792-17828c61345e/OneDrive.png/512x512bb.png" alt="OneDrive"></div>
        <div class="tile-title"><b>OneDrive</b></div>
        <div class="tile-version"><em><code>26.002.0105</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>January 30, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/onedrive/id823766827?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple124/v4/09/a4/f4/09a4f4b3-7aed-51c0-8e6b-5cb95ec6dada/rmssharing.png/512x512bb.png" alt="RMS Sharing"></div>
        <div class="tile-title"><b>RMS Sharing</b></div>
        <div class="tile-version"><em><code>1.3.4</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 19, 2021</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/rms-sharing/id908570259?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/e9/fb/8a/e9fb8ad8-d261-d447-6f2e-20ec4cb02c3c/AppIcon-0-0-85-220-0-0-5-0-2x.png/512x512bb.png" alt="Windows App"></div>
        <div class="tile-title"><b>Windows App</b></div>
        <div class="tile-version"><em><code>11.3.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>January 24, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/windows-app/id1295203466?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/dc/6f/73/dc6f735a-d9fb-e2eb-bb0e-733a1dec0cad/AppIcon-Release-0-85-220-0-4-2x-sRGB.png/512x512bb.png" alt="Microsoft To Do"></div>
        <div class="tile-title"><b>Microsoft To Do</b></div>
        <div class="tile-version"><em><code>2.159</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>October 10, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-to-do/id1274495053?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/82/e3/5f/82e35fe7-f3bc-3bb4-a206-3ee3b15daaf3/AppIcon-0-85-220-0-6-0-0-2x-0-0.png/512x512bb.png" alt="Microsoft Copilot"></div>
        <div class="tile-title"><b>Microsoft Copilot</b></div>
        <div class="tile-version"><em><code>25.3.440206001</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 07, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-copilot/id6738511300?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/fd/e1/79/fde1796c-45de-a318-3f02-419cdd1d2003/AppIcon-0-0-85-220-0-0-5-0-2x.png/512x512bb.png" alt="Azure VPN Client"></div>
        <div class="tile-title"><b>Azure VPN Client</b></div>
        <div class="tile-version"><em><code>2.8.100</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>October 28, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/azure-vpn-client/id1553936137?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/35/42/98/35429802-8ef5-c306-5279-ea3873609e14/AppIconProd-85-220-0-4-0-0-2x-0-0.png/512x512bb.png" alt="Universal Print"></div>
        <div class="tile-title"><b>Universal Print</b></div>
        <div class="tile-version"><em><code>1.0.5</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>May 30, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/universal-print/id6450432292?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple122/v4/4b/59/04/4b5904a2-060d-f5e1-707f-c96da43bd11f/AppIcon-85-220-4-2x.png/512x512bb.png" alt="Microsoft Rewards for Safari"></div>
        <div class="tile-title"><b>Microsoft Rewards for Safari</b></div>
        <div class="tile-version"><em><code>1.0.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>December 20, 2022</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-rewards-for-safari/id6443944644?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple112/v4/fe/9b/5a/fe9b5a2a-6cc9-41bd-604f-a6f3913dd240/AppIcon-0-0-85-220-4-2x.png/512x512bb.png" alt="Microsoft Bing for Safari"></div>
        <div class="tile-title"><b>Microsoft Bing for Safari</b></div>
        <div class="tile-version"><em><code>3.0.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>September 10, 2022</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-bing-for-safari/id1560727432?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple116/v4/9e/10/ce/9e10cee9-e04d-26b7-65b9-7dc32679c10a/AppIcon-85-220-0-4-2x.png/512x512bb.png" alt="Microsoft Accessory Updater"></div>
        <div class="tile-title"><b>Microsoft Accessory Updater</b></div>
        <div class="tile-version"><em><code>1.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 10, 2022</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-accessory-updater/id1599783787?mt=12&amp;uo=4">App Store</a>
        </div>
      </div>
    </div>
  </div>
</div>
