# This method makes a _firmware_ backup in case there is a need for restore or the system is bricked.

> [!WARNING]
>
> ### ❗ PERSONAL DATA IS NOT BACKED UP USING THIS METHOD.
>
> ### Use GDrive, another cloud service, or transfer your personal data to a physical media, wherever you feel it is safe.

---

# Table of Contents

I. [Backup](/md/backup.md#i-backup)  
II. [Restore](/md/backup.md#ii-restore)

## Prerequisites

- [USB2SER](https://drive.google.com/file/d/1_SWiU9Ip9-sf8D-7VVIxcfXUpjsKlAdz/view?usp=drive_link)
- [USBDk](https://github.com/daynix/UsbDk/releases/download/v1.00-22/UsbDk_1.0.22_x64.msi)
- [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)
- [MTK Client archive](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)

---

# I. Backup

- Install python, USB2SER (find the `cdc-acm.inf` file, right click and press `Install`) and USBdk

- Run `pip3 install -r requirements.txt` in a cmd in `MTK Client` folder to install all required dependencies.

1. Prepare a folder in which to store backed up partitions. For this example we'll use `firmware-backup`.

2. Turn your phone off, hold both volume buttons, run this command `python mtk rl --skip userdata "firmware-backup"` and connect your phone to your computer.

![](https://i.imgur.com/wBPSBxg.png)

##### This is what will show while the backup is running:

![](https://i.imgur.com/PTG4sik.png)

2. After the command finishes, check the folder to make sure the backup was made to the correct location and that there are _51 files_

![](https://i.imgur.com/HL49pJa.png)

# You are ready. Continue with the [GUIDE](/md/w-deep-testing.guide.md)

---

# II. Restore

## To flash the entire backup back to your device use `python mtk wl (folder name)` in a command prompt. To only flash some files use `python mtk w (partition) (file name)`.

> [!CAUTION]
>
> ## ❗ A preloader file will be backed up inside `mtk client` folder. Keep that file as safe as possible, as it's crucial to restoring the firmware.
>
> ## ❗ ONLY FLASH YOUR OWN FIRMWARE OR THE FIRMWARE PROVIDED IN THE GUIDE (exclude `cdt_engineering` AND `opporeserve2` for those)

###### There is NO WARRANTY, to the extent permitted by law.

###### Guide and Wiki (c) by @driedpampas, 2023-2024

###### backup.md | Licensed under CC-BY-SA 4.0 — check [license](/LICENSE) for more information.
