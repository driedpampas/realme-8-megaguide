> [!Warning]
> ## **अपने डिवाइस को ब्रिक होने से बचाने के लिए सभी चरणों को पढ़ें और करें।**

### वेबसाइट: [ऑनलाइन गाइड](dry.nl.eu.org/guide) 🥳 (विकी पोस्ट शामिल हैं)

### कोई सवाल? टेलीग्राम पर [रियलमी 8 AOSP](https://t.me/Realme8AOSPGroup) संदेश करें या एक नई [गिटहब चर्चा](https://github.com/driedpampas/realme-8-megaguide/discussions/new/choose) शुरू करें

### पहले से ही अनलॉक किया है? [कस्टम रिकवरी और रोम स्थापित करने](#iii-installing--a-custom-recovery-and-rom) पर जाएं

#### अस्वीकृति:
- कानून द्वारा परमिट किया जाने पर कोई वारंटी नहीं।
- समर्थित नहीं: विंडोज 7 (पुराना पायथन संस्करण) और RealmeUI 4 (lk मैथड पैच किया गया है)।

### चेतावनी: RUI4 पहले से ही अनलॉक किए जाने पर फास्टबूट एक्सेस को अक्षम कर देता है; समस्या हल होने तक RUI3 में अपग्रेड करें।

# दो तरीके हैं: mtkclient (नीचे स्क्रॉल करें) और [गहरी परीक्षण](/w-deep-testing.guide.md)।

