# This document is used for developing with Docker

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

