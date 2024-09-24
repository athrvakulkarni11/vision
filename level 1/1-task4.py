import cv2 as cv

image_files = cv.imread(["C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/pano1.jpg",
               "C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/pano2.jpg",
               "C:/Users/Moksha's Lappy/Desktop/code/VRC_tasks/pano3.jpg"
              ])

# images = []
# for image_file in image_files:
#     img = cv.imread(image_file)
#     if img is None:
#         continue
#     images.append(img)

stitcher = cv.Stitcher_create()
ret, result = stitcher.stitch(images)

if ret == cv.Stitcher_OK:
    print("done")
    cv.imshow("panorama", result)
    cv.waitKey(0)
else:
    print("failed")
    
    