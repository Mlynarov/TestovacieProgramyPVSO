import numpy as np
import cv2

cap = cv2.VideoCapture(0)

SharpenFilter = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])




while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    contrast = 1.05
    brightness = 20
    

    

    frame[:,:,2] = np.clip(contrast * frame[:,:,2] + brightness, 0, 230)

    frame = cv2.filter2D(src=frame, ddepth=-2, kernel=SharpenFilter)
    

    #frame = cv2.medianBlur(frame,3)

    #frame = cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()