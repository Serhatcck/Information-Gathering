# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 18:06:31 2020

@author: fikirsanat
"""

import sys
import os
import platform
from datetime import datetime
from threading import Thread
import queue
import time
import socket 



port_que = queue.Queue()

starTime = time.time()
target = input("Target:")


oper = platform.system()



print ("-->System:"+platform.system())
print ("-->Version:"+platform.version())
print ("-->Machine:"+platform.machine())
print("")
  
# Add Banner  
print("-" * 50) 
print("Scanning Target: " + target) 
print("Scanning started at:" + str(datetime.now())) 
print("-" * 50) 
   


def scanports(que):
    while True:
        port = que.get()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        socket.setdefaulttimeout(1) 
        result = s.connect_ex((target,port)) 
        if result ==0: 
            print("Port {} is open".format(port)) 
        s.close() 
        que.task_done()

if __name__=='__main__':
    

    try:
        
        
        #65535
        for i in range(0,65535):
            port_que.put(i)
        
        
        
        for i in range(1000):
            t = Thread(target=scanports,args=(port_que,))
            t.daemon = True
            t.start()
            
            
            
        port_que.join()
        
        print('Time Taken:',time.time()-starTime)
        print('Press any key for close')
        a = input()
        
    except KeyboardInterrupt: 
            print("\n Exitting Program !!!!") 
            sys.exit() 
    except socket.gaierror: 
            print("\n Hostname Could Not Be Resolved !!!!") 
            sys.exit() 
    except socket.error: 
            print("\ Server not responding !!!!") 
            sys.exit()