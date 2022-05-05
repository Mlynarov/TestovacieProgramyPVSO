# main.py
import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision
from hsvfilter import HsvFilter


# initialize the WindowCapture class
wincap = WindowCapture('Albion Online Client')
# initialize the Vision class
vision_limestone = Vision('albion_limestone_processed.jpg')
# initialize the trackbar window
vision_limestone.init_control_gui()

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    # permanent HSV filter
    hsv_filter = HsvFilter(0, 103, 207, 21, 151, 255, 54, 0, 133, 0)
    # pre-process the image
    processed_image = vision_limestone.apply_hsv_filter(screenshot, hsv_filter)

    # do object detection
    rectangles = vision_limestone.find(processed_image, 0.46)

    # draw the detection results onto the original image
    detection_image = vision_limestone.draw_rectangles(screenshot, rectangles)

    # display the processed image
    cv.imshow('Processed', processed_image)
    cv.imshow('Matches', detection_image)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # waits 1 ms every loop to process key presses
    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break

print('Done.')