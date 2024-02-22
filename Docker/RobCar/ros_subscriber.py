import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32

source = int(0)

class ros_subscriber(Node):
    def __init__(self, _db):
        super().__init__('ros_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            '/Control/Translation/forward_Velocity',
            self.callback_fw_vel,
            10)
        self.subscription  # prevent unused variable warning
        
        self.db = _db
        

    def callback_fw_vel(self, _msg):
        self.get_logger().info('forward Velocity: "%f"' % _msg.data)
        self.db.write_forward_Velocity(source, _msg.data) 
