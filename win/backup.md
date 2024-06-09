# This method makes a _firmware_ backup in case IMEI is erased or system is bricked.

> [!WARNING]
>
> ### ❗ PERSONAL DATA IS NOT BACKED UP USING THIS METHOD.
>
> ### Use GDrive, another cloud service, or transfer your personal data to a physical media, wherever you feel it is safe.

---

# Table of Contents

I. [Backup](/win/backup.md#i-backup)  
II. [Restore](/win/backup.md#ii-restore)

## Prerequisites

| Software | Drivers |
|:-------: | :-----: |
| [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5) | [Mediatek USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) |
| [MTK Client](https://codeload.github.com/bkerler/mtkclient/zip/f9fe6ca65c93c2eb05adef7787069103c0d79763) | [USBDk](https://github.com/daynix/UsbDk/releases/download/v1.00-22/UsbDk_1.0.22_x64.msi) |


---

# Installing prerequisites
### Mediatek USB
1. **Extract** and enter the folder of [Mediatek USB](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing) driver.
2. Find the **.inf** file, right click and press install
   <p align="center"><img src="https://i.imgur.com/niVRaOn.png"></p>
3. Install [USBDk](https://github.com/daynix/UsbDk/releases/)
4. Download [MTK Client](https://codeload.github.com/bkerler/mtkclient/zip/f9fe6ca65c93c2eb05adef7787069103c0d79763) and extract it. Then, run `pip3 install -r requirements.txt` in a Command Prompt to install all required dependencies

---

# I. Backup

1. Prepare a folder in which to store backed up partitions. For this example we'll use `firmware-backup`.

2. Turn your phone off, hold both volume buttons, run this command `python mtk rl --skip userdata,super "firmware-backup"` and connect your phone to your computer.

![](https://i.imgur.com/wBPSBxg.png)

##### This is what will show while the backup is running:

![](https://i.imgur.com/PTG4sik.png)

2. After the command finishes, check the folder to make sure the backup was made to the correct location and that there are _51 files_

![](https://i.imgur.com/HL49pJa.png)

# You are ready. Continue to [Landing](/win/landing.md)

---

# II. Restore

1. Flash a firmmware package (example: [C.18](https://drive.google.com/file/d/1YHSIr4itg_5dPE2IbWAH9N8g6L5CGmaG/view?usp=drive_link))

2. Run `python mtk wl (folder name)` in a command prompt. (To only flash some files use `python mtk w (partition) (file name)`)

> [!CAUTION]
>
> ## ❗ A preloader file will be backed up inside `mtk client` folder. Keep that file as safe as possible, as it's crucial to restoring the firmware.
>
> ## ❗ ONLY FLASH YOUR OWN FIRMWARE OR THE FIRMWARE PROVIDED IN THE GUIDE (exclude `cdt_engineering` AND `opporeserve2` for those)

###### backup.md | Licensed under CC BY-NC-SA 4.0 — check [license](/LICENSE) for more information.
