import rclpy

import threading

from database import database
from test_db import test_db

from ros_subscriber import ros_subscriber
from driver import Driver


def thread_ros_subscriber(_db):
    rclpy.init(args=None)
    ros_sub = ros_subscriber(_db)
    
    try: 
        rclpy.spin(ros_sub)
    except KeyboardInterrupt: 
        pass
    
    ros_sub.destroy_node()
    rclpy.shutdown()

def control(db, drv):
    command_forward_Velocity = float(db.read_forward_Velocity()) 
    command_yaw_Speed = float(db.read_yaw_Speed())
    
    if command_forward_Velocity > 0 :
        drv.move_forward(command_forward_Velocity) 
    elif command_forward_Velocity < 0 : 
        drv.move_backward(command_forward_Velocity) 
        
    if command_yaw_Speed > 0 : 
        drv.turn_left(command_yaw_Speed)
    elif command_yaw_Speed < 0 : 
        drv.turn_right(command_yaw_Speed)
    

def main():
    db = database() 
    drv = Driver()
    # test_db(db) 
    
    t_ros_sub = threading.Thread(target=thread_ros_subscriber, args=(db,))
    t_ros_sub.start()
    
    while True:
        try: 
            control(db, drv)
        except KeyboardInterrupt:
            print("!!!END!!!")
            break
            
    
    t_ros_sub.join()
    
    




if __name__ == "__main__":
    main()