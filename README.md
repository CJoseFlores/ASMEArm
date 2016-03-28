# ASME CuriosityJr Arm Team

### Arm Branch

### This branch's objectives include:

1. Move the arm in sync using:

  * Arm objects
	
  * Sensors
	
2. Create a "Default Position" 

![alt tag][defaultpos]

[defaultpos]: http://i.imgur.com/JYRuONC.jpg

----


  * This position will be used to calibrate the arm.
	
  * S1 and S2 will be used to tell the arm when to start/stop moving to return/exit the default position.
	
  * X and Y are distances that will be used to perform the above statement.
	  
  * The arm will return to the "Default Position" when powered on, and after picking up or dropping off the payload.

3. After the rover finds the object with the Object-Tracking camera, the arm will turn and pickup the payload, and return to the default position.

  * Once it sees the payload, it will move motors 2 & 3 to get the arm close, and finally motor 5 to grab/release it, as depicted below:
	
	![alt tag](http://i.imgur.com/y6iTx2m.jpg)

4. Once next to the drop-off area, the arm will drop the payload, and return to the default position.
	
### Materials needed for this branch:

  * [SHARP IR distance sensor](https://www.adafruit.com/products/164)

  * [MCP3008 with SPI interface](https://www.adafruit.com/products/856) 
	This product will be used to convert the analogue readings of the sensor to digital

  * [HC-SR04 Ultrasonic Sensor](http://www.amazon.com/SunFounder-Ultrasonic-Distance-Mega2560-Duemilanove/dp/B00E0NXTJW/ref=sr_1_1?ie=UTF8&qid=1459173388&sr=8-1&keywords=distance+sensor)
	These sensors would be best, but they do not work well on round surfaces. Testing is needed.

	