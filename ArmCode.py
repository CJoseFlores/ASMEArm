#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

UP = 1
DOWN = 0
RIGHT = UP
LEFT = DOWN

motorOneInit = 18
motorTwoInit = 11
motorTreeInit = 21
motorFourInit = 13
motorFiveInit = 22

############################################################################################

motorOneLeft = 14
motorOneRight = 15

motorTwoLeft = 10
motorTwoRight = 9

motorTreeLeft = 16
motorTreeRight = 20

motorFourLeft = 19
motorFourRight = 26

motorFiveLeft = 17
motorFiveRight = 27

#############################################################################################

GPIO.setup(motorOneInit, GPIO.OUT)
GPIO.setup(motorTwoInit, GPIO.OUT)
GPIO.setup(motorTreeInit, GPIO.OUT)
GPIO.setup(motorFourInit, GPIO.OUT)
GPIO.setup(motorFiveInit, GPIO.OUT)
GPIO.setup(motorOneLeft, GPIO.OUT)
GPIO.setup(motorOneRight, GPIO.OUT)
GPIO.setup(motorTwoLeft, GPIO.OUT)
GPIO.setup(motorTwoRight, GPIO.OUT)
GPIO.setup(motorTreeLeft, GPIO.OUT)
GPIO.setup(motorTreeRight, GPIO.OUT)
GPIO.setup(motorFourLeft, GPIO.OUT)
GPIO.setup(motorFourRight, GPIO.OUT)
GPIO.setup(motorFiveLeft,GPIO.OUT)
GPIO.setup(motorFiveRight,GPIO.OUT)
######################################################
GPIO.output(motorTreeInit,GPIO.HIGH)
GPIO.output(motorTreeRight,GPIO.HIGH)
time.sleep(.5)
GPIO.output(motorTreeRight,GPIO.LOW)

#GPIO.output(motorTwoInit,GPIO.HIGH)
#GPIO.output(motorTwoLeft,GPIO.HIGH)
#time.sleep(.2)
#GPIO.output(motorTwoLeft,GPIO.LOW)
#Left is Down for: 2
#Right is Up for: 2
#Left is Up for:
#Right is Down for:


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
        self.__speed = 0

    def movemotor(self, direction):
        if (direction == 1):

Motor m1(1,2,3)