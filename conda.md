# hi
# [conda](readme.md)

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
7 退出终端重新进入, 或者 
source ~/.bashrc  
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

# conda 基本操作
```
whereis conda
conda --version
conda list
conda env list
conda info -e                                     显示环境列表
conda create -n _name_ python=3.8                 创建环境
conda create -n _name_ --clone _name2_            克隆环境
conda activate _name_                             激活环境
conda install -c anaconda _name_                  使用官方源安装
conda remove -n _name_ --all                      删除环境 
conda update _name_
```
