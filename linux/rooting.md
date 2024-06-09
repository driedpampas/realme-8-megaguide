# IV. Rooting

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
| Please install from official software repositories before trying the manual download. [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) | [Magisk Manager](https://github.com/topjohnwu/Magisk/releases/tag/v27.0) |
| [platform-tools](https://dl.google.com/android/repository/platform-tools-latest-linux.zip) | |

1. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
2. Run `python mtk r boot boot.img`. Turn your device off, hold down both **Vol+, Vol-** and connect the device to the computer.
3. A `boot.img` file will be created in the folder. Turn your device on and copy the file to it.
4. Navigate to where you downloaded the Magisk Manager apk file and install it.
5. Open Magisk Manager and click install next to `Magisk`.
<p align="center"><img src="https://i.imgur.com/CAbHxPv.png" width=400></p>

6. Select `Select and patch a file`. The file picker will open, Find and select the `boot.img` you extracted. Then tap `let's go`.
<img src="https://i.imgur.com/4m7CJfB.png" height=131.830985915></p>

7. When you see this screen, the patching is done and you will be given the path of the patched `.img file`. Copy that file to your computer in the `platform-tools` folder.  
   ![](https://i.imgur.com/D9qyjbGm.png)

8. Connect your phone to your computer and enable usb debugging on your phone 
9. In the `platform-tools` folder open a Command Prompt and run the command `adb devices`. Accept USB Debugging on your phone and run `adb reboot bootloader`. The phone will reboot to a `fastboot_unlock_verify ok` screen.
10. Now in the cmd run the command `fastboot flash boot <<type magisk patched file name.img>>` and hit Enter. Once successfully transferred, run `fastboot reboot`
11. The phone will restart and you are now rooted with Magisk!
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
> Refer to [Kernels](https://preview.realme8.dry.nl.eu.org/Kernels) for more info

| ZIP | APKs |
| :-: | :--: |
| [KernelSU zip](https://github.com/HowWof/KernelSU_Builder/releases/latest) | [KSU manager APK](https://github.com/tiann/KernelSU/releases/download/v1.0.0/KernelSU_v1.0.0_11874-release.apk) |

1.  ### You need to be in recovery mode; run `adb reboot recovery`
2.  In recovery select `Apply update > Apply from ADB` and run `adb sideload kernelsu.zip`.

### If you get a "Signature verification error" continue anyways, the package will still flash, this goes the same to any other ZIPs you flash.

3. When completed tap `Reboot system now`. Your phone will restart. Navigate to where you donwnloaded the KernelSu Manager apk file and install it.
4. The app should show like this indicating thaat everything has been done correctly:
<p align="center"><img src="https://i.imgur.com/XhOFSXP.png" height="700"></p>

5. If you want to remove KernelSU root, extract the `custom-rom.zip` you downloaded to flash the ROM, find and move the `boot.img` to the folder where adb is and run these commands in a command prompt:
   - `adb reboot bootloader`
   - `fastboot flash boot boot.img`

###### rooting.md | Licensed under CC BY-NC-SA 4.0 — check [license](/LICENSE) for more information.
