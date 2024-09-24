import cv2 as cv

cap=cv.VideoCapture("captain levi.mp4")

def rescaling(frame,scale=0.5): # default parameters
   height=int(frame.shape[0]*scale)
   width=int(frame.shape[1]*scale)
   dimensions=(width,height)
   resized_frame = cv.resize(frame,dimensions, interpolation=cv.INTER_AREA)
   return resized_frame


while True:
  ret,frame=cap.read()
  cv.imshow('output 1',frame)
  resized=rescaling(frame)
  cv.imshow('output 2',resized)

  if(cv.waitKey(30)==ord('q')):
    break

cap.release()
cv.destroyAllWindows()

