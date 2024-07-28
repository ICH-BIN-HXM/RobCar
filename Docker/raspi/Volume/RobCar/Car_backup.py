from Motor import Motor
import numpy as np
import math

deg2rad = math.pi / 180 # factor from degree to radian 

min_turn_vel_deg = 60 # [degree/sec] 
max_turn_vel_deg = 75 # [degree/sec] 

max_fw_vel = 0.55 # [m/sec] 2.7 * 2pi * 0.065 / 2
min_fw_vel = - max_fw_vel

track_width = 0.128 # [m]

max_turn_vel = min([max_fw_vel, -min_fw_vel])

turn_radius = 0.064 # [m]

# 360 -> 2pi, 1 -> 2pi/360 
# 1 sec -> 30 grad -> 30 * 2pi/360  -*r-> 30 * 2pi/360 * 2*0.064  = 0.068

class Car:
    def __init__(self):
        self.__motor = Motor()
        
        self.__max_fw_vel = max_fw_vel
        self.__min_fw_vel = min_fw_vel
        
        self.__max_turn_vel = max_turn_vel
        
        self.__min_turn_vel_deg = min_turn_vel_deg
        self.__min_turn_vel_rad = min_turn_vel_deg * deg2rad
        self.__max_turn_vel_deg = max_turn_vel_deg
        self.__max_turn_vel_rad = max_turn_vel_deg * deg2rad

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
            
    # Function move 
    def move(self, _fw_vel, _yaw_speed, _turn_radius):
        fw_vel = float(_fw_vel) 
        yaw_speed = float(_yaw_speed)
        turn_radius = float(_turn_radius)
        
        if yaw_speed == 0 and fw_vel == 0:
            # stop
            self.__motor.control_left_front_Motor(0, 0)
            self.__motor.control_right_front_Motor(0 ,0)
        elif yaw_speed != 0 and fw_vel == 0:
            # just rotation
            if yaw_speed > 0:
                # turn left
                self.__motor.control_left_front_Motor(1, yaw_speed/self.__max_turn_vel_deg)
                self.__motor.control_right_front_Motor(1, yaw_speed/self.__max_turn_vel_deg)
            elif yaw_speed < 0:
                self.__motor.control_left_front_Motor(2, yaw_speed/self.__max_turn_vel_deg)
                self.__motor.control_right_front_Motor(2, yaw_speed/self.__max_turn_vel_deg)
        elif yaw_speed == 0 and fw_vel != 0:
            if fw_vel > 0:
                # just forward 
                self.__motor.control_left_front_Motor(2, fw_vel/self.__max_fw_vel)
                self.__motor.control_right_front_Motor(1, fw_vel/self.__max_fw_vel)
            elif fw_vel < 0:
                # just backward 
                self.__motor.control_left_front_Motor(1, fw_vel/self.__max_fw_vel)
                self.__motor.control_right_front_Motor(2, fw_vel/self.__max_fw_vel)
        elif yaw_speed != 0 and fw_vel != 0:
            if fw_vel > 0 and yaw_speed > 0:
                # turn left
                v_r = yaw_speed * deg2rad * (turn_radius + track_width / 2)
                v_l = yaw_speed * deg2rad * (turn_radius - track_width / 2)
                
                
                

