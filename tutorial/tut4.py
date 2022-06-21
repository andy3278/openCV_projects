from matplotlib import image
import cv2
import numpy as np

# a black image
img = np.zeros((600,600,3), np.uint8)

# a line, at (0,0) and (600,600) color white, width 5 pixels
# cv2.line(img, (0,0), (img.shape[1], img.shape[0]), (255,255,255), 5)

# a rectangle top left (0,0) and bottom right (1/3 of canvas, half of canvas) color yellow, width 5 pixels
#cv2.rectangle(img,(0,0), (img.shape[1]//3, img.shape[0]//2), (0,255,255), 5)

# a circle at (300,300) with radius 30 color green, filled
#cv2.circle(img, (img.shape[1]//2, img.shape[0]//2), 30, (0,255,0), cv2.FILLED)

# put text at (200,200) font size 24, color green
cv2.putText(img, "Hello World", (200, 200), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,0), 5)

cv2.imshow('image', img)
cv2.waitKey(0)