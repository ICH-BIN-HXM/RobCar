FROM ubuntu:22.04

WORKDIR /home/user 

# Time Zone 
RUN ln -snf /usr/share/zoneinfo/$CONTAINER_TIMEZONE /etc/localtime && echo $CONTAINER_TIMEZONE > /etc/timezone 

# apt update 
RUN apt update 

# snap 
RUN apt install -y \ 
    snapd 
# python3 
RUN apt install -y \ 
    python3 
# ROS2 Humble 
RUN apt install -y \ 
    software-properties-common
RUN add-apt-repository universe 
RUN apt install -y \ 
    curl 
RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
RUN echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null
RUN apt update 
RUN apt upgrade -y 
RUN apt install -y \ 
    ros-humble-desktop \
    ros-dev-tools 
## Setup the environment for ROS
RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc 

# RUN rm -rf /var/lib/apt/lists/*