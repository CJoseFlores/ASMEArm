#include <Atv.h>
#define LEFT 0
#define RIGHT 1
Atv leftSensor(2), centerSensor(1); // Creates two instance of Atv, one for left sensor, one for center sensor
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
void loop() {
  forward();
  stabilize();
  cornerTurn();
}
void findWall(){
  // Get distance to left wall. Left sensor
  ledtDistance = leftSensor.distance();
  // "While loop" will move motor forward until left sensor is close enough to the wal
  while(ledtDistance > 10){
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
    leftSensor.moveMotorDF(2, LEFT, 3, 0); // Stop right motor to align with wall
    delay(1000); // Continue for certain amunt of time
    leftSensor.moveMotorDF(1, LEFT, 3, 0); // Stop the other motor
    
} 

void forward(){   //This function simple makes the spider move forward as long as the center sensor does not sense a wall within 20 arbitrary units
 centerDistance = centerSensor.distance();
  while(centerDistance > 30){

     centerSensor.moveMotorDF(1, LEFT, 3, 40);
     centerSensor.moveMotorDF(2, LEFT, 3, 40);
     centerDistance = centerSensor.distance();
     Serial.print("Distance: "); // This line is optional if you want to monitor distance in the computer
     Serial.println(centerDistance); // This line is optional if you want to monitor distance in the computer
  }

}

void stabilize(){
  ledtDistance = leftSensor.distance();
  if (ledtDistance < 30 ){
    leftSensor.moveMotorDF(2, LEFT, 3, 0);
    delay(500);    //This is how long the motor is off for 
    leftSensor.moveMotorDF(2, LEFT, 3, 40);    // Stops the right motor, so the spider turns right
    delay(100);   //This is how long the motor is still on
  }
  if (ledtDistance > 30 ){
    leftSensor.moveMotorDF(1, LEFT, 3, 0); 
    delay(500);   //This is how long the motor is off for 
    leftSensor.moveMotorDF(1, LEFT, 3, 40);   //Stops the left motor, so the spider turns left
    delay(100);   //This is how long the motor is off for 
  }
}
        
void cornerTurn(){
  centerDistance = centerSensor.distance();
  ledtDistance = leftSensor.distance();
  if (ledtDistance && centerDistance <= 30){
        leftSensor.moveMotorDF(2, RIGHT, 3, 40);    //Runs the right motor backwards
        leftSensor.moveMotorDF(1, LEFT, 3, 40);  //Runs the left motor forward, so the whole spider is turning right
        delay (1000);
  }
}
        

