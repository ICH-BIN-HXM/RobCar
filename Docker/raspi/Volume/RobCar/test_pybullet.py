import pybullet as p
import time
import pybullet_data

# Connect to PyBullet simulation
p.connect(p.GUI)

# Set search path to find URDF files
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# Load plane and four-wheel car URDF
p.loadURDF("plane.urdf")
car = p.loadURDF("car.urdf", [0, 0, 0.1], useFixedBase=False)

# Set gravity
p.setGravity(0, 0, -9.81)

left_front_wheel_joint = 0
right_front_wheel_joint = 1
left_rear_wheel_joint = 2
right_rear_wheel_joint = 3

# Define motor maximum force
max_force = 0.5886  # 0.5886 Nm = 6 kgcm
max_velocity = 2.7  # 2.7 rad/s

# Set time step and simulation parameters
p.setTimeStep(1./240.)

# Define PWM to velocity conversion function
def pwm_to_velocity(direction, pwm):
    return direction * (pwm / 100.0) * max_velocity 

def velocity_to_pwm(velocity):
    return abs(velocity) / max_velocity * 100.0

# Define control functions
def control_left_front_motor(direction, pwm):
    velocity = pwm_to_velocity(direction, pwm)
    p.setJointMotorControl2(car, left_front_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=velocity, force=max_force)

def control_left_rear_motor(direction, pwm):
    velocity = pwm_to_velocity(direction, pwm)
    p.setJointMotorControl2(car, left_rear_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=velocity, force=max_force)

def control_right_front_motor(direction, pwm):
    velocity = pwm_to_velocity(direction, pwm)
    p.setJointMotorControl2(car, right_front_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=velocity, force=max_force)

def control_right_rear_motor(direction, pwm):
    velocity = pwm_to_velocity(direction, pwm)
    p.setJointMotorControl2(car, right_rear_wheel_joint, p.VELOCITY_CONTROL, targetVelocity=velocity, force=max_force)

# Define functions to read motor state
def read_left_front_motor():
    joint_state = p.getJointState(car, left_front_wheel_joint)
    velocity = joint_state[1]
    direction = 1 if velocity > 0 else (-1 if velocity < 0 else 0)
    pwm = velocity_to_pwm(velocity)
    return direction, pwm

def read_left_rear_motor():
    joint_state = p.getJointState(car, left_rear_wheel_joint)
    velocity = joint_state[1]
    direction = 1 if velocity > 0 else (-1 if velocity < 0 else 0)
    pwm = velocity_to_pwm(velocity)
    return direction, pwm

def read_right_front_motor():
    joint_state = p.getJointState(car, right_front_wheel_joint)
    velocity = joint_state[1]
    direction = 1 if velocity > 0 else (-1 if velocity < 0 else 0)
    pwm = velocity_to_pwm(velocity)
    return direction, pwm

def read_right_rear_motor():
    joint_state = p.getJointState(car, right_rear_wheel_joint)
    velocity = joint_state[1]
    direction = 1 if velocity > 0 else (-1 if velocity < 0 else 0)
    pwm = velocity_to_pwm(velocity)
    return direction, pwm

# Test control and feedback functions
try:
    while True:
        # Control motors
        control_left_front_motor(1, 100)  # Forward direction, PWM 100
        control_right_front_motor(1, 100)
        control_left_rear_motor(1, 100)
        control_right_rear_motor(1, 100)
        
        for _ in range(240):
            p.stepSimulation()
            time.sleep(1./240.)
        
        # Read motor state
        print("Left Front Motor:", read_left_front_motor())
        print("Right Front Motor:", read_right_front_motor())
        print("Left Rear Motor:", read_left_rear_motor())
        print("Right Rear Motor:", read_right_rear_motor())

except KeyboardInterrupt:
    pass

# Disconnect
p.disconnect()
