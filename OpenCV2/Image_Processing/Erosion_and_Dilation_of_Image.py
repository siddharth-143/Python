# Pyrhon program to demonstrate erosion and
# dilation of image

import cv2
import numpy as np

# reading the input image
img = cv2.imread("../images/1.jpeg")

# taking a matrix of size 5 as the kernel
kernel = np.ones((3, 3), np.uint8)

# the first parameter is the original image,
# kernel is the matrix with which image is
# convolved and third parameter is the number
# of iteration, which will determine how much
# you want to erode / dilate a given image.

img_erosion = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow("Original", img)
cv2.imshow("Erosion", img_erosion)
cv2.imshow("Dilation", img_dilation)

cv2.waitKey(0)