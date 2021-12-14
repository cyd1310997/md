# [docker.gpu.public](readme.md)  

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

# 换源
```
chmod 777 /etc/apt/sources.list
vim /etc/apt/sources.list

```

#  阿里源

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
apt install -y tmux fzf

```

# 安装 miniconda
<a href="https://mirrors.tuna.tsinghua.edu.cn/#" target="_blank">清华大学开源软件镜像站 | Tsinghua Open Source Mirror</a>  |  <br>  

获取 miniconda
```
右边, 获取下载链接, 应用软件, conda, Miniconda3-py38_4.9.2-Linux-x86_64.sh, 右键, 复制链接地址

终端中 输入
wget {链接地址}
wget https://mirrors.tuna.tsinghua.edu.cn/anaconda/miniconda/Miniconda3-py38_4.10.3-Linux-x86_64.sh

bash {文件名}
bash Miniconda3-py38_4.10.3-Linux-x86_64.sh
```

安装 miniconda
```
1 回车继续
2 空格阅读条款
3 输入 yes 同意条款
4 回车接受默认安装位置
5 等待安装完成(2分钟)
6 输入 yes 同意初始化conda
7 退出终端重新进入, 或者 source ~/.bashrc
```

# conda pip 换源
在终端中粘贴下面这些命令, 就可以将conda和pip的源都换成清华源 (已经加入了pytorch的清华源)
```
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
conda config --set show_channel_urls yes
pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple

```

# 配置pytorch环境

# 查看已有环境
```
conda info -e

```

# 删除环境
(如果要删除已有的 pytorch 环境)
```
conda activate base
conda remove -n pytorch --all

```

# 新建环境
(python 3.8) , 命名为 pytorch , 并激活
```
conda create -n pytorch python=3.8
conda activate pytorch
```

# 升级pip等基础包
```
conda install pip
pip install --upgrade setuptools
pip install ipython numpy matplotlib pandas
```

# 安装 pytorch
<a href="https://pytorch.org/get-started/locally/" target="_blank">Start Locally | PyTorch</a>  |  <br>  
<a href="https://blog.csdn.net/Boys_Wu/article/details/106623192" target="_blank">pytorch加速下载——清华镜像源(conda或者pip版本)_Boys_Wu的博客-CSDN博客_pytorch清华源下载</a>  |  <br>  

注意: 
先用 nvdia-smi 看一下 右上角的 cuda 版本 然后到官网选择对应版本的链接  
删除安装命令最后的 -c pytorch，才会采用清华源安装。  

```
conda install pytorch torchvision torchaudio cudatoolkit=10.1
conda install pytorch torchvision torchaudio cudatoolkit=11.3
```

# 验证是否成功
```
ipython

import torch
torch.cuda.is_available()

# 如果输出“True”，则说明GPU驱动和CUDA可以支持pytorch的加速计算！
# 恭喜安装成功！
```
