## Pi-ON-OFF

To be used with my RPi hat with voltage regulator and off switch. 
![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/8d26435a3e49da940b293ba6d257160a3ecb25c0/pihat.png)

## Default pinout of the hat is 

pin 2 - 5v  
pin 3 - GPIO 2 - SDA   
pin 4 - 5v  
pin 5 - GPIO 3 - SCL  
pin 6 - GND  
pin 7 - GPIO 4 - SQW  
pin 9 - GND  
pin 14 - GND  
pin 20 - GND  
pin 25 - GND  
pin 30 - GND  
pin 34 - GND  
pin 39 - GND  
pin 40 - GPIO21 - SLEEP  

*in the earlier versions, GNDs are not connected to the pins, instead the screws ground the hat to the pi and the screen)

the pinout can be changed by removing the shunt on the corresponding pin, and adding a jumper wire to the pin of choice. the same shunts can be used to enable/disable features.
![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/49924ea4ff7896585d0b00afd07f6906150456ac/pictures/WhatsApp%20Image%202021-05-19%20at%207.50.35%20PM%20(2).jpeg)

## Initial Setup

1. before starting, make sure that the voltage adjuster trim pot is all the way counter clock wise, give it around 25 turns just to be sure, this will make sure that the starting voltage is fixed at 5. and not at 12. as this can damage the RTC module. 

2. then give it 12v on the Batt, 12v on the IGN, and ground on the GND, once it starts, check voltage between 5v header pin and any ground, (best to use the pads on the mounting holes as a clean ground) to make sure the output voltage is within spec (set it to 5.15 if pi shows the lightning icon). if so, short the 5v header pins with the shunt jumber which would then power on the PI. 

## Premade Rom for this hat.  
ive made a image for a full PiDash rom by Alex Bartonek, you can just download, extract, and flash to your SD card using "Raspberry Pi Imager", this rom is a stripped out version of dietpi for use as a dash on in car installs, and boots in around 20 seconds.   
to flash the rom, 

download link for the rom.  
https://drive.google.com/file/d/1YWZ-EpVW9RMVvId_ljVKrSpwBvQlT_4O/view?usp=sharing

