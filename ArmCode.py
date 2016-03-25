#! /usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

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


class Arm:
    __motorID = None
    __speed = None
    __direction = None

    def __init__(self, motorID, speed, direction):
        self.__motorID = motorID
        self.__speed = speed
        self.__direction = direction

    def set_mtrid(self,motorID):
        self._motorID = motorID

    def get_mtrid(self):
        return(self.__motorID)

    def set_speed(self,speed):
        self.__speed = speed

    def get_speed(self):
        return(self.__speed)

    def set_dir(self,direction):
        self.__direction = direction

    def get_dir(self):
        return(self.__direction)

    def movemotor(self, motorID, speed, direction, time):
        # Checking valid parameters
        if (motorID < 1 or motorID > 2):
            return
        if (direction < 0 or direction > 1):
            return
        if (speed < 0 or speed > 10):
            return
        if (time < -1 or time > 41):
            return
        self.__speed = 105 + speed * 10
        # moving the motor



