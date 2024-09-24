import cv2
import numpy as np
blank=np.zeros((500,500,3),dtype="uint8")
cv2.imshow("blank",blank)
cv2.waitKey(0)

cv2.line(blank,(0,250),(500,250),(255,255,255),2)
cv2.line(blank,(250,0),(250,500),(255,255,255),2)
cv2.imshow("blank",blank)
cv2.waitKey(0)

cv2.rectangle(blank,(50,50),(200,200),(255,0,0),1)
cv2.imshow("blank",blank)
cv2.waitKey(0)

cv2.circle(blank,(125,375),100,(0,255,0),1)
cv2.imshow("blank",blank)
cv2.waitKey(0)

cv2.ellipse(blank,(375,125),(100,70),0,0,360,(0,0,255),1)
cv2.imshow("blank",blank)
cv2.waitKey(0)

points=np.array([[300,375],[375,400],[400,475],[300,300]])
cv2.polylines(blank,[points],True,(255,100,100),1)
cv2.imshow("blank",blank)
cv2.waitKey(0)

cv2.putText(blank,"Hello",(75,380),cv2.FONT_HERSHEY_TRIPLEX,1.0,(100,255,100),3)
cv2.imshow("blank",blank)
cv2.waitKey(0)

cv2.putText(blank,"Hello",(75,130),cv2.FONT_HERSHEY_SIMPLEX,1.0,(100,100,255),3)
cv2.imshow("blank",blank)
cv2.waitKey(0)

cv2.putText(blank,"Hello",(325,130),cv2.FONT_HERSHEY_COMPLEX,1.0,(100,50,100),3)
cv2.imshow("blank",blank)
cv2.waitKey(0)
