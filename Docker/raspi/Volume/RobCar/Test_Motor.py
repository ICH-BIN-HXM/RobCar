from Motor import Motor
import RPi.GPIO as GPIO 
import time

def main():
    motor = Motor()
    while True:
        try: 
            motor.control_left_front_Motor(0, 0)
            time.sleep(3)
            
            motor.control_left_front_Motor(1, 30)
            time.sleep(3)
            
            motor.control_left_front_Motor(1, 60)
            time.sleep(3)
            
            motor.control_left_front_Motor(1, 90)
            time.sleep(3)
            
            motor.control_left_front_Motor(0, 0)
            time.sleep(3)
            
            motor.control_left_front_Motor(2, 30)
            time.sleep(3)
            
            motor.control_left_front_Motor(2, 60)
            time.sleep(3)
            
            motor.control_left_front_Motor(2, 90)
            time.sleep(3)
        except KeyboardInterrupt:
            motor.control_left_front_Motor(0, 0)
            print("!!!END!!!")
            break
        

if __name__ == "__main__":
    main()