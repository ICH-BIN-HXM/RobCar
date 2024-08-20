from PyQt5.QtWidgets import QApplication, QMainWindow, QCheckBox, QPushButton, QButtonGroup
from PyQt5.QtCore import QTimer, Qt

from Command_Publisher import commandPublisher
import rclpy

remote_frequency = 20

class Control_Panel(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # Timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.send_cmd)
        self.timer.start(remote_frequency)  # Timer fires every 20 milliseconds
        
        # ROS
        rclpy.init(args=None)
        self.cmd_pub = commandPublisher()
        
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
        
    def send_cmd(self):
        direction = 0
        gas_pedal = 0
        steering_wheel = 0
        if self.dp_or_kb == 1:
            if self.b_forward_pressed and self.b_backward_pressed:
                print("You cannot press the forward and backward simultaneously!!!")
                direction = 0
                gas_pedal = 0
            elif self.b_forward_pressed and not self.b_backward_pressed:
                direction = 1 
                gas_pedal = 1
            elif not self.b_forward_pressed and self.b_backward_pressed:
                direction = -1
                gas_pedal = 1
            else :
                direction = 0
                gas_pedal = 0
                
            if self.b_left_pressed and self.b_right_pressed:
                print("You cannot press the left and right simultaneously!!!")
                steering_wheel = 0
            elif self.b_left_pressed and not self.b_right_pressed:
                steering_wheel = 1
            elif not self.b_left_pressed and self.b_right_pressed:
                steering_wheel = -1
            else :
                steering_wheel = 0
        
        elif self.dp_or_kb == 2:
            if self.k_forward_pressed and self.k_backward_pressed:
                print("You cannot press the forward and backward simultaneously!!!")
                direction = 0
                gas_pedal = 0
            elif self.k_forward_pressed and not self.k_backward_pressed:
                direction = 1 
                gas_pedal = 1
            elif not self.k_forward_pressed and self.k_backward_pressed:
                direction = -1
                gas_pedal = 1
            else :
                direction = 0
                gas_pedal = 0
                
            if self.k_left_pressed and self.k_right_pressed:
                print("You cannot press the left and right simultaneously!!!")
                steering_wheel = 0
            elif self.k_left_pressed and not self.k_right_pressed:
                steering_wheel = 1
            elif not self.k_left_pressed and self.k_right_pressed:
                steering_wheel = -1
            else :
                steering_wheel = 0
    
        # print(direction, gas_pedal, steering_wheel)
        self.cmd_pub.publish_command_direction(direction)
        self.cmd_pub.publish_command_gas_pedal(gas_pedal)
        self.cmd_pub.publish_command_steering_wheel(steering_wheel)

       
 
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