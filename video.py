#!/usr/bin/env python3



import cv2
#import torch
#import argparse
#import time
#import numpy as np
#from PIL import Image
import os
from os.path import isfile, join


def video_maker(video_name):

    cap = cv2.VideoCapture(f"./v/{video_name}")

    fps = cap.get(cv2.CAP_PROP_FPS)

    #paths-directories
    pathIn= './rotated_pic/'
    pathOut = "./rotated_video/" + f'rotated-{video_name}'

    #for finding the number of pictures
    APP_FOLDER = './rotated_pic/'
    totalFiles = 0

    #totalDir = 0
    for base, dirs, files in os.walk(APP_FOLDER):
        for Files in files:
            totalFiles += 1
        pass

    #print(totalFiles)


    #image reading
    frame_array = []
    for i in range(totalFiles):

        file=pathIn + f"{i}.jpg"
        #print(file) #558
        img = cv2.imread(file)

        height, width ,layers= img.shape
        h,w=height//4, width//4
        img=cv2.resize(img,(h,w))

        size = (h,w)
        frame_array.append(img)

    #writing image to a video file
    out = cv2.VideoWriter(pathOut,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
    for i in range(len(frame_array)):
        out.write(frame_array[i])
    out.release()

