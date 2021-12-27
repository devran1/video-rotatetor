#!/usr/bin/env python3


import cv2
import os

"""
parent_dir = "./"
directories="rotated_pic"

for i in directories:
    path = os.path.join(parent_dir, i)
    os.mkdir(path)
"""


def rotation():

    APP_FOLDER = './pic_file/'
    totalFiles = 0
    for base, dirs, files in os.walk(APP_FOLDER):

        for Files in files:

            totalFiles += 1

            img = cv2.imread(APP_FOLDER + "/" +Files)
            mage=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)
            cv2.imwrite("./rotated_pic/" + f"{Files}", mage) #add another folder for rotated

        pass


