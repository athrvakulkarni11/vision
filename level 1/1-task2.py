import cv2 as cv
import numpy as np

img=cv.imread("C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/resizimg.jpg")
hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)
cv.waitKey(0)

loworange=np.array([5,50,50])
highorange=np.array([15,255,255])
masked=cv.inRange(hsv,loworange,highorange)
cv.imshow("masked img",masked)
cv.waitKey(0)

blank=np.zeros(img.shape[:2],dtype="uint8")
contour,heirarchy=cv.findContours(masked,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
contour1=cv.drawContours(blank,contour,-1,255,1)
cv.imshow("contoured",contour1)
cv.waitKey(0)

x,y,w,h=150,100,250,300
bbox=cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow("Bbox",bbox)
cv.waitKey(0)
bbox2=cv.rectangle(masked,(x,y),(x+w,y+h),255,2)
cv.imshow("Bbox2",bbox2)
cv.waitKey(0)