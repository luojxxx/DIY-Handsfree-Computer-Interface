from __future__ import print_function
import sys
import os
import time
import pyautogui
from pytribe import EyeTribe
import serial

# # # # #
# PREPARING CONNECTIONS
# Setting up usb serial connection
#ser = serial.Serial('/dev/cu.usbmodem1411', 9600) #mac
ser = serial.Serial('/COM3', 9600) #windows

# Start communications with the EyeTribe tracker
tracker = EyeTribe()

# # # # #
# CONSTANTS
pyautogui.FAILSAFE = False
clickhold = False

x_factor = 1920/2880.0 #scalculating caling values for retina displays
y_factor = 1200/1800.0

# # # # #
# STARTING MAIN LOOP
i = 0
while i < 9999:
    i = i + 1
    time.sleep(.01)

    # Updates from Eyetracker
    X = int( tracker.sample()[0] )
    Y = int( tracker.sample()[1] )
    
    X = X * x_factor #scales values for retina displays
    Y = Y * y_factor

    pyautogui.moveTo(X, Y, .01) #moves pointer to coordinates

    # Updates from EMG
    reading = str(ser.readline()) #pulls EMG value from arduino
    reading = int(reading[0:1]) #strips carriage return from value

    if reading == 1 and clickhold == False: #registers click when not holding
        try: #deals with I/O overlap error
            pyautogui.click() #performs click command
        except:
            pass
        clickhold = True
    if reading == 0 and clickhold == True: #resets clickhold on release
        clickhold = False
            
    # Display Data
    print ("X= " + str(X) + " Y= " + str(Y) + " || EMG Reading: " + str(reading))

# # # # #
# Close connection to the tracker
tracker.close()

