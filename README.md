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

## Installation of ON/OFF script

1. [Connect to your Raspberry Pi via SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)

2. Clone this repo: `git clone https://github.com/amasood1193/Pi-ON-OFF.git`
3. Run the setup script: `./pi-power-button/script/install`

## Uninstallation of ON/OFF script

If you need to uninstall the power button script in order to use GPIO21 for another project or something:

1. Run the uninstall script: `./pi-power-button/script/uninstall`

## Configuing Real Time Clock. 

0. Make sure that the shunts are installed on SDA, SCL, and SQW

1. Type in [sudo raspi-config] set up raspberry pi and prepare to enable i2c interface, alternatively you can go to start > prefference > raspberry pi configuration. and enable it from there. 

![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/c7405fdc88c58e01fd788f40f2cd52225aeb679a/pictures/raspi%20config.JPG)
![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/19e3cf43d04addeb7a13eb8f7e7e76a83ab0a452/pictures/I2c%20enable.JPG)

2. type in [sudo vim.tiny /etc/modules] to open file modules

3. add i2c-dev device like picture below
![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/b28de494a65fcb38d893d0694359a955f7aacae2/pictures/add%20i2c%20device.JPG)

4. install i2c-tools ,type in [sudo apt-get install i2c-tools]

5. type in [sudo reboot] wait the raspberry pi restart

6. once pi has restarted, type in [sudo i2cdetect –y 1], if RTC works ,it should be like picture below
![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/b28de494a65fcb38d893d0694359a955f7aacae2/pictures/WhatsApp%20Image%202021-05-19%20at%207.50.36%20PM%20(2).jpeg)

7. Type in [sudo su –] change root user

8. Type in [modprobe i2c-dev] to load I2C device

9. Type in [echo "ds1307 0x68" > /sys/class/i2c-adapter/i2c-1/new_device] add RTC to
system

Then you can use “hwclock” command to use this RTC module
If you want to know more about hwclock command you can type in “man
hwclock” to get details
A brief description like following:
Command [hwclock –r] to get RTC time
Command [hwclock -w]set the system time to RTC time

![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/d4b96212a2cd0fe9ab5a38cc26f32c51ae67bd68/pictures/WhatsApp%20Image%202021-05-19%20at%207.50.35%20PM.jpeg)

power off script is based on howchoo power button and Mike Armstrongs work. 
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi

## Extra parts if needed

## Molex 4 pin connector  
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





 
