import rclpy

import threading

from database import database

from ros_subscriber import ros_subscriber
from Car import Car



    
def thread_ros_subscriber(_db):
    rclpy.init(args=None)
    ros_sub = ros_subscriber(_db)
    
    try: 
        rclpy.spin(ros_sub)
    except KeyboardInterrupt: 
        pass
    
    ros_sub.destroy_node()
    rclpy.shutdown()

def control(db, car):
    command_forward_Velocity = float(db.read_forward_Velocity()) 
    command_yaw_Speed = float(db.read_yaw_Speed())
    
    car.move(command_forward_Velocity, command_yaw_Speed)
    

def main():
    db = database() 
    car = Car()
    
    t_ros_sub = threading.Thread(target=thread_ros_subscriber, args=(db,))
    t_ros_sub.start()
    
    while True:
        try: 
            control(db, car)
        except KeyboardInterrupt:
            print("!!!END!!!")
            break
            
    
    t_ros_sub.join()
    
    




if __name__ == "__main__":
    main()