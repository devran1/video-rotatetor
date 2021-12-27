#!/usr/bin/env python3

#import pic.py



#import cv2

from pic import *
from rotation import *
from video import *

import os

from os.path import isfile, join



# directory for pictures and videos
parent_dir = "./"
directories=["pic_file","rotated_pic","rotated_video"]

for i in directories:
    path = os.path.join(parent_dir, i)
    os.mkdir(path)


filename="MOV_0009.mp4"

picture(filename)

rotation()

video_maker(filename)





