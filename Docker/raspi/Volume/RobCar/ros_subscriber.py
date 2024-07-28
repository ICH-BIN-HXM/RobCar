import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32

source = int(0)

class ros_subscriber(Node):
    def __init__(self, _db):
        super().__init__('ros_subscriber')
        
        # create Subscription
        self.sub_fw_vel = self.create_subscription(
            Float32,
            '/Control/Translation/forward_Velocity',
            self.callback_fw_Vel,
            10)
        self.sub_yaw_speed = self.create_subscription(
            Float32,
            '/Control/Rotation/yaw_Speed',
            self.callback_yaw_Speed,
            10)
        self.sub_turn_radius = self.create_subscription(
            Float32,
            '/Control/Rotation/turn_Radius',
            self.callback_turn_Radius,
            10)
        
        # Data base
        self.db = _db
        

    def callback_fw_Vel(self, _msg):
        # self.get_logger().info('forward Velocity: "%f"' % _msg.data)
        self.db.write_forward_Velocity(source, _msg.data) 
    def callback_yaw_Speed(self, _msg):
        # self.get_logger().info('sideward Velocity: "%f"' % _msg.data)
        self.db.write_yaw_Speed(source, _msg.data) 
    def callback_turn_Radius(self, _msg):
        self.db.write_turn_Radius(source, _msg.data) 
    
