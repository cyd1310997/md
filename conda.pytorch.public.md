# hi
# [conda.pytorch](home.md)

# 安装 miniconda, conda pip 换源
[conda](conda.md#hi)

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
conda update -n base -c defaults conda
conda install pip  
pip install --upgrade pip
pip install --upgrade setuptools  
pip install ipython numpy matplotlib pandas  
```  

# 安装 pytorch    
<a href="https://pytorch.org/get-started/locally/" target="_blank">Start Locally | PyTorch</a>  |  <br>    
<a href="https://download.pytorch.org/whl/torch_stable.html" target="_blank">https://download.pytorch.org/whl/torch_stable.html</a>  |  <br>    

<a href="https://blog.csdn.net/Boys_Wu/article/details/106623192" target="_blank">pytorch加速下载——清华镜像源(conda或者pip版本)_Boys_Wu的博客-CSDN博客_pytorch清华源下载</a>  |  <br>    

注意:     
先用 nvdia-smi 看一下 右上角的 cuda 版本 然后到官网选择对应版本的链接      
删除安装命令最后的 -c pytorch，才会采用清华源安装。      

先执行这个安装cuda cudnn 等    
```  
conda install pytorch torchvision torchaudio cudatoolkit=10.1  
conda install pytorch torchvision torchaudio cudatoolkit=11.3

```  

然后用这个修改torch的版本    
(旧服务器的cuda是10.1的, 最新支持10.1的torch版本是1.7，装pytorch时复制这个命令安装就好)    
```  
pip install torch==1.7.0+cu101 torchvision==0.8.1+cu101 torchaudio==0.7.0  -f https://download.pytorch.org/whl/torch_stable.html  
```  


# 验证是否成功    
```  
ipython  

import torch  
torch.cuda.is_available()  

# 如果输出“True”，则说明GPU驱动和CUDA可以支持pytorch的加速计算！    
# 恭喜安装成功！    

print(torch.cuda.get_device_name(0))
# NVIDIA A100-PCIE-40GB

```  

```
nvidia-smi
watch -n 2 nvidia-smi
(watch Ctrl+C 退出)
```

```
vim ~/.bashrc

conda activate pytorch
```



