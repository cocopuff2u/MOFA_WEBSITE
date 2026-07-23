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
    <span>Last Updated: <code class="status-ts">July 23, 2026 04:23 AM EDT</code></span>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/75/c4/6e/75c46ec1-bfa3-7532-b5a5-d174ff38d9d1/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Word"></div>
        <div class="tile-title"><b>Microsoft Word</b></div>
        <div class="tile-version"><em><code>2.112</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-word/id586447913?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/88/80/99/88809990-20e3-acfe-f7f7-951ec9e57c87/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Excel"></div>
        <div class="tile-title"><b>Microsoft Excel</b></div>
        <div class="tile-version"><em><code>2.112</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-excel/id586683407?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/49/38/b0/4938b097-be32-e2d1-32d6-74e466e6aa3b/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft PowerPoint"></div>
        <div class="tile-title"><b>Microsoft PowerPoint</b></div>
        <div class="tile-version"><em><code>2.112</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-powerpoint/id586449534?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/5b/c6/8c/5bc68c14-5fdf-93b2-9467-764d5ecb5c27/AppIcon-outlook.prod-0-0-1x_U007epad-0-1-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Outlook"></div>
        <div class="tile-title"><b>Microsoft Outlook</b></div>
        <div class="tile-version"><em><code>5.2628.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-outlook/id951937596?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/81/39/05/81390527-1a7d-0f1e-1039-07175c7b136c/AppIcon-0-0-1x_U007epad-0-1-0-sRGB-0-0-0-85-220.png/512x512bb.jpg" alt="Microsoft OneNote"></div>
        <div class="tile-title"><b>Microsoft OneNote</b></div>
        <div class="tile-version"><em><code>16.112</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-onenote/id410395246?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/19/3c/c1/193cc171-211a-68b4-09e8-11bec89a5ccc/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/512x512bb.jpg" alt="Microsoft OneDrive"></div>
        <div class="tile-title"><b>Microsoft OneDrive</b></div>
        <div class="tile-version"><em><code>18.6.5</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 21, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-onedrive/id477537958?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/39/f5/9e/39f59e3f-5392-b524-cb2f-fc642ebca3ba/AppIcon-0-0-1x_U007epad-0-1-0-sRGB-85-220.png/512x512bb.jpg" alt="Windows App Mobile"></div>
        <div class="tile-title"><b>Windows App Mobile</b></div>
        <div class="tile-version"><em><code>11.3.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>June 09, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/windows-app-mobile/id714464092?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/1c/5e/8c/1c5e8c24-2259-eca8-930b-449f5e8041c3/AppIcon-0-1x_U007epad-0-1-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Defender: Security"></div>
        <div class="tile-title"><b>Microsoft Defender: Security</b></div>
        <div class="tile-version"><em><code>1.1.79080103</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-defender-security/id1526737990?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/ef/99/cc/ef99cc2e-3630-734e-7b32-51bce9005a82/AppIcon_Production-0-0-1x_U007epad-0-4-85-220.png/512x512bb.jpg" alt="Microsoft Copilot"></div>
        <div class="tile-title"><b>Microsoft Copilot</b></div>
        <div class="tile-version"><em><code>30.0.440707001</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 09, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-copilot/id6472538445?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/48/09/1c/48091cf8-c383-9fca-69bf-7712bc222090/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Loop"></div>
        <div class="tile-title"><b>Microsoft Loop</b></div>
        <div class="tile-version"><em><code>2.111.5</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 13, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-loop/id1637682491?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/79/ef/b2/79efb2d6-d239-b3d5-e6da-9543d8f4d11c/AppIcon-0-1x_U007epad-0-1-85-220-0.png/512x512bb.jpg" alt="Microsoft Warehouse Management"></div>
        <div class="tile-title"><b>Microsoft Warehouse Management</b></div>
        <div class="tile-version"><em><code>4.1.4</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>May 28, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-warehouse-management/id6444014310?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/5e/86/cf/5e86cf2e-f2fe-dc35-5e2b-24d10a889a31/appicon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Store Commerce"></div>
        <div class="tile-title"><b>Store Commerce</b></div>
        <div class="tile-version"><em><code>9.58.26181</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 05, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/store-commerce/id1630004521?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/71/fe/78/71fe7828-44a4-8773-545c-636bf4dd568c/Sales_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Dynamics 365 Sales"></div>
        <div class="tile-title"><b>Dynamics 365 Sales</b></div>
        <div class="tile-version"><em><code>3.26073.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 13, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/dynamics-365-sales/id1485578688?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/9e/bc/aa/9ebcaa4a-2f17-4969-fe08-8c251c08674e/To-Do-AppStore-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft To Do"></div>
        <div class="tile-title"><b>Microsoft To Do</b></div>
        <div class="tile-version"><em><code>2.177</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 06, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-to-do/id1212616790?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/1f/20/37/1f20373d-b843-b1dd-a506-fb40ed6b1bec/FieldServices_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Dynamics 365 Field Service"></div>
        <div class="tile-title"><b>Dynamics 365 Field Service</b></div>
        <div class="tile-version"><em><code>13.26062.7</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>June 16, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/dynamics-365-field-service/id1485579247?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/e5/d4/61/e5d46183-fc78-b170-047f-34d182d1713a/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Viva Engage"></div>
        <div class="tile-title"><b>Viva Engage</b></div>
        <div class="tile-version"><em><code>11.47.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 14, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/viva-engage/id289559439?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/cf/12/20/cf12204a-2b70-d7d2-3fcb-bb3ed1e2030f/AppIcon-0-1x_U007epad-0-1-P3-85-220-0.png/512x512bb.jpg" alt="Whiteboard: just draw together"></div>
        <div class="tile-title"><b>Whiteboard: just draw together</b></div>
        <div class="tile-version"><em><code>2.7.1</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>June 07, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/whiteboard-just-draw-together/id1160517834?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/06/e2/03/06e20368-b53e-9f25-33e0-5f0e4cc03d25/AppIcon-0-0-1x_U007emarketing-0-11-0-0-85-220.png/512x512bb.jpg" alt="Opera: AI browser with VPN"></div>
        <div class="tile-title"><b>Opera: AI browser with VPN</b></div>
        <div class="tile-version"><em><code>6.6.2</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 09, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/opera-ai-browser-with-vpn/id1411869974?uo=4">App Store</a>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/7d/9e/90/7d9e90ec-8363-d83c-c321-1262a68fcc2f/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Microsoft Planner"></div>
        <div class="tile-title"><b>Microsoft Planner</b></div>
        <div class="tile-version"><em><code>1.17.18</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-planner/id1219301037?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/08/a0/f7/08a0f7ea-6851-719b-3185-7a7867fe8dcc/AppIcons-0-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Azure"></div>
        <div class="tile-title"><b>Microsoft Azure</b></div>
        <div class="tile-version"><em><code>8.1.10</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 21, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-azure/id1219013620?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/9e/bc/aa/9ebcaa4a-2f17-4969-fe08-8c251c08674e/To-Do-AppStore-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft To Do"></div>
        <div class="tile-title"><b>Microsoft To Do</b></div>
        <div class="tile-version"><em><code>2.177</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 06, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-to-do/id1212616790?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/45/2c/5b/452c5be8-226d-acc7-3e27-dac45371d03f/AppIcon-0-0-1x_U007epad-0-1-0-0-85-220.png/512x512bb.jpg" alt="Microsoft Teams"></div>
        <div class="tile-title"><b>Microsoft Teams</b></div>
        <div class="tile-version"><em><code>8.12.1</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 14, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-teams/id1113153706?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/48/f3/e1/48f3e18a-6336-610d-89f1-5219499fdf2b/SharePointAppIcon-0-0-1x_U007emarketing-0-8-0-0-85-220.png/512x512bb.jpg" alt="Microsoft SharePoint"></div>
        <div class="tile-title"><b>Microsoft SharePoint</b></div>
        <div class="tile-version"><em><code>5.0.3</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 21, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/87/6f/68/876f686c-95a6-b89c-4260-7d2e7e5b5721/PowerApps_AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Power Apps"></div>
        <div class="tile-title"><b>Power Apps</b></div>
        <div class="tile-version"><em><code>3.26072.5</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 21, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/power-apps/id1047318566?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/5f/a4/04/5fa4049e-a823-3dd6-267c-89cb83202a59/AppIcon-0-1x_U007emarketing-0-11-0-sRGB-85-220-0.png/512x512bb.jpg" alt="Microsoft Authenticator"></div>
        <div class="tile-title"><b>Microsoft Authenticator</b></div>
        <div class="tile-version"><em><code>6.8.51</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 22, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-authenticator/id983156458?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/b9/5b/3d/b95b3d0b-f5f6-1e94-a1cc-865c4f9bcb2f/AppIcon-0-0-1x_U007epad-0-1-0-85-220.png/512x512bb.jpg" alt="Meta Ads Manager"></div>
        <div class="tile-title"><b>Meta Ads Manager</b></div>
        <div class="tile-version"><em><code>484.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 17, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/meta-ads-manager/id964397083?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/a6/a0/ef/a6a0ef3d-67f6-7483-e8d5-22e05016e106/AppIcon-0-0-1x_U007ephone-0-11-0-85-220.png/512x512bb.jpg" alt="Lens: Translate &amp; Photo Finder"></div>
        <div class="tile-title"><b>Lens: Translate &amp; Photo Finder</b></div>
        <div class="tile-version"><em><code>3.1.15</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 14, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/lens-translate-photo-finder/id1587316791?uo=4">App Store</a>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple211/v4/7a/7d/99/7a7d9983-96c2-a9c8-0af1-42eed2fc176d/AppIcon-0-1x_U007emarketing-0-8-0-0-0-85-220-0.png/512x512bb.jpg" alt="Microsoft Power BI"></div>
        <div class="tile-title"><b>Microsoft Power BI</b></div>
        <div class="tile-version"><em><code>38.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 19, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-power-bi/id929738808?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/ae/33/81/ae3381f4-7438-5861-f7ee-b31d9585ba27/AppIcon-1x_U007emarketing-0-8-0-85-220-0.png/512x512bb.jpg" alt="Microsoft 365 Admin"></div>
        <div class="tile-title"><b>Microsoft 365 Admin</b></div>
        <div class="tile-version"><em><code>6.0.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 20, 2026</code></em></small></div>
        <div class="tile-spacer"></div>
        <div class="tile-links">
          <a class="btn" href="https://apps.apple.com/us/app/microsoft-365-admin/id761397963?uo=4">App Store</a>
        </div>
      </div>
    </div>
<div class="tile">
      <div class="tile-card">
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/73/96/7e/73967e6d-3368-4f87-1ffa-a878582a8e98/AppIcon-0-0-1x_U007emarketing-0-8-0-85-220.png/512x512bb.jpg" alt="Intune Company Portal"></div>
        <div class="tile-title"><b>Intune Company Portal</b></div>
        <div class="tile-version"><em><code>5.2606.0</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 08, 2026</code></em></small></div>
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
        <div class="tile-media"><img src="https://is1-ssl.mzstatic.com/image/thumb/Purple221/v4/35/f0/cc/35f0cc51-ca9c-f54d-2653-b44a8359fd38/AppIcon-0-0-1x_U007epad-0-1-0-0-sRGB-0-85-220.png/512x512bb.jpg" alt="Microsoft 365 Copilot"></div>
        <div class="tile-title"><b>Microsoft 365 Copilot</b></div>
        <div class="tile-version"><em><code>2.112.1</code></em></div>
        <div class="tile-updated"><small>Last Updated:<br><em><code>July 20, 2026</code></em></small></div>
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
