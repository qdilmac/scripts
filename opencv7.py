#!/usr/bin/env python3

# Color Filtering!

import numpy as np
import cv2

image = cv2.imread("images/tennis.jpeg")
cv2.imshow("Normal",image)

# first we convert RGB to HSV
hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV",hsv)

# tennis ball's color values / lower and upper values / find values that works, there is no specific value
yellowLower = (27.5, 10, 10) # for the image that i used these values are almost perfect
yellowUpper = (50, 255, 255)

# mask definition
mask = cv2.inRange(hsv,yellowLower,yellowUpper)
cv2.imshow("Mask",mask)

cv2.waitKey(0)
cv2.destroyAllWindows()