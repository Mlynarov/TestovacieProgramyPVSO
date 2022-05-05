import cv2
import numpy as np

#image = cv2.imread("red.png")
image = cv2.imread("colors.jpg")

x,y,z = image[5][5]
meaning=image.mean()
# if image type is b g r, then b g r value will be displayed.
# if image is gray then color intensity will be displayed.
print(x,y,z)
print(meaning)

color_hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
print('Farbaaaa',color_hsv)



img = cv2.imread('jp.png')
 
# get dimensions of image
dimensions = img.shape
 
# height, width, number of channels in image
height = img.shape[0]/2
width = img.shape[1]/2
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions)
print('Image Height       : ',height)
print('Image Width        : ',width)
print('Number of Channels : ',channels)


img = cv2.imread('jp.png')
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(gray,100,255,cv2.THRESH_BINARY)
contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.drawContours(img,contours,-1,(0,0,255),19)

for i in range(0,len(contours)):
    M = cv2.moments(contours[i])
    cx = int(M['m10']/M['m00'])
    cy = int(M['m01']/M['m00'])
    print("Centroid = ", cx, ", ", cy)

    center_px =  img[cx,cy]
    print(center_px)