## Prerequisites

| Software | Drivers | Firmware | APKs |
| -------- | ------- | -------- | ---- |
| [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5) | [Mediatek USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) | [C.11 Firmware](https://drive.google.com/file/d/192KboBbW1eXzb6DWVlGAkGE-PEcgnHBJ/view?usp=sharing) | [Deep Testing APK](https://drive.google.com/file/d/1pESMmJef6Gm9YlJAE7OA_DDNnhFn3Jpz/view?usp=sharing) |
| [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) | [USBDk](https://github.com/daynix/UsbDk/releases/download/v1.00-22/UsbDk_1.0.22_x64.msi) | [C.18 Firmware](https://drive.google.com/file/d/1YHSIr4itg_5dPE2IbWAH9N8g6L5CGmaG/view?usp=drive_link) |
| [SP Flash tool](https://drive.google.com/file/d/11XeUnCYtARZg2kx7J2JWWeLULieSIYrx/view?usp=sharing) | |
| [latest platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) |

# Table of Contents

0. [Back up](/w-deep-testing.guide.md#0-back-up-your-data)

I. [Unlocking the bootloader](/w-deep-testing.guide.md#i-unlocking)

1. [Installing Prerequisites](/w-deep-testing.guide.md#1-installing-prerequisites)
2. [Flash RUI3 C.11](/w-deep-testing.guide.md#2-flash-rui3-c11)
3. [Unlocking the bootloader](/w-deep-testing.guide.md#3-unlocking-the-bootloader)
4. [Upgrade to RealmeUI 3](/w-deep-testing.guide.md#4-upgrade-to-realmeui-3)

# 0. Back up your system partitions

> [!CAUTION]
>
> # HAVE YOU BACKED UP ALREADY? IF NOT FOLLOW THE [Backup guide (in wiki)](https://github.com/driedpampas/realme-8-megaguide/wiki/Back-up-your-data)

# I. Unlocking

## 1. Installing prerequisites

1. ### Mediatek USB
   1. **Extract** and enter the folder of [Mediatek USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) driver.
   2. Find the **.inf** file, right click and press install
   <p align="center"><img src="https://i.imgur.com/niVRaOn.png"></p>
2. ### Install [USBDk](https://github.com/daynix/UsbDk/releases/)
3. ### Install [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)

## 2. Flash RUI3 C.11

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
7. Get [C.11 Firmware](https://drive.google.com/file/d/192KboBbW1eXzb6DWVlGAkGE-PEcgnHBJ/view?usp=sharing) and unpack it
8. Load `MT6785_Android_scatter.txt` from the firmware's folder
   <p align="center"><img src="https://i.imgur.com/8APQvkx.png"></p>

<div align="center">
	<p><img src="https://i.imgur.com/sYaIBIN.png"></p><p>Remember to uncheck:</p>
	
| opporeserve2 [Signed partition] | cdt_engineering [Digital warranty codes] |
| ------------------------------- | ---------------------------------------- |
| <img src="https://i.imgur.com/9Kp65P7.png" width="150"> | <img src="https://i.imgur.com/S6XOitJ.png" width="150"> |

</div><br>

> [!CAUTION] 9. Remember to have **`Download Only`** mode or **you will lose critical partitions**

    <p align="center"><img src="https://i.imgur.com/M3aUNBs.png" width="300"></p>

10. Avoid moving your phone so as to not disconnect anything. This process will take up to 15-20 minutes. To get A.19 on your phone, click `Download`.
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

## 4. Upgrade to RealmeUI 3 C.18
### Either use below steps or update with settings ONLY TO C.18

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

# You may now continue with: [Installing a custom recovery and ROM](/guide.md#iii-installing--a-custom-recovery-and-rom)

###### w-deep-testing.guide.md. Licensed under CC-BY-SA 4.0. Check [license](/LICENSE) for more information.
