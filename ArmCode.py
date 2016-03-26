#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
from arms_module import Motor
from arms_module import Arm

GPIO.setmode(GPIO.BCM)
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

arm1.movepiv(U)
time.sleep(.5)
arm1.stoparm()