import os 
import time
import serial

arduino = serial.Serial("/dev/ttyACM0", 9600, timeout=5)
time.sleep(1)

top = 10
bottom = 0
interval = 1

arduino.flush()

def getValue(): 
    value = arduino.readline()
    time.sleep(1)
    return value
    
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
   value = getValue()
   setVolume(value)



