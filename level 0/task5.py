import cv2 as cv

img=cv.imread("C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/resizimg.jpg")
cv.imshow("original",img)
cv.waitKey(0)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

#simple
value,thresh=cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow("threshold",thresh)
cv.waitKey(0)
value,thresh1=cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow("threshold inverted",thresh1)
cv.waitKey(0)

#adaptive
ad_thresh=cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,7,3)
cv.imshow("adaptive threshold",ad_thresh)
cv.waitKey(0)