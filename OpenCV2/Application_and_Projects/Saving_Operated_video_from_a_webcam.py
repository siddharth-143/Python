"""
    Saving Operated Video from a webcam

    Firstly,  we specify the fourcc variable. FourCC is a 4-byte code used to specify the
    video codec. The codecs for Windows is DIVX and for OSX is avc1, h263. FourCC code
    is passed as
    cv2.VideoWrite_fourcc(*MJPG) for MJPG and
    cv2,VideoWrite_fourcc(*XVID) for DIVX

    cv2.VideoWrite(filename, fourcc, fps, frameSize)

    The parameters are

    filename : Specifies the name of the output video
    fourcc : (for recording) Defining the codec
    fps : Define frame rate of the output video stream
    framesize : Size of video frames
"""

# Python program to illustrate
# saving an operated video

# organize import
import cv2
import numpy as np

# this will return video from the first webcam on your computer
cap = cv2.VideoCapture(0)

# define the codec and create VideoWrite object
fourcc = cv2.VideoWriter_fourcc(*"XVID")
out = cv2.VideoWriter("output.avi", fourcc, 20.0, (640, 480))

# loop runs if capturing has been initialized
while True:

    # read frames from a camera
    # ret checks return at each frame
    ret, frame = cap.read()

    # convert to HSV color space, OCV reads color as BGR
    # frame is converted to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # output the frame
    out.write(hsv)

    # the original input frame is shown in the window
    cv2.imshow("Original", frame)

    # the window showing the operated video stream
    cv2.imshow("frame", hsv)

    # wait for "q" key to stop the program
    if cv2.waitKey(1) & 0xff == ord("q"):
        break

# close the window / release webcam
cap.release()

# after we release out webcam, we also release the output
out.release()

# de-allocate any associated memory usage
cv2.destroyAllWindows()