import cv2

# video stream taken from the camera live
def camera_stream():
    cv2.namedWindow("preview")
    vc = cv2.VideoCapture(0)
    if vc.isOpened(): # try to get the first frame
        rval, frame = vc.read()
    else:
        rval = False

    while rval:
        # live feed as video
        cv2.imshow("preview", frame)
        rval, frame = vc.read()
        
        
        # exit on ESC
        key = cv2.waitKey(20)
        if key == 27: 
            break

    vc.release()
    cv2.destroyWindow("preview")


camera_stream()