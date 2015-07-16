# native
import os
import time
import pyautogui

# custom
from pytribe import EyeTribe


# # # # #
# CONSTANTS

# screen stuff
RESOLUTION = (1920, 1080)
BGC = (0, 0, 0)

#screenWidth, screenHeight = pyautogui.size()
#currentMouseX, currentMouseY = pyautogui.position()
pyautogui.FAILSAFE = False

x_factor = 1920/2880.0
y_factor = 1200/1800.0

# files and paths
DIR = os.path.dirname(os.path.abspath(__file__))
LOGFILE = os.path.join(DIR, 'example_data.txt')

# # # # #
# PREPARE

# start communications with the EyeTribe tracker
tracker = EyeTribe(logfilename=LOGFILE)

i = 0
X_old = tracker.sample()[0]
Y_old = tracker.sample()[1]

while i < 9999:
	time.sleep(.01)
	X = tracker.sample()[0]
	Y = tracker.sample()[1]
	print ("X= " + str(X) + " Y= " + str(Y))

	X_smooth = X * x_factor
	Y_smooth = Y * y_factor

	pyautogui.moveTo(int(X_smooth), int(Y_smooth), .01)


	i = i + 1


# # # # #
# CLOSE

# close connection to the tracker
tracker.close()

