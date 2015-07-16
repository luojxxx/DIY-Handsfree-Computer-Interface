# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 23:42:33 2015

@author: cloudlife
"""
#import serial
#ser = serial.Serial('/dev/cu.usbmodem1411', 9600)
#while True:
#print ser.readline()
#print ser.readline() # Read the newest output from the Arduino

from __future__ import print_function
from time import sleep
import sys
import serial
ser = serial.Serial('/dev/cu.usbmodem1411', 9600) # Establish the connection on a specific port

##### Digital Read Version #####
while True:
    reading = ser.readline()
    print("Current reading: " + str(reading)) 
    sleep(.1)

##### Analog Read Version #####
# values = [0,0,0,0,0,0]
# while True:
#     reading = ser.readline()
#     reading = reading[0:-2]
#    #reading = int(reading)
#     print("Current reading: [" + str(reading) + "]")
#     if reading == '10001':
#         values[0] = ser.readline()[0:-2]

#     if reading == '10002':
#         values[1] = ser.readline()[0:-2]

#     if reading == '10003':
#         values[2] = ser.readline()[0:-2]

#     if reading == '10004':
#         values[3] = ser.readline()[0:-2]

#     if reading == '10005':
#         values[4] = ser.readline()[0:-2]

#     if reading == '10006':
#         values[5] = ser.readline()[0:-2]


#     sleep(.1) # Delay for one tenth of a second
#     print("Stored values:     " + str(values))



