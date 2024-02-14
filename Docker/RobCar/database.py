# Head 


# Control 
forward_Velocity = float(0) 
side_Velocity = float(0) 

translation = [forward_Velocity, side_Velocity] # [0]: forward_Velocity ; [1]: side_Velocity 

yaw_Speed = float(0) 
rotation = [yaw_Speed]  # [0]: yaw_Speed 

Control = {} 
Control["Translation"] = translation
Control["Rotation"] = rotation 

Feedback = {} 
Feedback["Translation"] = translation
Feedback["Rotation"] = rotation 

class database: 
    def __init__(self):
        self.ctrl_data = Control 
        self.feedback_data = Feedback
        
  
def test_db(_db):
    forward_vel = _db.ctrl_data["Translation"][0] 
    _db.feedback_data["Translation"][0] = forward_vel 
    


def main():
    db = database() 
    
    db.ctrl_data["Translation"][0] = 3.0 
    test_db(db) 
    
    print(db.feedback_data["Translation"][0]) 



if __name__ == "__main__":
    main()