0. after downloading, extract the image to any folder
1. install Raspberry Pi Imager,   
download link https://www.raspberrypi.org/software/
3. open it
4. click "choose OS"
5. scroll down and select "use custom"
6. select the image you just downloaded in step 0 
7. inset SD card in the computer, or use a SD card USB adapter.
8. click "choose SD card" and select the SD card you want to install the image on.  
9. select "write" to write image to the SD card.  
10. once the write is complete, insert the SD card back in the pi, power it on and youre all set. 
11. set your RTC time with following command in terminal (sudo timedatectl set-time 'YYYY-MM-DD HH:MM:SS') for example ('sudo timedatectl set-time '2021-05-26 15:45:20') without the (,) and hit enter.
12. to connect to internet, open updater on the desktop, and click "enable networking", it can take a couple of minutes, and if it doesnt work, restart and try the step 12 again. 

*point to note: this has a shutdown feature, as a result if the hat is not plugged in, and the shunt for "off" is not installed, the pi with shutdown before it even fully boots up, for bench testing purposes, you can install a jumper between pin 40 and gnd (short pin 40 to gnd), to stop the pi from shutting down***
  
*SD card has to be minimum 8gb  
and you wouldnt need to do anything with the code, the rom has real time clock, pi on, off script, and tunerstudio already installed and set to start at boot.   



all credits to alex bartonek for putting in the time to create this rom,  
https://www.bartonekdragracing.com/encyclopedia/pidash-knowledge-base/
https://www.facebook.com/PiDashByAB   
follow his work, and find out about more features imbedded within the rom such as file sharing and backups etc.   

## Installation of ON/OFF script 
alternatively you can build it manually on a rom of your chioce
1. [Connect to your Raspberry Pi via SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)

2. Clone this repo: `git clone https://github.com/Howchoo/pi-power-button.git`
3. Run the setup script: `./pi-power-button/script/install`

***if the git clone command doesnt work, 
run these 
1. sudo apt update
2. sudo apt install git

## Make changes to the downloaded script

1. edit script by 'sudo nano /usr/local/bin/listen-for-shutdown.py'

2. replace the text with

#!/usr/bin/env python


import RPi.GPIO as GPIO
import subprocess
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while GPIO.input(21) == 0:
        time.sleep(2)

subprocess.call(['sh', './home/pi/stopts.sh'])
time.sleep(8)

subprocess.call(['shutdown', '-h', 'now'], shell=False) 

3. Once the text has been replaced, click CTRL+X, Y, enter to save. 

3. test script using 'sudo /etc/init.d/listen-for-shutdown.sh start'

## Uninstallation of ON/OFF script

If you need to uninstall the power button script in order to use GPIO21 for another project or something:

1. Run the uninstall script: `./pi-power-button/script/uninstall`

## Configuing Real Time Clock. 

0. Make sure that the shunts are installed on SDA, SCL, and SQW

use this guide as its actually much better. 
https://learn.adafruit.com/adding-a-real-time-clock-to-raspberry-pi/set-up-and-test-i2c

alternatively.

1. Type in [sudo raspi-config] set up raspberry pi and prepare to enable i2c interface, alternatively you can go to start > prefference > raspberry pi configuration. and enable it from there. 

2. type "sudo nano /boot/config.txt"
and at the end, add the following 

dtoverlay=i2c-rtc,ds1307

save by CTRL+O, ENTER, CTRL+X

3. sudo reboot, 

4. once its back on, type "sudo i2cdetect -y 1"
you should see a table with UU where 68 previously was, this means the module is being used, if you dont, check to see that you are editing the right file, as in dietpi etc you will need to edit "sudo nano /dietpi/config.txt" instead. 

5. now disable the fake clock by 
"sudo apt-get -y remove fake-hwclock
sudo update-rc.d -f fake-hwclock remove
sudo systemctl disable fake-hwclock"

6. with fake clock off. run "sudo nano /lib/udev/hwclock-set", and comment the following lines out by adding a # behind them. 

#if [ -e /run/systemd/system ] ; then
#exit 0
#fi
#/sbin/hwclock --rtc=$dev --systz --badyear
#/sbin/hwclock --rtc=$dev --systz

save by CTRL+O, ENTER, CTRL+X

7. sync time on the pi by connecting it to a network, once the time is sync, check time by writing "date" or "sudo hwclock -r"
if time is correct, write "sudo hwclock -w" to save the time on the RTC. 

8. if the time is in a different region, write "sudo hwclock -l", if this time is correct write "sudo hwclock -l -w" to save it.  


![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/d4b96212a2cd0fe9ab5a38cc26f32c51ae67bd68/pictures/WhatsApp%20Image%202021-05-19%20at%207.50.35%20PM.jpeg)

power off script is based on howchoo power button and Mike Armstrongs work. 
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi

## Extra parts if needed

## raspberry pi stackable header 
Digi-Key Part Number: 1528-1385-ND.   

## Molex 4 pin connector (Mini-Fit Jr 5557)  
Manufacturer Part Number	0766500075  (for kit)  
Digi-Key Part Number	23-0766500075-ND  (for kit)     
*Digi-Key Part Number if you want to buy seperately, Receptacle	WM3701-ND, terminals WM2501-ND  
RS-components part numbers (seperate parts), Receptacle 484-1754, terminals 172-9134    

## shunt jumpers (use any shunt with a 0.1" or 2.54mm pitch)  
Manufacturer Part Number	STC02SYAN  
Digi-Key Part Number	S9000-ND  
RS-component part number 251-8503  

## battery holder  
Manufacturer Part Number	3034TR  
Digi-Key Part Number	36-3034TR-ND  
RS-component part number 185-4652  





 
