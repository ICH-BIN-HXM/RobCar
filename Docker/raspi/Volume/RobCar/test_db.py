from Docker.raspi.Volume.RobCar.database_backup import database

def test_db(_db):
    _db.write_forward_Velocity(0, 5.0) 
    _db.write_yaw_Speed(0, 4.0) 
    
    print(_db.read_forward_Velocity())
    print(_db.read_yaw_Speed())