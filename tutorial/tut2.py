import cv2
import numpy as np

img = np.empty((512,512,3), np.uint8)

for row in range(512):
    for col in range(512):
        img[row,col] = (row%255,col%255,(row+col)%255)
cv2.imshow('image', img)

cv2.waitKey(10)