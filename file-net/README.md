# File-net

For testing vae setup

Performs file and network Activity

creates 10 files
appends "created file (i)" in syslog.log
removes those 10 files

Perform apt update and installs git
git clone cilium, client-go, microservice-demo, golang-samples
rm those folders
curl location api
```bash
cd file-net
sudo docker build -t file-net .
sudo docker run file-net
sudo docker exec --user=root -it ID /bin/bash
```
check syslog.log
