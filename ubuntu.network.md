

# 常用命令
```
ip a
ifconfig -a
vim /etc/resolv.conf  # 临时修改DNS
```

# 配置网络

<a href="https://blog.csdn.net/u014454538/article/details/88646689" target="_blank">ubuntu18.04配置静态ip和动态ip_lucyLee的博客-CSDN博客_ubuntu配置静态ip</a>  |  <br>  

ubuntu nameserver 总是自动恢复
netplan 配置静态ip

```
cd /etc/netplan
sudo vim xxx.yaml
```

```
# This file is generated from information provided by the datasource.  Changes
# to it will not persist across an instance reboot.  To disable cloud-init's
# network configuration capabilities, write a file
# /etc/cloud/cloud.cfg.d/99-disable-network-config.cfg with the following:
# network: {config: disabled}
network:
    ethernets:
        enp195s0f0:
            dhcp4: no
            addresses: [192.168.1.2/24]
            gateway4: 192.168.1.1
            nameservers:
                    addresses: [8.8.8.8, 8.8.4.4]
        enxb03af2b6059f:
            dhcp4: true
    version: 2
  
```

```
sudo netplan apply
```
