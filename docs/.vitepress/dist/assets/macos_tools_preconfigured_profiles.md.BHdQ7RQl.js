import{_ as e,c as r,o as t,ag as i}from"./chunks/framework.ZX5IUNw2.js";const a="/images/mau_update_prompt.png",d=JSON.parse('{"title":"📱 Preconfigured Profiles","description":"","frontmatter":{},"headers":[],"relativePath":"macos_tools/preconfigured_profiles.md","filePath":"macos_tools/preconfigured_profiles.md","lastUpdated":1740242902000}'),n={name:"macos_tools/preconfigured_profiles.md"};function l(s,o,c,f,u,g){return t(),r("div",null,o[0]||(o[0]=[i('<h1 id="📱-preconfigured-profiles" tabindex="-1">📱 Preconfigured Profiles <a class="header-anchor" href="#📱-preconfigured-profiles" aria-label="Permalink to &quot;📱 Preconfigured Profiles&quot;">​</a></h1><p>Welcome to the <strong>Preconfigured Profiles</strong> page! 🌐 Here, you will find a collection of ready-to-use <strong>mobileconfig</strong> files designed to simplify the management of Microsoft Office products on macOS devices 🍏. These profiles are crafted for seamless deployment, allowing you to efficiently configure Office settings across your enterprise environment. Whether you choose to upload the <strong>mobileconfig</strong> files directly to your MDM 📤 or copy the contents to create custom configurations 📝, the process is straightforward and hassle-free. ⚙️</p><p>Below, you&#39;ll find a list of available <strong>mobileconfig</strong> files for download. 📑</p><h2 id="🔄-microsoft-autoupdate" tabindex="-1">🔄 Microsoft AutoUpdate <a class="header-anchor" href="#🔄-microsoft-autoupdate" aria-label="Permalink to &quot;🔄 Microsoft AutoUpdate&quot;">​</a></h2><p><strong>Preferences Domain: <code>com.microsoft.autoupdate2</code></strong> 🖥️</p><p>This section provides configuration profiles to enforce Microsoft AutoUpdate (MAU) settings for macOS. These profiles apply a global <strong>3-day</strong>, <strong>7-day</strong>, or <strong>14-day</strong> forced update policy for Microsoft apps such as Word, Excel, PowerPoint, and Teams.</p><img src="'+a+'" alt="MAU Prompt" style="vertical-align:middle;display:inline-block;"><p>Key settings include:</p><ul><li><strong>Update Channel:</strong> Current 🔄</li><li><strong>Automatic Downloads:</strong> Enabled 📥</li><li><strong>Update Initiation:</strong> Begins after 3/7/14 days ⏳</li><li><strong>Forced Quit Countdown:</strong> 60 minutes ⏰</li><li><strong>Update Check Frequency:</strong> Every 360 minutes 🔍</li></ul><h4 id="configuration-profiles-🛠️" tabindex="-1">Configuration Profiles 🛠️ <a class="header-anchor" href="#configuration-profiles-🛠️" aria-label="Permalink to &quot;Configuration Profiles 🛠️&quot;">​</a></h4><ul><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_3day_update_v1.mobileconfig" target="_blank" rel="noreferrer"><strong>3-Day Forced Update</strong></a> ⏳</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_7day_update_v1.mobileconfig" target="_blank" rel="noreferrer"><strong>7-Day Forced Update</strong></a> 📅</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_14day_update_v1.mobileconfig" target="_blank" rel="noreferrer"><strong>14-Day Forced Update</strong></a> 📆</li></ul><h4 id="configuration-profiles-outlook-daily-🛠️" tabindex="-1">Configuration Profiles (Outlook Daily) 🛠️ <a class="header-anchor" href="#configuration-profiles-outlook-daily-🛠️" aria-label="Permalink to &quot;Configuration Profiles (Outlook Daily) 🛠️&quot;">​</a></h4><ul><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_3day_update_outlook_daily_v1.mobileconfig" target="_blank" rel="noreferrer"><strong>3-Day Forced Update (Outlook Daily)</strong></a> ⏳</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_7day_update_outlook_daily_v1.mobileconfig" target="_blank" rel="noreferrer"><strong>7-Day Forced Update (Outlook Daily)</strong></a> 📅</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_14day_update_outlook_daily_v1.mobileconfig" target="_blank" rel="noreferrer"><strong>14-Day Forced Update (Outlook Daily)</strong></a> 📆</li></ul><p><i><small>To download a configuration, click the link and select “Download Raw File.”</small></i> ✅</p><h2 id="🔒-data-privacy-telemetry" tabindex="-1">🔒 Data Privacy &amp; Telemetry <a class="header-anchor" href="#🔒-data-privacy-telemetry" aria-label="Permalink to &quot;🔒 Data Privacy &amp; Telemetry&quot;">​</a></h2><p><strong>Preferences Domain: <code>com.microsoft.Excel</code>, <code>com.microsoft.Outlook</code>, <code>com.microsoft.PowerPoint</code>, <code>com.microsoft.Word</code>, <code>com.microsoft.OneNote.mac</code>, <code>com.microsoft.Office365ServiceV2</code>, <code>com.microsoft.AutoUpdate2</code></strong> 🖥️</p><p>This section provides configuration profiles to disable telemetry data collection across various Microsoft apps like Word, Excel, PowerPoint, Outlook, OneNote, Office365Servicesv2, and MAU. The objective is to strengthen user privacy by limiting the amount of data shared with Microsoft. This is particularly recommended for <a href="https://learn.microsoft.com/en-us/microsoft-365-apps/deploy/deploy-microsoft-365-apps-gcc-high-dod" target="_blank" rel="noreferrer"><strong>GCC High or DoD environments</strong></a>.</p><p>Key settings include:</p><ul><li><strong>SendAllTelemetryEnabled:</strong> False 🚫</li><li><strong>SendCriticalTelemetryEnabled:</strong> False 🚫</li><li><strong>SendASmileEnabled:</strong> False 🚫</li><li><strong>AcknowledgedDataCollectionPolicy:</strong> RequiredDataOnly 📋</li></ul><h4 id="configuration-profiles-🛠️-1" tabindex="-1">Configuration Profiles 🛠️ <a class="header-anchor" href="#configuration-profiles-🛠️-1" aria-label="Permalink to &quot;Configuration Profiles 🛠️&quot;">​</a></h4><ul><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_user_privacy.mobileconfig" target="_blank" rel="noreferrer"><strong>MAU User Privacy</strong></a> 🔒</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_office365servicesv2_user_privacy.mobileconfig" target="_blank" rel="noreferrer"><strong>Office365ServicesV2 User Privacy</strong></a> 🔒</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_excel_user_privacy.mobileconfig" target="_blank" rel="noreferrer"><strong>Excel User Privacy</strong></a> 🔒</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_onenote_user_privacy.mobileconfig" target="_blank" rel="noreferrer"><strong>OneNote User Privacy</strong></a> 🔒</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_outlook_user_privacy.mobileconfig" target="_blank" rel="noreferrer"><strong>Outlook User Privacy</strong></a> 🔒</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_powerpoint_user_privacy.mobileconfig" target="_blank" rel="noreferrer"><strong>PowerPoint User Privacy</strong></a> 🔒</li><li><a href="https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_word_user_privacy.mobileconfig" target="_blank" rel="noreferrer"><strong>Word User Privacy</strong></a> 🔒</li></ul><p><i><small>To download a configuration, click the link and select “Download Raw File.”</small></i> ✅</p><h2 id="📱-how-a-mobileconfig-works" tabindex="-1">📱 How a <strong>mobileconfig</strong> works? <a class="header-anchor" href="#📱-how-a-mobileconfig-works" aria-label="Permalink to &quot;📱 How a **mobileconfig** works?&quot;">​</a></h2><p>Click <a href="/macos_tools/profile_breakdown.html">here</a> to get the breakdown and understand its structure!</p><div style="text-align:center;"><h2 id="💬-got-a-need-let-us-know" tabindex="-1">💬 <strong>Got a Need? Let Us Know!</strong> <a class="header-anchor" href="#💬-got-a-need-let-us-know" aria-label="Permalink to &quot;💬 **Got a Need? Let Us Know!**&quot;">​</a></h2><p>If you need something, here are a few ways to reach out:</p><p>💭 <strong><a href="https://github.com/cocopuff2u/MOFA/discussions" target="_blank" rel="noreferrer">Start a Discussion</a></strong><br> Use this to ask questions, share ideas, or have conversations with the community. It&#39;s a great place to get feedback or advice!</p><p>🐛 <strong><a href="https://github.com/cocopuff2u/MOFA/issues" target="_blank" rel="noreferrer">Open an Issue</a></strong><br> If you&#39;re experiencing a problem, encountering a bug, or need help with something specific, create an issue here to bring it to our attention.</p><p>🔧 <strong><a href="https://github.com/cocopuff2u/MOFA/pulls" target="_blank" rel="noreferrer">Submit a Pull Request</a></strong><br> If you have improvements, bug fixes, or new features to contribute, submit a pull request and help make the project better!</p><p>📬 <strong><a href="https://mofa.cocolabs.dev/about_support/report_issue.html" target="_blank" rel="noreferrer">Contact Us</a></strong><br> If you&#39;re not familiar with GitHub or need assistance outside of the platform, feel free to reach out through our contact page!</p></div>',25)]))}const m=e(n,[["render",l]]);export{d as __pageData,m as default};
