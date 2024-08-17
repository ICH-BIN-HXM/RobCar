import time

from Parameters import control_frequency

from Control import Control

def main():
    controller = Control()
    controller.start_sub_ROS()
    while True:
        try: 
            controller.controlCar()
            # time.sleep(control_frequency)
        except KeyboardInterrupt:
            print("!!!END!!!")
            break

    controller.stop_sub_ROS()
    
    




if __name__ == "__main__":
    main()