#!/usr/bin/env python3

import numpy as np
import cv2

image_name = "bw"

print("Read an image from file")
img = cv2.imread("images/"+image_name+".png")

print("Create a window holder for the image")
cv2.namedWindow(image_name.upper(),cv2.WINDOW_NORMAL) # Name the window (in this case "Image"), WINDOW_NORMAL = resizable

print("Display the image")
cv2.imshow(image_name.upper(),img)

print("Wait until key press")
cv2.waitKey(0)

print("Copy the image")
cv2.imwrite("images/copy/"+image_name+"-copy.jpg",img) #overwrites if already exists