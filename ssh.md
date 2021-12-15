# [ssh](readme.md)      
<a href="https://www.jianshu.com/p/dd053c18e5ee" target="_blank">ssh-keygen - 简书</a>        

# 登录  
```
ssh 1.1.1.1
ssh user@1.1.1.1
ssh -p 10000 user@1.1.1.1
```

# 清除指纹
如果之前登录了这个ip地址, 但是这个ip地址对应的服务器重装了系统, 需要先清除指纹, 重新登录.
```
ssh-keygen -R 1.1.1.1
```


# 关于免密登录

## 生成公钥私钥      
```      
ssh-keygen      
```      
生成公钥私钥(`id_rsa.pub`, `id_rsa`)      
    
## 将id_rsa.pub 传输到服务器      
xftp    
scp    
    
## 服务器端接收公钥    
在服务器将其内容追加到 `~/.ssh/authorized_keys` 后面。      
```      
cat id_rsa.pub >> ~/.ssh/authorized_keys      
```      
    
## vscode 免密登录      
将之前在 `~/.ssh` 生成的公钥私钥 复制到 `C:\Users\xxx\.ssh` 即可实现 vscode 也能通过公钥私钥登录服务器      
(这里的`C:\Users\xxx\.ssh` 就相当于 ubuntu 中的 `~/.ssh`)      
    