# सामग्री सूची
0. [बैकअप](/guide.md#0-back-up-your-data)

I. [बूटलोडर को अनलॉक करना](/guide.md#i-unlocking)
1. [पूर्वापेक्षाएँ स्थापित करना](/guide.md#1-installing-prerequisites)
2. [RUI2 में डाउनग्रेड करें](/guide.md#2-downgrade-to-rui2)
3. [बूटलोडर को अनलॉक करना](/guide.md#3-unlocking-the-bootloader)
4. [RealmeUI 3 में अपग्रेड करें](/guide.md#4-upgrade-to-realmeui-3)

II. [पैचिंग `lk` - फास्टबूट एक्सेस प्राप्त करना और dm-verity और नारंजी स्थिति को हटाना](/guide.md#ii-patching-lk--qetting-fastboot-access-and-removing-dm-verity-and-orange-state-warnings--skip-only-if-you-unlocked-with-deep-testing)  
III. [कस्टम ROM स्थापित करना](/guide.md#iii-installing--a-custom-recovery-and-rom)  
IV. [रूट करना](/guide.md#iv-rooting)  
* * *

# 0. अपने सिस्टम पार्टीशन का बैकअप बनाएं
> [!CAUTION]
> # क्या आपने पहले से ही बैकअप बना लिया है? अगर नहीं, तो [Backup guide (in wiki)](https://github.com/driedpampas/realme-8-megaguide/wiki/Back-up-your-data) का पालन करें

# I. बूटलोडर को अनलॉक करना

# पूर्वापेक्षाएँ
| सॉफ़्टवेयर | ड्राइवर | फ़र्मवेयर |
|:-------: | :-----: | :------: |
| [Microsoft Store से Python](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5) | [मीडियाटेक USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) | [A.19 RUI2 फ़र्मवेयर](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link) |
| [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) | [USBDk](https://github.com/daynix/UsbDk/releases/download/v1.00-22/UsbDk_1.0.22_x64.msi) | [C.18 RUI3 फ़र्मवेयर](https://drive.google.com/file/d/1YHSIr4itg_5dPE2IbWAH9N8g6L5CGmaG/view?usp=drive_link) |
| [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) | |

## 1. पूर्वापेक्षाएँ स्थापित करना
1. ### मीडियाटेक USB
	1. [मीडियाटेक USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) ड्राइवर के फ़ोल्डर को निकालें और उसमें जाएं।
	2. **.inf** फ़ाइल को ढूंढें, उस पर दायाँ क्लिक करें और स्थापित करें
   <p align="center"><img src="https://i.imgur.com/niVRaOn.png"></p>
 3. ### [USBDk](https://github.com/daynix/UsbDk/releases/) को स्थापित करें
 4. ### [Microsoft Store से Python](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5) को स्थापित करें

## 2. RUI2 में डाउनग्रेड करें
1. [MTK Client archive](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) के फ़ोल्डर को निकालें और उसमें जाएं
2. [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) फ़ोल्डर में कंसोल खोलें
	<p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. आवश्यक लाइब्रेरी इस्तेमाल करने के लिए निम्नलिखित कमांड का उपयोग करें `python -m pip install -r requirements.txt`. यह काम इस तरह दिखेगा: 
	<p align="center"><img src="https://i.imgur.com/WSQsVj1.png"></p>
4. अपने फोन को बंद करें, दोनों **Vol+, Vol-** दबाएं और यूएसबी केबल को कनेक्ट करें। आपको कुछ इस प्रकार दिखेगा:
	<p align="center"><img src="https://i.imgur.com/lr7HIN0.png"></p>
5. फोन अब BROM मोड में है। [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) `flash_tool.exe` को चलाएं
6. `Options > Option...` पर क्लिक करें और सुनिश्चित करें कि सही **COM Port** का चयन किया गया है, UART सक्षम है और बौड दर को **921600** पर सेट किया गया है।
	<p align="center"><img src="https://i.imgur.com/hnMsyeN.png"></p>
7. [Haadi's A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtp

HgpyRDRHMZv13FTTvups/view?usp=share_link) को लोड करें
    <p align="center"><img src="https://i.imgur.com/VTwpXzC.png"></p>

<div align="center">
	<p><img src="https://i.imgur.com/sYaIBIN.png"></p><p>याद रखें कि:</p>
	
| opporeserve2 [साइन की गई पार्टीशन] | cdt_engineering [डिजिटल वारंटी कोड्स] |
| ------------------------------- | ---------------------------------------- |
| <img src="https://i.imgur.com/9Kp65P7.png" width="150"> | <img src="https://i.imgur.com/S6XOitJ.png" width="150"> |

</div><br>

> [!CAUTION]
>  9. **`केवल डाउनलोड`** मोड होने पर ध्यान दें या **आप महत्वपूर्ण पार्टीशन को खो देंगे**
	<p align="center"><img src="https://i.imgur.com/M3aUNBs.png" width="300"></p>
10. किसी भी चीज़ को खिसकने से बचें ताकि कुछ ना डिस्कनेक्ट हो। यह प्रक्रिया 15-20 मिनट तक चलेगी। A.19 को अपने फोन पर प्राप्त करने के लिए, `डाउनलोड` पर क्लिक करें।
	<p align="center"><img src="https://i.imgur.com/uSXflCJ.png" width="300"></p>
11. अगर सब कुछ ठीक हो जाता है, तो यह ऐसा दिखना चाहिए
	<p align="center"><img src="https://i.imgur.com/qeJWt3a.png" width="200"></p><br>
12. कुछ भी करने से पहले, हम **अपने फोन को सुरक्षित बनाने के लिए उसे वाइप करेंगे।** **Vol-, और पावर बटन** दोनों दबाएं, रिकवरी में डेटा को वाइप करें, और फिर **फॉर्मेट डेटा** का चयन करें।
 
## 3. बूटलोडर को अनलॉक करना
1. [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) फ़ोल्डर में कंसोल खोलें
2. अपने डिवाइस को रीबूट करें, इसे बंद करें और **दोनों Vol+, Vol-** दबाएं - **(कमांड पूरा होने तक बटन छोड़ने नहीं दें)**
3. `python mtk e metadata,userdata,md_udc` टाइप करें - यह कमांड आपके डेटा को मिटाता है। यह इस तरह दिखेगा:
   <p align="center"><img src="https://i.imgur.com/HfPsrpU.png"></p>
4. निम्नलिखित कमांड का उपयोग करके बूटलोडर को अनलॉक करें `python mtk da seccfg unlock`, उत्पाद निम्नलिखित दिखाई देगा
   <p align="center"><img src="https://i.imgur.com/Su8RtHk.png"></p>
 
> [!IMPORTANT]  
>   **इसके बाद, अपने फोन को चालू करें। पहला बूट लगभग 5-20 मिनट लगेगा।**
>   **आप `dm-verity corruption` और `orange state` चेतावनियाँ देखेंगे। जारी रखने के लिए *पावर बटन* दबाएं। ये सामान्य हैं और इसे बाद में पैच किया जाएगा।**

5. आपका बूटलोडर अब अनलॉक हो गया है।

### ❗ अगर कुछ काम नहीं कर रहा हो या आपके पास सवाल हो, तो [FAQ (अक्सर पूछे जाने वाले प्रश्न)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) की जांच करें

## 4. RealmeUI 3 में अपग्रेड करें

1. [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) के फ़ोल्डर में वापस जाएं
2. [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) फ़ोल्डर में फिर से कंसोल खोलें
   <p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. `python mtk payload` के साथ पेलोड भेजें। यह इस प्रकार दिखेगा: 
   <p align="center"><img src="https://i.imgur.com/WSQsVj1.png"></p>
   
4. यह सुनिश्चित करें कि आपका फोन बंद है, **Vol+, Vol-** दोनों दबाएं और यूएसबी केबल को कनेक्ट करें।
5. MTK Client को कुछ इस प्रकार आउटपुट करेगा:
   <p align="center"><

img src="https://i.imgur.com/lr7HIN0.png"></p>
   
6. फोन अब BROM मोड में है। [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) चलाएं -`flash_tool.exe`
7. `Options > Option...` पर क्लिक करें
8. सही **COM पोर्ट** चयनित है, UART सक्षम है और बॉड दर **921600** पर सेट किया गया है, सुनिश्चित करें।
   <p align="center"><img src="https://i.imgur.com/hnMsyeN.png"></p>
9. [SG का C.18 RUI3 Firmware](https://drive.google.com/file/d/1YHSIr4itg_5dPE2IbWAH9N8g6L5CGmaG/view?usp=drive_link) प्राप्त करें और इसे अनपैक करें
10. SG के फर्मवेयर से `MT6785_Android_scatter.txt` लोड करें
   <p align="center"><img src="https://i.imgur.com/8APQvkx.png"></p>

11. **`केवल डाउनलोड`** मोड होने पर ध्यान दें
    <p align="center"><img src="https://i.imgur.com/M3aUNBs.png" width="300"></p>

12. अपने फोन को स्थिर सतह पर रखें, कुछ ना डिस्कनेक्ट होने के लिए। यह प्रक्रिया 15-20 मिनट ले सकती है। अपने फोन पर C.18 प्राप्त करने के लिए, `डाउनलोड` पर क्लिक करें। [**कोई प्रगति नहीं? मुझे क्लिक करें**](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ)
    <p align="center"><img src="https://i.imgur.com/uSXflCJ.png" width="300"></p>
13. अगर सब कुछ ठीक हो जाता है, तो यह ऐसा दिखेगा:
    <p align="center"><img src="https://i.imgur.com/qeJWt3a.png" width="200"></p>

### ❗ अगर कुछ काम नहीं कर रहा हो या आपके पास सवाल हो, तो [FAQ (अक्सर पूछे जाने वाले प्रश्न)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) की जांच करें

14. आगे बढ़ने से पहले, **सुनिश्चित करें कि आपने अपडेट किया है / RUI3 C.18 फ्लैश किया है**
 
> [!IMPORTANT]
> ## Only continue after updating to / flashing RUI3 C.18

* * *
 
# II. Patching `lk`- getting fastboot access and removing dm-verity and orange state warnings
> [!NOTE]
> ### ❕ SKIP ONLY IF you unlocked with DEEP TESTING

1. Go back to the [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Open the console again in `MTK Client` folder
   <p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. Make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable.
4. Run  the command `python mtk r lk lk.bin`. There will now be a `lk.bin` file in **MTK Client** folder.
	<p align="center"><img src="https://i.imgur.com/gL4Qpc2.png"></p>
5. Go to this [website](https://lkpatcher.r0rt1z2.com/). Upload your lk.bin file and the `lk-patched.bin` will be downloaded. Move it to `MTK Client` folder. [**Check below if you get an error**](#if-you-get-this-error--could-not-find-the-lock-sequence-no-suitable-sequence-was-found)
	<p align="center"><img src="https://i.imgur.com/HOve3Mv.png"></p>
6. Run command `python mtk w lk lk-patched.bin`<br><br>

> [!IMPORTANT]
> ### Check [Manual patching](https://github.com/driedpampas/realme-8-megaguide/wiki/Patching-LK-(alternative-method)) if you have issues with the website

#### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ#4-i-patched-my-lk-but-the-phone-still-says-fastboot_verify_fail) if something does not work or you have questions

# III. Installing  a Custom Recovery and ROM

## Prerequisites
- [latest platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) - you will get an error `fastboot: usage: unknown reboot target recovery` if you use old platform-tools
- [QcomMtk-Driver](https://www.mediafire.com/file/nninaiiqy1e5csa/New+QcomMtk_Driver_Setup_V2.0.1.1_GsmMafia.Com.exe) - driver
- ❗️ If you get an error: `fastboot: usage: unknown reboot target recovery` try this adb installer [ADB and Fastboot ++](https://github.com/K3V1991/ADB-and-FastbootPlusPlus/releases/download/v1.0.8/ADB-and-Fastboot++_v1.0.8.exe)
- only flash once (you should not need to reflash it) - [vbmeta image](https://github.com/bengris32/releases/releases/download/arrow-1.1/vbmeta.img) - vbmeta.img file
- a custom rom package - check out the [Telegram group](https://t.me/Realme8AOSPGroup) for ROMs
- GAPPS package - recommended [MindTheGApps for Android 13](https://androidfilehost.com/?fid=4279422670115734716)
- check [recoveries](/recovery.md) for recovery images

## 1. Rebooting to fastboot
   ### Your device needs to be turned on
   1. Open a command prompt window in the **platform-tools** folder.
   2. **On your phone**, enable Developer Options and enable USB Debugging.
   3. In the platform-tools folder open a command prompt and run `adb devices`. You will see `Allow USB Debugging for ...` on phone, check `Always allow...` and hit `Allow`.
   4. In the command prompt run `adb reboot boootloader`. Phone will reboot to a screen that says `fastboot_unlock_verify ok`.

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

## 2. Installing custom recovery and sideloading custom rom

> [!TIP]
> #### ⚠️ If switching between custom roms skip step 2.
> #### ⚠️ If the required recovery has not changed you may skip step 3.
   
   1. Move the `recovery.img` and `vbmeta.img` files to the **platform-tools** folder.
   2. Run the command `fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img`. It should show 
		<p align="center"><img src="https://i.imgur.com/MZZyTBc.png"></p>
   3. Run the command `fastboot flash recovery recovery.img`:
		<p align="center"><img src="https://i.imgur.com/t7wYi3R.png"></p>
   #### The phone should show `USB Transmission ok`
   4. Now, reboot to recovery mode with the command `fastboot reboot recovery` 
		<p align="center"><img src="https://i.imgur.com/1zwXUmj.png"></p>
   5. In recovery, go to `Factory reset > Format data/factory reset > Format data`. **After** factory reset go back and select `Apply update > Apply from ADB`. You should see this when running `adb devices`:
 		<p align="center"><img src="https://i.imgur.com/MoiIS9k.png"></p>
   6. Now run the command `adb sideload custom-rom.zip` (replace *custom-rom.zip* with custom rom package name). For example I flashed LeafOS 2:
		<p align="center"><img src="https://i.imgur.com/QZqi1e1.png"></p>
   7. **ONLY** do this step on custom roms **WIHTOUT GAPPS / GMS** (check the rom's description to check). Select `Apply update > Apply from ADB` again and run `adb sideload gapps.zip` (replace *gapps.zip* with package name). 
		<p align="center"><img src="https://i.imgur.com/DUEMXrn.png"></p>
   #### If you get a "Signature verification error" on your phone, click `Yes` to continue anyways, this goes the same to any other ZIPs you flash.
   9. Once finished, in the recovery go back to `Reboot system now`. The phone will reboot into your Custom ROM.

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

# IV. Rooting 
## Go to [Rooting.md](/rooting.md)  
* * *
## More in [WIKI](https://github.com/driedpampas/realme-8-megaguide/wiki)
## Special thanks & credits
 
> [Ben](https://github.com/bengris32/android_kernel_realme_mt6785) - Made everything possible by making the kernel for Realme 8  
> [bkerler](https://twitter.com/viperbjk) - developer of [MtkClient](https://github.com/bkerler/mtkclient)  
> [Roger](https://t.me/R0rt1z2) - creator of [lkpatcher](https://github.com/R0rt1z2/lkpatcher)  
> [Haadi](https://t.me/Haadi786H) - RUI2 firmware  
> [SGtriangle](https://t.me/SGtriangle) - RUI3 firmware  
> [HowWof](https://t.me/HowWof) - A lot of help, Leaf OS 2 for RMX3085 developer  
> [Ripper_Hybrid](https://t.me/Ripper_Hybrid) - provided KSU zip file, helped with wiki guides  
> [MrPotato6](https://t.me/MrPotato6) - Info and screenshots for Magisk rooting<br>
> [Nand kumar](https://forum.xda-developers.com/m/nand-kumar.8476267/) - original poster of backup guide  
> [Zako Chan](https://t.me/zakolakov106/) - Information about walkthrough with downgrade  
> [Tony stark](https://forum.xda-developers.com/m/tony-stark.7582728/) - [RUI2 unlock guide](https://forum.xda-developers.com/t/guide-realme-8-unofficial-new-method-unlock-bootloader-flash-twrp-and-root-rmx3085.4386473/)  
> [Original Custom ROM Guide](https://telegra.ph/Flash-LineageOS-on-Realme-8-06-05)  
> [Magisk & Developers](https://github.com/topjohnwu/Magisk)  
> [KernelSU & Developers](https://github.com/tiann/KernelSU)  
> Banner and others via [Canva](https://canva.com) - Refer to [Canva's CLA](https://www.canva.com/policies/content-license-agreement/) for more info  
> Text images made in [Drawing](https://maoschanz.github.io/drawing)  

> Support in: [Realme 8 AOSP](https://t.me/Realme8AOSPGroup)
 
Witten by [me](https://dry.nl.eu.org/links) with 🫶.

* * *

###### There is NO WARRANTY, to the extent permitted by law.
###### Guide and Wiki (c) by @driedpampas, 2023-2024
###### guide.md | Licensed under CC-BY-SA 4.0. Check [license](/LICENSE) for more information.
