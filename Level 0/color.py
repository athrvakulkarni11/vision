import cv2 as cv
# import numpy as np
import matplotlib.pyplot as plt



# blank=np.zeros((1000,900,3),dtype='uint8')

img=cv.imread('images\\tenz.png')
cv.imshow('BGR',img)

plt.imshow(img)
plt.show()
# img=cv.resize(img,(450,450),interpolation=cv.INTER_AREA)

# img1=cv.cvtColor(img,cv.COLOR_BGR2GRAY)

# img2=cv.cvtColor(img,cv.COLOR_BGR2HSV)

# img3=cv.cvtColor(img,cv.COLOR_BGR2LAB)

# blank[0:450,0:450]=img
# #blank[0:450,450:900]=img1
# blank[450:900,0:450]=img2
# blank[450:900,450:900]=img3

# cv.imshow('blank',blank)
# cv.waitKey(0)



