import cv2
import numpy as np

print(cv2.__version__)


vid = cv2.VideoCapture(0)
  
while(True):
      
    _, frame = vid.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    edges = cv2.Canny(frame,100,100)

    median3 = cv2.medianBlur(frame,3)
    edges3 = cv2.Canny(median3,100,100)

    median5 = cv2.medianBlur(frame,5)
    edges5 = cv2.Canny(median5,100,100)

    median7 = cv2.medianBlur(frame,7)
    edges7 = cv2.Canny(median7,100,100)
  


    

    # Display the resulting frame
    cv2.imshow('The_Input_Frame',frame)
    cv2.imshow('edgesNOMED', edges)
    cv2.imshow('edgesMED3', edges3)
    cv2.imshow('edgesMED5', edges5)
    cv2.imshow('edgesMED7', edges7)

      

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  

vid.release()
cv2.destroyAllWindows()
