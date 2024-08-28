> [!Warning]
> ## **Make sure to read and do all of the steps to avoid your device being bricked.**

### Questions? Message [Realme 8 AOSP](https://t.me/Realme8AOSPGroup) on Telegram or start a new [Github Discussion](https://github.com/driedpampas/realme-8-megaguide/discussions/new/choose)

### Already unlocked? Skip to [Installing a Custom recovery and ROM](/common/custom-rom.guide.md)

#### Disclaimer:
- NO WARRANTY, as permitted by law.

### If you are on RUI4 please update to F.09 or higher to ensure LKPatcher compatibility.

# Table of Contents
0. [Back up](/linux/mtk.guide.md#0-back-up-your-data)

I. [Unlocking the bootloader](/linux/mtk.guide.md#i-unlocking)
1. [Installing Prerequisites](/linux/mtk.guide.md#1-installing-prerequisites)
2. [Downgrade to RUI2](/linux/mtk.guide.md#2-downgrade-to-rui2)
3. [Unlocking the bootloader](/linux/mtk.guide.md#3-unlocking-the-bootloader)
4. [Upgrade to RealmeUI 3](/linux/mtk.guide.md#4-upgrade-to-realmeui-3)

II. [Patching `lk`](/linux/mtk.guide.md#ii-patching-lk)  
III. [Installing a Custom ROM](/linux/mtk.guide.md#iii-installing-a-custom-recovery-and-rom)  
IV. [Rooting](/linux/mtk.guide.md#iv-rooting)  

* * *

# 0. Back up your system partitions
> [!CAUTION]
> # HAVE YOU BACKED UP ALREADY? IF NOT FOLLOW THE [Backup guide](/linux/backup.md)

# I. Unlocking

# Prerequisites
| Software | Firmware |
| :------: | :------: |
| Python | [A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link) |
| [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)  | [C.18 RUI3 Firmware](https://drive.google.com/file/d/1YHSIr4itg_5dPE2IbWAH9N8g6L5CGmaG/view?usp=drive_link) |
| [SP Flash tool](https://github.com/driedpampas/realme-8-megaguide/blob/main/linux/SP_Flash_Tool_v5.2044_Linux.tar.xz) | |

## 1. Installing prerequisites

1. Install `libusb`
2. Verify that `python` installation is newer than **`3.9`**

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
	
> [!IMPORTANT]
> # Remember to uncheck:
| opporeserve2 [Signed partition] | cdt_engineering [Digital warranty codes] |
| --- | --- |
| <img src="https://i.imgur.com/9Kp65P7.png" width="150"> | <img src="https://i.imgur.com/S6XOitJ.png" width="150"> |

> [!CAUTION]
> # 9. Remember to have **`Download Only`** mode or _**you will lose critical partitions**_.
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
>   **First boot will take around 5-20 minutes.**
>   **You will see `dm-verity corruption` and `orange state` warnings. Press the *Power Button* to continue. These are normal and will be patched later in the guide.**

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

* * *
 
# II. Patching `lk`

> [!warning]
> ## This is necessary for getting fastboot access and removing dm-verity and orange state warnings

1. Go back to the [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Open the console again in `MTK Client` folder
   <p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>
3. Make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable.
4. Run  the command `python mtk r lk lk.bin`. There will now be a `lk.bin` file in **MTK Client** folder.
	<p align="center"><img src="https://i.imgur.com/gL4Qpc2.png"></p>
5. Go to this [website](http://lkpatcher.cxwof.dev/). Upload your lk.bin file and the `lk-patched.bin` will be downloaded. Move it to `MTK Client` folder. [**Check below if you get an error**](#if-you-get-this-error--could-not-find-the-lock-sequence-no-suitable-sequence-was-found)
	<p align="center"><img src="https://i.imgur.com/HOve3Mv.png"></p>
6. Run command `python mtk w lk lk-patched.bin`<br><br>

> [!IMPORTANT]
> ### Check [Manual patching](https://github.com/driedpampas/realme-8-megaguide/wiki/Patching-LK-(local)) if you have issues with the website

#### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ#4-i-patched-my-lk-but-the-phone-still-says-fastboot_verify_fail) if something does not work or you have questions
* * *
# III. Installing a Custom Recovery and ROM
## Go to [Custom ROM Guide](/common/custom-rom.guide.md)
* * *
# IV. Rooting 
## Go to [Rooting](/common/rooting.md)  
* * *
## More in [WIKI](https://github.com/driedpampas/realme-8-megaguide/wiki)

* * *

###### mtk-guide.md | Licensed under CC BY-NC-SA 4.0 — check [license](/LICENSE) for more information.
