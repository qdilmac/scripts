#!/usr/bin/env python3

import numpy as np
import cv2

image_name = "tree"

img = cv2.imread("images/"+image_name+".jpg")

print(img)
print(type(img))
print(img.size)
print(len(img)) # number of pixels
print(img.shape) # length, width, number of colors/channels (rgb)
print(img.shape[0]) # we can specifically get the value we desire
print(img.dtype) # data type = 8-bit unsigned integer (range: 0-255)
print(img[:,:,1])