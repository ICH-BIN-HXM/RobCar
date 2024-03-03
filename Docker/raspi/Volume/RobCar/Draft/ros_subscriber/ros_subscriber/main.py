import rclpy
from rclpy.node import Node

from std_msgs.msg import String
from std_msgs.msg import Float32


class ros_subscriber(Node):

    def __init__(self):
        super().__init__('ros_subscriber')
        self.subscription = self.create_subscription(
            Float32,
            '/Control/Translation/forward_Velocity',
            self.callback_fw_vel,
            10)
        self.subscription  # prevent unused variable warning

    def callback_fw_vel(self, _msg):
        self.get_logger().info('I heard: "%f"' % _msg.data)


def main(args=None):
    rclpy.init(args=args)

    ros_sub = ros_subscriber()

    rclpy.spin(ros_sub)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    ros_sub.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()