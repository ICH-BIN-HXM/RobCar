import RPi.GPIO as GPIO 

# for GPIO numbering, choose BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Pin
AIN1 = 17 
AIN2 = 18 
BIN1 = 22
BIN2 = 23

E1A = 20
E1B = 21 
E2A = 26
E2B = 27

class Motor:
    def __init__(self):
        self.init_Motor()
    
    
    def init_Motor(self):
        GPIO.setup(AIN1, GPIO.OUT)
        self.__AIN1 = GPIO.PWM(AIN1, 50) #50 is the frequency of 50 Hz 
        self.__AIN1.start(0)

        GPIO.setup(AIN2, GPIO.OUT) 
        self.__AIN2 = GPIO.PWM(AIN2, 50) 
        self.__AIN2.start(0)

        GPIO.setup(BIN1, GPIO.OUT) 
        self.__BIN1 = GPIO.PWM(BIN1, 50) 
        self.__BIN1.start(0)

        GPIO.setup(BIN2, GPIO.OUT) 
        self.__BIN2 = GPIO.PWM(BIN2, 50)
        self.__BIN2.start(0)


        GPIO.setup(E1A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(E1B, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        GPIO.setup(E2A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(E2B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    

    def control_left_front_Motor(self, _direction, _pwm):
        direction = int(_direction)
        pwm = float(abs(_pwm))
        
        if direction == 0 or pwm == 0:
            self.__AIN1.start(100)
            self.__AIN2.start(100)
            print("Left front motor stopped")
        elif direction == 1:
            # clockwise
            self.__AIN1.start(100)
            self.__AIN2.start(100 - pwm)
            print(f"Left front motor is running with direction: clockwise and speed: {pwm}% of max. speed")
        elif direction == 2:
            # counterclockwise
            self.__AIN2.start(100)
            self.__AIN1.start(100 - pwm)
            print(f"Left front motor is running with direction: counterclockwise and speed: {pwm}% of max. speed")


    def control_right_front_Motor(self, _direction, _pwm):
        direction = int(_direction)
        pwm = float(abs(_pwm))
        
        if direction == 0 or pwm == 0:
            self.__BIN1.start(100)
            self.__BIN2.start(100)
            print("Right front motor stopped")
        elif direction == 1:
            # clockwise
            self.__BIN1.start(100)
            self.__BIN2.start(100 - pwm)
            print(f"Right front motor is running with direction: clockwise and speed: {pwm}% of max. speed")
        elif direction == 2:
            # counterclockwise
            self.__BIN2.start(100)
            self.__BIN1.start(100 - pwm)
            print(f"Right front motor is running with direction: counterclockwise and speed: {pwm}% of max. speed")
  

