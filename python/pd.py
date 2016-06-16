import os 
import time

top = 10
bottom = 0
interval = 1

def send2Pd(message=''):
    os.system("echo '" + message + "' | pdsend 3000")

def setVolume(vol):
    message = '1 ' + str(vol) + ';'
    print message
    send2Pd(message)

def up(): 
    for i in range(bottom, top, interval):
        setVolume(i) 
        time.sleep(0.1)

def down():
    for i in range(top, bottom, -interval):
        setVolume(i) 
        time.sleep(0.1)

while True:
   up()
   down()



