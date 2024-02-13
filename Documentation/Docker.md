# This document is used for developing with Docker

## Basic settings 
### delete docker image
[](https://stackoverflow.com/questions/51188657/image-is-being-used-by-stopped-container-error) 

### Get simpliest Docker for Arm64
[Running Ubuntu ARM64 with Docker](https://jkfran.com/running-ubuntu-arm-with-docker/) 


### Useful commands 
```bash
docker image ls -a 
docker rmi <repository_name> 
docker save -o /home/hxm-ubuntu/Project/RobCar/Docker/image/docker_20240213.tar raspi/ubuntu:latest
```

### Trouble Shooting 
[Failed to connect. Is Docker running? (Vs Code)](https://stackoverflow.com/questions/69530014/failed-to-connect-is-docker-running-vs-code) 
```bash
sudo chmod 666 /var/run/docker.sock
```

## Install ROS Humble in Docker 
[](https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html) 
(Reminder: Remember to delete the `sudo`) 
