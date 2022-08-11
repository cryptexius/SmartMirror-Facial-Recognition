import sys
import time

sys.path.insert(0, "/home/cryptexius/Projects");

from huskylib import HuskyLensLibrary

myCam = HuskyLensLibrary("I2C", "", address=0x32); 

# Check if commands are being received: 
print("Knock check: {}".format(myCam.knock())); 

# Initialization
# Sets HuskyLens camera to facial recognition mode: 

myCam.algorthim("ALGORITHM_FACE_RECOGNITION"); #yes "algorthim" is correct...
faceDict = {1: "Evan", 2: "Brian"};

# IF FUNCTION called from js - figure out how to do this!!!
while True: 
	blocks =  myCam.requestAll(); 
    
	for block in blocks:
		if block.learned == True:
			print(block.ID);
			print("Known face: {}".format(faceDict[block.ID]));
		else: 
			print("Unknown face: displaying default screen"); 
	time.sleep(1); 
