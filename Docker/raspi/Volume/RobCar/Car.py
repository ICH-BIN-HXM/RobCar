import numpy as np
import math

# flag for simulation or not. If False, command will be sent to motors. 
flag_simulation = True

if not flag_simulation:
    from Motor import Motor

deg2rad = math.pi / 180 # factor from degree to radian 

max_fw_vel = 0.55 # [m/sec] 2.7 * 2pi * 0.065 / 2
min_fw_vel = - max_fw_vel

min_yaw_speed_rotation_deg = 134 # [degree/sec] 
max_yaw_speed_rotation_deg = 360 # [degree/sec] 

min_yaw_speed_turn_deg = 19 # [degree/sec] 
max_yaw_speed_turn_deg = 57 # [degree/sec] 

track_width = 0.128 # [m]

turn_radius = 0.4 # [m]

class Car:
    def __init__(self):
        if not flag_simulation:
            self.__motor = Motor()
        
        self.__max_fw_vel = max_fw_vel
        self.__min_fw_vel = min_fw_vel


    # Function move 
    def move(self, _fw_vel, _yaw_speed):
        # initialize pwm value for left and right 
        pwm_l = float(0)
        pwm_r = float(0)
        
        if _yaw_speed == 0 and _fw_vel == 0:
            # stop
            if not flag_simulation:
                self.__motor.control_left_front_Motor(0, 0)
                self.__motor.control_right_front_Motor(0 ,0)
        
        elif _yaw_speed == 0 and _fw_vel != 0:
            # limit
            fw_vel = float(np.clip(_fw_vel, self.__min_fw_vel, self.__max_fw_vel))
            if fw_vel > 0:
                # just forward 
                pwm_l = fw_vel/self.__max_fw_vel
                pwm_r = fw_vel/self.__max_fw_vel
                
                if not flag_simulation:
                    self.__motor.control_left_front_Motor(2, pwm_l)
                    self.__motor.control_right_front_Motor(1, pwm_r)
            elif fw_vel < 0:
                # just backward 
                pwm_l = fw_vel/self.__min_fw_vel
                pwm_r = fw_vel/self.__min_fw_vel
                
                if not flag_simulation:
                    self.__motor.control_left_front_Motor(1, pwm_l)
                    self.__motor.control_right_front_Motor(2, pwm_r)
        
        elif _yaw_speed != 0 and _fw_vel == 0:
            self.__min_yaw_speed_deg = min_yaw_speed_rotation_deg
            self.__max_yaw_speed_deg = max_yaw_speed_rotation_deg
            
            # limit
            if _yaw_speed > 0:
                yaw_speed_deg = float(np.clip(_yaw_speed, self.__min_yaw_speed_deg, self.__max_yaw_speed_deg))
            elif _yaw_speed < 0:
                yaw_speed_deg = float(np.clip(_yaw_speed, -self.__max_yaw_speed_deg, -self.__min_yaw_speed_deg))   
            
            if yaw_speed_deg > 0:
                # rotate to left
                pwm_l = yaw_speed_deg * deg2rad * (track_width/2)/self.__max_fw_vel 
                pwm_r = yaw_speed_deg * deg2rad * (track_width/2)/self.__max_fw_vel 
                
                if not flag_simulation:
                    self.__motor.control_left_front_Motor(1, pwm_l)
                    self.__motor.control_right_front_Motor(1, pwm_r)
            elif yaw_speed_deg < 0:
                # rotate to right
                pwm_l = yaw_speed_deg * deg2rad * (track_width/2)/self.__min_fw_vel
                pwm_r =  yaw_speed_deg * deg2rad * (track_width/2)/self.__min_fw_vel 
                
                if not flag_simulation:
                    self.__motor.control_left_front_Motor(2, pwm_l)
                    self.__motor.control_right_front_Motor(2, pwm_r)

        elif _yaw_speed != 0 and _fw_vel != 0:
            self.__min_yaw_speed_deg = min_yaw_speed_turn_deg
            self.__max_yaw_speed_deg = max_yaw_speed_turn_deg
            
            # limit
            fw_vel = float(np.clip(_fw_vel, self.__min_fw_vel, self.__max_fw_vel))
            if _yaw_speed > 0:
                yaw_speed_deg = float(np.clip(_yaw_speed, self.__min_yaw_speed_deg, self.__max_yaw_speed_deg))
            elif _yaw_speed < 0:
                yaw_speed_deg = float(np.clip(_yaw_speed, -self.__max_yaw_speed_deg, -self.__min_yaw_speed_deg)) 
            
            if fw_vel > 0 and yaw_speed_deg > 0:
                # turn left
                v_l = abs(yaw_speed_deg) * deg2rad * (turn_radius - track_width / 2)
                v_r = abs(yaw_speed_deg) * deg2rad * (turn_radius + track_width / 2)

                pwm_l = v_l/self.__max_fw_vel
                pwm_r = v_r/self.__max_fw_vel
                
                if not flag_simulation:
                    self.__motor.control_left_front_Motor(2, pwm_l)
                    self.__motor.control_right_front_Motor(1, pwm_r)
            
            elif fw_vel > 0 and yaw_speed_deg < 0:
                # turn right
                v_l = abs(yaw_speed_deg) * deg2rad * (turn_radius + track_width / 2)
                v_r = abs(yaw_speed_deg) * deg2rad * (turn_radius - track_width / 2)

                pwm_l = v_l/self.__max_fw_vel
                pwm_r = v_r/self.__max_fw_vel
                
                if not flag_simulation:
                    self.__motor.control_left_front_Motor(2, pwm_l)
                    self.__motor.control_right_front_Motor(1, pwm_r)
            
            elif fw_vel < 0 and yaw_speed_deg > 0:
                # back and towards left
                v_l = abs(yaw_speed_deg) * deg2rad * (turn_radius - track_width / 2)
                v_r = abs(yaw_speed_deg) * deg2rad * (turn_radius + track_width / 2)
                
                pwm_l = v_l/self.__max_fw_vel
                pwm_r = v_r/self.__max_fw_vel
                
                if not flag_simulation:
                    self.__motor.control_left_front_Motor(1, pwm_l)
                    self.__motor.control_right_front_Motor(2, pwm_r)

            elif fw_vel < 0 and yaw_speed_deg < 0:
                # back and towards right
                v_l = abs(yaw_speed_deg) * deg2rad * (turn_radius + track_width / 2)
                v_r = abs(yaw_speed_deg) * deg2rad * (turn_radius - track_width / 2)
                
                pwm_l = v_l/self.__max_fw_vel
                pwm_r = v_r/self.__max_fw_vel
                
                if not flag_simulation:
                    self.__motor.control_left_front_Motor(1, pwm_l)
                    self.__motor.control_right_front_Motor(2, pwm_r)
                
        print(f"Left motor pwm: {round(pwm_l, 2)}, right motor pwm: {round(pwm_r, 2)}")