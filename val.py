import os 
import signal
import sys
import time

run = True

def signal_handler(signal, frame):
    global run
    print ("exiting")
    run = False

signal.signal(signal.SIGINT, signal_handler)
while run:
 d=os.stat("./text/logtest.txt").st_size == 0
 if d==False:
  os.system('grep "Signal strength" ./text/logtest.txt |cut -c 27-30 >./text/1.txt')
  os.system('tail -n 5 ./text/1.txt > ./text/dbm.txt')
  time.sleep(0.5)
 
 
