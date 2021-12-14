# [ssh.ssh-keygen](readme.md)      
<a href="https://www.jianshu.com/p/dd053c18e5ee" target="_blank">ssh-keygen - 简书</a>        
    
# 生成公钥私钥      
```      
ssh-keygen      
```      
生成公钥私钥(id_rsa.pub, id_rsa)      
    
# 将id_rsa.pub 传输到服务器      
xftp    
scp    
    
# 服务器端接收公钥    
在服务器将其内容追加到~/.ssh/authorized_keys 后面。      
```      
cat id_rsa.pub >> ~/.ssh/authorized_keys      
```      
    
# vscode       
将之前在 ~/.ssh 生成的公钥私钥 复制到 C:\Users\xxx\.ssh 即可实现 vscode 也能通过公钥私钥登录服务器      
(这里的C:\Users\xxx\.ssh 就相当于 ubuntu中的 ~/.ssh)      
    
