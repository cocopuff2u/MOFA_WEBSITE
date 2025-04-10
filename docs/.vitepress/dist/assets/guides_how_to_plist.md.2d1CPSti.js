import{_ as t,c as i,o,ag as s}from"./chunks/framework.ZX5IUNw2.js";const h=JSON.parse('{"title":"Guide: Creating and Deploying .plist Files with MDM (Jamf Pro or Intune)","description":"","frontmatter":{},"headers":[],"relativePath":"guides/how_to_plist.md","filePath":"guides/how_to_plist.md","lastUpdated":1734717543000}'),n={name:"guides/how_to_plist.md"};function a(r,e,l,c,p,g){return o(),i("div",null,e[0]||(e[0]=[s(`<h1 id="guide-creating-and-deploying-plist-files-with-mdm-jamf-pro-or-intune" tabindex="-1"><strong>Guide: Creating and Deploying .plist Files with MDM (Jamf Pro or Intune)</strong> <a class="header-anchor" href="#guide-creating-and-deploying-plist-files-with-mdm-jamf-pro-or-intune" aria-label="Permalink to &quot;**Guide: Creating and Deploying .plist Files with MDM (Jamf Pro or Intune)**&quot;">​</a></h1><p>Learn how to create <code>.plist</code> files, store them in the correct locations, and deploy them using MDM solutions like <strong>Jamf Pro</strong> or <strong>Intune</strong>. This guide will use Outlook as the example.</p><h3 id="_1-understanding-and-creating-plist-files" tabindex="-1"><strong>1. Understanding and Creating <code>.plist</code> Files</strong> <a class="header-anchor" href="#_1-understanding-and-creating-plist-files" aria-label="Permalink to &quot;**1. Understanding and Creating \`.plist\` Files**&quot;">​</a></h3><p>In macOS, <code>.plist</code> (Property List) files are used to store application configuration settings. These files allow administrators to define preferences, such as enabling or disabling features, to customize user experiences in Microsoft Outlook. These configurations can be deployed efficiently using a Mobile Device Management (MDM) solution, such as <strong>Jamf Pro</strong> or <strong>Intune</strong>, by converting <code>.plist</code> files into configuration profiles.</p><h4 id="creating-a-plist-file-from-scratch" tabindex="-1"><strong>Creating a .plist File from Scratch:</strong> <a class="header-anchor" href="#creating-a-plist-file-from-scratch" aria-label="Permalink to &quot;**Creating a .plist File from Scratch:**&quot;">​</a></h4><p>To create a <code>.plist</code> file from scratch for configuring Microsoft Outlook preferences, follow these steps:</p><ol><li><p><strong>Open a Text Editor:</strong> Use any text editor, such as <code>TextEdit</code> in plain text mode, or a code editor like <code>VS Code</code>.</p></li><li><p><strong>Add XML Structure:</strong></p><ul><li>Start with the XML declaration and a root <code>&lt;plist&gt;</code> element.</li><li>Inside the <code>&lt;dict&gt;</code> tag, define the key-value pairs that represent the configuration settings.</li></ul><p><strong>Example:</strong></p><div class="language-xml vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">xml</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&lt;?</span><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">xml</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> version</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">=</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;1.0&quot;</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> encoding</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">=</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;UTF-8&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">?&gt;</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&lt;!</span><span style="--shiki-light:#D73A49;--shiki-dark:#F97583;">DOCTYPE</span><span style="--shiki-light:#005CC5;--shiki-dark:#79B8FF;"> plist</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;"> PUBLIC &quot;-//Apple//DTD PLIST 1.0//EN&quot; &quot;http://www.apple.com/DTDs/PropertyList-1.0.dtd&quot;&gt;</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&lt;</span><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">plist</span><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;"> version</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">=</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;">&quot;1.0&quot;</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&gt;</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    &lt;</span><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">dict</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&gt;</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">        &lt;</span><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">key</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&gt;PlayMyEmailsEnabled&lt;/</span><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">key</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&gt;</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">        &lt;</span><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">false</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">/&gt;</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">    &lt;/</span><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">dict</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&gt;</span></span>
<span class="line"><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&lt;/</span><span style="--shiki-light:#22863A;--shiki-dark:#85E89D;">plist</span><span style="--shiki-light:#24292E;--shiki-dark:#E1E4E8;">&gt;</span></span></code></pre></div><ul><li><strong>Key:</strong> <code>PlayMyEmailsEnabled</code> controls the &quot;Play My Emails&quot; feature in Outlook.</li><li><strong>Value:</strong> <code>false</code> disables the feature.</li></ul></li><li><p><strong>Save the File:</strong> Name the file with a <code>.plist</code> extension, such as <code>com.microsoft.Outlook.plist</code>. Each application or suite will have its own required name.</p></li></ol><hr><h3 id="_2-location-of-plist-files-on-macos" tabindex="-1"><strong>2. Location of .plist Files on macOS</strong> <a class="header-anchor" href="#_2-location-of-plist-files-on-macos" aria-label="Permalink to &quot;**2. Location of .plist Files on macOS**&quot;">​</a></h3><p>The location of <code>.plist</code> files depends on whether the preferences are user-specific, computer specific or managed by MDM.</p><ul><li><p><strong>For User Preferences (Local, Unmanaged):</strong><em>These will apply to a specific local user account.</em></p><div class="language-plaintext vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">plaintext</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>~/Library/Preferences/com.microsoft.Outlook.plist</span></span></code></pre></div><p>This file contains the user-specific settings for Outlook.</p></li><li><p><strong>For Computer Preferences (Local, Managed via scripts or manually applied):</strong><em>These will apply to all local user accounts.</em></p><div class="language-plaintext vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">plaintext</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>/Library/Preferences/com.microsoft.Outlook.plist</span></span></code></pre></div><p>This file contains the computer-specific settings for Outlook.</p></li><li><p><strong>For Managed Preferences (Deployed via MDM):</strong><em>These will apply to all local user accounts.</em></p><div class="language-plaintext vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">plaintext</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span>/Library/Managed Preferences/com.microsoft.Outlook.plist</span></span></code></pre></div><p>MDM configurations are applied here, overriding user-specific preferences.</p></li></ul><hr><h3 id="_3-managed-preferences-deployed-via-mdm" tabindex="-1"><strong>3. Managed Preferences Deployed via MDM:</strong> <a class="header-anchor" href="#_3-managed-preferences-deployed-via-mdm" aria-label="Permalink to &quot;**3. Managed Preferences Deployed via MDM:**&quot;">​</a></h3><p>Once you&#39;ve created your <code>.plist</code> file, you can deploy it using <strong>Jamf Pro</strong> or <strong>Intune</strong> or <strong>some other mdm</strong>.</p><h4 id="jamf-pro" tabindex="-1"><strong>Jamf Pro</strong> <a class="header-anchor" href="#jamf-pro" aria-label="Permalink to &quot;**Jamf Pro**&quot;">​</a></h4><ol><li><p><strong>Create a Configuration Profile:</strong></p><ul><li>Log in to <strong>Jamf Pro</strong>.</li><li>Navigate to <strong>Configuration Profiles</strong> &gt; <strong>New</strong>.</li><li>Select the <strong>Custom Settings</strong> payload.</li><li>Upload the <code>.plist</code> file or paste its XML content into the <strong>Custom Settings</strong> field.</li></ul></li><li><p><strong>Assign Scope:</strong></p><ul><li>Assign the profile to devices or users using Smart Groups or Static Groups.</li></ul></li><li><p><strong>Deploy:</strong></p><ul><li>Save the profile. Devices will apply the configuration during the next MDM sync.</li></ul><hr></li></ol><h4 id="microsoft-intune-3-ways-to-manage-your-settings-pick-1-that-suits-your-needs" tabindex="-1"><strong>Microsoft Intune</strong> (3 ways to manage your settings. Pick 1 that suits your needs.) <a class="header-anchor" href="#microsoft-intune-3-ways-to-manage-your-settings-pick-1-that-suits-your-needs" aria-label="Permalink to &quot;**Microsoft Intune** (3 ways to manage your settings. Pick 1 that suits your needs.)&quot;">​</a></h4><ol><li><p><strong>The recommended way to manage configuration for Mac or iOS devices is to using the Settings Catalog</strong></p><ul><li><p>No need to manually create a <code>.plist</code> file.</p></li><li><p>Nearly all settings are available in a GUI to pick and choose what you want to manage.</p></li><li><p>Create your Settings Catalog Configuration:</p><ul><li>Log in to <strong>Microsoft Intune Admin Center</strong>.</li><li>Go to <strong>Devices</strong> &gt; <strong>macOS</strong> &gt; <strong>Configuration Profiles</strong> &gt; <strong>Create Profile</strong>.</li><li>Choose <strong>Settings Catalog</strong> and pick the settings you would like to manage.</li></ul></li><li><p>You can see the complete list of Settings Catalog settings keys in this repo (filter the latest Excel file for Mac or iOS): <a href="https://github.com/IntunePMFiles/DeviceConfig" target="_blank" rel="noreferrer">https://github.com/IntunePMFiles/DeviceConfig</a> (Goes way beyond just Microsoft apps.)</p></li><li><p>Intune documentation on working with settings catalog configuration: <a href="https://learn.microsoft.com/en-us/mem/intune/configuration/settings-catalog" target="_blank" rel="noreferrer">https://learn.microsoft.com/en-us/mem/intune/configuration/settings-catalog</a></p></li></ul></li><li><p><strong>Preference Files</strong></p><ul><li>If you find a preference key that is not yet supported in the Setting Catalog, or you like manually editing the XML, you can use a standard <code>.plist</code> file with a little bit of doctoring.</li><li>The files are essentially just macOS plist files with the opening and closing key tags removed.</li></ul><p><em>Opening keys:</em><code>&lt;?xml version=&quot;1.0&quot; encoding=&quot;UTF-8&quot;?&gt;</code><code>&lt;!DOCTYPE plist PUBLIC &quot;-//Apple//DTD PLIST 1.0//EN&quot; &quot;http://www.apple.com/DTDs/PropertyList-1.0.dtd&quot;&gt;</code><code>&lt;plist version=&quot;1.0&quot;&gt;</code><code>&lt;dict&gt;</code></p><p><em>Closing keys:</em><code>&lt;/dict&gt;</code><code>&lt;/plist&gt;</code></p><p>You should end up with a file like this: (Only the keys and values. Intune will wrap it for you and deliver it as a mobileconfig.)</p><p><code>&lt;key&gt;SomeKey&lt;/key&gt;</code><code>&lt;string&gt;someString&lt;/string&gt;</code><code>&lt;key&gt;AnotherKey&lt;/key&gt;</code><code>&lt;false/&gt;</code></p><ul><li>Save your edited file as <code>.txt</code> or <code>.xml</code>.</li><li>Upload your Intune Preference File: <ul><li>Log in to <strong>Microsoft Intune Admin Center</strong>.</li><li>Go to <strong>Devices</strong> &gt; <strong>macOS</strong> &gt; <strong>Configuration Profiles</strong> &gt; <strong>Create Profile</strong>.</li><li>Choose <strong>Templates</strong> &gt; <strong>Preference file</strong> and upload the <code>.xml</code> file.</li></ul></li><li>You can add this above and beyond the Setting Catalog for new keys that they have not added yet.</li><li>If you deploy both, do not duplicate settings keys between the two configurations. (Keys must be unique.)</li><li>Intune documentation on working with preference files: <a href="https://learn.microsoft.com/en-us/mem/intune/configuration/preference-file-settings-macos" target="_blank" rel="noreferrer">https://learn.microsoft.com/en-us/mem/intune/configuration/preference-file-settings-macos</a></li></ul></li><li><p><strong>Prepare the a Custom Configuration Profile:</strong></p><ul><li><p>You can always fall back to a custom file by wrapping the <code>.plist</code> file into a <code>.mobileconfig</code> profile with a tools like <strong>Profile Creator</strong>.</p></li><li><p>Or use the built in settings in <strong>iMazing Profile Editor</strong> to create the custom configuration profile.</p></li><li><p>Upload your Custom Configuration Profile:</p><ul><li>Log in to <strong>Microsoft Intune Admin Center</strong>.</li><li>Go to <strong>Devices</strong> &gt; <strong>macOS</strong> &gt; <strong>Configuration Profiles</strong> &gt; <strong>Create Profile</strong>.</li><li>Choose <strong>Templates</strong> &gt; <strong>Custom</strong> and upload the <code>.mobileconfig</code> file.</li></ul></li><li><p>Intune documentation on working with custom files: <a href="https://learn.microsoft.com/en-us/mem/intune/configuration/custom-settings-macos" target="_blank" rel="noreferrer">https://learn.microsoft.com/en-us/mem/intune/configuration/custom-settings-macos</a></p></li></ul></li><li><p><strong>After any of the above three options</strong></p><ul><li>Assign Scope: <ul><li>Assign the profile to the appropriate user or device groups.</li></ul></li><li>Deploy: <ul><li>Save and assign the profile. Devices will sync and apply the configuration during their next check-in.</li></ul></li></ul></li></ol><hr><h3 id="_4-helpful-resources-for-configuration-options" tabindex="-1"><strong>4. Helpful Resources for Configuration Options</strong> <a class="header-anchor" href="#_4-helpful-resources-for-configuration-options" aria-label="Permalink to &quot;**4. Helpful Resources for Configuration Options**&quot;">​</a></h3><p>For detailed guidance on available preferences and settings, refer to these valuable resources. We recommend starting with the Mac Admin Community&#39;s comprehensive, crowd-sourced list:</p><ul><li><p><strong>Mac Admin Community-Driven Preferences List:</strong></p><ul><li><a href="https://docs.google.com/spreadsheets/d/1ESX5td0y0OP3jdzZ-C2SItm-TUi-iA_bcHCBvaoCumw/edit?gid=0#gid=0" target="_blank" rel="noreferrer">View Google Doc</a></li></ul></li><li><p><strong>Microsoft Documentation for macOS Preferences:</strong></p><ul><li><a href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/deploy-preferences-for-office-for-mac" target="_blank" rel="noreferrer">General Plist Preferences</a></li><li><a href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/set-preference-per-app" target="_blank" rel="noreferrer">App-Specific Preferences</a></li><li><a href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/preferences-outlook" target="_blank" rel="noreferrer">Outlook Preferences</a></li><li><a href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/preferences-office" target="_blank" rel="noreferrer">Office Suite Preferences</a></li></ul></li></ul><p>These resources provide detailed <code>.plist</code> keys, values, and usage examples to help tailor your deployment.</p><hr><h3 id="_5-test-and-validate" tabindex="-1"><strong>5. Test and Validate</strong> <a class="header-anchor" href="#_5-test-and-validate" aria-label="Permalink to &quot;**5. Test and Validate**&quot;">​</a></h3><p>After deploying the <code>.plist</code> file, validate the configuration to ensure the settings were applied successfully:</p><ol><li><p><strong>Check Managed Preferences:</strong> On the target Mac, check for the applied configuration in:</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">/Library/Managed</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> Preferences/com.microsoft.Outlook.plist</span></span></code></pre></div></li><li><p><strong>Inspect Settings with <code>defaults</code>:</strong> Use the <code>defaults</code> command to verify the applied preference:</p><div class="language-bash vp-adaptive-theme"><button title="Copy Code" class="copy"></button><span class="lang">bash</span><pre class="shiki shiki-themes github-light github-dark vp-code" tabindex="0"><code><span class="line"><span style="--shiki-light:#6F42C1;--shiki-dark:#B392F0;">defaults</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> read</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> com.microsoft.Outlook</span><span style="--shiki-light:#032F62;--shiki-dark:#9ECBFF;"> PlayMyEmailsEnabled</span></span></code></pre></div></li><li><p><strong>Review Logs:</strong></p><ul><li><strong>Jamf Pro:</strong> Check the deployment status in the Jamf Pro dashboard.</li><li><strong>Intune:</strong> Review deployment reports in the <a href="http://intune.microsoft.com" target="_blank" rel="noreferrer">Intune Admin Center</a>.</li></ul></li></ol><hr><h3 id="_6-tips-for-success" tabindex="-1"><strong>6. Tips for Success</strong> <a class="header-anchor" href="#_6-tips-for-success" aria-label="Permalink to &quot;**6. Tips for Success**&quot;">​</a></h3><ul><li><strong>Microsoft Documentation:</strong> Always refer to Microsoft&#39;s official preference keys for Outlook on macOS. Example: <a href="https://learn.microsoft.com/en-us/microsoft-365-apps/mac/deploy-preferences-for-office-for-mac" target="_blank" rel="noreferrer">Office for Mac Preferences</a></li><li><strong>Test in Small Groups:</strong> Before deploying organization-wide, test profiles on a small group of devices to ensure compatibility.</li><li><strong>Bundle Identifier:</strong> Make sure the profile targets the correct app. For Outlook, the identifier is <code>com.microsoft.Outlook</code>.</li></ul><hr><h3 id="_7-troubleshooting-common-issues" tabindex="-1"><strong>7. Troubleshooting Common Issues</strong> <a class="header-anchor" href="#_7-troubleshooting-common-issues" aria-label="Permalink to &quot;**7. Troubleshooting Common Issues**&quot;">​</a></h3><p>Adding a troubleshooting section will help users address any common issues they might encounter when deploying <code>.plist</code> files with MDM.</p><ul><li><p><strong>Plist Not Applying:</strong></p><ul><li>Ensure that the <code>.plist</code> file is located in the correct directory (e.g., <code>/Library/Managed Preferences/</code> for MDM deployments).</li><li>Verify that the configuration profile is assigned to the correct target devices or users.</li></ul></li><li><p><strong>Outlook Settings Not Reflecting:</strong></p><ul><li>Use the <code>defaults</code> command to check if the setting has been applied. If not, ensure that the correct keys are being used in the <code>.plist</code>.</li><li>Check for conflicts with user-specific preferences located in <code>~/Library/Preferences/</code>.</li></ul></li><li><p><strong>MDM Sync Issues:</strong></p><ul><li>Ensure the device has checked in with the MDM server. You can force a sync from the <strong>Jamf Pro</strong> or <strong>Intune</strong> console or manually on the Mac.</li><li>Check MDM logs for any errors during profile deployment.</li></ul></li></ul><hr><h3 id="additional-resources-and-links" tabindex="-1"><strong>Additional Resources and Links</strong> <a class="header-anchor" href="#additional-resources-and-links" aria-label="Permalink to &quot;**Additional Resources and Links**&quot;">​</a></h3><ol><li><p><strong>Apple Developer Documentation:</strong></p><ul><li><a href="https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html" target="_blank" rel="noreferrer">Property List Programming Guide</a> This provides an in-depth understanding of <code>.plist</code> structure, serialization, and usage.</li></ul></li><li><p><strong>Jamf Pro Knowledge Base:</strong></p><ul><li><a href="https://jamf.com/resources/" target="_blank" rel="noreferrer">Jamf Pro Documentation</a> A great resource for learning more about Jamf Pro’s configuration profiles and the process for managing macOS devices.</li></ul></li><li><p><strong>Intune for Education Resources:</strong></p><ul><li><a href="https://learn.microsoft.com/en-us/mem/intune/" target="_blank" rel="noreferrer">Microsoft Intune Documentation</a> A comprehensive guide to managing Apple devices in Microsoft Intune.</li></ul></li><li><p><strong>Profile Creator Tool for macOS:</strong></p><ul><li><a href="https://github.com/ProfileCreator/ProfileCreator" target="_blank" rel="noreferrer">Profile Creator</a> An open-source tool for creating <code>.mobileconfig</code> profiles from <code>.plist</code> files.</li></ul></li><li><p><strong>Plist Editor Tools:</strong></p><ul><li><a href="https://www.fatcatsoftware.com/plisteditpro/" target="_blank" rel="noreferrer">PlistEdit Pro</a> A more advanced graphical tool for editing <code>.plist</code> files on macOS.</li></ul></li></ol>`,37)]))}const u=t(n,[["render",a]]);export{h as __pageData,u as default};
