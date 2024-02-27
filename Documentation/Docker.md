# This document is used for developing with Docker

## Install Docker 
[Installing Docker Using the Installation Script](https://kinsta.com/blog/install-docker-ubuntu/#3-installing-docker-using-the-installation-script) 
```bash
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

## Manage Docker  
### Container 
#### List 
```bash
docker container ls -a 
```
#### Stop 
```bash
docker stop ${CONTAINER_ID}
```
#### Delete 
```bash
docker rm ${CONTAINER_ID}
```
### Image 
#### List
```bash
docker image ls -a 
```
#### [Delete](https://stackoverflow.com/questions/51188657/image-is-being-used-by-stopped-container-error) 
```bash
docker rmi ${IMAGE_NAME}
```
### Backup
```bash
docker save -o /home/hxm-ubuntu/Project/RobCar/Docker/image/docker_20240213.tar raspi/ubuntu:latest
```

## Trouble Shooting 
[Failed to connect. Is Docker running? (Vs Code)](https://stackoverflow.com/questions/69530014/failed-to-connect-is-docker-running-vs-code) 
```bash
sudo chmod 666 /var/run/docker.sock
```

## Dockerfile 
### Reference 
[Install ROS Humble in Docker](https://docs.ros.org/en/humble/Installation/Alternatives/Ubuntu-Development-Setup.html) 
(Reminder: Remember to delete the `sudo`, [Set Time Zone](https://askubuntu.com/questions/909277/avoiding-user-interaction-with-tzdata-when-installing-certbot-in-a-docker-contai)) 

## ROS Communication 
### Domain ID
```bash
export ROS_DOMAIN_ID=0
```
### Trouble Shooting 
- [See Topics but no data](https://github.com/rosblox/ros-template?tab=readme-ov-file#solution) 
    - run docker arguments 
        ```bash
        --net=host --ipc=host --pid=host
        ```
    - same user id of docker and host 
        - check the user id 
            ```bash
            id -u 
            ```
        - set user and give the power same as root 
            ```bash
            ## Set the UID for the regular user
            ARG USER_ID=1000
            ## Add the pi user and set its UID to the specified USER_ID
            RUN useradd -u $USER_ID -m pi
            ## Add the pi user to the sudoers file and allow executing sudo commands without password
            RUN echo 'pi ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers
            ## Switch to the pi user
            USER pi
            ```

- Give user permission to write log
    - [ROS2 topics on Docker detected by host but can't subscribe](https://github.com/eProsima/Fast-DDS/issues/2956) 
        - run docker arguments 
            ```bash
            -v '/home/hxm-ubuntu/Project/RobCar/Docker/.ros/log:/home/pi/.ros/log'
            ```
