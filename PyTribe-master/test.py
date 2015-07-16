from __future__ import print_function
import sys
import os
import time
import pyautogui
from pytribe import EyeTribe
import serial

# # # # #
# PREPARING OBJECTS
# Setting up usb serial connection
#ser = serial.Serial('/dev/cu.usbmodem1411', 9600) #mac
ser = serial.Serial('/COM4', 9600) #windows

# Start communications with the EyeTribe tracker
tracker = EyeTribe()

# # # # #
# CONSTANTS
x_factor = 1920/2880.0
y_factor = 1200/1800.0
pyautogui.FAILSAFE = False
clickhold = False
i = 0

# # # # #
# STARTING MAIN LOOP
while i < 9999:
    time.sleep(.01)

    # Updates from Eyetracker
    X = tracker.sample()[0]
    Y = tracker.sample()[1]
    
    X_smooth = X * x_factor
    Y_smooth = Y * y_factor

    pyautogui.moveTo(int(X_smooth), int(Y_smooth), .01)

    # Updates from EMG
    reading = str(ser.readline()) #pulls EMG value from arduino
    reading = int(reading[0:1]) #strips carriage return from value

    if reading == 1 and clickhold == False: 
        try:
            pyautogui.click()
        except:
            pass
        clickhold = True

    if reading == 0 and clickhold == True: #resets clickhold on release
        clickhold = False
            
    # Display Data
    print ("X= " + str(X) + " Y= " + str(Y) + " || EMG Reading: " + str(reading))

    i = i + 1

# # # # #
# Close connection to the tracker
tracker.close()
