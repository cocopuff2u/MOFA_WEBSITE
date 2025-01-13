# 📱 Prebuilt Mobile Configurations

> [!CAUTION]  
> 💡 **Under Construction!**  
> The content on this page is still being developed and is not yet final. Please check back later for updates. 🔨

Welcome to the **Prebuilt Mobile Configurations** page! 🌐 Here, you'll find ready-to-use **mobileconfig** files for managing Microsoft Office products (such as Word, Excel, PowerPoint, and Teams) on macOS devices 🍏. These configurations are designed for easy deployment, enabling efficient management of Office settings across enterprise environments. You can upload these configurations to your MDM either by directly using the **mobileconfig** files or by copying the contents and uploading them as custom configurations. ⚙️

## 📂 Prebuilt Config Files

The following **mobileconfig** files are available for download. These files help you manage various settings within Microsoft Office products, such as activation, Teams configurations, and Outlook preferences. 📑

- **[Microsoft Office Activation](#)**  
  A mobileconfig file to automatically activate Microsoft Office apps on macOS devices, streamlining the process without requiring manual input. ✅

- **[Teams Configuration](#)**  
  A configuration to manage Microsoft Teams settings, including auto-login and startup preferences. 💬

- **[Outlook Configuration](#)**  
  A file for setting up email accounts, syncing calendars, and enforcing security policies in Microsoft Outlook. 📧

## 💻 Example File  
Let’s take a closer look at how one of these **mobileconfig** files is structured and what each section does. Below is an example of the **`mau_autoupdate_4_day.mobileconfig`** file for the **Microsoft Auto Update application**. 🔄

### 🧩 Structure Overview

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
    <dict>
        <key>HowToCheck</key>
        <string>AutomaticDownload</string>
        <key>ChannelName</key>
        <string>Current</string>
        <key>StartDaemonOnAppLaunch</key>
        <true/>
        <key>UpdateCheckInterval</key>
        <integer>240</integer>
        <key>UpdateDeadline.StartAutomaticUpdates</key>
        <integer>3</integer>
        <key>UpdateDeadline.FinalCountDown</key>
        <integer>60</integer>
        <key>Applications</key>
        <dict>
            <key>/Applications/Microsoft Excel.app</key>
            <dict>
                <key>Application ID</key>
                <string>XCEL2019</string>
                <key>UpdateDeadline.DaysBeforeForcedQuit</key>
                <integer>4</integer>
            </dict>
            <key>/Applications/Microsoft PowerPoint.app</key>
            <dict>
                <key>Application ID</key>
                <string>PPT32019</string>
                <key>UpdateDeadline.DaysBeforeForcedQuit</key>
                <integer>4</integer>
            </dict>
        </dict>
    </dict>
</plist>
```

*Please note that this file has been simplified for illustrative purposes.* ✍️

## 🔑 Key Sections

For more detailed information about the Microsoft Auto Update settings, refer to the official documentation [here](https://docs.microsoft.com/en-us/microsoft-365/admin/update/update-office-for-mac). 📚

1. **HowToCheck**  
   Specifies the method used to check for updates. The default value is `AutomaticDownload`, with the alternative option being `AutomaticCheck`. In this case, `AutomaticDownload` ensures updates are both downloaded and installed automatically. 📥

   ![HowToCheck Example](#)

2. **ChannelName**  
   Defines the update channel for the application. The default value is `Current`, with other options including `Beta`, `CurrentThrottle`, `Custom`, and `Preview`. Here, `Current` specifies that the current production channel is used for updates. 📡

   ![ChannelName Example](#)

3. **StartDaemonOnAppLaunch**  
   Ensures the update daemon starts automatically when the associated Office application is launched. The default value is `true`, with the option to set it to `false`. 🚀

4. **UpdateCheckInterval**  
   Determines the interval (in minutes) between update checks. The default value is `780` (13 hours), but any value can be set depending on your requirements. In this example, it’s set to `240` minutes (4 hours). ⏰

5. **UpdateDeadline.StartAutomaticUpdates**  
   Specifies the time (in hours) before automatic updates begin. The default value is `3`, but it can be set to any value greater than `3`. Here, it is set to `3` hours. 🕒

6. **UpdateDeadline.FinalCountDown**  
   Defines the countdown time (in minutes) before a forced quit is initiated. The default value is `60`, with a valid range between `10` and `720`. In this example, it’s set to `60` minutes (1 hour) before a forced shutdown occurs. ⏳

7. **Applications**  
   This section specifies the applications configured for updates, along with their respective settings:  
   - **Microsoft Excel**: 
     - **Application ID**: `XCEL2019`
     - **Update Deadline**: Forced quit occurs after `4` days of pending updates. 📊
   - **Microsoft PowerPoint**:  
     - **Application ID**: `PPT32019`
     - **Update Deadline**: Forced quit occurs after `4` days of pending updates. 📽️

## 🛠️ Customizing Configs

Each application may have unique formatting and spacing requirements for configuration files. To simplify the process, you can use specialized tools or edit unsigned **mobileconfig** files directly with an advanced text editor like Visual Studio Code for quick adjustments. 📝

Alternatively, you can use the application itself to configure settings, then locate and convert the corresponding **plist** file into a **mobileconfig** for deployment.  

#### 🔄 Step-by-Step Guide:  

1. **Open the Application**  
   Launch the application you want to configure. 💻

2. **Adjust Settings**  
   Navigate to the preferences or settings section and make the desired changes. ⚙️

3. **Locate the Generated plist**  
   After saving your settings, find the **plist** file containing the configuration you just set. Common locations include:  
   - `/Library/Preferences/` 📂
   - `/Users/<username>/Library/Preferences/` 📁

4. **Convert the plist to a mobileconfig**  
   - Open the **plist** file with tools like **ProfileCreator** or **iMazing**. 🔧  
   - Modify additional settings, metadata, or organizational details as necessary. 🛠️  
   - Export the file as a **mobileconfig** for deployment. 📤

This approach takes advantage of the app’s native configuration options, ensuring accuracy and compatibility when pushing settings via an MDM solution. 🔄

## 🧰 Tools for Configs

Here are some excellent tools to help you create custom configuration profiles from scratch or fine-tune existing ones with ease:

1. **Apple Configurator 2**  
   A user-friendly tool for creating and managing configuration profiles. Ideal for organizations using Apple devices. 🍏

2. **ProfileCreator**  
   A free, open-source macOS application designed specifically for building and editing configuration profiles. 🆓

3. **Visual Studio Code**  
   A powerful code editor that can be used to edit unsigned **mobileconfig** files. You can open an unsigned **mobileconfig** file directly in Visual Studio Code, make adjustments, and save your changes. This method is especially helpful for fine-tuning configurations or fixing issues in existing files. 💻

4. **Plist Editor Pro**  
   A specialized tool for working with property list files (`.plist`), which form the basis of **mobileconfig** files. 📂

5. **MCXToProfile**  
   A command-line tool that converts older MCX settings into modern configuration profiles. 🖥️

6. **iMazing**  
   A versatile tool for managing Apple devices, including creating, editing, and deploying configuration profiles. Its intuitive interface makes it easy to create custom **mobileconfig** files without requiring extensive technical knowledge. 📲

## 🚀 Uploading Configs

Once you’ve selected or customized a **mobileconfig** file for your environment, you can upload it to your Mobile Device Management (MDM) system for deployment. There are two primary methods for uploading configuration profiles: directly using the **mobileconfig** file or uploading it as a custom configuration.

### 📤 Upload via MobileConfig File

1. **Prepare the MobileConfig File**  
   Ensure that your **mobileconfig** file is ready and saved on your local machine. 💾

2. **Log into your MDM**  
   Access your MDM platform's administrative console (such as Jamf Pro, Intune, or another MDM solution). 🔐

3. **Upload the File**  
   Follow the steps provided by your MDM to upload the **mobileconfig** file. This typically involves navigating to a section for device profiles or configuration profiles and selecting the option to upload a file. Choose the **mobileconfig** file from your local storage. 📂

4. **Assign the Profile to Devices**  
   Once uploaded, assign the configuration profile to the appropriate device groups or individual devices within your MDM platform. Make sure the devices are registered and enrolled in the MDM system before deployment. 📱

5. **Deploy the Profile**  
   After assignment, deploy the configuration to the selected devices. The devices will receive the profile automatically once they sync with the MDM. 🌐

### ⚙️ Upload as a Custom Configuration

Alternatively, you can upload the configuration file as a custom profile in your MDM:

1. **Convert the File (if needed)**  
   If you have a **plist** file or need to make adjustments to your **mobileconfig** file, you can convert it using tools like **ProfileCreator** or **iMazing**. 🔄

2. **Access Custom Configuration Section**  
   In your MDM platform, navigate to the section for custom configurations or profiles. 📋

3. **Create a Custom Profile**  
   Create a new custom configuration profile, and paste the contents of your **mobileconfig** file into the relevant field. Depending on your MDM, this may involve directly inputting the XML content or importing the entire file. ⚙️

4. **Assign and Deploy**  
   As with the standard **mobileconfig** upload, assign the custom configuration to the target devices and deploy it as necessary. 📡