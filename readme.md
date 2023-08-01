# Disclaimer

- This method will **wipe your phone** and **temporarily downgrade your phone to RUI2**
- **Read this tutorial step by step to don't miss anything.**
- This method doesn't use **Deep Test**
- I used this method on my own device so I can confirm it works.

<p align="center" style="color: red;">Use this tutorial <b>only with RUI3</b></p>

<hr>

# Requirements
- [MTK Client archive](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
- [SP Flash tool](https://drive.google.com/file/d/1sfsm3EXhIf8TrS5Y-En1mifgg8e9VjXl/view?usp=drive_link)
- [A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link)
- [C.14 RUI3 Firmware](https://drive.google.com/file/d/1JezJL-mz8fJC0lkNGMNyQiGCNYxj-pKs/view?usp=share_link)
- [libusb-win32 Drivers](https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/libusb-win32-devel-filter-1.2.6.0.exe/download)
- [USBDk](https://github.com/daynix/UsbDk/releases/)
- [USB2SER](https://drive.google.com/file/d/1_SWiU9Ip9-sf8D-7VVIxcfXUpjsKlAdz/view?usp=drive_link)
- [Python from Microsoft Store](https://apps.microsoft.com/store/detail/python-310/9PJPW5LDXLZ5)
- A functioning brain and a emotional support after the unlock

# 1. Drivers - USB2SER
2. **Extract** and enter to the folder of [USB2SER](https://drive.google.com/file/d/1_SWiU9Ip9-sf8D-7VVIxcfXUpjsKlAdz/view?usp=drive_link) driver.
	1. Find the **.inf** file, right click and press install
   <p align="center"><img src="https://i.imgur.com/BZxtj6B.png"></p>

# 2. Drivers - libusb-win32
1. Download [libusb-win32](https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/libusb-win32-devel-filter-1.2.6.0.exe/download) and install it
2. Run [libusb-win32](https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/libusb-win32-devel-filter-1.2.6.0.exe/download) 
3. Take actions at  [libusb-win32](https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/libusb-win32-devel-filter-1.2.6.0.exe/download) window, selecting install a device filter
      <p align="center"><img src="https://i.imgur.com/f2qF7h8.png"></p>
4. Before pressing next, Connect your phone to your computer, make sure its powered off, as it is: Hold down **Vol+, Vol-, and power button**
5. Remember to not release the BROM buttons, it can be a quite hard, but with your second hand you can operate the mouse. **Click next**
6. You should see there a `MediaTek USB Port` device, Select it and **Click Install**
   <p align="center"><img src="https://i.imgur.com/mMKRfRG.png"></p>
7. After installing, **Leave your phone shut down**. We will get into the same state in downgrading to RUI2

# 3. Downgrade to RUI2
1. **Extract** and enter to the folder of [MTK Client archive](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
2. Open the console in the [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder, **a tip how to do it faster below**
   <p align="center"><img src="https://i.imgur.com/J5VAWoy.png"></p>
3. Run the payload by simply using command `python mtk payload`, It should look like this: 
   <p align="center"><img src="https://i.imgur.com/Y2mwRhR.png"></p>
   If there is any error with python, you dont have the libaries. get them using command `python -m pip install -r requirements.txt`
   
4. Make sure your phone is powered off, Make sure your phone is connected to your computer, as it is: Hold down **Vol+, Vol-, and power button** - **(Don't leave the buttons until the bypass is done)**
5. MTK Client should output something like this:
      <p align="center"><img src="https://i.imgur.com/KDp2u5O.png"></p>
   
6. Leave the phone alone in the BROM, Run the [SP Flash tool](https://drive.google.com/file/d/1sfsm3EXhIf8TrS5Y-En1mifgg8e9VjXl/view?usp=drive_link) [flash_tool.exe]
7. Click on `Options > Option...`
8. Make sure the right **COM Port** is selected, UART enabled and baud rate is set to 921600.
   <p align="center"><img src="https://i.imgur.com/C6n8awx.png"></p>
  
9. Get [Haadi's A.19 RUI2 Firmware](https://drive.google.com/file/d/1Iy2hwZ0mHQtpHgpyRDRHMZv13FTTvups/view?usp=share_link) and unpack it
   
10. Load scatter from Haadi's Firmware
    <p align="center"><img src="https://i.imgur.com/Tzavwau.png"></p>
<p align="center" style="color: red;">IMPORTANT: </p><p align="center">Remember to uncheck:<br>
- opporeserve2 [Signed partition] <br><img src="https://i.imgur.com/sIiT7t8.png"><br><br>
- cdt_engineering [Digital warranty codes] <br><img src="https://i.imgur.com/wfAfnCn.png">
</p>
11. Remember to have download only mode **Without authenticator**
    <p align="center"><img src="https://i.imgur.com/0xFJVuo.png"></p>
12. Place your phone on a stable surface, to not disconnect anything. This process will take up to 15-20 minutes, to get A.24 on your phone, click `Download`
    <p align="center"><img src="https://i.imgur.com/tJiKdLf.png"></p>
13. If anything will not fail, it should look like this
    <p align="center"><img src="https://i.imgur.com/QhJ6fVi.png"></p>

14. Before doing anything, remember to **WIPE down your phone for safety.** Hold down **Vol-, and power button**, In recovery select wipe data, and then **don't** select the option to retrieve contacts, etc. It will cause errors, select the clean wipe. **Act as you had RUI2 from the beggining LOL**

# 4. Unlocking the bootloader - MTK Client
1. Install [USBDk](https://github.com/daynix/UsbDk/releases/)
2. Open the console third time in the [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder
4. Reboot your device, turn it off and Hold down **Vol+, Vol-, and power button** - **(Don't leave the buttons until the bypass is done)**
5. Type `python mtk e metadata,userdata,md_udc` - This command wipes your data. It should look like this:
   <p align="center"><img src="https://i.imgur.com/olGdWYp.png"></p>
6. Unlock the bootloader using command `python mtk da seccfg unlock`, the output should look like this
   <p align="center"><img src="https://i.imgur.com/qezn6Af.png"></p>
      
   **After this, unlock your phone. First boot will take up to 5-20 minutes. Don't panic.**
      
   Bootloader is unlocked, **When you will boot your device, press one time power button to skip dm-verity**, there also will be a 5-second orange-state indicator
      
   -  Green state means the device is locked, it shouldnt show that it's locked on-boot
   -  Yellow state means that an alternate keystore was used to verify the boot image
   -  Orange state indicates that the device is unlocked.
   -  Red state means that a device in the locked or verified state had a boot image that did not verify. 

7. You will boot into RealmeUI with bootloader unlocked.

# 5. Upgrade to RealmeUI 3

1. Go back to the folder of [MTK Client](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip)
2. Open the console in [MTK Client's](https://github.com/bkerler/mtkclient/archive/refs/heads/main.zip) folder, **a tip how to do it faster below**
   <p align="center"><img src="https://i.imgur.com/J5VAWoy.png"></p>
3. Run the payload by simply using command `python mtk payload`, It should look like this: 
   <p align="center"><img src="https://i.imgur.com/Y2mwRhR.png"></p>
   If there is any error with python, you dont have the libaries. get them using command `python -m pip install -r requirements.txt`
   
4. Make sure your phone is powered off, Make sure your phone is connected to your computer, as it is: Hold down **Vol+, Vol-, and power button** - **(Don't leave the buttons until the bypass is done)**
5. MTK Client should output something like this:
      <p align="center"><img src="https://i.imgur.com/KDp2u5O.png"></p>
   
6. Leave the phone alone in the BROM, Run the [SP Flash tool](https://drive.google.com/file/d/1sfsm3EXhIf8TrS5Y-En1mifgg8e9VjXl/view?usp=drive_link) [flash_tool.exe]
7. Click on `Options > Option...`
8. Make sure the right **COM Port** is selected, UART enabled and baud rate is set to 921600.
   <p align="center"><img src="https://i.imgur.com/C6n8awx.png"></p>
9. Get [Haadi's C.14 RUI3 Firmware](https://drive.google.com/file/d/1JezJL-mz8fJC0lkNGMNyQiGCNYxj-pKs/view?usp=share_link) and unpack it
10. Load scatter from Haadi's Firmware
    <p align="center"><img src="https://i.imgur.com/Tzavwau.png"></p>
<p align="center" style="color: red;">IMPORTANT: </p><p align="center">Remember to uncheck:<br>
- opporeserve2 [Signed partition] <br><img src="https://i.imgur.com/sIiT7t8.png"><br><br>
- cdt_engineering [Digital warranty codes] <br><img src="https://i.imgur.com/wfAfnCn.png">
	
11. Remember to have download only mode **Without authenticator**
    <p align="center"><img src="https://i.imgur.com/0xFJVuo.png"></p>
12. Place your phone on a stable surface, to not disconnect anything. This process will take up to 15-20 minutes, to get A.24 on your phone, click `Download`
    <p align="center"><img src="https://i.imgur.com/tJiKdLf.png"></p>
13. If anything will not fail, it should look like this
    <p align="center"><img src="https://i.imgur.com/QhJ6fVi.png"></p>

# 6. Go into Settings and update to C.18

<p align="center" style="color: #909090">Congrats, you now have a unlocked phone with the latest version of RUI3!<br><br><img src="https://i.imgur.com/Z90bwAU.png"></p>
<hr>

# [BONUS] Getting fastboot [TODO]

# Special thanks

> [lemoekq](https://t.me/lemonekq) - The original guide on which this is based<br>
> [Zako Chan](https://t.me/zakolakov106/) - Information about walkthrough with downgrade<br>
> [Tony stark](https://forum.xda-developers.com/m/tony-stark.7582728/) - Provided [RUI2 unlock guide](https://forum.xda-developers.com/t/guide-realme-8-unofficial-new-method-unlock-bootloader-flash-twrp-and-root-rmx3085.4386473/).<br>
> [MtkClient](https://github.com/bkerler/mtkclient) - Basically, without that tool we wouldnt be able to do the unlock.<br>
> [Haadi](https://t.me/Haadi786H) - RUI2/A.19 Firmware files <br>
> [HowWof](https://t.me/HowWof) - A few of suggestions, thanks
> 
> Telegram: [Realme 8 Discussion](https://t.me/Realme8Discussion), [Realme 8 Updates](https://t.me/Realme8Updates), [Realme 8 AOSP](https://t.me/Realme8AOSPGroup)

Thanks for reading, written by [lemonek](https://t.me/lemonekq/) with 💖. Adapted by [me](t.me/driedpampas) also with 💗.
<br><br>
<p align="center" style="color: #909090;">Tested on 8/1/2023</p>
