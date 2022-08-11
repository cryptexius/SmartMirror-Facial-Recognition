# !/usr/bin/python
# coding: utf8

import sys
import os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/common/'))
sys.path.insert(0, "/home/cryptexius/Projects");

from huskylib import HuskyLensLibrary
from config import MMConfig

import signal

# Initialize HuskyLens Camera
myCam = HuskyLensLibrary("I2C", "", address=0x32);

# Checks if commands are being received
MMConfig.toNode("status", "Knock check: {}".format(myCam.knock()));

# Sets HuskyLens camera to facial recognition mode
myCam.algorthim("ALGORITHM_FACE_RECOGNITION"); # "algorthim" is "correct"!!

# Current setup configured for Evan & Brian facial recognition
# Number in dictionary corresponds to facialID from internal HuskyLens Facial Recognition Software
faceIDdict = {1: "Evan", 2: "Brian"};

# Setup variables
current_user = None
login_timestamp = time.time();

# Main Loop
while True:
    # Sleep for x seconds specified in module config
    time.sleep(MMConfig.getInterval());
    
    blocks = myCam.requestAll();
    
    # If no face found, logout user after time interval exceeded
    if len(blocks) == 0:
        # if last detection exceeds timeout and someone is logged in --> logout
        if(current_user is not None and time.time() - login_timestamp > MMConfig.getLogoutDelay()):
            # Callback logout to node helper
            MMConfig.toNode("logout", {"user": current_user})
            current_user = None;
        continue
    
    for block in blocks:
        if block.learned:
            # Sets login time
            login_timestamp = time.time();
            
            if current_user is None:
                current_user = faceIDdict[block.ID];
                # Callback current user to node helper
                MMConfig.toNode("login", {"user": faceIDdict[block.ID]});
                
            
    

