import cv2
import numpy as np

print(cv2.__version__)


vid = cv2.VideoCapture(0)
  
while(True):
      
    _, frame = vid.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    edges = cv2.Canny(frame,100,100)
  
    #filters
    lower_red = np.array([150,150,90])
    upper_red = np.array([180,255,150])

    mask = cv2.inRange(hsv,lower_red,upper_red)
    res =cv2.bitwise_and(frame,frame, mask=mask)

    # median filter - zbavuje sa sumu a vyhladzuje prednaska 4.
    median = cv2.medianBlur(frame,7)

    edgesmed = cv2.Canny(median,100,100)

    # Display the resulting frame
    cv2.imshow('The_Input_Frame',frame)
    cv2.imshow('edges', edges)
    cv2.imshow('edgesMED', edgesmed)
    cv2.imshow('Mask', mask)
    cv2.imshow('Res', res)
    cv2.imshow('Median', median)
      

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  

vid.release()
cv2.destroyAllWindows()
