## Pi-ON-OFF

To be used with my RPi hat with voltage regulator and off switch. 
![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/8d26435a3e49da940b293ba6d257160a3ecb25c0/pihat.png)

## Default pinout of the hat is 

1. pin 2 - 5v
1. pin 3 - GPIO 2 - SDA 
1. pin 4 - 5v
1. pin 5 - GPIO 3 - SCL
1. pin 6 - GND
1. pin 7 - GPIO 4 - SQW
1. pin 9 - GND
1. pin 14 - GND
1. pin 20 - GND
1. pin 25 - GND
1. pin 30 - GND
1. pin 34 - GND
1. pin 39 - GND
1. pin 40 - GPIO21 - SLEEP

the pinout can be changed by removing the shunt on the corresponding pin, and adding a jumper wire to the pin of choice. the same shunts can be used to enable/disable features.
![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/49924ea4ff7896585d0b00afd07f6906150456ac/pictures/WhatsApp%20Image%202021-05-19%20at%207.50.35%20PM%20(2).jpeg)

## Installation of ON/OFF script

1. [Connect to your Raspberry Pi via SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)

2. Clone this repo: `git clone https://github.com/amasood1193/Pi-ON-OFF.git`
3. Run the setup script: `./pi-power-button/script/install`

## Uninstallation of ON/OFF script

If you need to uninstall the power button script in order to use GPIO21 for another project or something:

1. Run the uninstall script: `./pi-power-button/script/uninstall`

## Configuing Real Time Clock. 

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

power off script is based on howchoo power button and Mike Armstrongs work. 
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi
