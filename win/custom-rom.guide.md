# III. Installing a Custom Recovery and ROM

## Prerequisites

| Software | Drivers | Images |
| :------: | :-----: | :----: |
| [latest platform-tools](https://dl.google.com/android/repository/platform-tools-latest-windows.zip) | [QcomMtk-Driver](https://www.mediafire.com/file/nninaiiqy1e5csa/New+QcomMtk_Driver_Setup_V2.0.1.1_GsmMafia.Com.exe) | [vbmeta image](https://github.com/bengris32/releases/releases/download/arrow-1.1/vbmeta.img) |

> [!TIP]
>❗️ If you get an error: `fastboot: usage: unknown reboot target recovery` try this adb installer [ADB and Fastboot ++](https://github.com/K3V1991/ADB-and-FastbootPlusPlus/releases/download/v1.0.8/ADB-and-Fastboot++_v1.0.8.exe)

| Custom ROM | GApps Package | Recovery |
| :--------: | :-----------: | :------: |
| new website: [Click here](https://realme8.dry.nl.eu.org) | Check for recommended GAPPS when downloading a rom! | also on the [new website](https://realme8.dry.nl.eu.org/Recoveries) |
| check out the [Telegram group](https://t.me/Realme8AOSPGroup) | [MindTheGApps A13](https://androidfilehost.com/?fid=4279422670115734716) | [recoveries page](/common/recovery.md) |

## 1. Rebooting to fastboot

### Your device needs to be turned on

1.  Open a command prompt window in the **platform-tools** folder.
2.  **On your phone**, enable Developer Options and enable USB Debugging.
3.  In the platform-tools folder open a command prompt and run `adb devices`. You will see `Allow USB Debugging for ...` on phone, check `Always allow...` and hit `Allow`.
4.  In the command prompt run `adb reboot bootloader`. Phone will reboot to a screen that says `fastboot_unlock_verify ok`.

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

## 2. Installing custom recovery and sideloading custom rom

> [!TIP]
>
> #### ⚠️ If switching between custom roms skip step 2.
>
> #### ⚠️ If the required recovery has not changed you may skip step 3.

1.  Move the `recovery.img` and `vbmeta.img` files to the **platform-tools** folder.
2.  Run the command `fastboot --disable-verity --disable-verification flash vbmeta vbmeta.img`. It should show
<p align="center"><img src="https://i.imgur.com/MZZyTBc.png"></p>

3.  Run the command `fastboot flash recovery recovery.img`:
<p align="center"><img src="https://i.imgur.com/t7wYi3R.png"></p>

#### The phone should show `USB Transmission ok`

4.  Now, reboot to recovery mode with the command `fastboot reboot recovery`
<p align="center"><img src="https://i.imgur.com/1zwXUmj.png"></p>

5.  In recovery, go to `Factory reset > Format data/factory reset > Format data`. **After** factory reset go back and select `Apply update > Apply from ADB`. You should see this when running `adb devices`:
<p align="center"><img src="https://i.imgur.com/MoiIS9k.png"></p>

6.  Now run the command `adb sideload custom-rom.zip` (replace _custom-rom.zip_ with custom rom package name). For example I flashed LeafOS 2:
<p align="center"><img src="https://i.imgur.com/QZqi1e1.png"></p>

7.  **ONLY** do this step on custom roms **WIHTOUT GAPPS / GMS** (check the rom's description to check). Select `Apply update > Apply from ADB` again and run `adb sideload gapps.zip` (replace _gapps.zip_ with package name).
<p align="center"><img src="https://i.imgur.com/DUEMXrn.png"></p>

#### If you get a "Signature verification error" on your phone, click `Yes` to continue anyways, this goes the same to any other ZIPs you flash.

9.  Once finished, in the recovery go back to `Reboot system now`. The phone will reboot into your Custom ROM.

### ❗ Check [FAQ (frequently asked questions)](https://github.com/driedpampas/realme-8-megaguide/wiki/FAQ) if something does not work or you have questions

###### custom-rom.guide.md | Licensed under CC BY-NC-SA 4.0 — check [license](/LICENSE) for more information.
