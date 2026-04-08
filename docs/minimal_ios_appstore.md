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
    <span>Last Updated: <code class="status-ts">April 08, 2026 04:33 AM EDT</code></span>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/5e/e4/3b/5ee43b5f-e62a-daa8-47fb-55d5f15a2fa6/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Word"></div>
        <div class="tile-title"><b>Microsoft Word</b></div>
        <div class="tile-version"><em><code>2.107.4</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 06, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-word/id586447913?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/7c/08/d8/7c08d847-71ea-c6b1-7947-2f826a3ac61c/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Excel"></div>
        <div class="tile-title"><b>Microsoft Excel</b></div>
        <div class="tile-version"><em><code>2.107.4</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 06, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-excel/id586683407?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/25/10/d5/2510d5b8-f11e-61ce-66c3-b22c44ef5b7e/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft PowerPoint"></div>
        <div class="tile-title"><b>Microsoft PowerPoint</b></div>
        <div class="tile-version"><em><code>2.107.4</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 06, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-powerpoint/id586449534?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/f9/23/55/f92355fe-1946-8e8a-26bf-77a80fdc6f97/AppIcon-outlook.prod-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Outlook"></div>
        <div class="tile-title"><b>Microsoft Outlook</b></div>
        <div class="tile-version"><em><code>5.2613.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 06, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-outlook/id951937596?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/12/c1/ba/12c1ba73-49aa-3fe5-82a2-d34e2ef2aeb4/AppIcon-0-0-1x_U007epad-0-1-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft OneNote"></div>
        <div class="tile-title"><b>Microsoft OneNote</b></div>
        <div class="tile-version"><em><code>16.107.4</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 06, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-onenote/id410395246?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/71/2c/25/712c2562-3108-e1e8-48e9-5665710bba2f/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/512x512bb.jpg" alt="Microsoft OneDrive"></div>
        <div class="tile-title"><b>Microsoft OneDrive</b></div>
        <div class="tile-version"><em><code>16.36.5</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 02, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/38/21/9c/38219cf6-d788-a35b-ccac-1649f83114a0/AppIcon-0-1x_U007epad-0-1-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Defender: Security"></div>
        <div class="tile-title"><b>Microsoft Defender: Security</b></div>
        <div class="tile-version"><em><code>1.1.75270101</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 01, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-defender-security/id1526737990?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/6e/1a/f1/6e1af134-a167-aa6d-4dc5-ef914221430d/AppIcon_Production-0-0-1x_U007epad-0-4-85-220.png/512x512bb.jpg" alt="Microsoft Copilot AI Assistant"></div>
        <div class="tile-title"><b>Microsoft Copilot AI Assistant</b></div>
        <div class="tile-version"><em><code>30.0.440407005</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 07, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-copilot-ai-assistant/id6472538445?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/0f/f9/fc/0ff9fcad-6d47-3579-6025-2bf463f08898/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Loop"></div>
        <div class="tile-title"><b>Microsoft Loop</b></div>
        <div class="tile-version"><em><code>2.107</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 09, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-loop/id1637682491?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/57/c0/5e/57c05eea-27db-98f9-6506-64ce2bda782a/AppIcon-0-1x_U007epad-0-1-85-220-0.png/512x512bb.jpg" alt="Microsoft Warehouse Management"></div>
        <div class="tile-title"><b>Microsoft Warehouse Management</b></div>
        <div class="tile-version"><em><code>4.0.39</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 24, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/28/31/c7/2831c7c3-6244-a56d-0a61-5420ff8c44b3/FieldServices_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Dynamics 365 Field Service"></div>
        <div class="tile-title"><b>Dynamics 365 Field Service</b></div>
        <div class="tile-version"><em><code>13.26021.11</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 27, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/dynamics-365-field-service/id1485579247?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/40/b1/f1/40b1f177-21a4-7c77-ac14-1061e160d8fb/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Viva Engage"></div>
        <div class="tile-title"><b>Viva Engage</b></div>
        <div class="tile-version"><em><code>11.32.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 23, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/91/1f/37/911f3713-2daf-eee5-3652-9055dd0264a2/AppIcon-0-0-1x_U007epad-0-0-0-1-0-0-sRGB-0-85-220.png/512x512bb.jpg" alt="Microsoft Edge: AI Browser"></div>
        <div class="tile-title"><b>Microsoft Edge: AI Browser</b></div>
        <div class="tile-version"><em><code>146.3856.102</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 07, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/5d/65/98/5d659850-7778-8a52-e165-08dfd1b4f297/AppIcons-0-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Azure"></div>
        <div class="tile-title"><b>Microsoft Azure</b></div>
        <div class="tile-version"><em><code>8.1.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 17, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/6b/10/0f/6b100f89-0b27-811b-00df-040b482c6900/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Teams"></div>
        <div class="tile-title"><b>Microsoft Teams</b></div>
        <div class="tile-version"><em><code>8.6.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 03, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-teams/id1113153706?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/b9/7b/61/b97b619c-18b5-5918-6e6b-109381e5d669/SharePointAppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Microsoft SharePoint"></div>
        <div class="tile-title"><b>Microsoft SharePoint</b></div>
        <div class="tile-version"><em><code>5.0.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 31, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/c7/50/64/c75064cf-9eb9-c3e0-48a9-4cf7a3ded021/PowerApps_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Power Apps"></div>
        <div class="tile-title"><b>Power Apps</b></div>
        <div class="tile-version"><em><code>3.26034.11</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 31, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/power-apps/id1047318566?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/30/12/3b/30123ba1-af82-2f0c-b465-a63337e2ee7a/AppIcon-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft Authenticator"></div>
        <div class="tile-title"><b>Microsoft Authenticator</b></div>
        <div class="tile-version"><em><code>6.8.44</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 03, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-authenticator/id983156458?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/0f/98/85/0f988540-42ec-9aba-016c-066763cc58fd/logo_ads_color-0-0-1x_U007emarketing-0-0-0-7-0-0-0-85-220.png/512x512bb.jpg" alt="Google Ads"></div>
        <div class="tile-title"><b>Google Ads</b></div>
        <div class="tile-version"><em><code>3.27.20079932</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 02, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/google-ads/id1037457231?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/70/4d/32/704d32a1-070b-8369-39ba-7c87cecb7c10/AppIconLite-0-0-1x_U007ephone-0-6-0-0-sRGB-85-220.png/512x512bb.jpg" alt="CamScanner - PDF Scanner App"></div>
        <div class="tile-title"><b>CamScanner - PDF Scanner App</b></div>
        <div class="tile-version"><em><code>7.15.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 07, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/84/4d/8e/844d8ea6-8594-540e-ef5f-29f5d5943df0/AppIcon-0-1x_U007emarketing-0-8-0-0-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Power BI"></div>
        <div class="tile-title"><b>Microsoft Power BI</b></div>
        <div class="tile-version"><em><code>37.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>March 29, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/a6/a7/d1/a6a7d129-4b3e-44b2-41a2-1bf7ae623a47/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Intune Company Portal"></div>
        <div class="tile-title"><b>Intune Company Portal</b></div>
        <div class="tile-version"><em><code>5.2602.1</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 02, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/44/7c/47/447c47f9-7f5c-35b2-e257-2997ec2390bf/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-85-220.png/512x512bb.jpg" alt="Microsoft 365 Copilot"></div>
        <div class="tile-title"><b>Microsoft 365 Copilot</b></div>
        <div class="tile-version"><em><code>2.108.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>April 01, 2026</code></em></small></div>
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
