"""
    White and black dot detection :

    Count black dots on a white surface :

    At first we need to import OpenCV library. All functions regarding image
    processing reside in the library. In order to store the path of the image we are
    going to process in a variable path.
"""

import cv2

# path
path = "../images/1.jpeg"

"""
    Loading an image in grayscale mode. By grayscale mode, the image is converted
    to a black & white image composing by shape of gray.
"""

gray = cv2.imread(path, 0)

"""
    The function cv2.threshold works as, if pixel value is greater than a threshold
    value, it is assigned one value (may be white), else it is assigned another value
    (may be black). First argument is the source image, which should be a grayscale
    image (done previously). Second argument is the threshold value which is used
    to classify the pixel values. For threshold value, simply pass zero. Then the
    algorithm finds the optimal threshold value and returns you as the second
    output, th. If Otsu thresholding is not used, th is same as the threshold value you
    used.
"""

# threshold
th, theshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV | cv2.THRESH_OTSU)

"""
    Contours can be explained simply as a curve joining all the continuous points
    (along the boundary), having same color or intensity. The contours are a useful
    tool for shape analysis and object detection and recognition. Contours given better
    accuracy for using binary images. There are three arguments in
    cv2.findContours() function, first one is source image, is contour
    retrieval mode, third is contour approximation method. It outputs the contours
    and hierarchy. Contours is a python list of all the contours in the image. Each
    individual contour is a Numpy array of (x, y) coordinates of boundary points of
    the object.
    
    It mainly connects the black dots of the image to count
"""

# find contours
cnts = cv2.findContours(theshed, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)[-2]

"""
    cv2.contourArea() can calculate the contour area of the object. Here the object is
    the black dots. When it gets a black dot it will calculate the area and if it satisfies
    the condition of minimum area to be count as a dot, then it will push the value of
    its area to the list xcnts.
"""

# filter by area
s1 = 3
s2 = 20
xcnts = []
for cnt in cnts:
    if s1 < cv2.contourArea(cnt) < s2:
        xcnts.append(cnt)

"""
    At last, we don't need the areas. It it is considered to be a dot, then its rea is
    included in the list xcnts. So, we will get number of the dots if we calculate the
    length of the list.
"""

print("\n Dots number : {}".format(len(xcnts)))

"""
    Count white dots on a black background
    
    Now for counting the white dots we need to change the threshold a little bit. We
    have to use cv2.THRESH_BINARY instead of cv2.THRESH_BINARY_INV because we are
    counting white values on the black surface. The other process are the same. We
    can change the s1 and s2 values to check for the best result.
    
    th, theshed = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
"""