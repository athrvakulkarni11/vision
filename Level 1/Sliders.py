import cv2
import numpy as np

cap=cv2.VideoCapture(1)

def callback(i):
   pass

cv2.namedWindow("TrackedBars")
cv2.resizeWindow("TrackedBars", 640, 240)

cv2.createTrackbar("Hue Min", "TrackedBars", 0, 179, callback)
cv2.createTrackbar("Hue Max", "TrackedBars", 179, 179, callback)
cv2.createTrackbar("Sat Min", "TrackedBars", 0, 255, callback)
cv2.createTrackbar("Sat Max", "TrackedBars", 255, 255, callback)
cv2.createTrackbar("Val Min", "TrackedBars", 0, 255, callback)
cv2.createTrackbar("Val Max", "TrackedBars", 255, 255, callback)

while True:

    ret,frame=cap.read()

    if not ret:
      break

    hue_min = cv2.getTrackbarPos("Hue Min", "TrackedBars")
    hue_max = cv2.getTrackbarPos("Hue Max", "TrackedBars")
    sat_min = cv2.getTrackbarPos("Sat Min", "TrackedBars")
    sat_max = cv2.getTrackbarPos("Sat Max", "TrackedBars")
    val_min = cv2.getTrackbarPos("Val Min", "TrackedBars")
    val_max = cv2.getTrackbarPos("Val Max", "TrackedBars")

    lower = np.array([hue_min, sat_min, val_min])
    upper = np.array([hue_max, sat_max, val_max])

    HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    mask = cv2.inRange(HSV, lower, upper)
    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Mask", result)

    gray=cv2.cvtColor(result,cv2.COLOR_BGR2GRAY)
    ret,threso=cv2.threshold(gray,0,255,cv2.THRESH_BINARY)

    #Contour detection and largest contour
    contours,heirarchy=cv2.findContours(threso,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)

   if len(contours)>0:
    areaOI=max(contours,key=cv2.contourArea)
    #Adding Bbox around it
    x,y,w,h=cv2.boundingRect(areaOI)
    rect=cv2.rectangle(result,(x,y),(x+w,y+h),(0,255,0),4)
   else:
      print("No contours detected")

    cv2.imshow('Final_Result',rect)
    if cv2.waitKey(20)==ord('q'):
      break

cap.release()
cv2.destroyAllWindows()
