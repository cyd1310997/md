


[linux](linux.md#linux)


# Ubuntu 18.04使用GPT分区并挂载硬盘
## 硬盘分区

<a href="https://unix.stackexchange.com/questions/38164/create-partition-aligned-using-parted/401118" target="_blank">gpt - Create partition aligned using parted - Unix & Linux Stack Exchange</a>  |  <br>  
<a href="https://www.tok9.com/archives/398/" target="_blank">Ubuntu 18.04使用GPT分区并挂载硬盘 - 雨林的Blog</a>  |  <br>  

<a href="https://support.huaweicloud.com/qs-evs/evs_01_0051.html" target="_blank">初始化容量大于2TB的Linux数据盘（parted）_云硬盘 EVS_快速入门_步骤4：初始化数据盘_华为云</a>  |  <br>  
<a href="https://blog.51cto.com/wangqh/2089129" target="_blank">Linux下使用gpt给磁盘分区、格式化、挂载_PeterWang2018_51CTO博客</a>  |  <br>  

<a href="https://www.cnblogs.com/kerrycode/p/9445608.html" target="_blank">Linux查看分区文件系统类型总结 - 潇湘隐者 - 博客园</a>  |  <br>  
<a href="https://askubuntu.com/questions/249387/df-h-used-space-avail-free-space-is-less-than-the-total-size-of-home" target="_blank">disk usage - df -h - Used space + Avail Free space is less than the Total size of /home - Ask Ubuntu</a>  |  <br>  

```
lsblk
fdisk -l
parted -l

df -h
df -Th
df -TH

```

进行 `fdisk -l` 查看机器上都插了哪些安装盘，
看到/dev/sda，没有分区没有挂载
(fdisk只能用于MBR分区，parted可以用于GPT分区)

```
parted /dev/sda

(parted)  
mklabel gpt

(parted)  
unit s

(parted)  
mkpart primary ext4 0% 100%

(parted)  
quit

fdisk -l

```


## 格式化为ext4
```
mkfs.ext4 -F /dev/sda1
```

## 挂载硬盘
```
mkdir -p /data/d
```

```
vim /etc/fstab
# 在文件末尾添加
/dev/sda1 /data/d ext4 defaults 0 0
```

```
mount -a
```
