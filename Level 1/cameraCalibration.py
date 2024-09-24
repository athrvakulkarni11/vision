#!/usr/bin/env python3m

import numpy as np
import cv2 as cv
import glob
import os

# Termination criteria for refining the corners
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# Prepare object points like (0,0,0), (1,0,0), ..., (13,12,0)
objp = np.zeros((12*13, 3), np.float32)
objp[:, :2] = np.mgrid[0:13, 0:12].T.reshape(-1, 2)

# Arrays to store object points and image points from all images
objpoints = []  # 3D points in real world space
imgpoints = []  # 2D points in image plane

# Path to the images directory (change this to match your images' extension)
images_path = '/home/livininamatrix/Sneha/CVop/chessboard/*.jpeg'  # Use *.jpg if your images are in jpg format

# Print the images path to verify
print(f"Looking for images in: {images_path}")

# Load images
images = glob.glob(images_path)

# Check if images are found
if not images:
    print(f"No images found in {images_path}")
    exit()

# Process each image
for fname in images:
    img = cv.imread(fname)
    if img is None:
        print(f"Failed to load image: {fname}")
        continue

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
        cv.waitKey(500)  # Display each image for 500ms

# Clean up windows if used for display
cv.destroyAllWindows()

# Check the number of images successfully processed
print(f"Number of valid images processed: {len(objpoints)}")
if len(objpoints) == 0 or len(imgpoints) == 0:
    print("No valid chessboard corners found in any image.")
    exit()

# Camera calibration
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)
if not ret:
    print("Calibration failed")
    exit()

# Print camera matrix and distortion coefficients
print("Camera matrix:\n", mtx)
print("Distortion coefficients:\n", dist)

# Load an image for undistortion
sample_img_path = os.path.join('/home/livininamatrix/Sneha/CVop/chessboard', 'sample.jpeg')
img = cv.imread(sample_img_path)
if img is None:
    print(f"Error loading image '{sample_img_path}'")
    exit()
h, w = img.shape[:2]

# Get new camera matrix to minimize distortion
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))

# Undistort the image using cv.undistort
dst = cv.undistort(img, mtx, dist, None, newcameramtx)

# Crop the image using roi if it's valid
if roi is not None:
    x, y, w, h = roi
    dst = dst[y:y+h, x:x+w]
cv.imwrite('calibresult_undistort.png', dst)

# Alternative undistortion using cv.remap
mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w, h), 5)
dst_remap = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)

# Crop using roi if it's valid
if roi is not None:
    x, y, w, h = roi
    dst_remap = dst_remap[y:y+h, x:x+w]
cv.imwrite('calibresult_remap.png', dst_remap)

# Calculate reprojection error
mean_error = 0
for i in range(len(objpoints)):
    imgpoints2, _ = cv.projectPoints(objpoints[i], rvecs[i], tvecs[i], mtx, dist)
    error = cv.norm(imgpoints[i], imgpoints2, cv.NORM_L2) / len(imgpoints2)
    mean_error += error

print(f"Total reprojection error: {mean_error / len(objpoints):.4f}")
