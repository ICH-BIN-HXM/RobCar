from Hardware import Hardware
from Parameters import pwm_increment

import numpy as np

class Hardware_Driver:
    def __init__(self, pwm_increment: int = pwm_increment):
        self.pwm_increment = pwm_increment
        
        self.hw = Hardware()
        self.hw.init()
        

    def forwards(self):
        states = self.hw.get_motorStates()
        if states == {}:
            for joint in self.hw.joints:
                self.hw.control_motor(index_motor= joint, direction= 0, pwm= 0)
            print("ERROR: Can not move correctly!!!")
        else:
            new_pwm_with_direction_left = np.clip((states[0] + states[2])/2.0 + self.pwm_increment, -100, 100)
            new_pwm_with_direction_right = np.clip((states[1] + states[3])/2.0 + self.pwm_increment, -100, 100)
            for joint in self.hw.joints:
                if joint % 2 == 0:
                    new_pwm = abs(new_pwm_with_direction_left)
                    if new_pwm_with_direction_left > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_left < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
                else:
                    new_pwm = abs(new_pwm_with_direction_right)
                    if new_pwm_with_direction_right > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_right < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
        
        self.hw.step()
    
            
    def forwardLeft(self):
        states = self.hw.get_motorStates()
        if states == {}:
            for joint in self.hw.joints:
                self.hw.control_motor(index_motor= joint, direction= 0, pwm= 0)
            print("ERROR: Can not move correctly!!!")
        else:
            new_pwm_with_direction_left = np.clip((states[0] + states[2])/2.0 - self.pwm_increment, -100, 100)
            new_pwm_with_direction_right = np.clip((states[1] + states[3])/2.0 + self.pwm_increment, -100, 100)
            for joint in self.hw.joints:
                if joint % 2 == 0:
                    new_pwm = abs(new_pwm_with_direction_left)
                    if new_pwm_with_direction_left > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_left < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
                else:
                    new_pwm = abs(new_pwm_with_direction_right)
                    if new_pwm_with_direction_right > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_right < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
        
        self.hw.step()
            
    def forwardRight(self):
        states = self.hw.get_motorStates()
        if states == {}:
            for joint in self.hw.joints:
                self.hw.control_motor(index_motor= joint, direction= 0, pwm= 0)
            print("ERROR: Can not move correctly!!!")
        else:
            new_pwm_with_direction_left = np.clip((states[0] + states[2])/2.0 + self.pwm_increment, -100, 100)
            new_pwm_with_direction_right = np.clip((states[1] + states[3])/2.0 - self.pwm_increment, -100, 100)
            for joint in self.hw.joints:
                if joint % 2 == 0:
                    new_pwm = abs(new_pwm_with_direction_left)
                    if new_pwm_with_direction_left > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_left < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
                else:
                    new_pwm = abs(new_pwm_with_direction_right)
                    if new_pwm_with_direction_right > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_right < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
        
        self.hw.step()

    def backwards(self):
        states = self.hw.get_motorStates()
        if states == {}:
            for joint in self.hw.joints:
                self.hw.control_motor(index_motor= joint, direction= 0, pwm= 0)
            print("ERROR: Can not move correctly!!!")
        else:
            new_pwm_with_direction_left = np.clip((states[0] + states[2])/2.0 - self.pwm_increment, -100, 100)
            new_pwm_with_direction_right = np.clip((states[1] + states[3])/2.0 - self.pwm_increment, -100, 100)
            for joint in self.hw.joints:
                if joint % 2 == 0:
                    new_pwm = abs(new_pwm_with_direction_left)
                    if new_pwm_with_direction_left > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_left < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
                else:
                    new_pwm = abs(new_pwm_with_direction_right)
                    if new_pwm_with_direction_right > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_right < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
        
        self.hw.step()
    
    def backwardLeft(self):
        states = self.hw.get_motorStates()
        if states == {}:
            for joint in self.hw.joints:
                self.hw.control_motor(index_motor= joint, direction= 0, pwm= 0)
            print("ERROR: Can not move correctly!!!")
        else:
            new_pwm_with_direction_left = np.clip((states[0] + states[2])/2.0 + self.pwm_increment, -100, 100)
            new_pwm_with_direction_right = np.clip((states[1] + states[3])/2.0 - self.pwm_increment, -100, 100)
            print(new_pwm_with_direction_left, new_pwm_with_direction_right)
            for joint in self.hw.joints:
                if joint % 2 == 0:
                    new_pwm = abs(new_pwm_with_direction_left)
                    if new_pwm_with_direction_left > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_left < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
                else:
                    new_pwm = abs(new_pwm_with_direction_right)
                    if new_pwm_with_direction_right > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_right < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
        
        self.hw.step()


    def backwardRight(self):
        states = self.hw.get_motorStates()
        if states == {}:
            for joint in self.hw.joints:
                self.hw.control_motor(index_motor= joint, direction= 0, pwm= 0)
            print("ERROR: Can not move correctly!!!")
        else:
            new_pwm_with_direction_left = np.clip((states[0] + states[2])/2.0 - self.pwm_increment, -100, 100)
            new_pwm_with_direction_right = np.clip((states[1] + states[3])/2.0 + self.pwm_increment, -100, 100)
            for joint in self.hw.joints:
                if joint % 2 == 0:
                    new_pwm = abs(new_pwm_with_direction_left)
                    if new_pwm_with_direction_left > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_left < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
                else:
                    new_pwm = abs(new_pwm_with_direction_right)
                    if new_pwm_with_direction_right > 0:
                        new_direction = 1
                    elif new_pwm_with_direction_right < 0:
                        new_direction = -1
                    else:
                        new_direction = 0
                    self.hw.control_motor(index_motor= joint, direction= new_direction, pwm= new_pwm)
        
        self.hw.step()
        
    
    def stop(self):
        for joint in self.hw.joints:
            self.hw.control_motor(index_motor= joint, direction= 0, pwm= 0)
        
        self.hw.step()