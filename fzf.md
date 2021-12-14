# [fzf](readme.md)  


# 安装

## apt安装法

(推荐)
其实只要换成阿里源, 就可以使用apt安装
[docker#ubuntu换源](docker.md#ubuntu换源)

```
sudo apt update
sudo apt install -y tmux fzf
```

## 二进制文件安装法

wget https://gh.api.99988866.xyz/https://github.com/junegunn/fzf/releases/download/0.28.0/fzf-0.28.0-linux_amd64.tar.gz
tar -xzvf fzf-0.28.0-linux_amd64.tar.gz
sudo cp fzf /usr/local/bin

## 源代码安装法

缺点是安装需要连接github.com

```
git clone https://hub.fastgit.org/junegunn/fzf.git
cd fzf
./install

```




