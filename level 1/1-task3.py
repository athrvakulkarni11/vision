import cv2 as cv
import numpy as np

# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.00001)

# prepare object points
objp = np.zeros((10*15, 3), np.float32)
objp[:, :2] = np.mgrid[0:15, 0:10].T.reshape(-1, 2)

# Arrays to store object points and image points from all the images.
objpoints = []
imgpoints = []

# List of image files
image_files = ["C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/d1.jpg",
               "C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/d3.jpg",
               "C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/d4.jpg"
              ]

for image_file in image_files:
    img = cv.imread(image_file)
    cv.imshow("original img", img)
    cv.waitKey(0)

    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (10, 15))

    # If found, add object points, image points
    if ret == True:
        objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
        imgpoints.append(corners2)
        draw=cv.drawChessboardCorners(img.copy(), (10, 15), corners2, ret)
        cv.imshow("img", draw)
        cv.waitKey(0)
        cv.destroyAllWindows()
# calibration
ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

# undisort
w, h = img.shape[:2]
newcameramtx, roi = cv.getOptimalNewCameraMatrix(mtx, dist, (w, h), 1, (w, h))
# dst = cv.undistort(img, mtx, dist, None, newcameramtx)

# #crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
# cv.imshow("result", dst)
# cv.waitKey(0)


mapx, mapy = cv.initUndistortRectifyMap(mtx, dist, None,mtx, (w,h), 5)
dst = cv.remap(img, mapx, mapy, cv.INTER_LINEAR)
 
# crop the image
# x, y, w, h = roi
# dst = dst[y:y+h, x:x+w]
cv.imshow("result", dst)
cv.waitKey(0)