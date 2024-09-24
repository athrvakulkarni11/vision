#!/usr/bin/env python3m

import numpy as np
import cv2 as cv


# Termination criteria for refining the corners
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points like (0,0,0), (1,0,0), ..., (13,12,0)
objp = np.zeros((12*13, 3), np.float32)
objp[:, :2] = np.mgrid[0:13, 0:12].T.reshape(-1, 2)

# Arrays to store object points and image points from all images
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

cap=cv.VideoCapture(1)

while True:

    ret,img=cap.read()
    if not ret:
       break
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find chessboard corners
    ret, corners = cv.findChessboardCorners(gray, (13,12))
    print(corners)

    # If found, add object points and image points after refining
    if ret:
        objpoints.append(objp)

        # Refine corner locations
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)

        # Optional: Draw and display corners for debugging
        cv.drawChessboardCorners(img, (13, 12), corners2, ret)
        cv.imshow('img', img)
        if cv.waitKey(1)==ord('q'):
         break

    # Check the number of images successfully processed
    print(f"Number of valid images processed: {len(objpoints)}")

cap.release()
cv.destroyAllWindows()
   
# Camera calibrationq
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
if not ret:
    print("Calibration failed")
      
# Print camera matrix and distortion coefficients
print("Camera matrix:\n", mtx)
print("Distortion coefficients:\n", dist)

    
