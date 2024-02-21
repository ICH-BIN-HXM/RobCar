# This document is used for configuration of the camera 

## Motion 
### Configuration 
#### Install Motion 
```bash
sudo apt update
sudo apt install motion
```
#### Config Motion 
[Installing and Configuring Motion to setup a Web Cam Server](https://youtu.be/p1An7l0PY2M?si=YRj94RmDif8keInj) 
2 Settings need to be changed 
- webcontrol_localhost off
- stream_localhost off

#### Official Documentaion of Motion 
[](https://motion-project.github.io/motion_config.html#basic_setup_network) 

### Start and Stop Service 
[Build a Raspberry Pi Webcam Server in Minutes](https://pimylifeup.com/raspberry-pi-webcam-server/) 
## Access 
```
http://XXX:8080 
```

### Trouble Shooting 
[](https://raspberrypi.stackexchange.com/questions/78715/motion-daemon-var-log-motion-motion-log-permission-denied)
```bash
sudo chown motion:motion /var/log/motion
```
