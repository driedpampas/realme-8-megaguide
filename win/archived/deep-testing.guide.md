# NO LONGER WORKS, REALME HAS REMOVED THE R8 FROM THE SERVERS

>[!Warning]
> ## **Make sure to read and do all of the steps to avoid your device being bricked.**

### Questions? Message [Realme 8 AOSP](https://t.me/Realme8AOSPGroup) on Telegram or start a new [Github Discussion](https://github.com/driedpampas/realme-8-megaguide/discussions/new/choose)

### Already unlocked? Skip to [Installing a Custom recovery and ROM](/md/custom-rom.guide.md)

#### Disclaimer:
- NO WARRANTY, as permitted by law.
- Windows 7 is not supported.

## Prerequisites

| Software | Drivers | Firmware | APKs |
| :------: | :-----: | :------: | :--: |
| [Python](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5) | [Mediatek USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) | [C.18 Firmware](https://drive.google.com/uc?id=1MPLnD4ofrW50u8V4C5I5srGucHJg60XW&export=download) | [Deep Testing](https://drive.google.com/file/d/1pESMmJef6Gm9YlJAE7OA_DDNnhFn3Jpz/view?usp=sharing) |
| [MTK Client](https://codeload.github.com/bkerler/mtkclient/zip/f9fe6ca65c93c2eb05adef7787069103c0d79763) | [USBDk](https://github.com/daynix/UsbDk/releases/download/v1.00-22/UsbDk_1.0.22_x64.msi) | |
| [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) |
| [adb tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) |

# Table of Contents

0. [Back up](/md/w-deep-testing.guide.md#0-back-up-your-data)

I. [Unlocking the bootloader](/md/w-deep-testing.guide.md#i-unlocking)

1. [Installing Prerequisites](/md/w-deep-testing.guide.md#1-installing-prerequisites)
2. [Flashing RUI3 C.18](/md/w-deep-testing.guide.md#2-flash-rui3-c18)
3. [Unlocking the bootloader](/md/w-deep-testing.guide.md#3-unlocking-the-bootloader)

II. [Installing a Custom ROM](/md/w-deep-testing.guide.md#iii-installing-a-custom-recovery-and-rom)  
III. [Rooting](/md/w-deep-testing.guide.md#iv-rooting)  
* * *

# 0. Back up your system partitions
> [!CAUTION]
> # HAVE YOU BACKED UP ALREADY? IF NOT FOLLOW THE [Backup guide](/md/backup.md)

# I. Unlocking

## 1. Installing prerequisites

1. ### Mediatek USB
   1. **Extract** and enter the folder of [Mediatek USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) driver.
   2. Find the **.inf** file, right click and press install
   <p align="center"><img src="https://i.imgur.com/niVRaOn.png"></p>
2. ### Install [USBDk](https://github.com/daynix/UsbDk/releases/)
3. ### Install [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)

## 2. Flash RUI3 C.18

1. **Extract** and enter the folder of [MTK Client archive](https://codeload.github.com/bkerler/mtkclient/zip/f9fe6ca65c93c2eb05adef7787069103c0d79763)
2. Open the console in [MTK Client's](https://codeload.github.com/bkerler/mtkclient/zip/f9fe6ca65c93c2eb05adef7787069103c0d79763) folder
<p align="center"><img src="https://i.imgur.com/RJtobaI.png"></p>

3. Get the needed libraries using command `python -m pip install -r requirements.txt`. Send the payload with `python mtk payload`. It should look like this:
<p align="center"><img src="https://i.imgur.com/WSQsVj1.png"></p>

4. Make sure your phone is powered off, hold down both **Vol+, Vol-** and connect the usb cable. You will see something like this:
<p align="center"><img src="https://i.imgur.com/lr7HIN0.png"></p>

5. The phone is now in BROM mode. Run the [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) `flash_tool.exe`

6. Click on `Options > Option...` and make sure the right **COM Port** is selected, UART enabled and baud rate is set to **921600**.

<p align="center"><img src="https://i.imgur.com/hnMsyeN.png"></p>

7. Get [C.18 Firmware](https://drive.google.com/uc?id=1MPLnD4ofrW50u8V4C5I5srGucHJg60XW&export=download) and unpack it
8. Load `MT6785_Android_scatter.txt` from the firmware's folder
   <p align="center"><img src="https://i.imgur.com/8APQvkx.png"></p>

> [!CAUTION] 
> 9. Remember to have **`Download Only`** mode or **you will lose critical partitions**

<p align="center"><img src="https://i.imgur.com/M3aUNBs.png" width="300"></p>

10. This process will take up to 15-20 minutes. To begin, click `Download` ([**No progress? Click me**](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ)). Make sure to not disconnect your phone.
<p align="center"><img src="https://i.imgur.com/uSXflCJ.png" width="300"></p>

11. If everything goes well, it should look like this
<p align="center"><img src="https://i.imgur.com/qeJWt3a.png" width="200"></p><br>

12. Before doing anything, we'll **WIPE the phone for safety.** Hold down **Vol-, and power button**, In recovery select wipe data, and then select **Format Data**.

## 3. Unlocking the bootloader with Deep Testing

1. Download and install the deep testing app, tap "Apply Now" and accept the agreement, you should be seeing this now:
<p align="center"><img src="https://i.imgur.com/MTeSOl3.png" width="300"></p>

2. Close the app and swipe away from recents. Open the app again and tap Query verification status. You should now see this:
<p align="center"><img src="https://i.imgur.com/FEN05v9.png" width="300"></p>

3. Tap "Start deep testing" and the device will reboot to fastboot mode:
<p align="center"><img src="https://i.imgur.com/G6NeOCQ.png" width="300"></p>

4. The device will reboot to fastboot mode. To unlock the bootloader plug the device into a PC and type `fastboot flashing unlock` in `platform-tools` directory, you should see this:
<p align="center"><img src="https://i.imgur.com/iYp4XAP.png" width="600"></p>

5. Press `Volume up` and the bootloader will be unlocked.

* * *
# III. Installing a Custom Recovery and ROM
## Go to [Custom ROM Guide](/md/custom-rom.guide.md)
* * *
# IV. Rooting 
## Go to [Rooting](/md/rooting.md) 

###### deep-testing.guide.md | Licensed under CC BY-NC-SA 4.0 — check [license](/LICENSE) for more information.
