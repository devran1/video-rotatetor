#!/usr/bin/env python3

#import pic.py



#import cv2

from pic import *
from rotation import *
from video import *
from mp4tomp3 import *
from audio_video_combine import *

import os
from os.path import isfile, join
import shutil   
import argparse


parser=argparse.ArgumentParser(description="rotates the videos by 90 degrees clockwise")
parser.add_argument("video_file",help="add video file to rotate",type=str)
args=parser.parse_args()



# directory for pictures and videos
parent_dir = "./"
directories=["pic_file","rotated_pic","rotated_video","audios"]


for i in directories:
    path = os.path.join(parent_dir, i)
    os.mkdir(path)



#filename="test.mp4"
filename=args.video_file


picture(filename)

rotation()

video_maker(filename)


mp4_to_mp3(filename)

#video_path=f"./v/{filename}"

#mp3_path=f"./audios/{filename}.mp3"


audio_video_combine(filename)

"""
#for i in directories:
#    os.rmdir(f"./{i}")
"""
 

for i in directories:
    shutil.rmtree(f"./{i}")
