import os
import time
import logging

logging.basicConfig(filename='output.log', level=logging.INFO, format='%(asctime)s: %(message)s')
logger = logging.getLogger()
#logger.addHandler(logging.Formatter("%(asctime)s;%(levelname)s;%(message)s"), logging.FileHandler('test.log'))

#performing file activity
def T1():
    print("Start!!!! \n Initiating T1 to run for 15min")

    start_time = time.time()
    seconds = 1200
    current_time = time.time()
    elapsed_time = current_time - start_time
    while elapsed_time < seconds:
        for i in range(0,10):
            file = "touch file" + str(i)
            os.system(file)
            os.system("touch syslog.log")
            c = "printf 'Created \n file'"+str(i)
            cat = str(c) + " >> syslog.log"
            print (cat)
            os.system(cat)
        print("Finished Creating Files")
        #os.system("sleep 10")
        for i in range(0,10):
            file = "rm file" + str(i)
            os.system(file)
        
        
        #Performing Network Activity
        os.system("apt-get -y update")   
        
        os.system("apt-get install -y git") 
        os.system("git clone https://github.com/cilium/cilium.git") 
        os.system("git clone https://github.com/kubernetes/client-go.git") 
        os.system("git clone https://github.com/GoogleCloudPlatform/microservices-demo.git")
        os.system("git clone https://github.com/GoogleCloudPlatform/golang-samples.git")
        
        os.system("rm -f -R cilium") 
        os.system("rm -f -R client-go")
        os.system("rm -f -R golang-samples")
        os.system("rm -f -R microservices-demo	")
        os.system("curl http://ip-api.com/json/24.48.0.1")
        #GET order Details
        #os.system("bash system_script.sh")
        elapsed_time = time.time() - start_time
        print("Finished T1 in: " + str(int(elapsed_time))  + " seconds")

#     T2()

# def T2():
#     print("!!!!!!!!!!!!DONE T1!!!!!!!!!!!!!!!!!  Resetting Time to t=0 \n Initiating T2 to run for 15min")
#     start_time = time.time()
#     seconds = 9
#     current_time = time.time()
#     elapsed_time = current_time - start_time
#     while elapsed_time < seconds:
#         #Get Customer Details
#         os.system("bash network_script.sh")

#         elapsed_time = time.time() - start_time
#         print("Finished T2 in: " + str(int(elapsed_time))  + " seconds")
#     T1()

for i in range(0, 1000):
    T1()
    print("Performing loop :   ", i)   