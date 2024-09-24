import cv2 as cv
import numpy as np

blank=np.zeros((500,500,3),dtype='uint8')

rect=cv.rectangle(blank.copy(),(40,40),(480,480),(255,255,255),-1)
circa=cv.circle(blank.copy(),(250,250),200,(255,255,255),-1)

aNd=cv.bitwise_and(rect,circa)
cv.imshow('AND',aNd)

oR=cv.bitwise_or(rect,circa)
cv.imshow('OR',oR)

xoR=cv.bitwise_xor(rect,circa)
cv.imshow('XOR',xoR)

noT=cv.bitwise_not(circa)
cv.imshow('NOT',noT)

noT1=cv.bitwise_not(rect)
cv.imshow('NOTT',noT1)

cv.waitKey(0)


