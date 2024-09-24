import cv2
img=cv2.imread("C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/image.jpg",1)
cv2.imshow('original',img)
cv2.waitKey(0)
def rescale(img,scale=0.5):
    width=int(img.shape[1]*scale)
    height=int(img.shape[0]*scale)
    dimentions=(width,height)
    return cv2.resize(img,dimentions,interpolation=cv2.INTER_AREA)
resizedimg=rescale(img)
cv2.imshow('rescaled',resizedimg)
cv2.waitKey(0)
ymin,ymax,xmin,xmax=250,800,250,800
cropedimg=img[ymin:ymax , xmin:xmax]
cv2.imshow('croped',cropedimg)
cv2.waitKey(0)
rotatedimg=cv2.rotate(img,cv2.ROTATE_90_CLOCKWISE)
cv2.imshow('rotated',rotatedimg)
cv2.waitKey(0)
cv2.destroyAllWindows()
