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

    def tmove(self, direction, t):
        if (direction == 1):
            GPIO.output(self.__upin, GPIO.HIGH)
            GPIO.output(self.__dpin, GPIO.LOW)
            time.sleep(t)
            self.stop()
        elif(direction == 0):
            GPIO.output(self.__dpin, GPIO.HIGH)
            GPIO.output(self.__upin, GPIO.LOW)
            time.sleep(t)
            self.stop()
        else:
            return

    def move(self,direction):
        if (direction == 1):
            GPIO.output(self.__upin, GPIO.HIGH)
            GPIO.output(self.__dpin, GPIO.LOW)
        elif (direction == 0):
            GPIO.output(self.__dpin, GPIO.HIGH)
            GPIO.output(self.__upin, GPIO.LOW)
        else:
            return
    def stop(self):
        GPIO.output(self.__upin, GPIO.LOW)
        GPIO.output(self.__dpin, GPIO.LOW)
        return

####################################################################################
# The Sensor class takes modified code from Matt Hawkin's Ultrasonic_2.py located at:
# http://www.raspberrypi-spy.co.uk/2013/01/ultrasonic-distance-measurement-using-python-part-2/
class UltraSonicSensor:
    __start = None
    __stop = None
    __elapsed = None
    __distance = None
    __GPIO_TRIGGER = None
    __GPIO_ECHO = None

    def __init__(self, ep, tp):
        self.__GPIO_ECHO = ep
        self.__GPIO_TRIGGER = tp
        return

    def measure(self):
        # This function measures a distance
        GPIO.output(GPIO_TRIGGER, True)
        time.sleep(0.00001)
        GPIO.output(GPIO_TRIGGER, False)
        self.__start = time.time()

        while GPIO.input(GPIO_ECHO) == 0:
            self.__start = time.time()

        while GPIO.input(GPIO_ECHO) == 1:
            self.__stop = time.time()

        self.__elapsed = self.__stop - self.__start
        self.__distance = (self.__elapsed * 34300) / 2
        return

    def measure_average(self):
        # This function takes 3 measurements and
        # returns the average.
        self.measure()
        distance1 = self.__distance
        time.sleep(0.1)
        self.measure()
        distance2 = self.__distance
        time.sleep(0.1)
        self.measure()
        distance3 = self.__distance
        self.__distance = distance1 + distance2 + distance3
        self.__distance = distance / 3
        return
###################################################################################
class Arm:
    __m1= None
    __m2 = None
    __m3 = None
    __m4 = None
    __m5 = None
    __snsr = [None]*2
    __dsnsr = [23,25,26]
    #Note that Arm() can only take in Motor Objects as parameters
    def __init__(self, m1, m2, m3, m4, m5):

        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.__m4 = m4
        self.__m5 = m5
        return
    #Assign Sensor Pins
    def setsensors(self, s1, s2):
        self.__snsr[0] = s1
        self.__snsr[1] = s2
        GPIO.setup(self.__snsr[0], GPIO.IN)
        GPIO.setup(self.__snsr[1], GPIO.IN)
        return

    #This function simply moves m2 & m3
    def movepiv(self, direction):
        self.__m2.move(direction)
        self.__m3.move(direction)
        return

    #Function Below Needs Lots of Work
    def readsensors(self):
        return

    #This function needs work
    #It will set the robot arm to a default state.
    def dconfig(self):
        self.stoparm()
        mainflag = 1
        flag = [1,1,1,1,1,1]
        while(mainflag == 1):
            return
        return



    def stoparm(self):
        self.__m1.stop()
        self.__m2.stop()
        self.__m3.stop()
        self.__m4.stop()
        self.__m5.stop()
        return