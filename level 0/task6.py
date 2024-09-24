import cv2 as cv
img=cv.imread("C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/resizimg.jpg")
cv.imshow("original",img)
cv.waitKey(0)

gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("gray",gray)
cv.waitKey(0)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)
cv.imshow("hsv",hsv)
cv.waitKey(0)

lab=cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow("LAB",lab)
cv.waitKey(0)

rgb=cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow("RBG",rgb)
cv.waitKey(0)