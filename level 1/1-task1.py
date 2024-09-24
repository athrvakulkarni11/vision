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

def nothing(x):
    pass
cv.namedWindow("image")
cv.createTrackbar("hue_min","image",0,179,nothing)
cv.createTrackbar("hue_max","image",179,179,nothing)
cv.createTrackbar("sat_min","image",0,255,nothing)
cv.createTrackbar("sat_max","image",255,255,nothing)
cv.createTrackbar("val_min","image",0,255,nothing)
cv.createTrackbar("val_max","image",255,255,nothing)

def masking(hsv):
    h_min=cv.getTrackbarPos("hue_min","image")
    h_max=cv.getTrackbarPos("hue_max","image")
    s_min=cv.getTrackbarPos("sat_min","image")
    s_max=cv.getTrackbarPos("sat_max","image")
    v_min=cv.getTrackbarPos("val_min","image")
    v_max=cv.getTrackbarPos("val_max","image")
    lower=np.array([h_min,s_min,v_min])
    upper=np.array([h_max,s_max,v_max])
    masking=cv.inRange(hsv,lower,upper)
    return masking

mask=masking(hsv)
masked2=cv.bitwise_and(hsv,hsv,mask=mask)
cv.imshow("image",masked2)
cv.waitKey(0)

contour,heirarchy=cv.findContours(masked2,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
contour1=cv.drawContours(masked.copy(),contour,-1,(0,0,255),1)
cv.imshow("contoured",contour1)
cv.waitKey(0)

x,y,w,h=150,100,250,300
bbox=cv.rectangle(masked2,(x,y),(x+w,y+h),(0,255,0),2)
cv.imshow("Bbox",bbox)
cv.waitKey(0)
