#### Disclaimer: NO WARRANTY, as permitted by law.

> [!CAUTION]
> # This is an experimental guide. If you are a normal user please go to [Landing page](/common/landing.md).

> [!INFO]
> This guide completely ommits fastboot access. This is not recommended unless as the last-resort of last-resorts.

* * *
# Table of Contents

0. [Back up](/common/experimental.md#0-back-up-your-data)

I. [Unlocking the bootloader](/common/experimental.md#i-unlocking)

1. [Installing Prerequisites](/common/experimental.md#1-installing-prerequisites)
2. [Downgrade to RUI2](/common/experimental.md#2-downgrade-to-rui2)
3. [Unlocking the bootloader](/common/experimental.md#3-unlocking-the-bootloader)
4. [Upgrade to RealmeUI 3](/common/experimental.md#4-upgrade-to-realmeui-3)

II. [Patching `lk` - qetting fastboot access and removing dm-verity and orange state](/common/experimental.md#ii-patching-lk--qetting-fastboot-access-and-removing-dm-verity-and-orange-state-warnings--skip-only-if-you-unlocked-with-deep-testing)  
III. [Installing a Custom ROM](/common/experimental.md#iii-installing-a-custom-recovery-and-rom)  
IV. [Rooting](/common/experimental.md#iv-rooting)

---

# 0. Back up your system partitions

> [!CAUTION]
>
> # HAVE YOU BACKED UP ALREADY? IF NOT FOLLOW THE [Backup guide](/common/backup.md)

# I. Unlocking

## Prerequisites

| Software | Drivers | Firmware |
| :------: | :-----: | :------: |
| [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5) | [Mediatek USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) | [A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link) |
| [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) | [USBDk](https://github.com/daynix/UsbDk/releases/download/v1.00-22/UsbDk_1.0.22_x64.msi) | [C.18 RUI3 Firmware](https://drive.google.com/file/d/1YHSIr4itg_5dPE2IbWAH9N8g6L5CGmaG/view?usp=drive_link) |
| [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) | |

## 1. Installing prerequisites

### Install [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)

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

</div>  

> [!CAUTION] 
> 9. Remember to have **`Download Only`** mode or **you will lose critical partitions**.

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
5. Reboot with `python mtk reset` or hold all hardware buttons until the phone reboots.

> [!IMPORTANT]  
>  **First boot will take around 5-20 minutes.**
> **You will see `dm-verity corruption` and `orange state` warnings. Press the _Power Button_ to continue. These are normal and will be patched later in the guide.**

6. Set your phone up and enable **Developer Options** and verify that the bootloader is unlocked under `OEM unlocking`

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
6. The phone is now in BROM mode. Run the [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) -`flash_tool.exe`
7. Click on `Options > Option...`
8. Make sure the right **COM Port** is selected, UART enabled and baud rate is set to **921600**.
   <p align="center"><img src="https://i.imgur.com/hnMsyeN.png"></p>
9. Get [SG's C.18 RUI3 Firmware](https://drive.google.com/file/d/1YHSIr4itg_5dPE2IbWAH9N8g6L5CGmaG/view?usp=drive_link) and unpack it
10. Load `MT6785_Android_scatter.txt` from SG's firmware
<p align="center"><img src="https://i.imgur.com/8APQvkx.png"></p>

11. Remember to have `Download Only` mode
    <p align="center"><img src="https://i.imgur.com/M3aUNBs.png" width="300"></p>

12. Place your phone on a stable surface, to not disconnect anything. This process will take up to 15-20 minutes. To get C.18 on your phone, click `Download`. [**No progress? Click me**](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ)
<p align="center"><img src="https://i.imgur.com/uSXflCJ.png" width="300"></p>

13. If everything goes well, it should look like this:
<p align="center"><img src="https://i.imgur.com/qeJWt3a.png" width="200"></p>

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

14. Before continuing, you'll need to **WIPE the phone for safety.** Hold down **Vol-, and power button**, In recovery select wipe data, and then select **Format Data**.

> [!IMPORTANT]
> ## Only continue after updating to / flashing RUI3 C.18

---

# II. Installing a Custom Recovery and ROM

## Prerequisites

| Software | Drivers | Images |
| :------: | :-----: | :----: |
| [latest platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) | [QcomMtk-Driver](https://www.mediafire.com/file/nninaiiqy1e5csa/New+QcomMtk_Driver_Setup_V2.0.1.1_GsmMafia.Com.exe) | [vbmeta image](https://github.com/bengris32/releases/releases/download/arrow-1.1/vbmeta.img) |

| Custom ROM | GApps Package | Recovery |
| :--------: | :-----------: | :------: |
| check out the [Telegram group](https://t.me/Realme8AOSPGroup) | [MindTheGApps for Android 13](https://androidfilehost.com/?fid=4279422670115734716) | [recoveries page](/common/recovery.md) |

## 1. Installing custom recovery

1. Go back to the folder of [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
2. Open the console again in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
   <p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. Send the payload with `python mtk payload`. It should look like this:
   <p align="center"><img src="https://i.imgur.com/WSQsVj1.png"></p>
4. Make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable.
5. Run `python mtk w vbmeta vbmeta.img` to flash the vbmeta image.
6. Run `python mtk w recovery recovery.img` to flash the custom recovery you downloaded from the [recoveries page](/common/recovery.md). Your phone might reset itself.
7. Run `python mtk reset`. After the phone reboots contiue to the next step.

## 2. Sideloading custom rom

1.  Open a command prompt window in the **platform-tools** folder.
2.  **On your phone**, enable Developer Options and enable USB Debugging.
3.  In the platform-tools folder open a command prompt and run `adb devices`. You will see `Allow USB Debugging for ...` on phone, check `Always allow...` and hit `Allow`.
4.  In the command prompt run `adb reboot recovery`. 

5.  In recovery, go to `Factory reset > Format data/factory reset > Format data`. **After** factory reset go back and select `Apply update > Apply from ADB`. You should see this when running `adb devices`:
<p align="center"><img src="https://i.imgur.com/MoiIS9k.png"></p>

6.  Now run the command `adb sideload custom-rom.zip` (replace _custom-rom.zip_ with custom rom package name). For example I flashed LeafOS 2:
<p align="center"><img src="https://i.imgur.com/QZqi1e1.png"></p>

7.  **ONLY** do this step on custom roms **WIHTOUT GAPPS / GMS** (check the rom's description to check). Select `Apply update > Apply from ADB` again and run `adb sideload gapps.zip` (replace _gapps.zip_ with package name).
<p align="center"><img src="https://i.imgur.com/DUEMXrn.png"></p>

#### If you get a "Signature verification error" on your phone, click `Yes` to continue anyways, this goes the same to any other ZIPs you flash.

8.  Once finished, reboot to `system`. The phone will reboot into your Custom ROM.

---

# III. Rooting

> [!IMPORTANT]
>
> ### Only use one method.
>
> | [Magisk](#with-magisk) | [KernelSU](#with-kernelsu) |
> | :--------------------: | :------------------------: |

# With Magisk
### You will need

| Software | APKs |
| :------: | :--: |
| [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) | [Magisk Manager](https://github.com/topjohnwu/Magisk/releases/tag/v27.0) |
| [platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) | |

1. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Run `python mtk r boot boot.img`. Turn your device off, hold down both **Vol+, Vol-** and connect the device to the computer.
3. A `boot.img` file will be created in the folder. Turn your device on and copy the file to it.
4. Navigate to where you downloaded the Magisk Manager apk file and install it.
5. Open Magisk Manager and click install next to `Magisk`.
<p align="center"><img src="https://i.imgur.com/CAbHxPv.png" width=400></p>

6. Select `Select and patch a file`. The file picker will open, Find and select the `boot.img` you extracted. Then tap `let's go`.
<img src="https://i.imgur.com/4m7CJfB.png" height=131.830985915></p>

7. When you see this screen, the patching is done and you will be given the path of the patched `.img file`. Copy that file to your computer in the `mtk-client` folder.  
   ![](https://i.imgur.com/D9qyjbGm.png)

8. In the `mtk-client` folder open a Command Prompt and run the command `python mtk w boot <<magisk patched file name.img>> `. After flashing run `python mtk reset`.
9. The phone will restart and you are now rooted with Magisk!
#### Note that you will get a prompt to reboot to finish the installation.

### To remove Magisk root, select `Uninstall > Complete uninstall` in the Magisk Manager app.
 * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *
# With KernelSU
> [!WARNING]
> #### ONLY WORKS ON CUSTOM ROMS

> [!IMPORTANT]
> #### If you keep your phone plugged in while rebooting when rooted with KSU it will bootloop and go to recovery. Unplug your phone before rebooting.

### You will need

> [!Tip]
> #### Clicking on the zip file will redirect to another repo. Download any kernel zip ending in KernelSU-v{x.y.z}.zip
> Refer to [Kernels](/kernels.md) for more info

| ZIP | APKs |
| :-: | :--: |
| [KernelSU zip](https://github.com/HowWof/KernelSU_Builder/releases/latest) | [KSU manager APK](https://github.com/tiann/KernelSU/releases/download/v0.7.6/KernelSU_v0.7.6_11458-release.apk) |

1.  ### You need to be in recovery mode; run `adb reboot recovery`
2.  In recovery select `Apply update > Apply from ADB` and run `adb sideload kernelsu.zip`.

### If you get a "Signature verification error" continue anyways, the package will still flash, this goes the same to any other ZIPs you flash.

3. When completed tap `Reboot system now`. Your phone will restart. Navigate to where you donwnloaded the KernelSu Manager apk file and install it.
4. The app should show like this indicating thaat everything has been done correctly:
<p align="center"><img src="https://i.imgur.com/XhOFSXP.png" height="700"></p>

### If you want to remove KernelSU root:
   - extract the `custom-rom.zip` you downloaded to flash the ROM, find and move the `boot.img` to the `mtk-client` folder
   - make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable.
   - run `python mtk w boot boot.img` then `python mtk reset`. The phone will restart and you are now unrooted.
---

## More in [WIKI](https://github.com/driedpampas/realme-8-megaguide/wiki)

###### experimental.md | Licensed under CC BY-NC-SA 4.0 — check [license](/LICENSE) for more information.
