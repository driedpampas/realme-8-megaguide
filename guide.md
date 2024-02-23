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
> ## केवल तभी जारी रखें जब आप RUI3 C.18 को अपडेट कर लेते हैं / फ़्लैश कर लेते हैं

* * *
 
# II. `lk` को पैच करना - फास्टबूट एक्सेस प्राप्त करना और dm-verity और नारंगी स्थिति चेतावनियाँ हटाना
> [!NOTE]
> ### ❕ केवल तभी छोड़ें अगर आपने गहरी जांच के साथ अनलॉक किया है

1. [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) फ़ोल्डर में वापस जाएं
2. `MTK Client` फ़ोल्डर में फिर से कंसोल खोलें
   <p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. सुनिश्चित करें कि आपका फोन बंद है, **Vol+, Vol-** दोनों दबाएं और यूएसबी केबल को कनेक्ट करें।
4. कमांड `python mtk r lk lk.bin` चलाएं। अब **MTK Client** फ़ोल्डर में एक `lk.bin` फ़ाइल होगी।
	<p align="center"><img src="https://i.imgur.com/gL4Qpc2.png"></p>
5. [इस वेबसाइट](https://lkpatcher.r0rt1z2.com/) पर जाएं। अपनी lk.bin फ़ाइल अपलोड करें और `lk-patched.bin` डाउनलोड किया जाएगा। इसे `MTK Client` फ़ोल्डर में ले जाएं। [**अगर आपको यह त्रुटि मिलती है तो नीचे देखें**](#if-you-get-this-error--could-not-find-the-lock-sequence-no-suitable-sequence-was-found)
	<p align="center"><img src="https://i.imgur.com/HOve3Mv.png"></p>
6. कमांड `python mtk w lk lk-patched.bin` चलाएं<br><br>

> [!IMPORTANT]
> ### [FAQ (अक्सर पूछे जाने वाले प्रश्न)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ#4-i-patched-my-lk-but-the-phone-still-says-fastboot_verify_fail) की जाँच करें अगर कुछ काम नहीं कर रहा है या आपके पास सवाल हैं

# III. कस्टम रिकवरी और ROM का स्थापना

## पूर्वापेक्षित आवश्यकताएँ
- [नवीनतम platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) - यदि आप पुराने platform-tools का उपयोग करते हैं, तो आपको त्रुटि मिलेगी `fastboot: usage: unknown reboot target recovery`
- [QcomMtk-Driver](https://www.mediafire.com/file/nninaiiqy1e5csa/New+QcomMtk_Driver_Setup_V2.0.1.1_GsmMafia.Com.exe) - ड्राइवर
- ❗️ यदि आपको त्रुटि मिलती है: `fastboot: usage: unknown reboot target recovery`, तो यह adb स्थापक का उपयोग करें [ADB and Fastboot ++](https://github.com/K3V1991/ADB-and-FastbootPlusPlus/releases/download/v1.0.8/ADB-and-Fastboot++_v1.0.8.exe)
- केवल एक बार फ्लैश करें (आपको पुनः फ्लैश करने की आवश्यकता नहीं होनी चाहिए) - [vbmeta छवि](https://github.com/bengris32/releases/releases/download/arrow-1.1/vbmeta.img) - vbmeta.img फ़ाइल
- एक कस्टम रोम पैकेज - ROMs के लिए [टेलीग्राम समूह](https://t.me/Realme8AOSPGroup) की जांच करें
- GAPPS पैकेज - Android 13 के लिए अनुशंसित [MindTheGApps](https://androidfilehost.com/?fid=4279422670115734716)
- रिकवरी छवियों की जांच करें [/recovery.md](/recovery.md) के लिए

## 1. फास्टबूट में पुनरावर्तन करना
   ### आपके डिवाइस को चालू होना चाहिए
   1. **platform-tools** फ़ोल्डर में एक कमांड प्रोम्प्ट विंडो खोलें।
   2. **अपने फोन** पर, Developer Options को सक्षम करें और USB Debugging को सक्षम करें।
   3. platform-tools फ़ोल्डर में एक कमांड प्रोम्प्ट खोलें और `adb devices` चलाएं। फोन पर `Allow USB Debugging for ...` दिखाई देगा, `Always allow...` की जाँच करें और `Allow` दबाएं।
   4. कमांड प्रोम्प्ट में `adb reboot boootloader` चलाएं। फोन त्वरितबूट एंड अनलॉक वेरिफाई ok लिखा होगा।

### ❗ यदि कुछ काम नहीं कर रहा है या आपके पास सवाल हैं तो [FAQ (अक्सर पूछे जाने वाले प्रश्न)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) की जाँच करें

## 2. कस्टम रिकवरी स्थापना और कस्टम रोम को साइडलोड करना

> [!TIP]
> #### ⚠️ कस्टम रोम्स के बीच स्विच करने पर चरण 2 को छोड़ें।
> #### ⚠️ यदि आवश्यक रिकवरी नहीं बदली है तो आप चरण 3 को छोड़ सकते हैं।
   
   1. `recovery.img` और `vbmeta.img` फ़ाइलों को **platform-tools** फ़ोल्डर में ले जाएं।
   2. कमांड चलाएं `fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img`। यह दिखाई देना चाहिए
		<p align="center"><img src="https://i.imgur.com/MZZyTBc.png"></p>
   3. कमांड

 चलाएं `fastboot flash recovery recovery.img`:
		<p align="center"><img src="https://i.imgur.com/t7wYi3R.png"></p>
   #### फोन पर `USB Transmission ok` दिखना चाहिए
   4. अब, कमांड चलाएं `fastboot reboot recovery` स्थानीय मोड में बूट करें
		<p align="center"><img src="https://i.imgur.com/1zwXUmj.png"></p>
   5. रिकवरी में, `Factory reset > Format data/factory reset > Format data` पर जाएं। फैक्टरी रीसेट के बाद `Apply update > Apply from ADB` चुनें। आपको यह दिखाई देना चाहिए जब `adb devices` चलाएं:
 		<p align="center"><img src="https://i.imgur.com/MoiIS9k.png"></p>
   6. अब कमांड चलाएं `adb sideload custom-rom.zip` (*custom-rom.zip* को कस्टम रोम पैकेज नाम के साथ बदलें)। उदाहरण के लिए मैंने LeafOS 2 को फ्लैश किया:
		<p align="center"><img src="https://i.imgur.com/QZqi1e1.png"></p>
   7. **केवल** इस स्टेप को कस्टम रोम्स **बिना GAPPS / GMS** पर करें (रोम का विवरण जांचने के लिए)। पुनः `Apply update > Apply from ADB` चुनें और `adb sideload gapps.zip` (*gapps.zip* के साथ पैकेज नाम को बदलें)। 
		<p align="center"><img src="https://i.imgur.com/DUEMXrn.png"></p>
   #### यदि आपको अपने फोन पर "हस्ताक्षर सत्यापन त्रुटि" मिलती है, तो `हां` पर क्लिक करें ताकि आगे बढ़ सकें, यह अन्य किसी भी अन्य ZIP के लिए भी लागू होता है।
   9. पूरा होने के बाद, रिकवरी में वापस जाएं `Reboot system now`। फोन आपके कस्टम रोम में बूट हो जाएगा।

### ❗ यदि कुछ काम नहीं कर रहा है या आपके पास सवाल हैं तो [FAQ (अक्सर पूछे जाने वाले प्रश्न)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) की जाँच करें

# IV. रूट करना 
## [Rooting.md](/rooting.md) पर जाएं
* * *
## और [विकि](https://github.com/driedpampas/realme-8-megaguide/wiki) में अधिक
## विशेष धन्यवाद और स्रोत
 
> [Ben](https://github.com/bengris32/android_kernel_realme_mt6785) - रियलमी 8 के लिए कर्नल बनाने के द्वारा सभी कुछ संभव बनाया  
> [bkerler](https://twitter.com/viperbjk) - [MtkClient](https://github.com/bkerler/mtkclient) के डेवलपर  
> [Roger](https://t.me/R0rt1z2) - [lkpatcher](https://github.com/R0rt1z2/lkpatcher) के निर्माता  
> [Haadi](https://t.me/Haadi786H) - RUI2 फर्मवेयर  
> [SGtriangle](https://t.me/SGtriangle) - RUI3 फर्मवेयर  
> [HowWof](https://t.me/HowWof) - बहुत सारी सहायता, RMX3085 डेवलपर के लिए लीफ ओएस 2  
> [Ripper_Hybrid](https://t.me/Ripper_Hybrid) - KSU ज़िप फ़ाइल प्रदान की, विकि गाइड के साथ मदद की  
> [MrPotato6](https://t.me/MrPotato6) - मैजिस्क रूटिंग के लिए जानकारी और स्क्रीनशॉट  
> [Nand kumar](https://forum.xda-developers.com/m/nand-kumar.8476267/) - बैकअप गाइड के मूल पोस्टर  
> [Zako Chan](https://t.me/zakolakov106/) - डाउनग्रेड के साथ चलन के बारे में जानकारी  
> [Tony stark](https://forum.xda-developers.com/m/tony-stark.7582728/) - [RUI2 अनलॉक गाइड](https://forum.xda-developers.com/t/guide-realme-8-unofficial-new-method-unlock-bootloader-flash-twrp-and-root-rmx3085.4386473/)  
> [Original Custom ROM Guide](https://telegra.ph/Flash-LineageOS-on-Realme-8-06-05)  
> [Magisk & Developers](https://github.com/topjohnwu/Magisk)  
> [KernelSU & Developers](https://github.com/tiann/KernelSU)  
> बैनर और अन्य कैनवा के माध्यम से - अधिक जानकारी के लिए [कैनवा का CLA](https://www.canva.com/policies/content-license-agreement/) देखें  
> टेक्स्ट छवियों बनाई गई [ड्रॉइंग](https://maoschanz.github.io/drawing) में  

> समर्थन: [Realme 8 AOSP](https://t.me/Realme8AOSPGroup)
 
[मैं](https://dry.nl.eu.org/links) द्वारा लिखा गया 🫶 के साथ।

* * *
###### इसके अधिकांश की नो वारंटी, जितनी कानून द्वारा प्राप्त होती है।
###### गाइड और विकि (c) द्वारा @driedpampas, 2023-2024
###### guide.md | CC-BY-SA 4.0 के तहत लाइसेंस प्राप्त करें। अधिक जानकारी के लिए [लाइसेंस](/LICENSE) की जाँच करें।