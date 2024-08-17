from Hardware_Driver import Hardware_Driver

import pybullet as p
import time

hw_dr = Hardware_Driver()

try:
    for counter in range(5):
        # t_end = time.time() + 5
        # while time.time() < t_end:
        #     hw_dr.backwards()
        
        t_end = time.time() + 15
        while time.time() < t_end:
            hw_dr.backwardLeft()
            # time.sleep(0.1)
            
        t_end = time.time() + 5
        while time.time() < t_end:
            hw_dr.backwards()
            
        t_end = time.time() + 3
        while time.time() < t_end:
            hw_dr.backwardRight()
            
        t_end = time.time() + 5
        while time.time() < t_end:
            hw_dr.backwards()
        
        t_end = time.time() + 5
        while time.time() < t_end:
            hw_dr.stop()
    
    print("finished")
    hw_dr.hw.close()

except KeyboardInterrupt:
    hw_dr.hw.close()