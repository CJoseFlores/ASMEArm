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
        return

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

class Arm:
    __m = [None]*5
    #Note that Arm() can only take in Motor Objects as parameters
    def __init__(self, m1, m2, m3, m4, m5):

        self.__m[0] = m1
        self.__m[1] = m2
        self.__m[2] = m3
        self.__m[3] = m4
        self.__m[4] = m5
        return
    #The Below function moves motors that move in the same direction, i.e. m2-m4
    def movemost(self, direction):
        for i in range(1,4):
            self.__m[i].move(direction)
        return

    def stopmost(self, direction):
        for i in range(1,4):
            self.__m[i].stop()
        return