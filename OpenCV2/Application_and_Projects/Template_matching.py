"""
    Template matching

    Template matching is a technique for finding areas of an image that are similar to
    a patch (template).
    A patch is a small image with certain features. The goal of template matching is
    to find the patch/template in an image.
    To find it, the user has to give two input images : Source Image (s) The image to
    find the template in and Template Image (T) - The image that is to be found in
    the source image.

    It is basically a method for searching and finding the location of a template
    image in a large image.
    The idea here is to find identical regions of an image that match a template we
    provide, giving a threshold

    The threshold depends on the accuracy with which we want to detect the
    template in the source image.
    For instance, if we are applying face recognition and we want to detect the
    eyes of a person, we can provide a random image of an eye as the template
    and search the source (the face of a person)

    In this case, since "eyes" show a large amount of variations from person to
    person, even if we set the threshold as 50%(0.5), the eye will be detected

    In cases where almost identical templates are to be searched, the
    threshold should be set high. (t>=0.8)


    How Template Matching Works?

    The template image simple slides over the input image (as in 2d convolution)
    The template and patch of input image under the template image are compared.
    The result obtained is compared with the threshold.
    If the function
    cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMAL) the first
    parameter is the mainimage, second parameter is the template to be matched
    and third parameter is the method used for matching.

"""


# Python program to illustrate
# template matching
import cv2
import numpy as np

# Read the main image
img_rgb = cv2.imread('../images/1.jpeg')

# Convert it to grayscale
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

# Read the template
template = cv2.imread('template', 0)

# Store width and height of template in w and h
w, h = template.shape[::-1]

# Perform match operations.
res = cv2.matchTemplate(img_gray,template,cv2.TM_CCOEFF_NORMED)

# Specify a threshold
threshold = 0.8

# Store the coordinates of matched area in a numpy array
loc = np.where( res >= threshold)

# Draw a rectangle around the matched region.
for pt in zip(*loc[::-1]):
	cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)

# Show the final image with the matched area.
cv2.imshow('Detected',img_rgb)
