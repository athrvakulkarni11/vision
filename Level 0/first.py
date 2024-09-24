import cv2 as cv

img = cv.imread('11.webp', 0)
cv.imwrite('new_img.jpg', img)
cv.imshow('Image1', img)
img=cv.resize(img,(500,500),fx=1,fy=1,interpolation=cv.INTER_AREA)
cv.imshow('Image2', img)
cv.waitKey(0)
cv.destroyAllWindows()