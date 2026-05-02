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
  .tile-media img { max-height: 80px; width: auto; height: auto; border-radius: 22%; }
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
<h1 class="page-title">iOS App Store apps</h1>

<!-- Status with last updated, raw links, and theme switch -->
<div class="status-bar">
  <div class="status-line">
    <span>Last Updated: <code class="status-ts">May 02, 2026 03:26 PM EDT</code></span>
    <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.xml"><strong>Raw XML</strong></a>
    <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.yaml"><strong>Raw YAML</strong></a>
    <a href="https://github.com/cocopuff2u/MOFA/blob/main/latest_raw_files/ios_appstore_latest.json"><strong>Raw JSON</strong></a>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/bd/b6/16/bdb6164e-fd6f-c9a6-f62b-c7d4bdb10315/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Word"></div>
        <div class="tile-title"><b>Microsoft Word</b></div>
        <div class="tile-version"><em><code>2.108.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-word/id586447913?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/d6/c4/3f/d6c43f26-f8d2-c344-6508-f46ab0624163/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Excel"></div>
        <div class="tile-title"><b>Microsoft Excel</b></div>
        <div class="tile-version"><em><code>2.108.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-excel/id586683407?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/ae/89/cd/ae89cd27-75bd-c931-2556-73f2d5123164/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft PowerPoint"></div>
        <div class="tile-title"><b>Microsoft PowerPoint</b></div>
        <div class="tile-version"><em><code>2.108.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-powerpoint/id586449534?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/83/8b/ad/838badba-26df-32a9-e76f-40efecfaf825/AppIcon-outlook.prod-0-0-1x_U007epad-0-1-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Outlook"></div>
        <div class="tile-title"><b>Microsoft Outlook</b></div>
        <div class="tile-version"><em><code>5.2616.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-outlook/id951937596?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/5b/f8/21/5bf821f3-dd5d-9c03-5cda-15fdac6d51d3/AppIcon-0-0-1x_U007epad-0-1-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft OneNote"></div>
        <div class="tile-title"><b>Microsoft OneNote</b></div>
        <div class="tile-version"><em><code>16.108.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-onenote/id410395246?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/6d/7e/7c/6d7e7cb7-de62-d184-24f6-23fdef4aace0/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/512x512bb.jpg" alt="Microsoft OneDrive"></div>
        <div class="tile-title"><b>Microsoft OneDrive</b></div>
        <div class="tile-version"><em><code>18.0.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-onedrive/id477537958?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/12/02/51/1202518b-aeee-b085-adb0-6fdbd38b6960/AppIcon-0-0-1x_U007epad-0-1-0-sRGB-85-220.png/512x512bb.jpg" alt="Windows App Mobile"></div>
        <div class="tile-title"><b>Windows App Mobile</b></div>
        <div class="tile-version"><em><code>11.3.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 06, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/windows-app-mobile/id714464092?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/ff/a6/bb/ffa6bb38-839d-78b1-a7d5-e87ef5e5f1a2/AppIcon-0-1x_U007epad-0-1-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Defender: Security"></div>
        <div class="tile-title"><b>Microsoft Defender: Security</b></div>
        <div class="tile-version"><em><code>1.1.76200101</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 24, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-defender-security/id1526737990?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/2a/44/cd/2a44cd77-a334-6589-7a6c-5cd63a443eec/AppIcon_Production-0-0-1x_U007epad-0-4-85-220.png/512x512bb.jpg" alt="Microsoft Copilot"></div>
        <div class="tile-title"><b>Microsoft Copilot</b></div>
        <div class="tile-version"><em><code>30.0.440427001</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 28, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-copilot/id6472538445?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/0d/d6/04/0dd60498-7339-3aed-7642-3b4426ef4a86/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Loop"></div>
        <div class="tile-title"><b>Microsoft Loop</b></div>
        <div class="tile-version"><em><code>2.108</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 13, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-loop/id1637682491?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/82/79/28/82792855-0257-872f-fc18-391dc2c23d9e/AppIcon-0-1x_U007epad-0-1-85-220-0.png/512x512bb.jpg" alt="Microsoft Warehouse Management"></div>
        <div class="tile-title"><b>Microsoft Warehouse Management</b></div>
        <div class="tile-version"><em><code>4.1.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-warehouse-management/id6444014310?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/ef/3f/eb/ef3febbb-9cb6-58c9-6d0f-1fc2e198089c/appicon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Store Commerce"></div>
        <div class="tile-title"><b>Store Commerce</b></div>
        <div class="tile-version"><em><code>9.56.26077</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 22, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/store-commerce/id1630004521?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/4b/c9/01/4bc9019e-a89d-de7f-7d9d-9bbdd3d81b92/Sales_AppIcon-1x_U007emarketing-0-7-0-85-220-0.png/512x512bb.jpg" alt="Dynamics 365 Sales"></div>
        <div class="tile-title"><b>Dynamics 365 Sales</b></div>
        <div class="tile-version"><em><code>3.24104.15</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>November 11, 2024</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/dynamics-365-sales/id1485578688?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/e1/01/52/e101525b-283c-ff27-26b5-5da5e6919cd4/To-Do-AppStore-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft To Do"></div>
        <div class="tile-title"><b>Microsoft To Do</b></div>
        <div class="tile-version"><em><code>2.169</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 09, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-to-do/id1212616790?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/ff/fc/8f/fffc8fa4-015a-4dad-c3a7-7f571fa5acfc/FieldServices_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Dynamics 365 Field Service"></div>
        <div class="tile-title"><b>Dynamics 365 Field Service</b></div>
        <div class="tile-version"><em><code>13.26041.13</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 16, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/dynamics-365-field-service/id1485579247?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/bb/e6/86/bbe686aa-2133-8739-4892-0ac9e3baac64/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Viva Engage"></div>
        <div class="tile-title"><b>Viva Engage</b></div>
        <div class="tile-version"><em><code>11.38.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 28, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/viva-engage/id289559439?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/4b/53/7e/4b537e0f-ad6d-1b86-85f6-f7b65e7918c7/AppIcon-0-1x_U007epad-0-1-P3-85-220-0.png/512x512bb.jpg" alt="Whiteboard: just draw together"></div>
        <div class="tile-title"><b>Whiteboard: just draw together</b></div>
        <div class="tile-version"><em><code>2.6.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>January 07, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/whiteboard-just-draw-together/id1160517834?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/6a/b1/3b/6ab13b3d-9531-e6e3-7d7f-1db16d9dacc8/AppIcon-0-0-1x_U007epad-0-0-0-1-0-0-sRGB-0-85-220.png/512x512bb.jpg" alt="Microsoft Edge: AI Browser"></div>
        <div class="tile-title"><b>Microsoft Edge: AI Browser</b></div>
        <div class="tile-version"><em><code>147.3912.87</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 28, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-edge-ai-browser/id1288723196?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/be/a6/66/bea6661d-294b-f35d-34e1-3128b7b12006/AppIcons-0-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Seeing AI"></div>
        <div class="tile-title"><b>Seeing AI</b></div>
        <div class="tile-version"><em><code>5.6.1</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>September 04, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/seeing-ai/id999062298?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/c7/56/8a/c7568a5c-04f9-5e91-a2f3-9986abc3e485/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Microsoft Planner"></div>
        <div class="tile-title"><b>Microsoft Planner</b></div>
        <div class="tile-version"><em><code>1.17.15</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 03, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-planner/id1219301037?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/8b/c7/25/8bc725c3-5862-1ac1-92fc-722db0112836/AppIcons-0-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Azure"></div>
        <div class="tile-title"><b>Microsoft Azure</b></div>
        <div class="tile-version"><em><code>8.1.6</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 24, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-azure/id1219013620?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/e1/01/52/e101525b-283c-ff27-26b5-5da5e6919cd4/To-Do-AppStore-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft To Do"></div>
        <div class="tile-title"><b>Microsoft To Do</b></div>
        <div class="tile-version"><em><code>2.169</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 09, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-to-do/id1212616790?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/3c/6e/5e/3c6e5ea8-4b60-1ad9-fb11-0798325277ac/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Teams"></div>
        <div class="tile-title"><b>Microsoft Teams</b></div>
        <div class="tile-version"><em><code>8.7.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 30, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-teams/id1113153706?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/e3/57/22/e3572210-1147-9a7f-0a88-c3006b053d47/SharePointAppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Microsoft SharePoint"></div>
        <div class="tile-title"><b>Microsoft SharePoint</b></div>
        <div class="tile-version"><em><code>5.0.1</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 30, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-sharepoint/id1091505266?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/48/27/dd/4827dddc-01ba-e5ab-60c5-6b38ee8677f4/AppIcon-1x_U007emarketing-0-11-0-0-0-85-220-0.png/512x512bb.jpg" alt="Dynamics 365 Business Central"></div>
        <div class="tile-title"><b>Dynamics 365 Business Central</b></div>
        <div class="tile-version"><em><code>4.5</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 10, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/dynamics-365-business-central/id1093325047?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/39/db/b1/39dbb190-9c47-ee66-a613-1a99d81d9ad0/PowerApps_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Power Apps"></div>
        <div class="tile-title"><b>Power Apps</b></div>
        <div class="tile-version"><em><code>3.26043.16</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/power-apps/id1047318566?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/7c/5d/9d/7c5d9d54-5a0b-ec09-7b86-01f48b09b262/AppIcon-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft Authenticator"></div>
        <div class="tile-title"><b>Microsoft Authenticator</b></div>
        <div class="tile-version"><em><code>6.8.45</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 14, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-authenticator/id983156458?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/62/84/2c/62842c3d-de89-8d2e-151a-435596703de4/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/512x512bb.jpg" alt="Meta Ads Manager"></div>
        <div class="tile-title"><b>Meta Ads Manager</b></div>
        <div class="tile-version"><em><code>473.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 30, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/meta-ads-manager/id964397083?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/c1/b0/0c/c1b00c8e-1f66-123d-8fcf-47cbd67ce189/AppIconLite-0-0-1x_U007ephone-0-6-0-0-sRGB-85-220.png/512x512bb.jpg" alt="CamScanner - PDF Scanner App"></div>
        <div class="tile-title"><b>CamScanner - PDF Scanner App</b></div>
        <div class="tile-version"><em><code>7.16.5</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/camscanner-pdf-scanner-app/id388627783?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple114/v4/ed/46/15/ed46150c-83ff-e2bc-4caa-8b5948d65bd2/AppIcon-0-1x_U007emarketing-0-0-GLES2_U002c0-512MB-sRGB-0-0-0-85-220-0-0-0-6.png/512x512bb.jpg" alt="Work Folders"></div>
        <div class="tile-title"><b>Work Folders</b></div>
        <div class="tile-version"><em><code>2.2.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>January 18, 2019</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/work-folders/id950878067?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/63/5d/4e/635d4e6d-292c-fafc-32ce-8f96194ab8ec/AppIcon-0-1x_U007emarketing-0-8-0-0-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Power BI"></div>
        <div class="tile-title"><b>Microsoft Power BI</b></div>
        <div class="tile-version"><em><code>37.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 26, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-power-bi/id929738808?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/e1/0d/b8/e10db871-3c82-f649-3686-5eb88efa87aa/AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Microsoft 365 Admin"></div>
        <div class="tile-title"><b>Microsoft 365 Admin</b></div>
        <div class="tile-version"><em><code>5.7.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>September 05, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-365-admin/id761397963?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/df/81/d7/df81d7be-ad3d-b7e6-1e7c-c37cf306da2f/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Intune Company Portal"></div>
        <div class="tile-title"><b>Intune Company Portal</b></div>
        <div class="tile-version"><em><code>5.2603.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 29, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/intune-company-portal/id719171358?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/9d/f6/d8/9df6d87e-66ad-d6ab-aad9-d030ef4aa9cb/AppIcons-1x_U007emarketing-0-7-0-85-220-0.png/512x512bb.jpg" alt="Azure Information Protection"></div>
        <div class="tile-title"><b>Azure Information Protection</b></div>
        <div class="tile-version"><em><code>2.1.4</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>August 25, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/azure-information-protection/id689516635?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/26/aa/41/26aa417e-d775-1b0c-4f3a-6a6561668c4c/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-85-220.png/512x512bb.jpg" alt="Microsoft 365 Copilot"></div>
        <div class="tile-title"><b>Microsoft 365 Copilot</b></div>
        <div class="tile-version"><em><code>2.109.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 29, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-365-copilot/id541164041?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/b3/27/ee/b327ee1f-d14c-6650-21cf-71294902677e/AppIcon-0-0-1x_U007emarketing-0-6-0-85-220.png/512x512bb.jpg" alt="Skype for Business"></div>
        <div class="tile-title"><b>Skype for Business</b></div>
        <div class="tile-version"><em><code>6.34.119</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>June 10, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/skype-for-business/id605841731?uo=4">App Store</a>
        </div>
      </div>
    </div>
  </div>
</div>
