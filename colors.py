import cv2
import numpy as np

print(cv2.__version__)


vid = cv2.VideoCapture(0)

color =3
  
while(True):
      
    _, frame = vid.read()
    hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)





    edges = cv2.Canny(frame,100,100)
  

    #filters
    lower_red = np.array([150,150,90])
    upper_red = np.array([180,255,150])
    maskRED = cv2.inRange(hsv,lower_red,upper_red)

    light_blue = np.array([110,50,50])
    dark_blue = np.array([130,255,255])
    maskBLUE = cv2.inRange(hsv,light_blue,dark_blue)

    light_green = np.array([36,0,0])
    dark_green = np.array([70,255,255])
    maskGREEN = cv2.inRange(hsv,light_green,dark_green)



    res =cv2.bitwise_and(frame,frame, mask=maskRED)


    if maskRED is not None:
            print ("found red", flush=True)
#           print circlesred
    if maskGREEN is not None:
            print ("found green", flush=True)
#           print circlesgreen
    if maskBLUE is not None:
            print ("found blue", flush=True)
#           print circle
    else:
            print ("no ball", flush=True) 

    # Display the resulting frame
    cv2.imshow('The_Input_Frame',frame)
    #cv2.imshow('edges', edges)
    cv2.imshow('RED', maskRED)
    cv2.imshow('GREEN', maskGREEN)
    cv2.imshow('BLUE', maskBLUE)
    #cv2.imshow('Res', res)
      

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
  

vid.release()
cv2.destroyAllWindows()



