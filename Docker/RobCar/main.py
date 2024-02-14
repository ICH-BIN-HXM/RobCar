from database import database


def test_db(_db):
    _db.write_forward_Velocity(5.0) 
    _db.write_yaw_Speed(4.0) 
    
    print(_db.read_forward_Velocity())
    print(_db.read_yaw_Speed())
    

def main():
    db = database() 
    
    test_db(db) 



if __name__ == "__main__":
    main()