import PIL.Image
import numpy as np
import cv2

# video stream taken from the camera live
def video_stream():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        # convert from rgb to gray
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

        # live feed as video
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        key = cv2.waitKey(20)
        if key == 27: # exit on ESC
            break

    vc.release()
    cv2.destroyWindow("preview")


video_stream()