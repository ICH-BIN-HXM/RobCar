from rclpy.node import Node

from std_msgs.msg import Float32

class Ros_Publisher(Node):
    def __init__(self):
        super().__init__("ros_pub")
        self.publisher_fw_vel = self.create_publisher(Float32, "/Control/Translation/forward_Velocity", 10)
        self.publisher_yaw_speed = self.create_publisher(Float32, "/Control/Rotation/yaw_Speed", 10)
    
    def publish_ctrl_fw_vel(self, _fw_vel):
        msg_fw_vel = Float32()
        msg_fw_vel.data = float(_fw_vel)
        
        self.publisher_fw_vel.publish(msg_fw_vel)
        
    def publish_ctrl_yaw_speed(self, _yaw_speed):
        msg_yaw_speed = Float32()
        msg_yaw_speed.data = float(_yaw_speed)
        
        self.publisher_yaw_speed.publish(msg_yaw_speed)