import cv2 as cv

img=cv.imread("images//kitty.jpeg",0)

adaptive=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,3)
cv.imshow('output',adaptive)
cv.waitKey(0)