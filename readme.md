![](https://repository-images.githubusercontent.com/673466903/8e5d0af8-1861-46dd-8358-2e3374654cfe)

###### Version 17.12.23 feat. [Wiki](https://github.com/driedpampas/realme-8-megaguide/wiki)

 > [!Warning]
 > ## **Make sure to read and do all of the steps to avoid your device being bricked.**

### We have a website now 🥳 [Guide Online](https://guide.driedpampas.ro.eu.org) (includes wiki posts)

### If you have any questions message [Realme 8 AOSP](https://t.me/Realme8AOSPGroup) on Telegram or [open a new Discussion](https://github.com/driedpampas/realme-8-megaguide/discussions/new/choose) right here on GitHub.

### If you have unlocked already skip to [Installing a Custom recovery and ROM](#iii-installing--a-custom-recovery-and-rom)

## Disclaimer

- We WON'T be responsible if anything happens with your device.
- Neither Windows 7 (old python version) nor RealmeUI 4 (lk method was patched) are supported

<p align="center"><b>WARNING: RUI4 disables fastboot access if previously unlocked, only upgrade to RUI3 until it is resolved.</b><hr>
	
# Table of Contents
0. [Back up](#0-back-up-your-data)

I. [Unlocking the bootloader](#i-unlocking)
1. [Installing Prerequisites](#1-installing-prerequisites)
2. [Downgrade to RUI2](#2-downgrade-to-rui2)
3. [Unlocking the bootloader](#3-unlocking-the-bootloader)
4. [Upgrade to RealmeUI 3](#4-upgrade-to-realmeui-3)

II. [Patching `lk` - qetting fastboot access and removing dm-verity and orange state](#ii-patching-lk--qetting-fastboot-access-and-removing-dm-verity-and-orange-state-warnings--skip-only-if-you-unlocked-with-deep-testing)<br>
III. [Installing a Custom ROM](#iii-installing--a-custom-recovery-and-rom)<br>
IV. [Rooting](#iv-rooting)<br>

# 0. Back up your system partitions
> [!CAUTION]
> # BEFORE ATTEMPTING ANY OPERATIONS FOLLOW THE [Backup guide (in wiki)](https://github.com/driedpampas/realme-8-megaguide/wiki/Back-up-your-data)

# I. Unlocking

# Prerequisites
- [Mediatek USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing)
- [USBDk](https://github.com/daynix/UsbDk/releases/download/v1.00-22/UsbDk_1.0.22_x64.msi)
- [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)
- [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
- [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing)
- [A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link)
- [C.18 RUI3 Firmware](https://drive.google.com/file/d/1YHSIr4itg_5dPE2IbWAH9N8g6L5CGmaG/view?usp=drive_link)

## 1. Installing prerequisites
1. ### Mediatek USB
	1. **Extract** and enter the folder of [Mediatek USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) driver.
	2. Find the **.inf** file, right click and press install
   <p align="center"><img src="https://i.imgur.com/niVRaOn.png"></p>
 3. ### Install [USBDk](https://github.com/daynix/UsbDk/releases/)
 4. ### Install [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)

## 2. Downgrade to RUI2
1. **Extract** and enter the folder of [MTK Client archive](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
2. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
	<p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. Get the needed libraries using command `python -m pip install -r requirements.txt`. Send the payload with `python mtk payload`. It should look like this: 
	<p align="center"><img src="https://i.imgur.com/WSQsVj1.png"></p>
4. Make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable. You will see something like this:
	<p align="center"><img src="https://i.imgur.com/lr7HIN0.png"></p>
5. The phone is now in BROM mode. Run the [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) `flash_tool.exe`
6. Click on `Options > Option...` and make sure the right **COM Port** is selected, UART enabled and baud rate is set to **921600**.
	<p align="center"><img src="https://i.imgur.com/hnMsyeN.png"></p>
7. Get [Haadi's A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link) and unpack it
8. Load `scatter.txt` from Haadi's Firmware
    <p align="center"><img src="https://i.imgur.com/VTwpXzC.png"></p>

<div align="center">
	<p><img src="https://i.imgur.com/sYaIBIN.png"></p><p>Remember to uncheck:</p>
	
| opporeserve2 [Signed partition] | cdt_engineering [Digital warranty codes] |
| ------------------------------- | ---------------------------------------- |
| <img src="https://i.imgur.com/9Kp65P7.png" width="150"> | <img src="https://i.imgur.com/S6XOitJ.png" width="150"> |

</div><br>

> [!CAUTION]
>  9. Remember to have **`Download Only`** mode or **you will destroy critical partition data**
	<p align="center"><img src="https://i.imgur.com/M3aUNBs.png" width="300"></p>
10. Avoid moving your phone so as to not disconnect anything. This process will take up to 15-20 minutes. To get A.19 on your phone, click `Download`.
	<p align="center"><img src="https://i.imgur.com/uSXflCJ.png" width="300"></p>
11. If everything goes well, it should look like this
	<p align="center"><img src="https://i.imgur.com/qeJWt3a.png" width="200"></p><br>
12. Before doing anything, we'll **WIPE the phone for safety.** Hold down **Vol-, and power button**, In recovery select wipe data, and then select **Format Data**.
 
## 3. Unlocking the bootloader
1. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Reboot your device, turn it off and Hold down both **Vol+, Vol-** - **(Don't leave the buttons until the command is done)**
3. Type `python mtk e metadata,userdata,md_udc` - This command wipes your data. It should look like this:
   <p align="center"><img src="https://i.imgur.com/HfPsrpU.png"></p>
4. Unlock the bootloader using command `python mtk da seccfg unlock`, the output should look like this
   <p align="center"><img src="https://i.imgur.com/Su8RtHk.png"></p>
 

> [!IMPORTANT]  
>   **After this, turn on your phone. First boot will take around 5-20 minutes.**
>   **You will see `dm-verity corruption` and `orange state` warnings. Press the *Power Button* to continue. These are normal and will be patched later in the guide.**

5. Your bootloader is now unlocked.

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions


## 4. Upgrade to RealmeUI 3

1. Go back to the folder of [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
2. Open the console again in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
   <p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. Send the payload with `python mtk payload`. It should look like this: 
   <p align="center"><img src="https://i.imgur.com/WSQsVj1.png"></p>
   
4. Make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable.
5. MTK Client should output something like this:
      <p align="center"><img src="https://i.imgur.com/lr7HIN0.png"></p>
   
6. The phone is now in BROM mode. Run the [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) [flash_tool.exe]
7. Click on `Options > Option...`
8. Make sure the right **COM Port** is selected, UART enabled and baud rate is set to **921600**.
   <p align="center"><img src="https://i.imgur.com/hnMsyeN.png"></p>
9. Get [SG's C.18 RUI3 Firmware](https://drive.google.com/file/d/1YHSIr4itg_5dPE2IbWAH9N8g6L5CGmaG/view?usp=drive_link) and unpack it
10. Load `MT6785_Android_scatter.txt` from SG's firmware
    <p align="center"><img src="https://i.imgur.com/8APQvkx.png"></p>	
11. Remember to have `Download Only` mode
    <p align="center"><img src="https://i.imgur.com/M3aUNBs.png" width="300"></p>
12. Place your phone on a stable surface, to not disconnect anything. This process will take up to 15-20 minutes. To get C.18 on your phone, click `Download`. [**No progress? Click me**](#if-you-click-download-but-there-is-no-progress-go-to-options--option--general-and-untick-storage-life-cycle-check-if-still-no-progress-go-back-to-options--option--connection-and-try-another-com-port)
    <p align="center"><img src="https://i.imgur.com/uSXflCJ.png" width="300"></p>
13. If everything goes well, it should look like this:
    <p align="center"><img src="https://i.imgur.com/qeJWt3a.png" width="200"></p>

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

14. Before continuing, you'll need to **WIPE the phone for safety.** Hold down **Vol-, and power button**, In recovery select wipe data, and then select **Format Data**.
 
> [!IMPORTANT]
> ## Only continue after updating to / flashing RUI3 C.18

* * *
 
# II. Patching `lk`- qetting fastboot access and removing dm-verity and orange state warnings
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
- example recovery images:
	- 🎉 We now have [OrangeFox recovery](https://fcloud.howwof.pl/s/RBmEeMRZyDam8fZ) 🎉	
	- [lineage-os recovery](https://github.com/bengris32/releases/releases/download/3.0/lineage-20.0-20230613-UNOFFICIAL-nashc-recovery.img) - compatible with Pixel Experience and Lineage OS (and others, check the Custom ROM's description)	
	- [leaf-os recovery](https://github.com/HowWof/releases/releases/download/leaf-2.0.1/recovery.img) - use ONLY with Leaf OS 2

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
<p align="center"><img src="https://i.imgur.com/tm2MVru.png"></p>

## 1. With Magisk 
### You will need
- [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) - donwload on your pc
- [Magisk Manager (apk file)](https://drive.google.com/file/d/1LsHqdNqO7zOR2vhtxVCzC-JHiCN_l3gM/view?usp=drive_link) - download on your phone
- [latest platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip)

1. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Run `python mtk r boot boot.img`. Turn your device off, hold down both **Vol+, Vol-** and connect the device to the computer.
3. A `boot.img` file will be created in the folder. Turn your device on and copy the file to it.
4. Navigate to where you donwnloaded the Magisk Manager apk file and install it.
5. Open Magisk Manager and click install next to `Magisk`.
	<p align="center"><img src="https://i.imgur.com/CAbHxPv.png" width=400></p>
6. Select `Patch vbmeta in boot image` and click `Select and patch a file`. The file picker will open, Find and select the `boot.img` you extracted.
	<p align=center><img src="https://i.imgur.com/d3QC6S8.png" width=400><img src="https://i.imgur.com/4m7CJfB.png" height=131.830985915></p> 
8. When you see this screen, the patching is done and you will be givne the path of the patched `.img file`. Copy that file to your computer in the `platform-tools` folder.
	<p align=center><img src="https://i.imgur.com/D9qyjbG.png" width=400></p>
9. Connect your pphone to your computer, enable usb debugging on your phone and, in the `platform-tools` folder open a Command Prompt and run the command `adb devices`. Accept USB Debugging on your phone and run `and reboot bootloader`. The phone will reboot to a `fastboot_unlock_verify ok` screen.
10. Now in the cmd run the command `fastboot flash boot <<type magisk patched file name.img>>` and hit Enter. Once successfully transferred, run `fastboot reboot`
11. The phone will restart and you are now rooted with Magisk!

### To remove Magisk root, select `Uninstall > Complete uninstall` in the Magisk Manager app.

## 2. With KernelSU - ONLY WORKS ON CUSTOM ROMS (do NOT ATTEMPT on RealmeUI or it will BRICK your device)
### You will need
- [KernelSU zip file](https://drive.google.com/file/d/1UUQe_5XH-9IBiz-SNp6I4fSyE1QQgtw4/view?usp=sharing) - download on pc
- [KernelSU manager (apk file)](https://github.com/tiann/KernelSU/releases/download/v0.7.0/KernelSU_v0.7.0_11326-release.apk) - Download this on your phone.

1.  ### You need to be in recovery mode; run `adb reboot recovery`
2. In recovery select `Apply update > Apply from ADB` and run `adb sideload kernelsu.zip`.
### If you get a "Signature verification error" continue anyways, the package will still flash, this goes the same to any other ZIPs you flash.
3. When completed tap `Reboot system now`. Your phone will restart. Navigate to where you donwnloaded the KernelSu Manager apk file and install it.
4. The app should show like this indicating thaat everything has been done correctly:
	<p align="center"><img src="https://i.imgur.com/XhOFSXP.png" height="700"></p>

5. If you want to remove KernelSU root, extract the `custom-rom.zip` you downloaded to flash the ROM, find and move the `boot.img` to the folder where adb is and run these commands in a command prompt:
   - `adb reboot bootloader`
   - `fastboot flash boot boot.img`

# More extras in [WIKI](https://github.com/driedpampas/realme-8-megaguide/wiki#more-extras)

## Special thanks & credits
 
> [Ben](https://github.com/bengris32/android_kernel_realme_mt6785) - Made everything possible by making the kernel for Realme 8<br>
> [bkerler](https://twitter.com/viperbjk) - developer of [MtkClient](https://github.com/bkerler/mtkclient)<br>
> [Roger](https://t.me/R0rt1z2) - creator of [lkpatcher](https://github.com/R0rt1z2/lkpatcher)<br>
> [Haadi](https://t.me/Haadi786H) - RUI2 firmware<br>
> [SGtriangle](https://t.me/SGtriangle) - RUI3 firmware<br>
> [HowWof](https://t.me/HowWof) - A lot of help, Leaf OS 2 for RMX3085 developer<br>
> [Ripper_Hybrid](https://t.me/Ripper_Hybrid) - provided KSU zip file, helped with wiki guides<br>
> [MrPotato6](https://t.me/MrPotato6) - Info and screenshots for Magisk rooting<br>
> [Nand kumar](https://forum.xda-developers.com/m/nand-kumar.8476267/) - original poster of backup guide<br>
> [Zako Chan](https://t.me/zakolakov106/) - Information about walkthrough with downgrade<br>
> [Tony stark](https://forum.xda-developers.com/m/tony-stark.7582728/) - [RUI2 unlock guide](https://forum.xda-developers.com/t/guide-realme-8-unofficial-new-method-unlock-bootloader-flash-twrp-and-root-rmx3085.4386473/)<br>
> [Original Custom ROM Guide](https://telegra.ph/Flash-LineageOS-on-Realme-8-06-05)<br>
> [Magisk & Developers](https://github.com/topjohnwu/Magisk)<br>
> [KernelSU & Developers](https://github.com/tiann/KernelSU)<br>
> Banner and others via [Canva](https://canva.com) - Refer to [Canva's CLA](https://www.canva.com/policies/content-license-agreement/) for more info
> Text images made in [Drawing](https://maoschanz.github.io/drawing)

> Telegram: [Realme 8 AOSP](https://t.me/Realme8AOSPGroup)
 
Witten by [me](https://t.me/driedpampas) with 🫶.

* * *

<div align="center">

No guarantees are given at any point. Use with caution. Neither me nor contributors are responsible for any damage you do to your device(s).</p>

</div>

Guide and Wiki (c) by @driedpampas, 2023

This content is licensed under a
Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this
work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.
