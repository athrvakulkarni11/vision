import cv2 as cv
import numpy as np

img=cv.imread('images\\oslo.jpg')
print (img.shape)
cv.imshow('BGR_img',img)

blank=np.zeros(img.shape[:2], dtype='uint8')

b,g,r=cv.split(img)

cv.imshow('BLUE',b)
cv.imshow('GREEN',g)
cv.imshow('RED',r)

print(b.shape)
print(g.shape)
print(r.shape)

merged_img=cv.merge([b,g,r])
cv.imshow('MERGED',merged_img)

#to merge images such that only the red pixels are allowed only the blue are allowed and so on
merged_b=cv.merge([b,blank,blank])
cv.imshow('blue',merged_b)
merged_g=cv.merge([blank,g,blank])
cv.imshow('green',merged_g)
merged_r=cv.merge([blank,blank,r])
cv.imshow('red',merged_r)



cv.waitKey(0)