# IV. Rooting

> [!IMPORTANT]
>
> ### केवल एक विधि का उपयोग करें।
>
> | [Magisk](#with-magisk) | [KernelSU](#with-kernelsu) |
> | :--------------------: | :------------------------: |

# With Magisk
### आपको जरूरत होगी

| सॉफ़्टवेयर | APKs |
| :------: | :--: |
| [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) | [Magisk Manager](https://github.com/topjohnwu/Magisk/releases/tag/v27.0) |
| [platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) | |

1. [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) फ़ोल्डर में कन्सोल खोलें
2. `python mtk r boot boot.img` को चलाएं। अपनी डिवाइस को बंद करें, **Vol+, Vol-** दोनों को दबाएं और डिवाइस को कंप्यूटर से जोड़ें।
3. एक `boot.img` फ़ाइल फ़ोल्डर में बनाई जाएगी। अपनी डिवाइस को चालू करें और फ़ाइल की कॉपी करें।
4. मैजिस्क मैनेजर apk फ़ाइल को डाउनलोड किये गए स्थान पर जाएं और इसे इंस्टॉल करें।
5. मैजिस्क मैनेजर खोलें और `Magisk` के पास स्थापना क्लिक करें।
<p align="center"><img src="https://i.imgur.com/CAbHxPv.png" width=400></p>

6. `फ़ाइल का चयन करें और पैच करें` का चयन करें। फ़ाइल पिकर खुलेगा, `boot.img` को खोजें और चयन करें। फिर `आइए चलें` टैप करें।
<img src="https://i.imgur.com/4m7CJfB.png" height=131.830985915></p>

7. जब आप इस स्क्रीन को देखते हैं, पैचिंग पूरी हो जाती है और आपको पैच की गई `.img फ़ाइल` का पथ दिया जाएगा। उस फ़ाइल को अपने कंप्यूटर में `platform-tools` फ़ोल्डर में कॉपी करें।  
   ![](https://i.imgur.com/D9qyjbGm.png)

8. अपने फ़ोन को अपने कंप्यूटर से जोड़ें और अपने फ़ोन पर usb debugging को सक्षम करें 
9. `platform-tools` फ़ोल्डर में एक कमांड प्रॉम्प्ट खोलें और कमांड `adb devices` चलाएं। अपने फ़ोन पर USB डीबगिंग को स्वीकार करें और `adb reboot bootloader` चलाएं। फ़ोन एक `fastboot_unlock_verify ok` स्क्रीन पर पुनः आरंभ होगा।
10. अब cmd में कमांड `fastboot flash boot <<मैजिस्क पैच की गई फ़ाइल का नाम टाइप करें.img>>` चलाएं और Enter दबाएं। सफलतापूर्वक स्थानांतरित होने के बाद, `fastboot reboot` चलाएं।
11. फ़ोन पुनः आरंभ हो जाएगा और आप अब मैजिस्क के साथ रूट किए गए हैं!
#### ध्यान दें कि स्थापना को पूरा करने के लिए आपको पुनरारंभ करने के लिए प्रॉम्प्ट मिलेगा।

### मैजिस्क रूट को हटाने के लिए, मैजिस्क मैनेजर ऐप में `Uninstall > Complete uninstall` का चयन करें।
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# With KernelSU
> [!WARNING]
> #### केवल कस्टम ROMs पर काम करता है (RealmeUI पर प्रयास न करें या यह आपके डिवाइस को ब्रिक कर देगा)

> [!IMPORTANT]
> #### KSU के साथ रूट करते समय जब आप फ़ोन को रिबूट करते समय अपने फ़ोन को प्लगड इन रखते हैं तो यह बूटलूप हो जाएगा और रिकवरी में जाएगा। रिबूट करने से पहले अपने फ़ोन को अनप्लग करें।

### आपको जरूरत होगी

| ZIP | APKs |
| :-: | :--: |
| [KernelSU ज़िप फ़ाइल](https://drive.google.com/file/d/1UUQe_5XH-9IBiz-SNp6I4fSyE1QQgtw4/view?usp=sharing) | [KernelSU मैनेजर (apk फ़ाइल)](https://github.com/tiann/KernelSU/releases/download/v0.7.6/KernelSU_v0.7.6_11458-release.apk) |

1.  ### रिकवरी मोड में होना आवश्यक है; `adb reboot recovery` चलाएं
2.  रिकवरी में `Apply update > Apply from ADB` का चयन करें और `adb sideload kernelsu.zip` चलाएं।

### यदि आपको "सिग्नेचर सत्यापन त्रुटि" मिलती है तो फिर भी जारी रखें, पैकेज फ्लैश हो जाएगा, इसका यही समान अन्य किसी भी ZIP के लिए भी है।

3. पूरा होने पर `Reboot system now` टैप करें। आपका फोन पुनः आरंभ होगा। KernelSu Manager apk फ़ाइल जोड़ने के स्थान पर जाएं और इसे इंस्टॉल करें।
4. ऐप इस प्रकार दिखना चाहिए जिससे सब कुछ सही तरीके से किया गया है:
<p align="center"><img src="https://i.imgur.com/XhOFSXP.png" height="700"></p>

5. यदि आप KernelSU रूट को हटाना चाहते हैं, तो आपको फ़्लैश करने के लिए डाउनलोड किए गए `custom-rom.zip` को निकालें, `boot.img` को खोजें और उसे वहां ले जाएं जहां एडबी है और निम्नलिखित कमांड प्रॉम्प्ट में इन कमांड्स को चलाएं:
   - `adb reboot bootloader`
   - `fastboot flash boot boot.img`