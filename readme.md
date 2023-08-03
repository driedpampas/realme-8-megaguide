<div align="center">
	
<H1>Realme 8 MEGAGUIDE</H1>

</div>

# Disclaimer

- This method will **wipe your phone** and **temporarily downgrade your phone to RUI2**
- **Read this tutorial step by step to don't miss anything.**
- This method doesn't use **Deep Test**
- I used this method on [my](t/me.driedpampas) own device so I can confirm it works. Others have also used this method.

<p align="center" style="color: red;">Use this tutorial <b>only with RUI3</b></p>

<hr>

# Table of Contents

1. [Installing Prerequisites](#1-installing-prerequisites)
2. [Downgrade to RUI2](#2-downgrade-to-rui2)
3. [Unlocking the bootloader - MTK Client](#3-unlocking-the-bootloader---mtk-client)
4. [Upgrade to RealmeUI 3](#4-upgrade-to-realmeui-3)
5. [EXTRA: Getting fastboot access](#extra-getting-fastboot-access)
6. [EXTRA: Installing a Custom ROM](#extra-installing--a-custom-rom)
7. [EXTRA: Rooting](#extra-rooting-i-used-lineage-os-200-for-this)

# Prerequisites
- [USB2SER](https://drive.google.com/file/d/1_SWiU9Ip9-sf8D-7VVIxcfXUpjsKlAdz/view?usp=drive_link)
- [USBDk](https://github.com/daynix/UsbDk/releases/latest)
- [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)
- [MTK Client archive](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
- [SP Flash tool](https://drive.google.com/file/d/1McZ11On8XbxGgE-hMA_nZqErHI_QwjQT/view?usp=sharing)
- [A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link)
- [C.14 RUI3 Firmware](https://drive.google.com/file/d/1JezJL-mz8fJC0lkNGMNyQiGCNYxj-pKs/view?usp=share_link)

- A functioning brain and a emotional support after the unlock

# 1. Installing prerequisites
1. ## USB2SER
	1. **Extract** and enter the folder of [USB2SER](https://drive.google.com/file/d/1_SWiU9Ip9-sf8D-7VVIxcfXUpjsKlAdz/view?usp=drive_link) driver.
	2. Find the **.inf** file, right click and press install
   <p align="center"><img src="https://i.imgur.com/BZxtj6B.png"></p>

 3. ## Install [USBDk](https://github.com/daynix/UsbDk/releases/)
 4. ## Install [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)

# 2. Downgrade to RUI2
1. **Extract** and enter the folder of [MTK Client archive](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
2. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder, **a tip how to do it faster below**
   <p align="center"><img src="https://i.imgur.com/J5VAWoy.png"></p>
3. Get the needed libraries using command `python -m pip install -r requirements.txt`. 3. Send the payload with `python mtk payload`. It should look like this: 
   <p align="center"><img src="https://i.imgur.com/cASEARQ.png"></p>
   
4. Make sure your phone is powered off, hold down **Vol+, Vol-, and power button** and connect the usb cable.
5. MTK Client should output something like this:
      <p align="center"><img src="https://i.imgur.com/KDp2u5O.png"></p>
   
6. The phone is now in BROM mode. Run the [SP Flash tool](https://drive.google.com/file/d/1sfsm3EXhIf8TrS5Y-En1mifgg8e9VjXl/view?usp=drive_link) `flash_tool.exe`
7. Click on `Options > Option...`
8. Make sure the right **COM Port** is selected, UART enabled and baud rate is set to **921600**.
   <p align="center"><img src="https://i.imgur.com/C6n8awx.png"></p>
  
9. Get [Haadi's A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link) and unpack it
   
10. Load `scatter.txt` from Haadi's Firmware
    <p align="center"><img src="https://i.imgur.com/Tzavwau.png"></p>

<div align="center">
<p><img <img src="https://i.ibb.co/bgnMVdM/Caje-RNwf-OCt-Vb-DZ.png"></p><p>Remember to uncheck:</p>
	
| opporeserve2 [Signed partition] | cdt_engineering [Digital warranty codes] |
| ------------------------------- | ---------------------------------------- |
| <img src="https://i.imgur.com/sIiT7t8.png"> | <img src="https://i.imgur.com/wfAfnCn.png"> |

</div><br>

11. Remember to have `Download Only` mode
    <p align="center"><img src="https://i.imgur.com/0xFJVuo.png"></p>
12. Avoid moving your phone so as to not disconnect anything. This process will take up to 15-20 minutes. To get A.19 on your phone, click `Download`.
    <p align="center"><img src="https://i.imgur.com/tJiKdLf.png"></p>
13. If everything goes well, it should look like this
    <p align="center"><img src="https://i.imgur.com/QhJ6fVi.png"></p><br>

14. Before doing anything, we'll **WIPE the phone for safety.** Hold down **Vol-, and power button**, In recovery select wipe data, and then select **Format Data**.

# 3. Unlocking the bootloader - MTK Client
1. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Reboot your device, turn it off and Hold down **Vol+, Vol-, and power button** - **(Don't leave the buttons until the bypass is done)**
3. Type `python mtk e metadata,userdata,md_udc` - This command wipes your data. It should look like this:
   <p align="center"><img src="https://i.imgur.com/olGdWYp.png"></p>
4. Unlock the bootloader using command `python mtk da seccfg unlock`, the output should look like this
   <p align="center"><img src="https://i.imgur.com/qezn6Af.png"></p>
      
   **After this, turn on your phone. First boot will take up to 5-20 minutes. Don't panic.**

   ### ❗️ When you boot your device, you will see `dm-verity corruption / This device is corrupt and cannot be trusted` THIS IS COMPLETELY NORMAL, PRESS POWER BUTTON TO CONTINUE - be quick, the phone will turn off automatically in 5 seconds (this will show up at every boot)<br>
   ### If bootloader is unlocked, there also will be a 5-second orange-state indicator [**¹**](#-more-info-on-the-orange-state-indicator-and-other-indicators)

5. Your bootloader is now unlocked.

# 4. Upgrade to RealmeUI 3

1. Go back to the folder of [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
2. Open the console again in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder, **a tip how to do it faster below**
   <p align="center"><img src="https://i.imgur.com/J5VAWoy.png"></p>
3. Send the payload with `python mtk payload`. It should look like this: 
   <p align="center"><img src="https://i.imgur.com/Y2mwRhR.png"></p>
   
4. Make sure your phone is powered off, hold down **Vol+, Vol-, and power button** and connect the usb cable.
5. MTK Client should output something like this:
      <p align="center"><img src="https://i.imgur.com/KDp2u5O.png"></p>
   
6. The phone is now in BROM mode. Run the [SP Flash tool](https://drive.google.com/file/d/1sfsm3EXhIf8TrS5Y-En1mifgg8e9VjXl/view?usp=drive_link) [flash_tool.exe]
7. Click on `Options > Option...`
8. Make sure the right **COM Port** is selected, UART enabled and baud rate is set to **921600**.
   <p align="center"><img src="https://i.imgur.com/C6n8awx.png"></p>
9. Get [Haadi's C.14 RUI3 Firmware](https://drive.google.com/file/d/1JezJL-mz8fJC0lkNGMNyQiGCNYxj-pKs/view?usp=share_link) and unpack it
10. Load `MT6785_scatter.xml` from Haadi's Firmware
    <p align="center"><img src="https://i.imgur.com/Tzavwau.png"></p>

<div align="center">
<p><img <img src="https://i.ibb.co/bgnMVdM/Caje-RNwf-OCt-Vb-DZ.png"></p><p>Remember to uncheck:</p>
	
| opporeserve2 [Signed partition] | cdt_engineering [Digital warranty codes] |
| ------------------------------- | ---------------------------------------- |
| <img src="https://i.imgur.com/sIiT7t8.png"> | <img src="https://i.imgur.com/wfAfnCn.png"> |

</div><br>
	
11. Remember to have `Download Only` mode
    <p align="center"><img src="https://i.imgur.com/0xFJVuo.png"></p>
12. Place your phone on a stable surface, to not disconnect anything. This process will take up to 15-20 minutes. To get C.14 on your phone, click `Download`
    <p align="center"><img src="https://i.imgur.com/tJiKdLf.png"></p>
13. If everything goes well, it should look like this:
    <p align="center"><img src="https://i.imgur.com/QhJ6fVi.png"></p>
   ### If you click download but there is no progress go to `Options > Option > General` and untick `Storage Life Cycle Check`

14. Before continuing, you'll need to **WIPE the phone for safety.** Hold down **Vol-, and power button**, In recovery select wipe data, and then select **Format Data**.
15. ## Go into Settings and update to C.18

<p align="center">Congrats, you now have a unlocked phone with the latest version of RUI3!<br><br><img src="https://i.imgur.com/Z90bwAU.png"></p>
<hr>

# [EXTRA] Getting fastboot access
<p><img src="https://dummyimage.com/1000x70/ffffff/FF0000?text=Do this ONLY AFTER UPDATING to desired RUI3 version (ex: C.18)"></p>

## There are 2 ways: [Website](#2-website) or [local install](#1-local-install)

## 1. Local install
1. Go back to the [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Open the console again in `MTK Client` folder, **a tip how to do it faster below**
   <p align="center"><img src="https://i.imgur.com/J5VAWoy.png"></p>
3. Send the payload with `python mtk payload`. It should look like this: 
   <p align="center"><img src="https://i.imgur.com/Y2mwRhR.png"></p>
   
4. Make sure your phone is powered off, hold down **Vol+, Vol-, and power button** and connect the usb cable.
5. MTK Client should output something like this:
      <p align="center"><img src="https://i.imgur.com/KDp2u5O.png"></p>
6. Run  the command `python mtk r lk lk.bin`. There will now be a `lk.bin` file in **MTK Client** folder.
7. Download [oplus-unlock](https://github.com/R0rt1z2/oplus-unlock) and extract it. Navigate to the `oplus_unlock folder`. It should contain a file `main.py`
	<p align="center"><img src="https://i.ibb.co/r68tF52/Screenshot-from-2023-08-02-16-29-59.png"></p>
 	<p align="center"><img src="https://i.ibb.co/R9VhQPn/Screenshot-from-2023-08-02-16-30-22.png"></p>
8. Move `lk.bin` to oplus_unlock folder. Open the console in **oplus_unlock** folder, **a tip how to do it faster below**
   <p align="center"><img src="https://i.imgur.com/J5VAWoy.png"></p>
9. Run command `python main.py lk.bin -o lk-patched.bin`. A `lk-patched.bin` file will be created. Move it to **MTK Client** folder. [**Check below website section if you get an error**](#if-you-get-this-error--could-not-find-the-lock-sequence-no-suitable-sequence-was-found)
	<p align="center"><img src="https://i.ibb.co/9rc1cKF/Untitled.jpg" alt="Untitled"></p>
10. Run command `python mtk w lk lk-patched.bin`<br>

## 2. Website
#### Go through steps 1 - 6 from [Local install](#1-local-install)
7. Go to this [website](https://lkpatcher.r0rt1z2.com/). Upload your lk.bin file and the `lk-patched.bin` will be downloaded. Move it to `MTK Client` folder. [**Check below if you get an error**](#if-you-get-this-error--could-not-find-the-lock-sequence-no-suitable-sequence-was-found)
	<p align="center"><img src="https://i.ibb.co/gJ3H6hZ/Screenshot-from-2023-08-03-13-19-49.png"></p>
8. Run command `python mtk w lk lk-patched.bin`<br><br>

# ❗️ If you get this error: `[!]: Could not find the lock sequence (no suitable sequence was found)`
	
 <p align="center"><img src="https://i.ibb.co/YN42tZ5/Screenshot-from-2023-08-02-21-45-15.png"></p>

## USE *lk2* instead of *lk*, and replace it in all of the commands where needed. On *step 10* use the command `python mtk w lk lk2-patched.bin`

### Now flash whatever custom rom you want. 

# [EXTRA] Installing  a Custom ROM

## Prerequisites
- [latest platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
- ❗️ If you get an error: `fastboot: usage: unknown reboot target recovery` try this adb installer [ADB and Fastboot ++](https://github.com/K3V1991/ADB-and-FastbootPlusPlus)
- [ADB Driver Installer](https://forum.xda-developers.com/attachment.php?attachmentid=4623157&d=1540039037) - drivers
- [QcomMtk-Driver](http://www.mediafire.com/file/nninaiiqy1e5csa/New_QcomMtk_Driver_Setup_V2.0.1.1_GsmMafia.Com.exe/file) - also drivers
- [vbmeta image](https://github.com/bengris32/releases/releases/download/arrow-1.1/vbmeta.img) - vbmeta.img (USE WITH CAUTION, NO GUARANTEES) - some people have gotten rid of the **dm-verity corrupt** message by flashing this
- recovery image (usually `recovery.img`) - depends on the custom rom
- a custom rom package (in this guide I used Leaf OS 2)

1. ## Rebooting to fastboot
	1. Open a command prompt window in the **platform-tools** folder.
  	2. Enable Developer Options on device and enable USB Debugging.
	3. In the platform-tools folder open a command prompt and run `adb devices`. You will see something like this on phone, check `Always allow...` and hit `Allow`.
 	4. In the command prompt run `adb reboot boootloader`. Phone will reboot to a screen that says `fastboot_verify_ok` or similar.

2. ## Installing custom recovery and sideloading custom rom
   ##### If switching between custom roms skip step 2.
   ##### If the required recovery has not changed you may skip step 3 as well.
   
	1. Move the `recovery.img` and `vbmeta.img` files to the **platform-tools** folder.
 	2. Run the command `fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img`. It should show 
		<p align="center"><img src="https://i.ibb.co/X8jnCCB/Screenshot-from-2023-08-03-09-59-05.png"></p>
 	3. Run the command `fastboot flash recovery recovery.img`:
		<p align="center"><img src="https://i.ibb.co/L9YZXdn/Screenshot-from-2023-08-02-11-41-25.png"></p>
  	#### The phone will show `USB Transmission ok`
	4. Now, reboot to recovery mode with the command `fastboot reboot recovery` 
		<p align="center"><img src="https://i.ibb.co/Y0B19X6/Screenshot-from-2023-08-02-11-41-34.png"></p>
	5. In recovery, go to `Factory reset > Format data/factory reset > Format data`. **After** factory reset go back and select `Apply update > Apply from ADB`. You should see this when running `adb devices`:
 		<p align="center"><img src="https://i.ibb.co/znj0gVk/image.png"></p>
   	6. Now run the command `adb sideload custom-rom.zip` (replace *custom-rom.zip* with custom rom package name). For example I flashed LeafOS 2:
		<p align="center"><img src="https://i.ibb.co/3B0Xv7x/Screenshot-from-2023-08-02-11-38-48.png"></p>
  	7. <u>**Optional**</u> *ONLY* if  it is specified / needed to sideload a gapps package. Select `Apply update > Apply from ADB` again and run `adb sideload gapps.zip` (replace *gapps.zip* with package name). 
		<p align="center"><img src="https://i.ibb.co/XXj5CVx/image.png"></p>
	### If you get a "Signature verification error" continue anyways, the package will still flash, this goes the same to any other ZIPs you flash.
  	9. Once finished, in the recovery go back to `Reboot system now`. The phone will reboot into your Custom ROM.

# [EXTRA] Rooting (I used Lineage OS 20.0 for this)
<p><img src="https://dummyimage.com/400x100/ffffff/FF0000?text=ONLY USE ONE METHOD"></p>


## 1. With Magisk 
## You will need
- [magisk.zip](https://drive.google.com/file/d/1keLQuMiNhPFWg7pEQbvE3e3QVmSjmOMz/view?usp=sharing) - donwload on your pc
- [Magisk Manager (apk file)](https://drive.google.com/file/d/1LsHqdNqO7zOR2vhtxVCzC-JHiCN_l3gM/view?usp=drive_link) - download on your phone

1. ### You need to be in recovery mode. One way is to connect phone to pc, allow debugging and run `adb reboot recovery`
2. In recovery select `Apply update > Apply from ADB` and run `adb sideload magisk.zip`.
### If you get a "Signature verification error" continue anyways, the package will still flash, this goes the same to any other ZIPs you flash.
3. When completed tap `Reboot system now`. Your phone will restart. Navigate to where you donwnloaded the Magisk apk file and install it.
4. When opening the app you will get an error `Requires Additional Setup`. *This is normal*. Tap `OK`.
	<p align="center"><img src="https://i.ibb.co/C0LCSc8/Screenshot-20230802-145234-Magisk.png"></p>
5. Select `Direct Install` and tap `LET'S GO ->`
	<p align="center"><img src="https://i.ibb.co/fS7dDp2/Screenshot-20230802-145238-Magisk.png"></p>
6. You will see this. When it is finished tap `Reboot` (bottom-right corner)
	<p align="center"> <img src="https://i.ibb.co/nBTcVrz/Screenshot-20230802-145245-Magisk.png"></p>
7. The phone will restart and you are now rooted with Magisk!
##### If you want to uninstall, open Magisk Manager and tap `Uninstall > Complete uninstall`

## 2. With KernelSU - ONLY WORKS ON CUSTOM ROMS
## You will need
- [MTK Client](https://github.com/bkerler/mtkclient/releases/tag/1.52) - you used for bypass to brom and to unlock
- [KernelSU image](https://drive.google.com/file/d/1T8aQN5hf-gIY22eIaAGmhMTJcodhx3Iw/view?usp=sharing) - download on pc
- [KernelSU manager (apk file)](https://github.com/tiann/KernelSU/releases/latest) - Scroll down until you see `KernelSU_XXXXXXX-release.apk` (X replaces whatever the latest version is). Download this on your phone.

1. Open a command prompt in `MTK Client` folder and run this command `python mtk r boot boot.img`. This will create a file `boot.img`. This is in case you want to remove kernelsu.
2.  ### You need to be in recovery mode. One way is to connect phone to pc, allow debugging and run `adb reboot recovery`
3. In recovery select `Apply update > Apply from ADB` and run `adb sideload kernelsu.zip`.
### If you get a "Signature verification error" continue anyways, the package will still flash, this goes the same to any other ZIPs you flash.
3. When completed tap `Reboot system now`. Your phone will restart. Navigate to where you donwnloaded the KernelSu Manager apk file and install it.
4. The app should show like this indicating thaat everything has been done correctly:
	<p align="center"><img src="https://i.ibb.co/jRfXS5b/Screenshot-20230802-154216-Kernel-SU.png"></p>

5. If you want to remove KernelSU root, move the `boot.img` file you created at step 1 to the folder where adb is and run these commands in a command prompt:
   - `adb reboot bootloader`
   - `fastboot flash boot boot.img`

# Special thanks & credits

> [Ben](https://github.com/bengris32/android_kernel_realme_mt6785) - Made everything possible by making the kernel for Realme 8<br>
> [lemoekq](https://t.me/lemonekq) - The original guide on which this is based<br>
> [Zako Chan](https://t.me/zakolakov106/) - Information about walkthrough with downgrade<br>
> [Tony stark](https://forum.xda-developers.com/m/tony-stark.7582728/) - Provided [RUI2 unlock guide](https://forum.xda-developers.com/t/guide-realme-8-unofficial-new-method-unlock-bootloader-flash-twrp-and-root-rmx3085.4386473/).<br>
> [MtkClient](https://github.com/bkerler/mtkclient) - the tool that made unlocking possible<br>
> [oplus-unlock](https://github.com/R0rt1z2/oplus-unlock) - The tool used to unlock fastboot access, made by [Roger](t.me/R0rt1z2).<br>
> [Haadi](https://t.me/Haadi786H) - RUI2/RUI3 Firmware files<br>
> [HowWof](https://t.me/HowWof) - A few of suggestions, Leaf OS 2 main developer<br>
> [Ripper_Hybrid](t/me/Ripper_Hybrid) - KSU zip file<br>
> [Redline](https://forum.xda-developers.com/m/5988026/) - ADB Driver Installer<br>
> [Original Custom ROM Guide](https://telegra.ph/Flash-LineageOS-on-Realme-8-06-05)<br>
> [Magisk & Developers](https://github.com/topjohnwu/Magisk)<br>
> [KernelSU & Developers](https://github.com/tiann/KernelSU)<br>

> Telegram: [Realme 8 Discussion](https://t.me/Realme8Discussion), [Realme 8 Updates (MOVED)](https://t.me/Realme8Updates), [Realme 8 AOSP](https://t.me/Realme8AOSPGroup)

Thanks for reading, written by [lemonek](https://t.me/lemonekq/) with 💖 and by [me](t.me/driedpampas) also with 💗.

#### ¹ More info on the orange-state indicator and other indicators:
   -  Green state means the device is locked, it shouldnt show that it's locked on-boot
   -  Yellow state means that an alternate keystore was used to verify the boot image
   -  Orange state indicates that the device is unlocked.
   -  Red state means that a device in the locked or verified state had a boot image that did not verify. 
<br><br>
<div align="center">

Tested on 07/31/2023 by Me and a few others. No guarantees are given at any point. Use with caution.</p>
</div>
