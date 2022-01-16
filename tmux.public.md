
# [tmux](home.md)    


# 安装 tmux  

```  
sudo apt install tmux  
```  

# 安装 fzf  

[fzf](fzf.md#hi)  


# 在 .bashrc 中配置  

```  

t() {  
  [ -n "$TMUX" ]( -n "$TMUX" .md) && change="switch-client" || change="attach-session"  
  if [ $1 ]; then  
    tmux -u $change -t "$1" 2>/dev/null || (tmux -u new-session -d -s $1 && tmux -u $change -t "$1"); return  
  fi  
  session=$(tmux -u list-sessions -F "#{session_name}" 2>/dev/null | fzf --exit-0) &&  tmux -u $change -t "$session" || echo "No sessions found."  
}  


```  

# tmux 使用手册  
<a href="http://louiszhai.github.io/2017/09/30/tmux/" target="_blank">Tmux使用手册 | louis blog</a>  |  <br>    


