import cv2 as cv
import numpy as np

img=cv.imread('kitty.jpeg')
img=cv.resize(img,(300,300),interpolation=cv.INTER_AREA)
img2=cv.cvtColor(img,cv.COLOR_BGR2HSV)
img2=cv.resize(img2,(300,300),interpolation=cv.INTER_AREA)

blank=np.zeros((600,600,3),dtype='uint8')
blank[0:300,0:300]=img
blank[300:600,300:600]=img2

cap=cv.VideoCapture("captain levi.mp4")
fourcc=cv.VideoWriter_fourcc(*'mp4v')
out=cv.VideoWriter('output_vid.mp4',fourcc,30,(600,600))

while True:
  ret,frame=cap.read()
  frame=cv.resize(frame,(300,300),interpolation=cv.INTER_AREA)
  blank[0:300,300:600]=frame
  blank[300:600,0:300]=frame
  cv.imshow("output",blank)
  out.write(blank)
  if(cv.waitKey(25)==ord('q')):
    break

cap.release()
out.release()
cv.destroyAllWindows()
