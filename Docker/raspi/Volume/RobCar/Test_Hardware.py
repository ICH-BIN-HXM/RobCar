from Hardware import Hardware

import pybullet as p
import time

h = Hardware(time_step= 0.02, flag_simulation= True)
try:
    h.init()
    
    t_end = time.time() + 10
    while time.time() < t_end:
        # Control motors
        h.control_left_front_motor(1, 100)  # Forward direction, PWM 100
        h.control_right_front_motor(1, 100)
        h.control_left_rear_motor(1, 100)
        h.control_right_rear_motor(1, 100)
        
        h.step()
        
        # Read motor state
        print("Left Front Motor:", h.read_left_front_motor())
        print("Right Front Motor:", h.read_right_front_motor())
        print("Left Rear Motor:", h.read_left_rear_motor())
        print("Right Rear Motor:", h.read_right_rear_motor())
    
    print("finished")
    h.close()

except KeyboardInterrupt:
    h.close()