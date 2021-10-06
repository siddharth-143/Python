"""
    Play a video in reverse mode

    OpenCV library can be used to perform multiple operations on videos. Let's try to
    do something interesting using cv2. Take a video as input and play it in a reverse
    mode by breaking the video into frame y frame and simultaneously store that
    frame in the list. After getting list of frame we perform iteration over the frames.
    For playing video in reverse mode, we need only to iterate reverse in the list of
    frames. Use reverse method of the list for reversing the order of frames in the
    list.

"""

# python program to play a video
# in reverse mode using opencv

# import cv2 library
import cv2

# VideoCapture method of cv2 return video object

# pass absolute address of video file
cap = cv2.VideoCapture("../Videos/v1.mp4")

# read method of video object will return
# a tuple with 1st element denotes whether
# the frame was read successfully or not,
# 2nd element is the actual frame

# grab the current frame
check, vid = cap.read()

# counting variable for
# counting frame
counter = 0

# intialize the value
# of check variable
check = True

frame_list = []

# if reached the end of the video
# then we got False value of check

# keep looping until we
# got False value of check
while check == True:

    # imwrite method of cv2 saves the
    # image to the specified format
    cv2.imwrite("frame%d.jpg" %counter, vid)
    check, vid = cap.read()

    # add each frame in the list by
    # using append method of the list
    frame_list.append(vid)

    # increment the counter by 1
    counter += 1

# last value in the frame_list is none
# beacuse when video reaches to the end
# then false valus store in check variable
# and None value is store in vide variable

# remove the last value from the
# frame_list by using pop method of list
frame_list.pop()

# looping in the list of frames
for frame in frame_list:

    # show the frame
    cv2.imshow("frame", frame)

    # waitkey method to stoping the frame
    # for some time. q key is presses,
    # stop the loop
    if cv2.waitKey(25) and 0xff == ord("q"):
        break

# release method of video
# object clean the input video
cap.release()

# close any open window
cv2.destroyAllWindows()

# reverse the order of the element
# present in the list by using
# reverse method of the list
frame_list.reverse()

for frame in frame_list:
    cv2.imshow("frame", frame)
    if cv2.waitKey(25) and 0xff == ord("q"):
        break



cap.release()
cv2.destroyAllWindows()