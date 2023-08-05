<p align="center"><img src="https://i.imgur.com/oBsyb5O.png"></p>

<div align="center">
 
<H1>Realme 8 MEGAGUIDE</H1>
<h6>Version 3.2 feat. Wiki<h6>

</div>

### Please check wiki page for [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions. 

### If you have any questions at any moment feel free to message this Telegram channel: [Realme 8 AOSP](https://t.me/Realme8AOSPGroup), message [me](t.me/driedpampas) or [open a new Discussion](https://github.com/driedpampas/realme-8-megaguide/discussions/new/choose) right here on GitHub.

# Disclaimer

## If you unlocked with deep testing skip to [[EXTRA] Installing a Custom recoery and ROM](#extra-installing--a-custom-recovery-and-rom)
## Make sure to back up your data, because you will lose it - [Backup guide (in wiki)](https://github.com/driedpampas/realme-8-megaguide/wiki/Back-up-your-data)
### - **Make sure to read and do all of the steps to avoid your device being bricked.**
### - This method doesn't use the **Deep Testing** app. 
### - I used this method on [my](t/me.driedpampas) own device so I can confirm it works. Others have also used this method.
  
<p align="center"><img src="https://i.imgur.com/xc6lSJb.png"></p>
<p align="center">*If you are on RUI4 you'll need to downgrade to RUI2 as well*

<hr>

