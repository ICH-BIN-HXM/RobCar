from Motor import Motor
import numpy as np

max_fw_vel = 0.6 # [m/sec]
min_fw_vel = - max_fw_vel
max_turn_vel = min([max_fw_vel, -min_fw_vel])

class Car:
    def __init__(self):
        self.__motor = Motor()
        
        self.__max_fw_vel = max_fw_vel
        self.__min_fw_vel = min_fw_vel
        
        self.__max_turn_vel = max_turn_vel

    # Function for limiting speed
    def limit_speed(self, _speed, _min_speed, _max_speed):
        speed = np.clip(_speed, _min_speed, _max_speed)
        
        return speed
        
    # Function for moving forward with _speed 
    def move_forward(self, _speed):     
        if _speed > 0 :
            speed = self.limit_speed(_speed, 0, self.__max_fw_vel)
            self.__motor.control_left_front_Motor(2, speed/self.__max_fw_vel)
            self.__motor.control_right_front_Motor(1, speed/self.__max_fw_vel)
            
            print(f"The Car is moving forward with speed {float(speed)}") 
        else:
            print("Please give a positive speed value for moving forward")
        
        
    # Function for moving backward with _speed 
    def move_backward(self, _speed):
        if _speed > 0 :
            speed = self.limit_speed(_speed, 0, -self.__min_fw_vel)
            self.__motor.control_left_front_Motor(1, speed/(-self.__min_fw_vel))
            self.__motor.control_right_front_Motor(2, speed/(-self.__min_fw_vel))
            
            print(f"The Car is moving backward with speed {float(speed)}") 
        else:
            print("Please give a positive speed value for moving backward")
        
    # Function for turning left with _speed 
    def turn_left(self, _speed):
        if _speed > 0 :
            speed = self.limit_speed(_speed, 0, self.__max_turn_vel)
            self.__motor.control_left_front_Motor(1, speed/self.__max_turn_vel)
            self.__motor.control_right_front_Motor(1, speed/self.__max_turn_vel)
            
            print(f"The Car is turning left with speed {float(speed)}") 
        else:
            print("Please give a positive speed value for turning left")
    
    
    # Function for turning right with _speed 
    def turn_right(self, _speed):
        if _speed > 0 :
            speed = self.limit_speed(_speed, 0, self.__max_turn_vel)
            self.__motor.control_left_front_Motor(2, speed/self.__max_turn_vel)
            self.__motor.control_right_front_Motor(2, speed/self.__max_turn_vel)
            
            print(f"The Car is turning right with speed {float(speed)}") 
        else:
            print("Please give a positive speed value for turning right")
        
    # Function for stopping
    def stop(self):
        self.__motor.control_left_front_Motor(0, 0)
        self.__motor.control_right_front_Motor(0 ,0)
    
