# 📱 Preconfigured Profiles

Welcome to the **Preconfigured Profiles** page! 🌐 Here, you will find a collection of ready-to-use **mobileconfig** files designed to simplify the management of Microsoft Office products on macOS devices 🍏. These profiles are crafted for seamless deployment, allowing you to efficiently configure Office settings across your enterprise environment. Whether you choose to upload the **mobileconfig** files directly to your MDM 📤 or copy the contents to create custom configurations 📝, the process is straightforward and hassle-free. ⚙️

Below, you'll find a list of available **mobileconfig** files for download. 📑

## 🔄 Microsoft AutoUpdate
**Preferences Domain: `com.microsoft.autoupdate2`** 🖥️

This section provides configuration profiles to enforce Microsoft AutoUpdate (MAU) settings for macOS. These profiles apply a global **3-day**, **7-day**, or **14-day** forced update policy for Microsoft apps such as Word, Excel, PowerPoint, and Teams.  

Key settings include:  
- **Update Channel:** Current 🔄  
- **Automatic Downloads:** Enabled 📥  
- **Update Initiation:** Begins after 3/7/14 days ⏳  
- **Forced Quit Countdown:** 60 minutes ⏰  
- **Update Check Frequency:** Every 360 minutes 🔍  

#### Configuration Profiles 🛠️  
- [**3-Day Forced Update**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_3day_update_v1.mobileconfig) ⏳  
- [**7-Day Forced Update**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_7day_update_v1.mobileconfig) 📅  
- [**14-Day Forced Update**](https://github.com/cocopuff2u/MOFA/blob/main/mobileconfig_profiles/MOFA_mau_14day_update_v1.mobileconfig) 📆  

<i><small>To download a configuration, click the link and select “Download Raw File.”</small></i> ✅

## 📱 How a **mobileconfig** works?  
Click [here](/macos_tools/profile_breakdown) to get the breakdown and understand its structure!