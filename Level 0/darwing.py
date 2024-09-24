import cv2 as cv
import numpy as np

blank=np.zeros((640,640,3),dtype='uint8')

square_size = 80

# Loop to create a chessboard pattern
for i in range(0, 640, square_size):
    for j in range(0, 640, square_size):
        # Alternate coloring by checking if the sum of i and j is even
        if (i // square_size + j // square_size) % 2 == 0:
            blank[i:i + square_size, j:j + square_size] = (0, 255, 0)

blank2=np.zeros((500,500,3),dtype='uint8')


cv.rectangle(blank2,(200,100),(100,200),(32,58,26),-1)
cv.line(blank2,(200,100),(100,200),(26,26,26),thickness=2)
cv.circle(blank2,(440,440),50,(0,0,250),cv.FILLED)
cv.putText(blank2,"Shinzo Sasageyo!",(30,30),cv.FONT_ITALIC,1,(255,255,255),1,cv.LINE_AA)
cv.imshow("op",blank)
cv.imshow("op2",blank2)
cv.waitKey(0)
