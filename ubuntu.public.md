# hi
# [ubuntu](home.md)    



# 装系统

## download  
<a href="http://old-releases.ubuntu.com/releases/18.04/" target="_blank">Index of /releases/18.04</a>  |  <br>    
```
ubuntu-18.04.4-live-server-amd64.iso  
```

## rufus 
(启动盘制作工具)  
<a href="https://rufus.ie/zh/" target="_blank">Rufus - 轻松创建USB启动盘</a>  |  <br>    
```
rufus-3.5.exe  
```

## raid 1  
<a href="https://blog.csdn.net/qq_44673299/article/details/113771436?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-4.fixedcolumn&spm=1001.2101.3001.4242.3" target="_blank">ubuntu18.04组软RAID1和10及修复_失°疯_失她じ的博客-CSDN博客_ubuntu组raid</a>  |  <br>    



# network
[ubuntu.network](ubuntu.network.md#hi)



# ssh    
```  
apt update  
apt install -y sudo vim git tmux openssh-server  
service ssh restart  
```  

# useradd    
```  
useradd -m ubuntu -d /home/ubuntu -s /bin/bash  
echo "ubuntu:1234" | chpasswd  
adduser ubuntu sudo  
```  

# apt换源    
```  
lsb_release -a
# Ubuntu 18.04

chmod 777 /etc/apt/sources.list  
vim /etc/apt/sources.list  

deb http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse  
deb http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse  
deb http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse  
deb http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse  
deb http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-security main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-updates main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-proposed main restricted universe multiverse  
deb-src http://mirrors.aliyun.com/ubuntu/ bionic-backports main restricted universe multiverse  

apt update  
```  


# [ubuntu.disk](ubuntu.disk.md#hi)


