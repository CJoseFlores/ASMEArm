/*
  Atv.h v-3.3 - Atv library for OWI-535
  Copyright (c) 2014 Wilmer Arellano.  All right reserved.
*/

// ensure this library description is only included once
#ifndef Atv_h
#define Atv_h

#include <Arduino.h>

// library interface description
class Atv
{
  // user-accessible "public" interface
  public:
    Atv(int);
	void initialize(int);
    void checkData(void);
	void moveMotor(int, int, int, int);
     void moveMotorDF(int, int, int, int);
	int distance();
int distanceW();

  // library-accessible "private" interface
  private:
    int sensorPin, motorID, Speed, Duration, index;    
};

#endif

