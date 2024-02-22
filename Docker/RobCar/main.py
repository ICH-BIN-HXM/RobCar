import rclpy

import threading

from database import database
from test_db import test_db

from ros_subscriber import ros_subscriber


def thread_ros_subscriber(_db):
    rclpy.init(args=None)
    ros_sub = ros_subscriber(_db)
    
    try: 
        rclpy.spin(ros_sub)
    except KeyboardInterrupt: 
        pass
    
    ros_sub.destroy_node()
    rclpy.shutdown()


def main():
    db = database() 
    # test_db(db) 
    
    t_ros_sub = threading.Thread(target=thread_ros_subscriber, args=(db,))
    t_ros_sub.start()
    
    # print(db.read_forward_Velocity())
    
    t_ros_sub.join()
    
    



    

if __name__ == "__main__":
    main()