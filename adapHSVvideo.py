import cv2
import numpy as np

cap = cv2.VideoCapture(0)


foundred = False

while(True):
    success,img = cap.read()  
    img = cv2.GaussianBlur(img,(5,5),0)
            # Convert to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
            # Convert to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
            # HSV Thresholding
    res,hsvThresh = cv2.threshold(hsv[:,:,0], 25, 250, cv2.THRESH_BINARY_INV)
            # Show adaptively thresholded image
    adaptiveThresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

    cv2.imshow('Median', adaptiveThresh)


    if cv2.waitKey(1) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()