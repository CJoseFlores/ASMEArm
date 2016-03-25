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
        if (motorID < 1 || motorID > 2):
            return
        if (direction < 0 || direction > 1):
            return
        if (speed < 0 || speed > 10):
            return
        if (time < -1 || time > 41):
            return
        self.__speed = 105 + speed * 10
        # moving the motor

Forward = 1
Backwards = 2

motor1 = Arm(1,2,Forward)

print("\nThis is the motorID:",motor1.get_mtrid(),"\nThis is the Speed:",motor1.get_speed(),"\nThis is the Direction:",motor1.get_dir())

