import RPi.GPIO as GPIO 
import time

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

class Car:
    def __init__(self):
        self.init_Motor()
        
    def init_Motor(self):
        GPIO.setup(AIN1, GPIO.OUT)
        self.AIN1 = GPIO.PWM(AIN1, 50) #50 is the frequency of 50 Hz 
        self.AIN1.start(0)

        GPIO.setup(AIN2, GPIO.OUT) 
        self.AIN2 = GPIO.PWM(AIN2, 50) 
        self.AIN2.start(0)

        GPIO.setup(BIN1, GPIO.OUT) 
        self.BIN1 = GPIO.PWM(BIN1, 50) 
        self.BIN1.start(0)

        GPIO.setup(BIN2, GPIO.OUT) 
        self.BIN2 = GPIO.PWM(BIN2, 50)
        self.BIN2.start(0)


        GPIO.setup(E1A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(E1B, GPIO.IN, pull_up_down=GPIO.PUD_UP) 
        GPIO.setup(E2A, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        GPIO.setup(E2B, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    

    def control_left_front_wheel(self, _direction, _pwm):
        direction = _direction
        pwm = _pwm
        
        if direction == 1:
            # clockwise
            self.AIN1.start(100)
            self.AIN2.start(100 - pwm)
            print(f"Left front motor is running with direction: clockwise and speed: {pwm}% of max. speed")
        elif direction == 2:
            self.AIN2.start(100)
            self.AIN1.start(100 - pwm)
            print(f"Left front motor is running with direction: counterclockwise and speed: {pwm}% of max. speed")
        


