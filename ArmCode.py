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
GPIO.setwarnings(False)

U = 1
D = 0
R = U
L = D

#InitPin,UpPin,DownPin
#time.sleep(timeinseconds) -> Same as arduino Delay(timeinms)
m1 = Motor(23, 15, 14) # changed from 18 to s3
m2 = Motor(22, 27, 17) #changed from 11 to 22, and 9 to 27, and 10 to 17
m3 = Motor(21, 20, 16)
m4 = Motor(13, 6, 5)
m5 = Motor(7, 25, 24) #changed from 8 to 24
# DOWN is close
# UP is open
arm1 = Arm(m1, m2, m3, m4, m5)
#tmove(direction, time in seconds)
#m1.tmove(U,1.1)

#sensor1 = UltraSonicSensor(23, 24)

#print (sensor1.measure())
print("Sensor 1's Distance: ", irdist.get_distance(0))
print("Sensor 2's Distance: ", irdist.get_distance(1))


