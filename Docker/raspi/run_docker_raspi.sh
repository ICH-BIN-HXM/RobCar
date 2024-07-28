#!/bin/bash

#docker run -it --network=host --ipc=host --pid=host -v '/home/hxm-ubuntu/Project/RobCar/Docker/RobCar:/home/pi/RobCar' -v '/home/hxm-ubuntu/Project/RobCar/Docker/.ros/log:/home/pi/.ros/log' --platform linux/arm64 raspi/ubuntu 

# Automatically detect platform
ARCH=$(uname -m)
if [[ $ARCH == "x86_64" ]]; then
    PLATFORM="linux/amd64"
elif [[ $ARCH == "aarch64" ]]; then
    PLATFORM="linux/arm64"
else
    echo "Unsupported architecture: $ARCH"
    exit 1
fi

# Get current directory
CURRENT_DIR=$(pwd)

# Run Docker container
docker run -it --network=host --ipc=host --pid=host \
    -e DISPLAY=$DISPLAY \
    -v /tmp/.X11-unix/:/tmp/.X11-unix/ \
    -v "$CURRENT_DIR/Volume/RobCar:/home/pi/RobCar" \
    -v "$CURRENT_DIR/Volume/.ros/log:/home/pi/.ros/log" \
    -v "$CURRENT_DIR/Volume/.local:/home/pi/.local" \
    --platform $PLATFORM raspi/ubuntu