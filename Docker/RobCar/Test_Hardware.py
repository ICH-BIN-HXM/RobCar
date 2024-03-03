from Hardware import Car
import RPi.GPIO as GPIO 
import time

def main():
    c = Car()
    while True:
        try: 
            c.control_left_front_wheel(1, 0)
            time.sleep(3)
            
            c.control_left_front_wheel(1, 30)
            time.sleep(3)
            
            c.control_left_front_wheel(1, 60)
            time.sleep(3)
            
            c.control_left_front_wheel(1, 90)
            time.sleep(3)
            
            c.control_left_front_wheel(1, 0)
            time.sleep(3)
            
            c.control_left_front_wheel(2, 30)
            time.sleep(3)
            
            c.control_left_front_wheel(2, 60)
            time.sleep(3)
            
            c.control_left_front_wheel(2, 90)
            time.sleep(3)
        except KeyboardInterrupt:
            c.control_left_front_wheel(1, 0)
            print("!!!END!!!")
            break
        

if __name__ == "__main__":
    main()