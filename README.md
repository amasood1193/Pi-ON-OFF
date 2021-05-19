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


## Installation

1. [Connect to your Raspberry Pi via SSH](https://www.raspberrypi.org/documentation/remote-access/ssh/)

2. Clone this repo: `git clone https://github.com/amasood1193/Pi-ON-OFF.git`
3. Run the setup script: `./pi-power-button/script/install`

## Uninstallation

If you need to uninstall the power button script in order to use GPIO21 for another project or something:

1. Run the uninstall script: `./pi-power-button/script/uninstall`



its based on howchoo power button and Mike Armstrongs work. 
https://howchoo.com/g/mwnlytk3zmm/how-to-add-a-power-button-to-your-raspberry-pi
