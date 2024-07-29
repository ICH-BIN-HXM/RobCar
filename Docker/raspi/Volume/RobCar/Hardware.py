import pybullet as p
import time
import pybullet_data

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
    def __init__(self, freq: int = 50, flag_simulation: bool = True):
        self.freq = freq
        self.flag_simulation = flag_simulation
    
    def init(self):
        if self.flag_simulation:
            self.left_front_wheel_joint = 0
            self.right_front_wheel_joint = 1
            self.left_rear_wheel_joint = 2
            self.right_rear_wheel_joint = 3
            
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
            p.setTimeStep(1./float(self.freq))
    
    def step(self):
        if self.flag_simulation:
            p.stepSimulation()
            time.sleep(1./float(self.freq))
    
    def close(self):
        if self.flag_simulation:
            # Disconnect
            p.disconnect()

    # Define control functions
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

    # Define functions to read motor state
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