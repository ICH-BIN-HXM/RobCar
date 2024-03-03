from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtCore import QTimer, Qt

from Ros_Publisher import Ros_Publisher
import rclpy


time_unit = 100 # [ms] 
max_fw_vel = 0.6 # [m/s] = 3 rad/sec * 2pi * (65mm/2) 
min_fw_vel = - max_fw_vel
hold_to_fw_vel = 0.05 * abs(max_fw_vel)  # factor: hold for 1 time_unit -> forward velocity will be changed for 5% of max velocity


class Control_Panel(QWidget):
    def __init__(self):
        super().__init__()
        # Load static UI
        self.ui = uic.loadUi("Control_Panel.ui") 
        self.ui.show()
        
        
        ## Button for method to control
        self.b_cmd_display = self.ui.b_cmd_display 
        self.b_cmd_keyboard = self.ui.b_cmd_keyboard 
        
        ## Button on display
        self.b_forward = self.ui.b_forward
        self.b_backward = self.ui.b_backward
        
        ## Key on keyboard
        self.k_forward = Qt.Key.Key_W
        self.k_backward = Qt.Key.Key_S
        
        # ROS
        rclpy.init(args=None)
        self.ros_pub = Ros_Publisher()
        
        
        # Method to control:  Display (1) or Keyboard (2)?
        self.dp_or_kb = int(0)
        ## Initialization with the default method: display
        self.b_cmd_display.setChecked(True)
        self.b_cmd_keyboard.setChecked(False)
        self.dp_or_kb = int(0)
        self.switch_method_control()
        self.b_cmd_display.clicked.connect(self.callback_cmd_display)
        self.b_cmd_keyboard.clicked.connect(self.callback_cmd_keyboard)
        

        
        
        
        
        # Command for forward velocity: forward and backward
        ## Timer
        self.timer_cmd_fw_vel = QTimer()
        self.timer_cmd_fw_vel.timeout.connect(self.callback_timer_cmd_fw_vel)
        self.hold_cmd_fw_vel = int(0)
        
    
    
    # Callback-Function for pressed
    def pressed_cmd_fw_vel(self):
        if self.dp_or_kb == 1: 
            # Control with display
            if self.b_forward.isDown() and not self.b_backward.isDown() :
                # forward: factor -> 1 
                self.hold_to_fw_vel = 1 * abs(hold_to_fw_vel)
                print("forwards!")
            elif self.b_backward.isDown() and not self.b_forward.isDown() : 
                # forward: factor -> -1 
                self.hold_to_fw_vel = (-1) * abs(hold_to_fw_vel)
                print("backwards!")
            else:
                print("Don't press forward and backward simultaneously!!!")
                return
            
            # Start a timer
            self.timer_cmd_fw_vel.start(time_unit) 
        
        elif self.dp_or_kb == 2:
            # Control with keyboard 
            if self.k_forward_pressed and not self.k_backward_pressed :
                # forward: factor -> 1 
                self.hold_to_fw_vel = 1 * abs(hold_to_fw_vel)
                print("forwards!")
            elif self.k_backward_pressed and not self.k_forward_pressed : 
                # forward: factor -> -1 
                self.hold_to_fw_vel = (-1) * abs(hold_to_fw_vel)
                print("backwards!")
            else:
                print("Don't press forward and backward simultaneously!!!")
                return
            
            # Start a timer
            self.timer_cmd_fw_vel.start(time_unit) 
        
    # Callback-Function for released
    def released_cmd_fw_vel(self):
        # Reset the timer
        try:
            self.timer_cmd_fw_vel.stop()
            self.hold_cmd_fw_vel = int(0)
        except:
            pass
        
        # Publish to ROS
        self.ros_pub.publish_ctrl_fw_vel(0)
        
        
    def callback_timer_cmd_fw_vel(self):
        self.hold_cmd_fw_vel += 1 

        # convert hold action to velocity
        cmd_fw_vel = self.hold_cmd_fw_vel * self.hold_to_fw_vel 
        # limit with max and min
        if cmd_fw_vel > max_fw_vel: 
            cmd_fw_vel = max_fw_vel
        elif cmd_fw_vel < min_fw_vel:
            cmd_fw_vel = min_fw_vel
        # publish to ROS
        print(f"forward Velocity: {cmd_fw_vel}")
        self.ros_pub.publish_ctrl_fw_vel(cmd_fw_vel)
        
    def keyPressEvent(self, event):
        print("event")
        # Only act, if the method is keyboard
        if self.dp_or_kb == 2:  
            if event.key() == Qt.Key.Key_W : 
                print("up pressed!!!")
                self.k_forward_pressed = True
                self.pressed_cmd_fw_vel()
            if event.key() == self.k_backward:
                self.k_backward_pressed = True
                self.pressed_cmd_fw_vel()

    def keyReleaseEvent(self, event):
        # Only act, if the method is keyboard
        if self.dp_or_kb == 2:  
            if event.key() == self.k_forward : 
                self.k_forward_pressed = False
                self.released_cmd_fw_vel()
            if event.key() == self.k_backward:
                self.k_backward_pressed = False
                self.released_cmd_fw_vel()
            
            
                
        
        
        
        
        
    

    def callback_cmd_display(self):
        # only need to deal with the 2 unnormal situations
        if (not self.b_cmd_display.isChecked() and not self.b_cmd_keyboard.isChecked()) or self.b_cmd_display.isChecked() and self.b_cmd_keyboard.isChecked() :
            self.b_cmd_keyboard.toggle()
        
        self.switch_method_control()
    
    def callback_cmd_keyboard(self):
        # only need to deal with the 2 unnormal situations
        if (not self.b_cmd_display.isChecked() and not self.b_cmd_keyboard.isChecked()) or self.b_cmd_display.isChecked() and self.b_cmd_keyboard.isChecked() :
            self.b_cmd_display.toggle()
        
        self.switch_method_control()

    def switch_method_control(self):
        if self.b_cmd_display.isChecked() and not self.b_cmd_keyboard.isChecked() :
            self.b_forward.pressed.connect(self.pressed_cmd_fw_vel)
            self.b_backward.pressed.connect(self.pressed_cmd_fw_vel)
            self.b_forward.released.connect(self.released_cmd_fw_vel)
            self.b_backward.released.connect(self.released_cmd_fw_vel)
            
            self.dp_or_kb = 1
            print("You have chosen control with display") 
            
        elif self.b_cmd_keyboard.isChecked() and not self.b_cmd_display.isChecked() :
            try:
                self.b_forward.pressed.disconnect(self.pressed_cmd_fw_vel)
                self.b_backward.pressed.disconnect(self.pressed_cmd_fw_vel)
                self.b_forward.released.disconnect(self.released_cmd_fw_vel)
                self.b_backward.released.disconnect(self.released_cmd_fw_vel)
            except:
                pass
            
            
            self.dp_or_kb = 2
            print("You have chosen control with keyboard") 
        else:
            self.dp_or_kb = 0
            print("No method for control detected!!!")
            

            
        
def main(args = None):
    app = QApplication([])
    window = Control_Panel()
    app.exec_()
    rclpy.shutdown()
 	           

if __name__ == '__main__':
    main()

    