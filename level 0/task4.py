import cv2 as cv
import numpy as np

img=cv.imread("C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/resizimg.jpg")
cv.imshow("original",img)
cv.waitKey(0)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray scaled",gray)
cv.waitKey(0)

blur1=cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur1",blur1)
cv.waitKey(0)
blur2=cv.blur(gray,(5,5),cv.BORDER_DEFAULT)
cv.imshow("blur2",blur2)
cv.waitKey(0)
blur3=cv.medianBlur(gray,5)
cv.imshow("blur3",blur3)
cv.waitKey(0)
blur4=cv.bilateralFilter(gray,5,1.0,cv.BORDER_DEFAULT)
cv.imshow("blur4",blur4)
cv.waitKey(0)

canny=cv.Canny(blur1,10,50)
cv.imshow("canny",canny)
cv.waitKey(0)

dilated=cv.dilate(canny,(5,5),iterations=3)
cv.imshow("dilated",dilated)
cv.waitKey(0)

eroded=cv.erode(canny,(5,5),iterations=1)
cv.imshow("eroded",eroded)
cv.waitKey(0)

blank=np.zeros((img.shape[:2]),dtype="uint8")
contour,heirarchy= cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
contour1=cv.drawContours(blank,contour,-1,(255,255,255),1)
contour2=cv.drawContours(img,contour,-1,(0,255,0),1)
cv.imshow("contour1",contour1)
cv.waitKey(0)
cv.imshow("contour on img",contour2)
cv.waitKey(0)
