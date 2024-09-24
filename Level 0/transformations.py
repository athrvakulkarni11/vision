import cv2 as cv
import numpy as np

# image translation
image=cv.imread("images\\nagi.webp")
image=cv.resize(image,(600,600),)

def translation(img,x,y):
    transMat=np.float32([[1,0,x],[0,1,y]])#creation of an affine matrix transformation for shifting along x and y
    dimensions=img.shape[1],img.shape[0] #dimensons of the resulting image
    return cv.warpAffine(img,transMat,dimensions)

translated_img=translation(image,100,100)
cv.imshow('output1',translated_img)
translated_img=translation(translated_img,-100,-100)
cv.imshow('output2',translated_img)
#why dont i get the image in the centre


#rotating
def rotation(img,angle,rotPoint=None):
    if rotPoint==None :
        rotPoint=image.shape[1]//2,image.shape[0]//2
    dimensions=img.shape[1],img.shape[0]
    rotMat=cv.getRotationMatrix2D(rotPoint,angle,1) #getRotationMatrix2d function returns a affine transformaton matrix
    return cv.warpAffine(image,rotMat,dimensions)

rotated_img=rotation(image,-45)
cv.imshow('output3',rotated_img)

flipped_img=cv.flip(rotated_img,-1)
cv.imshow('FLIP',flipped_img)

cv.waitKey(0)
