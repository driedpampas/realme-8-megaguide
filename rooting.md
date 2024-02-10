# IV. Rooting

> [!CAUTION]
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
4. Navigate to where you donwnloaded the Magisk Manager apk file and install it.
5. Open Magisk Manager and click install next to `Magisk`.
<p align="center"><img src="https://i.imgur.com/CAbHxPv.png" width=400></p>
6. Select `Patch vbmeta in boot image` and click `Select and patch a file`. The file picker will open, Find and select the `boot.img` you extracted.
<p align=center><img src="https://i.imgur.com/d3QC6S8.png" width=400><img src="https://i.imgur.com/4m7CJfB.png" height=131.830985915></p>
7. When you see this screen, the patching is done and you will be givne the path of the patched `.img file`. Copy that file to your computer in the `platform-tools` folder.
   ![](https://i.imgur.com/D9qyjbG.png)
8. Connect your pphone to your computer, enable usb debugging on your phone and, in the `platform-tools` folder open a Command Prompt and run the command `adb devices`. Accept USB Debugging on your phone and run `adb reboot bootloader`. The phone will reboot to a `fastboot_unlock_verify ok` screen.
9. Now in the cmd run the command `fastboot flash boot <<type magisk patched file name.img>>` and hit Enter. Once successfully transferred, run `fastboot reboot`
10. The phone will restart and you are now rooted with Magisk!

### To remove Magisk root, select `Uninstall > Complete uninstall` in the Magisk Manager app.
 * * *
# With KernelSU
> [!WARNING]
> ONLY WORKS ON CUSTOM ROMS (do NOT ATTEMPT on RealmeUI or it will BRICK your device)

### You will need

| ZIP | APKs |
| :-: | :--: |
| [KernelSU zip file](https://drive.google.com/file/d/1UUQe_5XH-9IBiz-SNp6I4fSyE1QQgtw4/view?usp=sharing) | [KernelSU manager (apk file)](https://github.com/tiann/KernelSU/releases/download/v0.7.0/KernelSU_v0.7.0_11326-release.apk) |

1.  ### You need to be in recovery mode; run `adb reboot recovery`
2.  In recovery select `Apply update > Apply from ADB` and run `adb sideload kernelsu.zip`.

### If you get a "Signature verification error" continue anyways, the package will still flash, this goes the same to any other ZIPs you flash.

3. When completed tap `Reboot system now`. Your phone will restart. Navigate to where you donwnloaded the KernelSu Manager apk file and install it.
4. The app should show like this indicating thaat everything has been done correctly:
<p align="center"><img src="https://i.imgur.com/XhOFSXP.png" height="700"></p>

5. If you want to remove KernelSU root, extract the `custom-rom.zip` you downloaded to flash the ROM, find and move the `boot.img` to the folder where adb is and run these commands in a command prompt:
   - `adb reboot bootloader`
   - `fastboot flash boot boot.img`
