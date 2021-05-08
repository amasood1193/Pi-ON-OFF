## Pi-ON-OFF

To be used with my RPi hat with voltage regulator and off switch. 
![alt text](https://github.com/amasood1193/Pi-ON-OFF/blob/8d26435a3e49da940b293ba6d257160a3ecb25c0/pihat.png)

Default pinout of the hat is 
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


## Installation

1. [Connect to your Raspberry Pi via SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)

2. Clone this repo: `git clone https://github.com/amasood1193/Pi-ON-OFF.git`
3. Run the setup script: `./pi-power-button/script/install`

## Uninstallation

If you need to uninstall the power button script in order to use GPIO21 for another project or something:

4. Run the uninstall script: `./pi-power-button/script/uninstall`



its based on howchoo power button and Mike Armstrongs work. 
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi
