from rclpy.node import Node

from std_msgs.msg import Float32

class Ros_Publisher(Node):
    def __init__(self):
        super().__init__("ros_pub")
        self.publisher_fw_vel = self.create_publisher(Float32, "/Control/Translation/forward_Velocity", 10)
    
    def publish_ctrl_fw_vel(self, _fw_vel):
        msg_fw_vel = Float32()
        msg_fw_vel.data = round(float(_fw_vel), 2)
        
        self.publisher_fw_vel.publish(msg_fw_vel)