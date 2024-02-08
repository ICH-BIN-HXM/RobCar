# This document is used for reference for network configuration

```bash
sudo -i
cd /etc/netplan/
vim ...
```

network:
    version: 2
    ethernets:
        eth0:
            dhcp4: true
            nameservers:
              addresses: [8.8.8.8, 1.1.1.1]
            optional: true
    wifis:
        renderer: networkd
        wlan0:
            access-points:
                HXM-Hotspot:
                    hidden: true
                    password: 60591e3579143312f88e250bd13f34d480522d241d37a58787e75c196f0d4d1b
            dhcp4: true
            optional: true


```bash
netplan apply
```