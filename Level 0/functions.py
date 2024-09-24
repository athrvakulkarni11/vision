import cv2 as cv


#images\kitty.jpeg this path was giving error.Had to add \\ to remove the error

img=cv.imread("images\\kitty.jpeg") #basic function 1 cv.cvtColor()
img=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('output1',img)

img2=cv.cvtColor(img,cv.COLOR_BGR2BGRA) #alpha channels
#This is invalid ---> img2=cv.imread(img,-1)
print(img2.shape)

blurred_img=cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)# basic function 2 cv.GaussianBlur()
cv.imshow('output3',blurred_img)

edges=cv.Canny(img,100,200) #basic function 3 cv.Canny()
cv.imshow('Edges',edges)

dilated_img=cv.dilate(edges,(5,3),iterations=2)
cv.imshow('dilated',dilated_img)

eroded_img=cv.erode(dilated_img,(5,3),iterations=2)
cv.imshow('Eroded',eroded_img)

cv.waitKey(0)




