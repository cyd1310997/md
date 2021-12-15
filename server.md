# .

# [server](readme.md)    

- 挑选并购买硬件
- 组装并安置电脑

# 装系统

## 下载系统  
<a href="http://old-releases.ubuntu.com/releases/18.04/" target="_blank">Index of /releases/18.04</a>  |  <br>    
```
ubuntu-18.04.4-live-server-amd64.iso  
```

## rufus (启动盘制作工具)  
<a href="https://rufus.ie/zh/" target="_blank">Rufus - 轻松创建USB启动盘</a>  |  <br>    
```
rufus-3.5.exe  
```

## raid 1  
<a href="https://blog.csdn.net/qq_44673299/article/details/113771436?utm_medium=distribute.pc_relevant.none-task-blog-2~default~baidujs_baidulandingword~default-4.fixedcolumn&spm=1001.2101.3001.4242.3" target="_blank">ubuntu18.04组软RAID1和10及修复_失°疯_失她じ的博客-CSDN博客_ubuntu组raid</a>  |  <br>    


# 配置网络  
[ubuntu.network](ubuntu.network.md#.)

# 启用ssh    
```  
sudo apt install -y sudo vim git openssh-server  
sudo service ssh restart  
```  
应该会开机自启动, 可以重启试一下, 看有没有自动启动ssh  

# ubuntu换源
[docker#ubuntu换源](docker.md#ubuntu换源)    


# 安装必备软件

```
sudo apt install -y sudo vim git openssh-server  
sudo apt install make gcc g++ -y
sudo apt install -y vim git tmux fzf
```

# nvidia
[nvidia](nvidia.md#.)    
禁用 开源显卡驱动 nouveau  
安装 nvidia 驱动  
cuda 和 cudnn 不需要安装, 因为docker容器自带cuda和cudnn  

# docker
[docker](docker.md#.)  

# 挂载硬盘
[ubuntu.disk](ubuntu.disk.md#.)
