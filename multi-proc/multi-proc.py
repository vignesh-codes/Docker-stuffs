# importing the requests library 
import requests 
import json 
import os
from time import time, sleep
import threading
import logging

logging.basicConfig(filename='mpOut.log', level=logging.INFO, format='%(asctime)s: %(message)s')
logger = logging.getLogger()
#logger.addHandler(logging.Formatter("%(asctime)s;%(levelname)s;%(message)s"), logging.FileHandler('test.log'))
print = logger.info
def getReq():
    #change number to change time period of api req
    threading.Timer(10, getReq).start()
    response = requests.get("http://ip-api.com/json/27.62.133.109")
    print("GET Request: %s", response.json())


def postReq():
    threading.Timer(20, postReq).start()
    url = "http://ip-api.com/batch"
    myData ='[{"query": "208.80.152.201", "fields": "country"}, "8.8.8.8"]'
    posts = requests.post(url, myData)
    print ("POST&GET Request: %s", posts.json())


def writeFile(): 
# Writing to dummy.txt
    l = "{'status': 'success', 'country': 'India', 'countryCode': 'IN', 'region': 'TN', 'regionName': 'Tamil Nadu', 'city': 'Chennai', 'zip': '600004', 'lat': 13.0878, 'lon': 80.2785, 'timezone': 'Asia/Kolkata', 'isp': 'Bharti Airtel', 'org': 'Bharti Airtel Ltd', 'as': 'AS45609 Bharti Airtel Ltd. AS for GPRS Service', 'query': '27.62.133.109'}"

    json_object = json.dumps(l, indent = 4) 
    threading.Timer(25.0, writeFile).start()
    
    obj = open('dummy.txt', 'w')
    obj.write(l)
    obj.close
    print("CREATED a Text File")


def delFile():
    threading.Timer(30, delFile).start()
    if os.path.exists("dummy.txt"):
        os.remove("dummy.txt")
        print("REMOVED the text file")
    else:
        print("The file does not exist")
    
    
getReq()
postReq()
writeFile()
delFile()