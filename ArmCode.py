#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import mcp3008
import irdist
import os
from arms_module import Motor
from arms_module import Arm
from arms_module import UltraSonicSensor

GPIO.setmode(GPIO.BCM)#Sets the ping Numbering System
GPIO.cleanup() #Defaults pins to input, used to not power-up with code
GPIO.setwarnings(False)

U = 1
D = 0
R = U
L = D

#InitPin,UpPin,DownPin
#time.sleep(timeinseconds) -> Same as arduino Delay(timeinms)
m1 = Motor(18, 15, 14)
m2 = Motor(11, 9, 10)
m3 = Motor(21, 20, 16)
m4 = Motor(13, 6, 5)
m5 = Motor(7, 25, 8)
# DOWN is close
# UP is open
arm1 = Arm(m1, m2, m3, m4, m5)
#tmove(direction, time in seconds)
#m1.tmove(U,1.1)

sensor1 = UltraSonicSensor(23, 24)

print ("sensor1.measure")



