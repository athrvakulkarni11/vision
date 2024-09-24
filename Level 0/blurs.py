import cv2 as cv

img=cv.imread('images\\oslo.jpg')

#Averaging
mediocre=cv.blur(img,(3,5))
cv.imshow('AVERAGE',mediocre)

#Gaussian Blur
gauss=cv.GaussianBlur(img, (5,5),cv.BORDER_DEFAULT)
cv.imshow('GAUSSIAN',gauss)

#Median
med=cv.medianBlur(img,5)
cv.imshow('MEDIAN',med)

#bilateral 
bi=cv.bilateralFilter(img,5,50,50)
cv.imshow('BILATERAL',bi)

cv.waitKey(0)
