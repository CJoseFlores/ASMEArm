#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

U = 1
D = 0
R = U
L = D

class Motor:
    __ipin = None
    __upin = None
    __dpin = None
    __speed = None
    __index = None

    def __init__(self, ipin, upin, dpin):
        self.__ipin = ipin
        self.__upin = upin
        self.__dpin = dpin
        GPIO.setup(ipin, GPIO.OUT)
        GPIO.setup(upin, GPIO.OUT)
        GPIO.setup(dpin, GPIO.OUT)
        GPIO.output(ipin, GPIO.HIGH)
        self.__speed = 0

    def move(self, direction):
        if (direction == 1):
            GPIO.output(self.__upin, GPIO.HIGH)
            GPIO.output(self.__dpin, GPIO.LOW)
        elif(direction == 0):
            GPIO.output(self.__dpin, GPIO.HIGH)
            GPIO.output(self.__upin, GPIO.LOW)
        else:
            return

    def stop(self):
        GPIO.output(self.__upin, GPIO.LOW)
        GPIO.output(self.__dpin, GPIO.LOW)
        return

#InitPin,UpPin,DownPin
#time.sleep(timeinseconds) -> Same as arduino Delay(timeinms)
m1 = Motor(18, 15, 14)
m2 = Motor(11, 9, 10)
m3 = Motor(21, 20, 16)
m4 = Motor(13, 6, 5)
m5 = Motor(7, 25, 8)
# DOWN is close
# UP is open

