# Objectives of this project:

1. Create a spider robot that can:

	* Move autonomously
	
	* Follow along walls when it reaches a certain distance
	
	* Continue to follow any walls, while turning around corners
	
2. Optimize the program in the following ways:

	* Use the least amount of sensors possible 
	  that allows the robot to continue to function
	  
	* Use less than 80 lines of code
	
# Materials of this project:

* [Romeo V 1.2 (or newer)](http://www.dfrobot.com/index.php?route=product/product&product_id=656#.ViGU8ysZMtE)

* [DFROBOT DIY B/O Spider Robot](http://www.dfrobot.com/index.php?route=product/product&product_id=913#.ViGUySsZMtE)

* [IR distance sensor (10cm-80cm)](https://www.adafruit.com/products/164)

# Libraries utilized in the project:

* [ATV.h (this can be found under the source files as Newest ATV.zip)](https://bitbucket.org/bazacorp/autonomous-spider-robot/src/b4fa62fe97b7309b6e51637df9eb34d5d5634ab4/Newest%20ATV.zip?at=master&fileviewer=file-view-default)

### Romeo motor driver pinouts:

    int E1 = 5;     //M1 Speed Control
    int E2 = 6;     //M2 Speed Control
    int M1 = 4;    //M1 Direction Control
    int M2 = 7;    //M1 Direction Control

    ///For previous Romeo, please use these pins.
    //int E1 = 6;     //M1 Speed Control
    //int E2 = 9;     //M2 Speed Control
    //int M1 = 7;    //M1 Direction Control
    //int M2 = 8;    //M1 Direction Control`

###### Current Project Version: V2.03