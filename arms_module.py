#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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
