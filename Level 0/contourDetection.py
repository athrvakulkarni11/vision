# Function for contour detection
import numpy as np
import cv2 as cv


#Step 1 : Convert the image to grayscale
img2=cv.imread('images\\nagi.webp') #used a flag could've used cvtColor function too
img=cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
cv.imshow('GRAY',img)

img=cv.resize(img,(0,0),fx=0.5,fy=0.5,interpolation=cv.INTER_AREA)
img2=cv.resize(img2,(0,0),fx=0.5,fy=0.5,interpolation=cv.INTER_AREA)

blank=np.zeros(img2.shape,dtype='uint8')

#Step 2 : convert the grayscale image to binary via threshold fn or cannny edge detetcion fn
edges=cv.Canny(img,100,200)
cv.imshow('EDGES',edges)
_,thresho=cv.threshold(img,100,200,cv.THRESH_BINARY)
cv.imshow('BINARY_IMG',thresho)

#Step 3 : use findContours function
output,heirarchy=cv.findContours(edges,cv.RETR_LIST,cv.CHAIN_APPROX_SIMPLE)
print(len(output))
contoured=cv.drawContours(blank,output,578,(255,0,0),1)
cv.imshow('CONTOURED IMAGE',contoured)

cv.waitKey(0)

