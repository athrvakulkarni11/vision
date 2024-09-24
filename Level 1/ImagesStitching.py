#!/usr/bin/env python3
import numpy as np
import cv2
import glob
import os  # Import os to use absolute paths if needed
import imutils

# Path to the images directory (change this to match your images' extension)
images_path = 'skyline/*.jpeg'  # Use *.jpg if your images are in jpg format

# Print the images path to verify
print(f"Looking for images in: {images_path}")

# Load images
image_files = glob.glob(images_path)
print(f"Found {len(image_files)} images: {image_files}")  # Check how many images are found

images = []

# Check if images are loaded properly
for image_file in image_files:
    if not os.path.isabs(image_file):
        image_file = os.path.abspath(image_file)  # Use absolute path if necessary
    print(f"Loading image: {image_file}")
    img = cv2.imread(image_file)
    if img is None:
        print(f"Failed to load image: {image_file}")
    else:
        images.append(img)
        cv2.imshow("Image", img)
        cv2.waitKey(500)  # Display each image for 500ms

# Close all windows
cv2.destroyAllWindows()

# Check if we have images to stitch
if len(images) == 0:
    print("No images to stitch. Exiting.")
else:
    # Create image stitcher
    imageStitcher = cv2.Stitcher_create()

    # Perform stitching
    error, stitched_img = imageStitcher.stitch(images)

    # Check if stitching was successful
    if error == cv2.Stitcher_OK:
        # Save and display the stitched image
        cv2.imwrite("stitchedOutput.png", stitched_img)
        cv2.imshow("Stitched Image", stitched_img)
        cv2.waitKey(0)

        # Add a border to the stitched image
        stitched_img = cv2.copyMakeBorder(stitched_img, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=(0, 0, 0))

        # Convert to grayscale and threshold to find the region of interest
        gray = cv2.cvtColor(stitched_img, cv2.COLOR_BGR2GRAY)
        thresh_img = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY)[1]

        cv2.imshow("Threshold Image", thresh_img)
        cv2.waitKey(0)

        # Find contours
        contours = cv2.findContours(thresh_img.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)

        # Find the largest contour
        areaOI = max(contours, key=cv2.contourArea)

        # Create a mask and find bounding rectangle
        mask = np.zeros(thresh_img.shape, dtype="uint8")
        x, y, w, h = cv2.boundingRect(areaOI)
        cv2.rectangle(mask, (x, y), (x + w, y + h), 255, -1)

        minRectangle = mask.copy()
        sub = mask.copy()

        # Erode until all non-zero pixels are gone
        while cv2.countNonZero(sub) > 0:
            minRectangle = cv2.erode(minRectangle, None)
            sub = cv2.subtract(minRectangle, thresh_img)

        # Find contours of the eroded rectangle
        contours = cv2.findContours(minRectangle.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        contours = imutils.grab_contours(contours)
        areaOI = max(contours, key=cv2.contourArea)

        # Display the minimal rectangle image
        cv2.imshow("Min Rectangle Image", minRectangle)
        cv2.waitKey(0)

        # Get bounding rectangle of the largest contour
        x, y, w, h = cv2.boundingRect(areaOI)

        # Crop the stitched image to the bounding rectangle
        stitched_img = stitched_img[y:y + h, x:x + w]

        # Save and display the processed stitched image
        cv2.imwrite("stitchedOutputProcessed.png", stitched_img)
        cv2.imshow("Stitched Image Processed", stitched_img)
        cv2.waitKey(0)

        # Close all windows
        cv2.destroyAllWindows()
    else:
        print("Images could not be stitched!")
        print("Likely not enough keypoints being detected!")