# Table of Contents
1. [Installing Prerequisites](#1-installing-prerequisites)
2. [Downgrade to RUI2](#2-downgrade-to-rui2)
3. [Unlocking the bootloader - MTK Client](#3-unlocking-the-bootloader---mtk-client)
4. [Upgrade to RealmeUI 3](#4-upgrade-to-realmeui-3)
5. [EXTRA: Getting fastboot access](https://github.com/driedpampas/realme-8-megaguide#extra-getting-fastboot-access---skip-only-if-you-unlocked-with-deep-testing)
6. [EXTRA: Installing a Custom ROM](#extra-installing--a-custom-rom)
7. [EXTRA: Rooting](#extra-rooting-i-used-lineage-os-200-for-this)

# Prerequisites
- [USB2SER](https://drive.google.com/file/d/1_SWiU9Ip9-sf8D-7VVIxcfXUpjsKlAdz/view?usp=drive_link)
- [USBDk](https://github.com/daynix/UsbDk/releases/download/v1.00-22/UsbDk_1.0.22_x64.msi)
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
   <p align="center"><img src="https://i.imgur.com/niVRaOn.png"></p>

 3. ## Install [USBDk](https://github.com/daynix/UsbDk/releases/)
 4. ## Install [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)

# 2. Downgrade to RUI2
1. **Extract** and enter the folder of [MTK Client archive](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
2. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
	<p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. Get the needed libraries using command `python -m pip install -r requirements.txt`. Send the payload with `python mtk payload`. It should look like this: 
	<p align="center"><img src="https://i.imgur.com/WSQsVj1.png"></p>
   
4. Make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable.
5. MTK Client should output something like this:
	<p align="center"><img src="https://i.imgur.com/lr7HIN0.png"></p>
   
6. The phone is now in BROM mode. Run the [SP Flash tool](https://drive.google.com/file/d/1sfsm3EXhIf8TrS5Y-En1mifgg8e9VjXl/view?usp=drive_link) `flash_tool.exe`
7. Click on `Options > Option...`
8. Make sure the right **COM Port** is selected, UART enabled and baud rate is set to **921600**.
	<p align="center"><img src="https://i.imgur.com/hnMsyeN.png"></p>
  
9. Get [Haadi's A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link) and unpack it
   
10. Load `scatter.txt` from Haadi's Firmware
    <p align="center"><img src="https://i.imgur.com/VTwpXzC.png"></p>

<div align="center">
	<p><img src="https://i.imgur.com/sYaIBIN.png"></p><p>Remember to uncheck:</p>
	
| opporeserve2 [Signed partition] | cdt_engineering [Digital warranty codes] |
| ------------------------------- | ---------------------------------------- |
| <img src="https://i.imgur.com/9Kp65P7.png" width="150"> | <img src="https://i.imgur.com/S6XOitJ.png" width="150"> |

</div><br>

11. Remember to have `Download Only` mode
	<p align="center"><img src="https://i.imgur.com/M3aUNBs.png" width="300"></p>
12. Avoid moving your phone so as to not disconnect anything. This process will take up to 15-20 minutes. To get A.19 on your phone, click `Download`.
	<p align="center"><img src="https://i.imgur.com/uSXflCJ.png" width="300"></p>
13. If everything goes well, it should look like this
	<p align="center"><img src="https://i.imgur.com/qeJWt3a.png" width="200"></p><br>

14. Before doing anything, we'll **WIPE the phone for safety.** Hold down **Vol-, and power button**, In recovery select wipe data, and then select **Format Data**.

# 3. Unlocking the bootloader - MTK Client
1. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Reboot your device, turn it off and Hold down both **Vol+, Vol-** - **(Don't leave the buttons until the bypass is done)**
3. Type `python mtk e metadata,userdata,md_udc` - This command wipes your data. It should look like this:
   <p align="center"><img src="https://i.imgur.com/HfPsrpU.png"></p>
4. Unlock the bootloader using command `python mtk da seccfg unlock`, the output should look like this
   <p align="center"><img src="https://i.imgur.com/Su8RtHk.png"></p>
      
   **After this, turn on your phone. First boot will take up to 5-20 minutes. Don't panic.**
   ### ❗ If bootloader is unlocked, there also will be a 5-second orange-state indicator [**¹**](#-more-info-on-the-orange-state-indicator-and-other-indicators)

5. Your bootloader is now unlocked.

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions


# 4. Upgrade to RealmeUI 3

1. Go back to the folder of [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
2. Open the console again in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
   <p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. Send the payload with `python mtk payload`. It should look like this: 
   <p align="center"><img src="https://i.imgur.com/WSQsVj1.png"></p>
   
4. Make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable.
5. MTK Client should output something like this:
      <p align="center"><img src="https://i.imgur.com/lr7HIN0.png"></p>
   
6. The phone is now in BROM mode. Run the [SP Flash tool](https://drive.google.com/file/d/1sfsm3EXhIf8TrS5Y-En1mifgg8e9VjXl/view?usp=drive_link) [flash_tool.exe]
7. Click on `Options > Option...`
8. Make sure the right **COM Port** is selected, UART enabled and baud rate is set to **921600**.
   <p align="center"><img src="https://i.imgur.com/hnMsyeN.png"></p>
9. Get [Haadi's C.14 RUI3 Firmware](https://drive.google.com/file/d/1JezJL-mz8fJC0lkNGMNyQiGCNYxj-pKs/view?usp=share_link) and unpack it
10. Load `MT6785_Android_scatter.xml` from Haadi's Firmware
    <p align="center"><img src="https://i.imgur.com/VTwpXzC.png"></p>

<div align="center">
	<p><img src="https://i.imgur.com/sYaIBIN.png"></p><p>Remember to uncheck:</p>
	
| opporeserve2 [Signed partition] | cdt_engineering [Digital warranty codes] |
| ------------------------------- | ---------------------------------------- |
| <img src="https://i.imgur.com/9Kp65P7.png" width="150"> | <img src="https://i.imgur.com/S6XOitJ.png" width="150"> |

</div><br>
	
11. Remember to have `Download Only` mode
    <p align="center"><img src="https://i.imgur.com/M3aUNBs.png" width="300"></p>
12. Place your phone on a stable surface, to not disconnect anything. This process will take up to 15-20 minutes. To get C.14 on your phone, click `Download`. [**No progress? Click me**](#if-you-click-download-but-there-is-no-progress-go-to-options--option--general-and-untick-storage-life-cycle-check-if-still-no-progress-go-back-to-options--option--connection-and-try-another-com-port)
    <p align="center"><img src="https://i.imgur.com/uSXflCJ.png" width="300"></p>
13. If everything goes well, it should look like this:
    <p align="center"><img src="https://i.imgur.com/qeJWt3a.png" width="200"></p>

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

14. Before continuing, you'll need to **WIPE the phone for safety.** Hold down **Vol-, and power button**, In recovery select wipe data, and then select **Format Data**.
15. ## Go into Settings and update to C.18

<p align="center"><img src="https://i.imgur.com/xCYhCEM.png"></p>
<hr>

<p><img src="https://i.imgur.com/UkNf5aM.png"></p>

# [EXTRA] Getting fastboot access - SKIP ONLY IF you unlocked with DEEP TESTING

## There are 2 ways: [local install](#1-local-install) or [Website](#2-website) - choose whatever way you want

## 1. Local install
1. Go back to the [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Open the console again in `MTK Client` folder
   <p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. Make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable.
4. Run  the command `python mtk r lk lk.bin`. There will now be a `lk.bin` file in **MTK Client** folder.
	<p align="center"><img src="https://i.imgur.com/gL4Qpc2.png"></p>
5. Download [oplus-unlock](https://github.com/R0rt1z2/oplus-unlock/archive/refs/heads/master.zip) and extract it. Navigate to the `oplus_unlock folder`. It should contain a file `main.py`
	<p align="center"><img src="https://i.ibb.co/r68tF52/Screenshot-from-2023-08-02-16-29-59.png"></p>
 	<p align="center"><img src="https://i.ibb.co/R9VhQPn/Screenshot-from-2023-08-02-16-30-22.png"></p>
6. Move `lk.bin` to oplus_unlock folder. Open the console in **oplus_unlock** folder
   <p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
7. Run command `python main.py lk.bin -o lk-patched.bin`. A `lk-patched.bin` file will be created. Move it to **MTK Client** folder. [**Check below website section if you get an error**](#if-you-get-this-error--could-not-find-the-lock-sequence-no-suitable-sequence-was-found)
	<p align="center"><img src="https://i.ibb.co/9rc1cKF/Untitled.jpg" alt="Untitled"></p>
8. Run command `python mtk w lk lk-patched.bin`<br>

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

## 2. Website
#### Go through steps 1 - 4 from [Local install](#1-local-install)
5. Go to this [website](https://lkpatcher.r0rt1z2.com/). Upload your lk.bin file and the `lk-patched.bin` will be downloaded. Move it to `MTK Client` folder. [**Check below if you get an error**](#if-you-get-this-error--could-not-find-the-lock-sequence-no-suitable-sequence-was-found)
	<p align="center"><img src="https://i.imgur.com/kddEiuG.png"></p>
6. Run command `python mtk w lk lk-patched.bin`<br><br>

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ#4-i-patched-my-lk-but-the-phone-still-says-fastboot_verify_fail) if something does not work or you have questions

### Now flash whatever custom rom you want. 

# [EXTRA] Installing  a Custom Recovery and ROM

## Prerequisites
- [latest platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)
- ❗️ If you get an error: `fastboot: usage: unknown reboot target recovery` try this adb installer [ADB and Fastboot ++](https://github.com/K3V1991/ADB-and-FastbootPlusPlus/releases/download/v1.0.8/ADB-and-Fastboot++_v1.0.8.exe)
- [ADB Driver Installer](https://forum.xda-developers.com/attachment.php?attachmentid=4623157&d=1540039037) - drivers
- [QcomMtk-Driver](https://download2434.mediafire.com/oujse6nv0amgSlaKhG_5IT5vEREODBIhSkqFC1JuR1aOORwPa_UD8YhxGRy1AikoG2PkekfmgOtaL0-xqTgbm_hrGhTRUx0piW3s9Am-bcSMj5bO0jR5tvWgN0qOv5vuHONzUrlzgzqhuKA1EWI6EIbxL5dJUyyHX1RxNSk5bQ/nninaiiqy1e5csa/New+QcomMtk_Driver_Setup_V2.0.1.1_GsmMafia.Com.exe) - also drivers
- [vbmeta image](https://github.com/bengris32/releases/releases/download/arrow-1.1/vbmeta.img) - vbmeta.img file
- a custom rom package - **you can use any Custom ROM you want** (as an example, I used Leaf OS 2)
- GAPPS package - recommended [MindTheGApps](https://androidfilehost.com/?fid=4279422670115734716)
- 2 example recovery images:
	- [lineage-os recovery](https://github.com/bengris32/releases/releases/download/3.0/lineage-20.0-20230613-UNOFFICIAL-nashc-recovery.img) - compatible with Pixel Experience and Lineage OS (and others, check the Custom ROM's description)	
	- [leaf-os recovery](https://github.com/HowWof/releases/releases/download/leaf-2.0.1/recovery.img) - ONLY for Leaf OS 2 (if you want OTA updates)

1. ## Rebooting to fastboot
	### Your device needs to be turned on
 	1. Open a command prompt window in the **platform-tools** folder.
  	2. **On your phone**, enable Developer Options and enable USB Debugging.
	3. In the platform-tools folder open a command prompt and run `adb devices`. You will see `Allow USB Debugging for ...` on phone, check `Always allow...` and hit `Allow`.
 	4. In the command prompt run `adb reboot boootloader`. Phone will reboot to a screen that says `fastboot_unlock_verify ok`.

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

2. ## Installing custom recovery and sideloading custom rom
   #### ⚠️ If switching between custom roms skip step 2.
   #### ⚠️ If the required recovery has not changed you may skip step 3 as well, and run `adb reboot recovery` directly.
   
	1. Move the `recovery.img` and `vbmeta.img` files to the **platform-tools** folder.
 	2. Run the command `fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img`. It should show 
		<p align="center"><img src="https://i.imgur.com/MZZyTBc.png"></p>
 	3. Run the command `fastboot flash recovery recovery.img`:
		<p align="center"><img src="https://i.imgur.com/t7wYi3R.png"></p>
  	#### The phone will show `USB Transmission ok`
	4. Now, reboot to recovery mode with the command `fastboot reboot recovery` 
		<p align="center"><img src="https://i.imgur.com/1zwXUmj.png"></p>
	5. In recovery, go to `Factory reset > Format data/factory reset > Format data`. **After** factory reset go back and select `Apply update > Apply from ADB`. You should see this when running `adb devices`:
 		<p align="center"><img src="https://i.imgur.com/MoiIS9k.png"></p>
   	6. Now run the command `adb sideload custom-rom.zip` (replace *custom-rom.zip* with custom rom package name). For example I flashed LeafOS 2:
		<p align="center"><img src="https://i.imgur.com/QZqi1e1.png"></p>
  	7. **ONLY** do this step on custom roms **WIHTOUT GAPPS / GMS** (check the rom's description to check). Select `Apply update > Apply from ADB` again and run `adb sideload gapps.zip` (replace *gapps.zip* with package name). 
		<p align="center"><img src="https://i.imgur.com/DUEMXrn.png"></p>
	### If you get a "Signature verification error" on your phone, click `Yes` to continue anyways, this goes the same to any other ZIPs you flash.
  	9. Once finished, in the recovery go back to `Reboot system now`. The phone will reboot into your Custom ROM.

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

# [EXTRA] Rooting (I used Lineage OS 20.0 for this)
<p><img src="https://i.imgur.com/tm2MVru.png"></p>


## 1. With Magisk 
## You will need
- [magisk.zip](https://drive.google.com/file/d/1keLQuMiNhPFWg7pEQbvE3e3QVmSjmOMz/view?usp=sharing) - donwload on your pc
- [Magisk Manager (apk file)](https://drive.google.com/file/d/1LsHqdNqO7zOR2vhtxVCzC-JHiCN_l3gM/view?usp=drive_link) - download on your phone

1. ### You need to be in recovery mode. One way is to connect phone to pc, allow debugging and run `adb reboot recovery`
2. In recovery select `Apply update > Apply from ADB` and run `adb sideload magisk.zip`.
### If you get a "Signature verification error" continue anyways, the package will still flash, this goes the same to any other ZIPs you flash.
3. When completed tap `Reboot system now`. Your phone will restart. Navigate to where you donwnloaded the Magisk apk file and install it.
4. When opening the app you will get an error `Requires Additional Setup`. *This is normal*. Tap `OK`.
	<p align="center"><img src="https://i.imgur.com/4pSY7xF.png" height="700"></p>
5. Select `Direct Install` and tap `LET'S GO ->`
	<p align="center"><img src="https://i.imgur.com/SO1bVT8.png" height="400"></p>
6. You will see this. When it is finished tap `Reboot` (bottom-right corner)
	<p align="center"> <img src="https://i.imgur.com/kHKnvf0.png" height="700"></p>
7. The phone will restart and you are now rooted with Magisk!
##### If you want to uninstall, open Magisk Manager and tap `Uninstall > Complete uninstall`

## 2. With KernelSU - ONLY WORKS ON CUSTOM ROMS (do NOT ATTEMPT on RealmeUI or it will BRICK your device)
## You will need
- [KernelSU zip file](https://drive.google.com/file/d/1-47z-ax0zRGGoUou766zzrcccxVH_u5K/view?usp=sharing) - download on pc
- [KernelSU manager (apk file)](https://github.com/tiann/KernelSU/releases/download/v0.6.2/KernelSU_v0.6.2_11089-release.apk) - Download this on your phone.

1.  ### You need to be in recovery mode. One way is to connect phone to pc, allow debugging and run `adb reboot recovery`
2. In recovery select `Apply update > Apply from ADB` and run `adb sideload kernelsu.zip`.
### If you get a "Signature verification error" continue anyways, the package will still flash, this goes the same to any other ZIPs you flash.
3. When completed tap `Reboot system now`. Your phone will restart. Navigate to where you donwnloaded the KernelSu Manager apk file and install it.
4. The app should show like this indicating thaat everything has been done correctly:
	<p align="center"><img src="https://i.imgur.com/XhOFSXP.png" height="700"></p>

5. If you want to remove KernelSU root, extract the `custom-rom.zip` you downloaded to flash the ROM, find and move the `boot.img` to the folder where adb is and run these commands in a command prompt:
   - `adb reboot bootloader`
   - `fastboot flash boot boot.img`

# More extras in [WIKI](https://github.com/driedpampas/realme-8-megaguide/wiki)


## Special thanks & credits

> [Ben](https://github.com/bengris32/android_kernel_realme_mt6785) - Made everything possible by making the kernel for Realme 8<br>
> [lemoekq](https://t.me/lemonekq) - The original guide on which this is based<br>
> [Zako Chan](https://t.me/zakolakov106/) - Information about walkthrough with downgrade<br>
> [Tony stark](https://forum.xda-developers.com/m/tony-stark.7582728/) - Provided [RUI2 unlock guide](https://forum.xda-developers.com/t/guide-realme-8-unofficial-new-method-unlock-bootloader-flash-twrp-and-root-rmx3085.4386473/).<br>
> [MtkClient](https://github.com/bkerler/mtkclient) - the tool that made unlocking possible<br>
> [Roger](t.me/R0rt1z2) - creator of [oplus-unlock](https://github.com/R0rt1z2/oplus-unlock)<br>
> [Haadi](https://t.me/Haadi786H) - RUI2/RUI3 Firmware files<br>
> [HowWof](https://t.me/HowWof) - A few of suggestions, Leaf OS 2 main developer<br>
> [Ripper_Hybrid](t/me/Ripper_Hybrid) - KSU zip file<br>
> [Redline](https://forum.xda-developers.com/m/5988026/) - ADB Driver Installer<br>
> [Original Custom ROM Guide](https://telegra.ph/Flash-LineageOS-on-Realme-8-06-05)<br>
> [Magisk & Developers](https://github.com/topjohnwu/Magisk)<br>
> [KernelSU & Developers](https://github.com/tiann/KernelSU)<br>

> Telegram: [Realme 8 Discussion](https://t.me/Realme8Discussion), [Realme 8 AOSP](https://t.me/Realme8AOSPGroup)

Thanks for reading, written by [lemonek](https://t.me/lemonekq/) with 💖 and by [me](t.me/driedpampas) also with 💗.

#### ¹ More info on the orange-state indicator and other indicators:
   -  Green state means the device is locked, it shouldnt show that it's locked on-boot
   -  Yellow state means that an alternate keystore was used to verify the boot image
   -  Orange state indicates that the device is unlocked.
   -  Red state means that a device in the locked or verified state had a boot image that did not verify. 
<br><br>
<div align="center">

Tested me and others. No guarantees are given at any point. Use with caution.</p>
</div>
