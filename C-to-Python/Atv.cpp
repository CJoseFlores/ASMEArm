/*
  Atv.h v-3.3 - Atv library for OWI-535
  Copyright (c) 2014 Wilmer Arellano.  All right reserved.
*/


// include this library's description file
#include "Atv.h"
#include <Arduino.h>

// Constructor /////////////////////////////////////////////////////////////////
// Function that handles the creation and setup of instances

Atv::Atv(int pin)
{
  // do whatever is required to initialize the library
  for(index = 3; index < 13; index++){
      digitalWrite(index, LOW);
      pinMode(index, OUTPUT);
} 
  sensorPin = pin;
}

// Public Methods //////////////////////////////////////////////////////////////
// Functions available Atv sketches

void Atv::initialize(int time){
	unsigned long start, finish, timeElapsed, timeElapsedPrevious; // variables to measure time
	start = millis()/1000; // "millis()" returns current time in milliseconds
	finish = millis()/1000;// "start" and "finish" measure time in seconds. Why?
	timeElapsed = finish - start;
	timeElapsedPrevious = 1;
	while((timeElapsed) < time){ // Wait for time seconds
		if(timeElapsed != timeElapsedPrevious) // Print seconds elapsed if seconds increased
			Serial.println(timeElapsed);
		checkData(); // Use this time to position your grip manually
		timeElapsedPrevious = timeElapsed; // Store previous seconds count
		finish = millis()/1000; // finish will increase in each iteration
		timeElapsed = finish - start; // Calculate new seconds count
	}
}

void Atv::checkData(){
  int data, dist;
  data = Serial.read();

  if(data > 48 && data < 54){
    Serial.print("Motor: ");
    motorID = data - 48;
    Serial.println(motorID);
    Speed = 2;
    Duration = 1;
  }
  if(data == 65 || data == 97){
    moveMotor(motorID, 0, Speed, Duration);
  } 
  if(data == 83 || data == 115){
    moveMotor(motorID, 1, Speed, Duration);
  } 
  if(data == 87 || data == 119){
    moveMotor(motorID, 1, Speed, Duration);
  }  
  if(data == 90 || data == 122){
    moveMotor(motorID, 0, Speed, Duration);
  }
  if(data == 68 || data == 100){
  dist = distance();
  Serial.print("Distance: ");
  Serial.println(dist);
  }
}

void Atv::moveMotor(int motorID, int Direction, int Speed, int time){
// Checking valid parameters  
  if(motorID < 1 || motorID > 5){
    return;
  }
  if(Direction < 0 || Direction > 1){
    return;    
  }  
  if(Speed < 0 || Speed > 10){
    return;
  }
    if(time < -1 || time > 41){
    return;
  }
  Speed = 205 + Speed*5;
// Moving motor backwards 
for(index = 0; index <= time; index++){
  if(Direction == 0){
    if(motorID != 2){
      analogWrite(motorID + 2, Speed);
      digitalWrite(motorID + 7, Direction);
      if(time == 40){
        index = 40;
      }
    }
    else{
      analogWrite(motorID + 7, 255 - Speed);
      digitalWrite(motorID + 2, 1 - Direction);
      if(time == 40){
        index = 40;
      }
    }
  }
// Moving Motor forward  
  if(Direction == 1){
    if(motorID != 2){
      analogWrite(motorID + 2, 255 - Speed);
      digitalWrite(motorID + 7, Direction);
      if(time == 40){
        index = 40;
      }
    }
     else{
      analogWrite(motorID + 7, Speed);
      digitalWrite(motorID + 2, 1- Direction);
      if(time == 40){
        index = 40;
      }
    }
  }
if(time < 40){
    delay(50);    
    analogWrite(motorID + 2, 0);
    digitalWrite(motorID + 7, 0);
  }   
}
}
void Atv::moveMotorDF(int motorID, int Direction, int Speed, int time){
// Checking valid parameters  
  if(motorID < 1 || motorID > 2){
    return;
  }
  if(Direction < 0 || Direction > 1){
    return;    
  }  
  if(Speed < 0 || Speed > 10){
    return;
  }
    if(time < -1 || time > 41){
    return;
  }
  Speed = 105 + Speed*10;
// Moving motor
for(index = 0; index <= time; index++){
  if(motorID == 1){
    analogWrite(5 , Speed);
    digitalWrite(4 , Direction);   
  }
  else{
    analogWrite(6 , Speed);
    digitalWrite(7 , Direction);    
  }
  

  if(time == 40){
    index = 40;
    }
if(time < 40){
if(time != 0)
    delay(50);    
    analogWrite(2*motorID + 2, 0);
    digitalWrite(2*motorID + 3, 0);
  }   
}
}

int Atv::distance(){
    int dist = 0;
    long adcRes;
//    pinMode(pin, INPUT);
  if(sensorPin < 0 || sensorPin > 5){
    Serial.println("Wrong Pin for distance");
    return -1;
  }
    adcRes = analogRead(sensorPin);
//    Serial.println("Voltage");
//    Serial.println(adcRes);
    adcRes = adcRes*500/1023; // Transform  ADC result into volts
	if(adcRes == 0){
		adcRes = 1;    
	}
//    Serial.println(adcRes);
    adcRes = 3200/adcRes-3;   // Calculates distance
    dist = (int)adcRes;
    return dist;
}
int Atv::distanceW(){
    int dist = 0;
    long adcRes;
//    pinMode(pin, INPUT);
  if(sensorPin < 0 || sensorPin > 5){
    Serial.println("Wrong Pin for distance");
    return -1;
  }
    adcRes = analogRead(sensorPin);
//    Serial.println("Voltage");
//    Serial.println(adcRes);
    adcRes = adcRes*500/1023; // Transform  ADC result into volts
	if(adcRes == 0){
		adcRes = 1;    
	}
//    Serial.println(adcRes);
    adcRes = 2177*adcRes/1000;   // Calculates distance
    dist = (int)adcRes;
    return dist;
}