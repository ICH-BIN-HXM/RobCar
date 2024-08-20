from rclpy.node import Node

from std_msgs.msg import Int64

class commandPublisher(Node):
    def __init__(self):
        super().__init__("command_publisher")
        self.publisher_direction = self.create_publisher(Int64, "/Motion/Direction", 10)
        self.publisher_gas_pedal = self.create_publisher(Int64, "/Motion/GasPedal", 10)
        self.publisher_steering_wheel = self.create_publisher(Int64, "/Motion/SteeringWheel", 10)
    
    def publish_command_direction(self, direction: int = 0):
        msg_direction = Int64()
        msg_direction.data = int(direction)
        
        self.publisher_direction.publish(msg_direction)
        
    def publish_command_gas_pedal(self, gas_pedal: int = 0):
        msg_gas_pedal = Int64()
        msg_gas_pedal.data = int(gas_pedal)
        
        self.publisher_gas_pedal.publish(msg_gas_pedal)
        
    def publish_command_steering_wheel(self, steering_wheel: int = 0):
        msg_steering_wheel = Int64()
        msg_steering_wheel.data = int(steering_wheel)
        
        self.publisher_steering_wheel.publish(msg_steering_wheel)