import cv2
import numpy as np
ones = np.ones((5,5), np.uint8)

original = cv2.imread('tutorial/unicon.png')
original = cv2.resize(original, (0,0), fx=0.6, fy=0.6)
gray = cv2.imread('tutorial/unicon.png', cv2.IMREAD_GRAYSCALE)
gray = cv2.resize(gray, (0,0), fx=0.6, fy=0.6)


# cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(original, (7,7), 1.5)
canny = cv2.Canny(original, 150, 200)
dilate = cv2.dilate(canny, ones, iterations=2)
erode = cv2.erode(dilate, ones, iterations=2)

#cv2.imshow('original', original)
#cv2.imshow('gray', gray)
#cv2.imshow('blur', blur)
cv2.imshow('canny', canny)
cv2.imshow('dilate', dilate)
cv2.imshow('erode', erode)
cv2.waitKey(0)