import cv2 as cv 
import numpy as np

img = cv.imread('D:\\Tomas\\ING\\Pocitacove_videnie_spracovanie_obrazu\\proj\\auto_result.png', 0) 
_, th1 = cv.threshold (img, 130, 255, cv.THRESH_BINARY) 
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2)
cv.imshow ("Image", img) 
cv.imshow ("th1", th1) 
cv.imshow("th2", th2)
cv.imshow ("th3", th3)

img = cv.imread('D:\\Tomas\\ING\\Pocitacove_videnie_spracovanie_obrazu\\proj\\auto_result.png')
img = cv.GaussianBlur(img,(5,5),0)
        # Convert to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        # Convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
        # HSV Thresholding
res,hsvThresh = cv.threshold(hsv[:,:,0], 25, 250, cv.THRESH_BINARY_INV)
        # Show adaptively thresholded image
adaptiveThresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115, 1)
        # Show both thresholded images
        # cv2.imshow("HSV Thresholded",hsvThresh)

cv.imshow("Adaptive Thresholding", adaptiveThresh)

cv.waitKey (0) 
cv.destroyAllWindows()