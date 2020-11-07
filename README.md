# Docker-stuffs

For testing vae setup

multi proc scenario:
get 1 api response every 10 seconds
another api response every 20 seconds
creates dummy file every 600 seconds
Deletes that dummy file every 650 seconds


```bash
cd multi-proc
sudo docker build -t multi-proc .
sudo docker start multi-proc
sudo docker exec --user=root -it ID /bin/bash
```

source file is in /home/multi-proc/multi-proc.py
log found in home/mpOut.log 
