import pybullet as p
import time
import numpy as np
import pybullet_data
from Parameters import LEFT_FRONT_WHEEL, LEFT_REAR_WHEEL, RIGHT_FRONT_WHEEL, RIGHT_REAR_WHEEL

# Define motor maximum force
MAX_FORCE = 0.5886  # 0.5886 Nm = 6 kgcm
# Define motor maximum velocity
MAX_VELOCITY = 2.7  # 2.7 rad/s



urdf_name = "Hardware"

def pwm_to_velocity(direction, pwm):
    return direction * (pwm / 100.0) * MAX_VELOCITY 

def velocity_to_pwm(velocity):
    return abs(velocity) / MAX_VELOCITY * 100.0

class Hardware:
    def __init__(self, time_step: float = 0.02, flag_simulation: bool = True):
        self.time_step = time_step
        self.flag_simulation = flag_simulation
    
    def init(self):
        if self.flag_simulation:
            self.left_front_wheel_joint = LEFT_FRONT_WHEEL
            self.right_front_wheel_joint = RIGHT_FRONT_WHEEL
            self.left_rear_wheel_joint = LEFT_REAR_WHEEL
            self.right_rear_wheel_joint = RIGHT_REAR_WHEEL
            
            self.joints = [self.left_front_wheel_joint, self.right_front_wheel_joint, self.left_rear_wheel_joint, self.right_rear_wheel_joint]
            
            # Connect to PyBullet simulation
            p.connect(p.GUI)

            # Set search path to find URDF files
            p.setAdditionalSearchPath(pybullet_data.getDataPath())

            # Load plane and car URDF
            p.loadURDF("plane.urdf")
            self.car = p.loadURDF(urdf_name + ".urdf", [0, 0, 0.1], useFixedBase=False)

            # Set gravity
            p.setGravity(0, 0, -9.81)
            
            # Set time step
            p.setTimeStep(self.time_step/100)
    
    def step(self):
        if self.flag_simulation:
            for counter in range(100):
                p.stepSimulation()
            time.sleep(self.time_step)
    
    def close(self):
        if self.flag_simulation:
            # Disconnect
            p.disconnect()

    # Define control functions
    def control_motor(self, index_motor: int, direction: int = 0, pwm: float = 0.0):
        if index_motor == self.left_front_wheel_joint:
            self.control_left_front_motor(direction, pwm)
        elif index_motor == self.right_front_wheel_joint:
            self.control_right_front_motor(direction, pwm)
        elif index_motor == self.left_rear_wheel_joint:
            self.control_left_rear_motor(direction, pwm)
        elif index_motor == self.right_rear_wheel_joint:
            self.control_right_rear_motor(direction, pwm)
        
    def control_left_front_motor(self, direction, pwm):
        velocity = pwm_to_velocity(direction, pwm)
        p.setJointMotorControl2(self.car, self.left_front_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=velocity, force=MAX_FORCE)

    def control_left_rear_motor(self, direction, pwm):
        velocity = pwm_to_velocity(direction, pwm)
        p.setJointMotorControl2(self.car, self.left_rear_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=velocity, force=MAX_FORCE)

    def control_right_front_motor(self, direction, pwm):
        velocity = pwm_to_velocity(direction, pwm)
        p.setJointMotorControl2(self.car, self.right_front_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=velocity, force=MAX_FORCE)

    def control_right_rear_motor(self, direction, pwm):
        velocity = pwm_to_velocity(direction, pwm)
        p.setJointMotorControl2(self.car, self.right_rear_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=velocity, force=MAX_FORCE)

    # Define functions to get motor state
    def get_motorStates(self):
        states = {}
        
        if self.flag_simulation:
            for index_joint in [self.left_front_wheel_joint, self.right_front_wheel_joint, self.left_rear_wheel_joint, self.right_rear_wheel_joint]:
                if index_joint == self.left_front_wheel_joint:
                    direction, pwm = self.read_left_front_motor()
                    pwm = np.clip(pwm, 0.0, 100.0)
                    states[index_joint] = direction * pwm
                elif index_joint == self.right_front_wheel_joint:
                    direction, pwm = self.read_right_front_motor()
                    pwm = np.clip(pwm, 0.0, 100.0)
                    states[index_joint] = direction * pwm
                elif index_joint == self.left_rear_wheel_joint:
                    direction, pwm = self.read_left_rear_motor()
                    pwm = np.clip(pwm, 0.0, 100.0)
                    states[index_joint] = direction * pwm
                elif index_joint == self.right_rear_wheel_joint:
                    direction, pwm = self.read_right_rear_motor()
                    pwm = np.clip(pwm, 0.0, 100.0)
                    states[index_joint] = direction * pwm
        
        return states
            
                
    
    def read_left_front_motor(self):
        joint_state = p.getJointState(self.car, self.left_front_wheel_joint)
        velocity = joint_state[1]
        direction = 1 if velocity > 0 else (-1 if velocity < 0 else 0)
        pwm = velocity_to_pwm(velocity)
        return direction, pwm

    def read_left_rear_motor(self):
        joint_state = p.getJointState(self.car, self.left_rear_wheel_joint)
        velocity = joint_state[1]
        direction = 1 if velocity > 0 else (-1 if velocity < 0 else 0)
        pwm = velocity_to_pwm(velocity)
        return direction, pwm

    def read_right_front_motor(self):
        joint_state = p.getJointState(self.car, self.right_front_wheel_joint)
        velocity = joint_state[1]
        direction = 1 if velocity > 0 else (-1 if velocity < 0 else 0)
        pwm = velocity_to_pwm(velocity)
        return direction, pwm

    def read_right_rear_motor(self):
        joint_state = p.getJointState(self.car, self.right_rear_wheel_joint)
        velocity = joint_state[1]
        direction = 1 if velocity > 0 else (-1 if velocity < 0 else 0)
        pwm = velocity_to_pwm(velocity)
        return direction, pwm