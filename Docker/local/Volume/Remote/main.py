from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton, QButtonGroup
from PyQt5.QtCore import QTimer, Qt

from Ros_Publisher import Ros_Publisher
import rclpy

import numpy as np


time_unit = 100 # [ms] 

max_fw_vel = 0.55 # [m/sec] = 2.7 rad/sec * 2pi * (65mm/2) 
min_fw_vel = - max_fw_vel
hold_to_fw_vel = 0.05 * abs(max_fw_vel)  # factor: hold for 1 time_unit -> forward velocity will be changed for 5% of max velocity

max_yaw_speed = 360 # [degree/sec]
min_yaw_speed = 19 # [degree/sec]
hold_to_yaw_speed = 0.05 * (max_yaw_speed - min_yaw_speed)


class Control_Panel(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # get constant 
        self.max_fw_vel = max_fw_vel
        self.min_fw_vel = min_fw_vel
        self.hold_to_fw_vel = hold_to_fw_vel
        
        self.max_yaw_speed = max_yaw_speed
        self.min_yaw_speed = min_yaw_speed
        self.hold_to_yaw_speed = hold_to_yaw_speed
        
        # ROS
        rclpy.init(args=None)
        self.ros_pub = Ros_Publisher()
        
        # set Window size
        self.setGeometry(0, 0, 630, 300)
        
        # Buttons for method control
        self.grp_b_cmd_dp_or_kb = QButtonGroup(self)
        
        self.b_cmd_display = QCheckBox("Display", self)     # Button control with display 
        self.b_cmd_display.setGeometry(120, 20, 90, 20)     
        
        self.b_cmd_keyboard = QCheckBox("Keyboard", self)   # Button control with Keyboard 
        self.b_cmd_keyboard.setGeometry(380, 20, 90, 20)
        
        self.grp_b_cmd_dp_or_kb.addButton(self.b_cmd_display)
        self.grp_b_cmd_dp_or_kb.addButton(self.b_cmd_keyboard)
        
        self.grp_b_cmd_dp_or_kb.buttonClicked.connect(self.handle_method_control)
        
        self.ini_method_control()
        
        
        # Buttons on display 
        self.b_forward = QPushButton("Forward", self)       # Button command forward
        self.b_forward.setGeometry(250, 70, 90, 60)
        self.b_forward.pressed.connect(self.callback_b_fw_pressed)
        self.b_forward.released.connect(self.callback_b_fw_released)
        self.b_forward_pressed = False
        
        self.b_backward = QPushButton("Backward", self)     # Button command backward
        self.b_backward.setGeometry(250, 160, 90, 60)
        self.b_backward.pressed.connect(self.callback_b_bw_pressed)
        self.b_backward.released.connect(self.callback_b_bw_released)
        self.b_backward_pressed = False
        
        self.b_left = QPushButton("Left", self)       # Button command left
        self.b_left.setGeometry(120, 70, 90, 60)
        self.b_left.pressed.connect(self.callback_b_left_pressed)
        self.b_left.released.connect(self.callback_b_left_released)
        self.b_left_pressed = False
        
        self.b_right = QPushButton("Right", self)     # Button command right
        self.b_right.setGeometry(380, 70, 90, 60)
        self.b_right.pressed.connect(self.callback_b_right_pressed)
        self.b_right.released.connect(self.callback_b_right_released)
        self.b_right_pressed = False
        
        
        
        # Key on keyboard
        self.k_forward = Qt.Key.Key_W
        self.k_forward_pressed = False
        
        self.k_backward = Qt.Key.Key_S
        self.k_backward_pressed = False
        
        self.k_left = Qt.Key.Key_A
        self.k_left_pressed = False

        self.k_right = Qt.Key.Key_D
        self.k_right_pressed = False


        # Velocity
        self.cmd_fw_vel = 0
        self.cmd_yaw_speed = 0
        
        # Counter
        self.counter_fw_bw = 0
        self.counter_turn = 0
        
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.calc_cmd)
        self.timer.start(time_unit)  # Timer fires every 100 milliseconds
    
    def ini_method_control(self):
        # Method to control:  Display (1) or Keyboard (2)?
        self.dp_or_kb = int(1)  # default method: display
        self.b_cmd_display.setChecked(True)
        self.b_cmd_keyboard.setChecked(False)
        
    def handle_method_control(self):
        # check state 
        if self.b_cmd_display.isChecked() and not self.b_cmd_keyboard.isChecked() :
            self.dp_or_kb = 1
            print("You have chosen control with display") 
            
        elif self.b_cmd_keyboard.isChecked() and not self.b_cmd_display.isChecked() :
            self.dp_or_kb = 2
            print("You have chosen control with keyboard") 
        
        elif not self.b_cmd_display.isChecked() and not self.b_cmd_keyboard.isChecked() :
            self.dp_or_kb = 0
            print("No method for control detected!!!")
        
        elif self.b_cmd_keyboard.isChecked() and self.b_cmd_display.isChecked() :
            self.dp_or_kb = 0
            print("Only 1 method can be chosen!!!")
    
    # Press
    def keyPressEvent(self, event):
        key = event.key()
        
        if key == self.k_forward:
            self.k_forward_pressed = True
        
        if key == self.k_backward:
            self.k_backward_pressed = True
            
        if key == self.k_left:
            self.k_left_pressed = True
            
        if key == self.k_right:
            self.k_right_pressed = True
            
    def callback_b_fw_pressed(self):
        self.b_forward_pressed = True
        
    def callback_b_bw_pressed(self):
        self.b_backward_pressed = True
        
    def callback_b_left_pressed(self):
        self.b_left_pressed = True
    
    def callback_b_right_pressed(self):
        self.b_right_pressed = True

    # Release
    def keyReleaseEvent(self, event):
        key = event.key()
        
        if key == self.k_forward:
            self.k_forward_pressed = False
        
        if key == self.k_backward:
            self.k_backward_pressed = False
        
        if key == self.k_left:
            self.k_left_pressed = False
        
        if key == self.k_right:
            self.k_right_pressed = False
     
    def callback_b_fw_released(self):
        self.b_forward_pressed = False
        
    def callback_b_bw_released(self):
        self.b_backward_pressed = False
        
    def callback_b_left_released(self):
        self.b_left_pressed = False
        
    def callback_b_right_released(self):
        self.b_right_pressed = False


    def calc_cmd(self):
        if self.dp_or_kb == 1:
            if self.b_forward_pressed and self.b_backward_pressed:
                print("You cannot press the forward and backward simultaneously!!!")
                self.counter_fw_bw = 0
            elif self.b_forward_pressed and not self.b_backward_pressed:
                self.counter_fw_bw += 1
            elif not self.b_forward_pressed and self.b_backward_pressed:
                self.counter_fw_bw -= 1
            else :
                self.counter_fw_bw = 0
                
            if self.b_left_pressed and self.b_right_pressed:
                print("You cannot press the left and right simultaneously!!!")
                self.counter_turn = 0
            elif self.b_left_pressed and not self.b_right_pressed:
                self.counter_turn += 1
            elif not self.b_left_pressed and self.b_right_pressed:
                self.counter_turn -= 1
            else :
                self.counter_turn = 0
        
        elif self.dp_or_kb == 2:
            if self.k_forward_pressed and self.k_backward_pressed:
                print("You cannot press the forward and backward simultaneously!!!")
                self.counter_fw_bw = 0
            elif self.k_forward_pressed and not self.k_backward_pressed:
                self.counter_fw_bw += 1
            elif not self.k_forward_pressed and self.k_backward_pressed:
                self.counter_fw_bw -= 1
            else :
                self.counter_fw_bw = 0
                
            if self.k_left_pressed and self.k_right_pressed:
                print("You cannot press the left and right simultaneously!!!")
                self.counter_turn = 0
            elif self.k_left_pressed and not self.k_right_pressed:
                self.counter_turn += 1
            elif not self.k_left_pressed and self.k_right_pressed:
                self.counter_turn -= 1
            else :
                self.counter_turn = 0


        # limit forward vel
        self.cmd_fw_vel = np.clip(self.counter_fw_bw * self.hold_to_fw_vel, self.min_fw_vel, self.max_fw_vel) 

        # limit yaw speed
        if self.counter_turn == 0:
            self.cmd_yaw_speed = 0
        
        elif self.counter_turn >= 0:
            self.cmd_yaw_speed = np.clip(self.min_yaw_speed + self.counter_turn * self.hold_to_yaw_speed, self.min_yaw_speed, self.max_yaw_speed)
        
        elif self.counter_turn < 0:
            self.cmd_yaw_speed = np.clip(-self.min_yaw_speed + self.counter_turn * self.hold_to_yaw_speed, -self.max_yaw_speed, -self.min_yaw_speed) 
        
        self.send_cmd()
        
    def send_cmd(self):
        # print(f"fw_vel:{self.cmd_fw_vel}")
        self.ros_pub.publish_ctrl_fw_vel(self.cmd_fw_vel)
        # print(f"yaw_speed:{self.cmd_yaw_speed}")
        self.ros_pub.publish_ctrl_yaw_speed(self.cmd_yaw_speed)
        
        
    
            
        
def main(args = None):
    app = QApplication([])
    window = Control_Panel()
    window.show()
    
    try:
        app.exec()
    except KeyboardInterrupt:
        rclpy.shutdown()
        app.quit()
        
    
 	           

if __name__ == '__main__':
    main()

    