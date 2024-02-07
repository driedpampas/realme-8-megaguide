  
>   
> Links:  
> MTKClient: [https://drive.google.com/file/d/13KohUUeuzVoGKxVWIuLDZx11PV8EeMBj/view?usp=sharing](https://drive.google.com/file/d/13KohUUeuzVoGKxVWIuLDZx11PV8EeMBj/view?usp=sharing)  
> SP Flash Tool: [https://drive.google.com/file/d/1McZ11On8XbxGgE-hMA\_nZqErHI\_QwjQT/view?usp=sharing](https://drive.google.com/file/d/1McZ11On8XbxGgE-hMA_nZqErHI_QwjQT/view?usp=sharing)  
> MTK Drivers: [https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing](https://drive.google.com/file/d/1UExJQxI1DmBGeDoYPul5YTXitOnsU6zx/view?usp=sharing)  
> Thailand Firmware: [https://drive.google.com/file/d/192KboBbW1eXzb6DWVlGAkGE-PEcgnHBJ/view?usp=sharing](https://drive.google.com/file/d/192KboBbW1eXzb6DWVlGAkGE-PEcgnHBJ/view?usp=sharing)  
> Deep Testing APK: [https://drive.google.com/file/d/1pESMmJef6Gm9YlJAE7OA\_DDNnhFn3Jpz/view?usp=sharing](https://drive.google.com/file/d/1pESMmJef6Gm9YlJAE7OA_DDNnhFn3Jpz/view?usp=sharing)  
> Libusb port filter: [https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/libusb-win32-devel-filter-1.2.6.0.exe/download](https://sourceforge.net/projects/libusb-win32/files/libusb-win32-releases/1.2.6.0/libusb-win32-devel-filter-1.2.6.0.exe/download)

### Flashing Thailand firmware:

We are going to flash this in SP flash tool, first, let's setup MTK authorization bypass (if you have already setup python and drivers then skip this)

1.  Install python from [https://www.python.org/downloads/](https://www.python.org/downloads/) and make sure it's configured

![](https://telegra.ph/file/8644e90695308de2be0c7.png)

Installing MTK drivers

  

1.  Go to the Driver folder, right click cdc.acm.inf and install it.
2.  Install libusb port filter, afterwards click Next and hold volume up and down button, then choose MediaTek USB Port.

![](https://telegra.ph/file/99bc0494740baebde354f.png)

libusb device filter selection.

Now click install, next install UsbDK from here: [https://github.com/daynix/UsbDk/releases/](https://github.com/daynix/UsbDk/releases/)

  

Once you have done that, open a CMD/Powershell in the directory of MTKClient, write _pip3 install -r requirements.txt_ and _python mtk payload,_ hold the volume up and down button and plug the device in

![](https://telegra.ph/file/8d61915200caa6d9aaa26.png)

MTKClient waiting for a device in BROM mode

If everything went well, you should be seeing this:

![](https://telegra.ph/file/a00ff10337914042bf8cb.png)

MTKClient succesfully bypassing authorization

Now open SP Flash tool, go to Options > Option

![](https://telegra.ph/file/824b691bc85200473df5d.png)

Screenshot of SP Flash Tool

Now go to Connection and select UART, set the baud rate to 921600

![](https://telegra.ph/file/8eb7dbb9c6643d887eae0.png)

SP Flash Tool Connection setting

Now, open the scatter file (MT6785\_Android\_scatter.txt) from the directory of the firmware, it should load the firmware

![](https://telegra.ph/file/1339184bc1fed17e6ca1d.png)

SP Flash Tool with the firmware loaded.

Unselect _opporeserve2_ and click the Download button, it should start flashing

Once it is done flashing, you should see this:

![](https://telegra.ph/file/2c07cc828399c79ec50e6.png)

SP Flash Tool when the firmware successfully flashes

Boot to recovery by holding volume down + power button, format the data in recovery and reboot, if the device boots, you have now flashed Thailand firmware.

### Using the deep testing app and unlocking the bootloader:

Download and install the deep testing app, tap "Apply Now" and accept the agreement, you should be seeing this now:

![](https://telegra.ph/file/6f7db30beb0497b33f50b.png)

Realme 8 processing a deep test request.

Wait 3 to 5 minutes, close the app and reopen again, tap "Query verification status" and you should see this:

![](https://telegra.ph/file/c85ec0df92f7004f7b246.png)

Realme 8 with approved deep test application

  

This means your device now has unlocked fastboot access, tap "Start deep testing" and the device will reboot to fastboot mode

![](https://telegra.ph/file/beb8f9c3563ea2c9bd88c.png)

Realme 8 in fastboot mode

If you see this, the device is now in fastboot mode, to unlock the bootloader plug the device into a PC and write _fastboot flashing unlock_ in Fastboot/ADB directory, you should see this:

![](https://telegra.ph/file/828b81d91a3eabcc5d254.png)

Realme 8 after entering fastboot flashing unlock

Press the volume up button, the bootloader is now unlocked, congratulations!

> NOTE: you can return to any EEA/Indian firmware you were on before and still have the bootloader unlocked.  
>   
> Credits:[  
> @bkerler](https://github.com/bkerler/mtkclient) for MTKClient

  

  

EditPublish
