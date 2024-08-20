from Hardware_Driver import Hardware_Driver
from Parameters import control_frequency

import rclpy
from rclpy.node import Node

from std_msgs.msg import Int64

import threading

import time

class DataBase:
    def __init__(self):
        self.Motion = {
            "Direction": 0,
            "GasPedal": 0,
            "SteeringWheel": 0,
        }

class commandSubscriber(Node):
    def __init__(self, db: DataBase):
        super().__init__('command_subscriber')
        self.subscriber_direction = self.create_subscription(
            Int64,
            'Motion/Direction',
            lambda msg: self.subscriber_direction_callback(msg, db),
            10)
        self.subscriber_direction  # prevent unused variable warning
        
        self.subscriber_gas_pedal = self.create_subscription(
            Int64,
            'Motion/GasPedal',
            lambda msg: self.subscriber_gas_pedal_callback(msg, db),
            10)
        self.subscriber_gas_pedal  # prevent unused variable warning
        
        self.subscriber_steering_wheel = self.create_subscription(
            Int64,
            'Motion/SteeringWheel',
            lambda msg: self.subscriber_steering_wheel_callback(msg, db),
            10)
        self.subscriber_steering_wheel  # prevent unused variable warning

    def subscriber_direction_callback(self, msg, db : DataBase):
        direction = msg.data
        # self.get_logger().info('I heard: "%s"' % msg.data)
        db.Motion["Direction"] = direction
    
    def subscriber_gas_pedal_callback(self, msg, db : DataBase):
        gas_pedal = msg.data
        # self.get_logger().info('I heard: "%s"' % msg.data)
        db.Motion["GasPedal"] = gas_pedal
    
    def subscriber_steering_wheel_callback(self, msg, db : DataBase):
        steering_wheel = msg.data
        # self.get_logger().info('I heard: "%s"' % msg.data)
        db.Motion["SteeringWheel"] = steering_wheel

def thread_ros_subscriber(db: DataBase):
    rclpy.init(args= None)

    cmd_sub = commandSubscriber(db)
    
    try: 
        rclpy.spin(cmd_sub)
    except KeyboardInterrupt: 
        pass
    
    cmd_sub.destroy_node()
    rclpy.shutdown()

class Control:
    def __init__(self):
        self.hw_drv = Hardware_Driver()

        self.db = DataBase()
        
        self.t_ros_sub = threading.Thread(target=thread_ros_subscriber, args=(self.db,))
    
    def start_sub_ROS(self):
        self.t_ros_sub.start()
    
    def stop_sub_ROS(self):
        self.t_ros_sub.join()
    
    def controlCar(self):
        direction = self.db.Motion["Direction"]
        gas_pedal = self.db.Motion["GasPedal"]
        steering_wheel = self.db.Motion["SteeringWheel"]
        
        if gas_pedal == 0:
            self.hw_drv.stop()
        else:
            if direction > 0 and steering_wheel > 0:
                self.hw_drv.forwardLeft()
            elif direction > 0 and steering_wheel == 0:
                self.hw_drv.forwards()
            elif direction > 0 and steering_wheel < 0:
                self.hw_drv.forwardRight()
            elif direction < 0 and steering_wheel > 0:
                self.hw_drv.backwardLeft()
            elif direction < 0 and steering_wheel == 0:
                self.hw_drv.backwards()
            elif direction < 0 and steering_wheel < 0: 
                self.hw_drv.backwardRight()
            else:
                print("ERROR: Combination of direction and steeringwheel not valid!!!")
                self.hw_drv.stop()
            
                