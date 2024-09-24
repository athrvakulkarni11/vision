import cv2

cap=cv2.VideoCapture("C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/video.mp4")
while(True):
    istrue,frames=cap.read()
    cv2.imshow("video",frames)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
    
cap=cv2.VideoCapture(0)
while(True):
    istrue,frames=cap.read()
    cv2.imshow("video",frames)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
    
cap=cv2.VideoCapture(1)
while(True):
    istrue,frames=cap.read()
    cv2.imshow("video",frames)
    if cv2.waitKey(20) & 0xFF==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
