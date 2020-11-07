#publicly available docker image "python" on docker hub will be pulled

FROM python

#creating directory multi-proc in container (linux machine)

RUN mkdir c:\home\multi-proc

#copying multi-proc.py from local directory to container's helloworld folder

COPY multi-proc.py /home/multi-proc/multi-proc.py

#running multi-proc.py in container
RUN pip install requests
CMD python /home/multi-proc/multi-proc.py