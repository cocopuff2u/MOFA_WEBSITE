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
    <span>Last Updated: <code class="status-ts">March 08, 2026 09:39 PM EDT</code></span>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/2a/f0/35/2af035f3-fc83-d56e-8a57-05da1bcad566/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Word"></div>
        <div class="tile-title"><b>Microsoft Word</b></div>
        <div class="tile-version"><em><code>2.106.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 02, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-word/id586447913?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/a3/6b/5b/a36b5b38-5570-cda4-d5c1-9e5532fdf40c/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Excel"></div>
        <div class="tile-title"><b>Microsoft Excel</b></div>
        <div class="tile-version"><em><code>2.106.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 02, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-excel/id586683407?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/76/a7/57/76a75731-c20b-a9a6-a33e-794da303159c/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft PowerPoint"></div>
        <div class="tile-title"><b>Microsoft PowerPoint</b></div>
        <div class="tile-version"><em><code>2.106.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 02, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-powerpoint/id586449534?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/07/35/55/07355553-d782-158a-12f2-daa122973b2b/AppIcon-outlook.prod-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Outlook"></div>
        <div class="tile-title"><b>Microsoft Outlook</b></div>
        <div class="tile-version"><em><code>5.2607.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 23, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-outlook/id951937596?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/36/48/39/364839fb-521d-5ecb-6a02-de3b8c6f9d43/AppIcon-0-0-1x_U007epad-0-1-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft OneNote"></div>
        <div class="tile-title"><b>Microsoft OneNote</b></div>
        <div class="tile-version"><em><code>16.106.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 02, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-onenote/id410395246?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/a9/ae/e9/a9aee983-0703-81c8-caca-f744b21d4434/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/512x512bb.jpg" alt="Microsoft OneDrive"></div>
        <div class="tile-title"><b>Microsoft OneDrive</b></div>
        <div class="tile-version"><em><code>16.34.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 02, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-onedrive/id477537958?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/33/95/21/339521a0-181c-987b-fca4-161a61a47fb4/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/512x512bb.jpg" alt="Windows App Mobile"></div>
        <div class="tile-title"><b>Windows App Mobile</b></div>
        <div class="tile-version"><em><code>11.2.5</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>December 18, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/windows-app-mobile/id714464092?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/db/0b/c0/db0bc048-1cc8-7bf7-85cf-7440e3f351db/AppIcon-0-1x_U007epad-0-1-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Defender: Security"></div>
        <div class="tile-title"><b>Microsoft Defender: Security</b></div>
        <div class="tile-version"><em><code>1.1.74260102</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-defender-security/id1526737990?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/e5/9b/75/e59b75fd-d257-d6bd-c21e-90f021b4fa8a/AppIcon_Production-0-0-1x_U007epad-0-4-85-220.png/512x512bb.jpg" alt="Microsoft Copilot AI Assistant"></div>
        <div class="tile-title"><b>Microsoft Copilot AI Assistant</b></div>
        <div class="tile-version"><em><code>30.0.440304005</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 05, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-copilot-ai-assistant/id6472538445?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/79/36/5f/79365f19-27a9-b7e0-d0b3-3caaa75fc826/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Loop"></div>
        <div class="tile-title"><b>Microsoft Loop</b></div>
        <div class="tile-version"><em><code>2.106</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 09, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-loop/id1637682491?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/a4/66/d4/a466d4c0-8979-346d-bd2f-a0e57b4ce7d7/AppIcon-0-1x_U007epad-0-1-85-220-0.png/512x512bb.jpg" alt="Microsoft Warehouse Management"></div>
        <div class="tile-title"><b>Microsoft Warehouse Management</b></div>
        <div class="tile-version"><em><code>4.0.37</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 24, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-warehouse-management/id6444014310?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/8f/7b/ef/8f7bef3a-1e8b-f822-e0e5-a8f4645c6c09/appicon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Store Commerce"></div>
        <div class="tile-title"><b>Store Commerce</b></div>
        <div class="tile-version"><em><code>9.56.26063</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 08, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/74/91/e4/7491e4b5-0352-3c01-50f8-c3e6faa96056/To-Do-AppStore-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft To Do"></div>
        <div class="tile-title"><b>Microsoft To Do</b></div>
        <div class="tile-version"><em><code>2.161</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>November 12, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-to-do/id1212616790?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/ea/96/85/ea9685af-e064-b33e-9f5a-30bde6599245/FieldServices_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Dynamics 365 Field Service"></div>
        <div class="tile-title"><b>Dynamics 365 Field Service</b></div>
        <div class="tile-version"><em><code>13.26021.9</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 23, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/dynamics-365-field-service/id1485579247?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/b9/2f/0b/b92f0b73-3ea4-b7c7-f773-2ac5beb1e25b/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Viva Engage"></div>
        <div class="tile-title"><b>Viva Engage</b></div>
        <div class="tile-version"><em><code>11.31.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 25, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/2a/1e/b2/2a1eb229-203b-46eb-bd23-9ac6ed70adfd/AppIcon-0-0-1x_U007epad-0-0-0-1-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Edge: AI Browser"></div>
        <div class="tile-title"><b>Microsoft Edge: AI Browser</b></div>
        <div class="tile-version"><em><code>145.3800.99</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 07, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/fa/78/c9/fa78c99d-ea2d-e409-6fd1-8d3efeb11cc3/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Microsoft Planner"></div>
        <div class="tile-title"><b>Microsoft Planner</b></div>
        <div class="tile-version"><em><code>1.17.14</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-planner/id1219301037?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/77/44/50/774450a9-74c5-b32c-121d-e3976ebca3cb/AppIcons-0-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Azure"></div>
        <div class="tile-title"><b>Microsoft Azure</b></div>
        <div class="tile-version"><em><code>8.1.1</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-azure/id1219013620?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/74/91/e4/7491e4b5-0352-3c01-50f8-c3e6faa96056/To-Do-AppStore-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft To Do"></div>
        <div class="tile-title"><b>Microsoft To Do</b></div>
        <div class="tile-version"><em><code>2.161</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>November 12, 2025</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-to-do/id1212616790?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/d3/27/8e/d3278e1e-2352-8365-0a74-d13ad76c08f5/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Teams"></div>
        <div class="tile-title"><b>Microsoft Teams</b></div>
        <div class="tile-version"><em><code>8.3.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 02, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-teams/id1113153706?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/a0/cd/d8/a0cdd882-b3b5-8847-c5e3-c235d9d7b016/SharePointAppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Microsoft SharePoint"></div>
        <div class="tile-title"><b>Microsoft SharePoint</b></div>
        <div class="tile-version"><em><code>4.55.4</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 10, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-sharepoint/id1091505266?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/0b/86/68/0b866877-ca04-1d24-cfdd-07aa2da2cda9/Dynamics_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Dynamics 365 for phones"></div>
        <div class="tile-title"><b>Dynamics 365 for phones</b></div>
        <div class="tile-version"><em><code>13.24093.1</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>September 11, 2024</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/dynamics-365-for-phones/id1003997947?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/31/50/16/31501686-cee5-3dcb-4262-6a7e1c32b14d/PowerApps_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Power Apps"></div>
        <div class="tile-title"><b>Power Apps</b></div>
        <div class="tile-version"><em><code>3.26024.13</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 03, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/power-apps/id1047318566?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/82/6a/c8/826ac8a1-b2f5-ac31-5bd6-5f2fbbaa36f3/AppIcon-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft Authenticator"></div>
        <div class="tile-title"><b>Microsoft Authenticator</b></div>
        <div class="tile-version"><em><code>6.8.42</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 02, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-authenticator/id983156458?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/55/32/37/553237da-6a44-5f30-7715-78bbffe433b0/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/512x512bb.jpg" alt="Meta Ads Manager"></div>
        <div class="tile-title"><b>Meta Ads Manager</b></div>
        <div class="tile-version"><em><code>465.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 05, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/meta-ads-manager/id964397083?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/80/7e/3f/807e3fde-b4c4-9f7b-6f44-d7d01702c254/AppIconLite-0-0-1x_U007ephone-0-6-0-0-sRGB-85-220.png/512x512bb.jpg" alt="CamScanner - PDF Scanner App"></div>
        <div class="tile-title"><b>CamScanner - PDF Scanner App</b></div>
        <div class="tile-version"><em><code>7.12.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 09, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/a7/49/e4/a749e48f-3002-8d8f-9611-5229fd2be028/AppIcon-0-1x_U007emarketing-0-8-0-0-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Power BI"></div>
        <div class="tile-title"><b>Microsoft Power BI</b></div>
        <div class="tile-version"><em><code>37.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 04, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/01/47/d0/0147d08c-ecec-9acf-40af-c074cd0ca013/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Intune Company Portal"></div>
        <div class="tile-title"><b>Intune Company Portal</b></div>
        <div class="tile-version"><em><code>5.2602.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 02, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/07/35/55/07355553-d782-158a-12f2-daa122973b2b/AppIcon-outlook.prod-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Outlook"></div>
        <div class="tile-title"><b>Microsoft Outlook</b></div>
        <div class="tile-version"><em><code>5.2607.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>February 23, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-outlook/id951937596?uo=4">App Store</a>
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
