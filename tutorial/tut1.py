import cv2
import numpy as np

cap = cv2.VideoCapture(0) # 0 is the default camera

while True:
    # ret stand for return value, its a boolean value
    # frame is the frame that is being captured
    ret, frame = cap.read()
    if ret:
        frame = cv2.resize(frame, (0,0), fx=1.2, fy=1.2)
        cv2.imshow('video', frame)
    else:
        break
    if cv2.waitKey(10) == ord('q'): 
        # wait 10ms for a keypress if q is pressed then break
        break