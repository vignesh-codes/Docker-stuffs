#publicly available docker image "python" on docker hub will be pulled

FROM python

#creating directory multi-proc in container (linux machine)

RUN mkdir c:\home\file-net

#copying multi-proc.py from local directory to container's helloworld folder

COPY fs.py /home/file-net/fs.py
#COPY na.py /home/file-net/na.py

#running multi-proc.py in container
RUN pip install requests
CMD python3 /home/file-net/fs.py
#CMD python3 /home/file-net/na.py