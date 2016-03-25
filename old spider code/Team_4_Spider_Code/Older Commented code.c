#include <Atv.h>
Atv leftSensor(0), centerSensor(1); // Creates two instance of Atv, one for left sensor, one for center sensor
int LEFT = 0, DOWN = 0; // Backward direction, Left and Down
int RIGHT = 1, UP = 1; // Forward direction, Right and Up
int ledtDistance, centerDistance;

void setup() { 
  
  // Just to know program is running
  Serial.begin(9600);
  Serial.println("Hello");
  
  // Make sure both motors are stopped
  leftSensor.moveMotorDF(1, LEFT, 1, 0);
  leftSensor.moveMotorDF(2, LEFT, 1, 0);
  
  // Wait some time to set robot in start position
  delay(2000);
  
  // Robot will find wall if set at convenient angle
  findWall(); 
}
void loop() {    //Here, the forward, stabilize and cornerTurn functions are called upon (respectively)
  forward();
  stabilize();
  cornerTurn();
}
void findWall(){
  // Get distance to left wall. Left sensor
  ledtDistance = leftSensor.distance();
  // "While loop" will move motor forward until left sensor is close enough to the wall
  while(ledtDistance > 20){
    // Move forward. Motors were wired to move forward this way
    leftSensor.moveMotorDF(1, LEFT, 3, 40);
    leftSensor.moveMotorDF(2, LEFT, 3, 40);
    // Refresh distance to left wall. Left sensor
    ledtDistance = leftSensor.distance();
    // Next two lines good for debugging
    Serial.print("Distance: "); // This line is optional if you want to monitor distance in the computer
    Serial.println(ledtDistance); // This line is optional if you want to monitor distance in the computer
  }
  // Position robot to follow left wall
    leftSensor.moveMotorDF(1, LEFT, 3, 0); // Stop right motor to align with wall
    delay(1000); // Continue for certain amount of time
    leftSensor.moveMotorDF(2, LEFT, 3, 0); // Stop the other motor
}

void forward(){   //This function simple makes the spider move forward as long as the center sensor does not sense a wall within 20 arbitrary units
 centerDistance = centerSensor.distance();
 while(centerDistance > 20){

 temp = atv.distance();
  atv.moveMotor(1, LEFT, 3, 40);    //Here both motors are moving forward
 atv.moveMotor(2, LEFT, 3, 40);
 Serial.print("Distance: "); // This line is optional if you want to monitor distance in the computer
 Serial.println(temp); // This line is optional if you want to monitor distance in the computer
 }
}

void stabilize(){
  ledtDistance = leftSensor.distance();
  if (ledtDistance < 20 ){    //Will only execute the command below if the left sensor detects an object at a distance less than 20 units
    leftSensor.moveMotorDF(1, LEFT, 3, 0);     // Stops the right sensor, so the spider turns right
    delay(1000);
  }
  if (ledtDistance > 20 ){   //Will only execute the command below if the left sensor detects an object at a distance greater than 20 units
    leftSensor.moveMotorDF(2, LEFT, 3, 0);    //Stops the left sensor, so the spider turns left
    delay(1000);
  }
}
        
void cornerTurn(){
  centerDistance = centerSensor.distance();    
  ledtDistance = leftSensor.distance();
  if (ledtDistance && centerDistance == 20){   //The following commands will only execute if both the left sensor and center sensor detect the same distance (20 units)
        leftSensor.moveMotorDF(1, RIGHT, 3, 40);    //Runs the right motor backwards
        leftSensor.moveMotorDF(2, LEFT, 3, 40);  //Runs the left motor forward, so the whole spider is turning right
        delay (1000);
  }
  
}
        