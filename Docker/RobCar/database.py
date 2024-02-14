# Define Translation as array 
forward_Velocity = float(0) 
side_Velocity = float(0) 

translation = [forward_Velocity, side_Velocity] # [0]: forward_Velocity ; [1]: side_Velocity 

# Define rotation as array 
yaw_Speed = float(0) 
rotation = [yaw_Speed]  # [0]: yaw_Speed 

# Control 
Control = {} 
Control["TimeStamp"] = float(0) # TODO: TimeStamp needs to be added 
Control["Translation"] = translation
Control["Rotation"] = rotation 

# Feedback 
Feedback = {} 
Feedback["TimeStamp"] = float(0) # TODO: TimeStamp needs to be added 
Feedback["Translation"] = translation
Feedback["Rotation"] = rotation 


class database: 
    def __init__(self):
        self.ctrl_data = Control 
        self.feedback_data = Feedback 
    
    
    # Methods for data collection, e.g. from ROS or MQTT 
    ## forward_Velocity 
    def write_forward_Velocity(self, _forward_Velocity): 
        # TODO: TimeStamp needs to be written 
        self.ctrl_data["Translation"][0] = float(_forward_Velocity) 
    
    ## yaw_Speed 
    def write_yaw_Speed(self, _yaw_Speed): 
        # TODO: TimeStamp needs to be written 
        self.ctrl_data["Rotation"][0] = float(_yaw_Speed) 
    
    
    # Methods for data Selection, e.g. useful for the control of robcar 
    ## forward_Velocity 
    def read_forward_Velocity(self): 
        # TODO: TimeStamp needs to be qualified 
        return self.ctrl_data["Translation"][0] 
    
    ## yaw_Speed 
    def read_yaw_Speed(self): 
        # TODO: TimeStamp needs to be qualified 
        return self.ctrl_data["Rotation"][0] 

 

def test_db(_db):
    _db.write_forward_Velocity(2.0) 
    _db.write_yaw_Speed(4.0) 
    
    print(_db.read_forward_Velocity())
    print(_db.read_yaw_Speed())
    


def main():
    db = database() 
    
    test_db(db) 



if __name__ == "__main__":
    main()