# hi
# [docker](readme.md)    


# 安装docker    
<a href="https://docs.docker.com/engine/install/ubuntu/" target="_blank">Install Docker Engine on Ubuntu | Docker Documentation</a>  |  <br>  
<a href="https://yeasy.gitbook.io/docker_practice/install/ubuntu" target="_blank">Ubuntu - Docker —— 从入门到实践</a>  |  <br>    

```
# 卸载旧版本, 旧版本的 Docker 称为 docker 或者 docker-engine，使用以下命令卸载旧版本：
sudo apt remove docker \
               docker-engine \
               docker.io
```
```
# 使用 APT 安装, 由于 apt 源使用 HTTPS 以确保软件下载过程中不被篡改。因此，我们首先需要添加使用 HTTPS 传输的软件包以及 CA 证书。
sudo apt update
sudo apt install \
    apt-transport-https \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
```
# 为了确认所下载软件包的合法性，需要添加软件源的 GPG 密钥。
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
```
```
# 然后，我们需要向 sources.list 中添加 Docker 软件源
echo \
  "deb [arch=amd64 signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://mirrors.aliyun.com/docker-ce/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
```
# 安装 Docker, 更新 apt 软件包缓存，并安装 docker-ce：
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
```
```
# 启动 Docker
sudo systemctl enable docker
sudo systemctl start docker
```

```
# 建立 docker 用户组:
sudo groupadd docker

# 将当前用户加入 docker 组：
sudo usermod -aG docker _username_
```
```
# 退出当前终端并重新登录，进行如下测试。
docker run --rm hello-world
```

# docker 使用 cuda
<a href="https://github.com/NVIDIA/nvidia-docker" target="_blank">NVIDIA/nvidia-docker: Build and run Docker containers leveraging NVIDIA GPUs</a>  |  <br>  
<a href="https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/install-guide.html#docker" target="_blank">Installation Guide — NVIDIA Cloud Native Technologies documentation</a>  |  <br>  
<a href="https://blog.csdn.net/weixin_41783910/article/details/109072936" target="_blank">ubuntu18.04安装nvidia-docker备忘_南沙的星星-CSDN博客</a>  |  <br>  

```
distribution=$(. /etc/os-release;echo $ID$VERSION_ID)

curl -s -L https://nvidia.github.io/nvidia-docker/gpgkey | sudo apt-key add -

curl -s -L https://nvidia.github.io/nvidia-docker/$distribution/nvidia-docker.list | sudo tee /etc/apt/sources.list.d/nvidia-docker.list
```

```
curl -s -L https://nvidia.github.io/nvidia-container-runtime/experimental/$distribution/nvidia-container-runtime.list | sudo tee /etc/apt/sources.list.d/nvidia-container-runtime.list
```
```
sudo apt-get update
sudo apt-get install -y nvidia-docker2
```
```
sudo systemctl restart docker
```
```
sudo docker run --rm --gpus all nvidia/cuda:11.0-base nvidia-smi
```




# 修改docker的默认存储位置

<a href="https://zhuanlan.zhihu.com/p/95533274" target="_blank">修改 Docker 的默认存储路径 - 知乎</a>  |  <br>  

<a href="https://blog.csdn.net/BigData_Mining/article/details/104921479" target="_blank">三种方法修改docker的默认存储位置_BigData_Mining的博客-CSDN博客</a>  |  <br>  
<a href="https://blog.csdn.net/wenwenxiong/article/details/78728696" target="_blank">Docker配置本地镜像与容器的存储位置_wenwenxiong的专栏-CSDN博客_docker配置文件位置</a>  |  <br>  

```
sudo su

docker ps -a

docker info | grep "Docker Root Dir"

service docker stop

vim /etc/docker/daemon.json

{
  "data-root": "/data/d/docker"
}

systemctl restart docker

docker info | grep "Docker Root Dir"

df -h
df -Th
df -TH

```




# 新建容器    
```  
docker run -itd -p {real_port}:{container_port} --name {container_name} --restart=always -v {real_location}:{container_location} --gpus device=all --shm-size=32G tensorflow/tensorflow:latest-gpu-py3-jupyter /bin/bash  

-p 10000:22 -p 10001-10010:10001-10010  
-v /data:/data -v /data2:/data2  

--gpus device=all  
--gpus='"device=0,1"'  

```  

# 进入容器    
```  
docker exec -it {container_name / container_id} /bin/bash  
```  

# 启用 ssh    
```  
apt update  
apt install -y sudo vim git openssh-server  
service ssh restart  
```  

# 新建用户    
```  
useradd -m ubuntu -d /home/ubuntu -s /bin/bash  
echo "ubuntu:1234" | chpasswd  
adduser ubuntu sudo  
```  

# ubuntu换源    
```  
chmod 777 /etc/apt/sources.list  
vim /etc/apt/sources.list  

```  

# 阿里源    

```  
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

```  

# 安装软件    
```  
apt update  
apt install -y tmux  

wget https://gh.api.99988866.xyz/https://github.com/junegunn/fzf/releases/download/0.28.0/fzf-0.28.0-linux_amd64.tar.gz  
tar -xzvf fzf-0.28.0-linux_amd64.tar.gz  
cp fzf /usr/local/bin  


```  


# 配置pytorch环境
[conda.pytorch](conda.pytorch.md#hi)

