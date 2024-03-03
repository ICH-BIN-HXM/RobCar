import rclpy
from rclpy.node import Node

from std_msgs.msg import Int32

class Ros_Publisher(Node):
    def __init__(self):
        super().__init__("ros_pub")
        self.publisher_fw_vel = self.create_publisher(Int32, "/Control/Translation/forward_Velocity", 10)
    
    def publish_ctrl_fw_vel(self, _fw_vel):
        msg_fw_vel = Int32()
        msg_fw_vel.data = int(_fw_vel)
        
        self.publisher_fw_vel.publish(msg_fw_vel)