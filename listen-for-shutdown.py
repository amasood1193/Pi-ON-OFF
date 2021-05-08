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
