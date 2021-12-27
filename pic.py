#!/usr/bin/env python3

import cv2



def picture(video_name):

  vidcap = cv2.VideoCapture(f"./v/{video_name}")

  count = 0

  while(True):
      ret,frame = vidcap.read()
      if ret:
          name = f'pic_file/{count}.jpg'
          cv2.imwrite(name, frame)
          count += 1
      else:
          break




