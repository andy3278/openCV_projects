import cv2

img = cv2.imread('tutorial/unicon.png', cv2.IMREAD_GRAYSCALE)
img = cv2.resize(img, (0,0), fx=0.6, fy=0.6)

# cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

cv2.imshow('image', img)
cv2.waitKey(0)