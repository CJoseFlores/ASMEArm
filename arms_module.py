#! /usr/bin/env python
import RPi.GPIO as GPIO
import time
import mcp3008
import irdist

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Motor:
    __upin = None
    __dpin = None
    __speed = None
    __index = None

    def __init__(self, upin, dpin):
        self.__upin = upin
        self.__dpin = dpin
        GPIO.setup(upin, GPIO.OUT)
        GPIO.setup(dpin, GPIO.OUT)
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
#This class is working well, but this kind of sensor will not suit our purposes
class UltraSonicSensor:
    __start = None
    __stop = None
    __elapsed = None
    __distance = None
    __GPIO_T = None
    __GPIO_E = None

    def __init__(self, ep, tp):
        self.__GPIO_E = ep
        self.__GPIO_T = tp
        GPIO.setup(self.__GPIO_T, GPIO.OUT)
        GPIO.setup(self.__GPIO_E, GPIO.IN)
        GPIO.output(self.__GPIO_T, False)
        return

    def measure(self):
        # This function measures a distance
        GPIO.output(self.__GPIO_T, True)
        time.sleep(0.00001)
        GPIO.output(self.__GPIO_T, False)

        while GPIO.input(self.__GPIO_E) == 0:
            self.__start = time.time()

        while GPIO.input(self.__GPIO_E) == 1:
            self.__stop = time.time()

        self.__elapsed = (self.__stop) - (self.__start)
        self.__distance = (self.__elapsed * 17150)
        self.__distance = round(self.__distance, 2)

        return self.__distance

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
        return self.__distance
###################################################################################
class Arm:
    __m1= None
    __m2 = None
    __m3 = None
    __m4 = None
    __snsr = None
    #Note that Arm() can only take in Motor Objects as parameters
    def __init__(self, m1, m2, m3, m4, snsr):
        self.__m1 = m1
        self.__m2 = m2
        self.__m3 = m3
        self.__m4 = m4
        self.__snsr = snsr
        return

    #This dconfig is based from the original plan.
    #This function will set the robot arm to the default state.
    #The first if statement refers to the sensor connected to channel 1 of the mcp3008
    #The second if statement refers to the sensor connected to channel 2 of the mcp 3008
    def defaultconfig1(self):
        self.stoparm()
        stopflag = [0,0]
        while(stopflag[0] == 0 or stopflag[1] == 0):
            if(irdist.get_distance(1)>123123): #12123 will be replaced with a certain distance reading, reading from channel 1. Ch1 sensor on top of m1
                self.__m1.move(1)#moves up
            else:
                self.__m1.stop()
                stopflag[0] = 1
            if(irdist.get_distance(2)>123123): #Sensor Connected to Channel 2, next to the baseplate
                self.__m2.move(0)#moves down
            else:
                self.__m2.stop()
                stopflag[1] = 1
        return
    #This is from the second plan, where we have 1 sensor on the bottom, 1 on top of m5, and then
    #1 one possibly on top of m1

    def defaultconfig2(self):
        self.stoparm()
        stopflag = 0
        while(stopflag == 0):
            if(irdist.get_distance(1)>5): #ch1 sensor is ontop of m1. If the sensor doesn't detect the arm part, the following if statements
                if(self.__snsr.measure()<123123):
                    self.__m1.move(1) #m1 begins to move up if the sensor is too low to the ground.
                    self.__m2.stop()
                elif(self.__snsr.measure()>123123):
                    self.__m2.move(0) #m2 begins to move down if the sensor is too high from the ground.
                    self.__m1.stop()
            else:
                self.__stoparm() #stops all arm movement/operation. The arm should now be in default position.
            stopflag = 1
        return

    #The code below is the original plan.
    #This function will lunge into position to grab or drop the payload
    def lunge1(self):
        self.stoparm()
        stopflag = 0
        while(stopflag == 0):
            if(irdist.get_distance(2)<123123):
                self.__m1.move(0)#moves down
                self.__m2.move(1)#moves up
            else:
                self.stoparm()
                stopflag = 1
        return

    def lunge2(self):
        self.stoparm()
        stopflag = 0
        while (stopflag == 0):
            if (irdist.get_distance(3) < 123123):#ch3 sensor is the sensor on top of the rover.
                if (self.__snsr.measure() < 123123):
                        self.__m1.move(0)  # m2 begins to move down if the sensor is too high to the ground.
                        self.__m2.stop()
                elif (self.__snsr.measure() > 123123):
                        self.__m2.move(1)  # m3 begins to move up if the sensor is too low from the ground.
                        self.__m1.stop()
            else:
                self.__stoparm()
                stopflag = 1
        return

    #This function grabs or releases the payload. "action" means either grab or release
    def claw(self, action):
        self.stoparm()
        self.__m4.tmove(action,1.2)#Moves for 1.2 seconds
        return

    def stoparm(self):
        self.__m1.stop()
        self.__m2.stop()
        self.__m3.stop()
        self.__m4.stop()
        return