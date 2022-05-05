import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display, clear_output





# Automatic brightness and contrast optimization with optional histogram clipping
def automatic_brightness_and_contrast(cv2image):

    maxPercent=100.0
    hist_percent=15
    minGrayScale = 0

    grayFrame = cv2.cvtColor(cv2image, cv2.COLOR_BGR2GRAY)

    # Calculate grayscale histogram
    oldHistogram = cv2.calcHist([grayFrame],[0],None,[256],[0,256])
    histogramActualSize = len(oldHistogram)

    # Calculate cumulative distribution from the histogram
    accumulator = []
    accumulator.append(float(oldHistogram[0]))
    for index in range(1, histogramActualSize):
        accumulator.append(accumulator[index -1] + float(oldHistogram[index]))

    # Locate points to clip
    maxAcc = accumulator[-1]
    hist_percent *= (maxAcc/maxPercent)
    hist_percent /= 2.0

    while accumulator[minGrayScale] < hist_percent:
        minGrayScale += 1

    maxGrayScale = histogramActualSize -1
    while accumulator[maxGrayScale] >= (maxAcc - hist_percent):
        maxGrayScale -= 1

    # Calculate alpha and beta values
    gamma = 255 / (maxGrayScale - minGrayScale)
    delta = -minGrayScale * gamma

    #auto_result = convertScale(cv2image, alpha, beta)

    cv2image = cv2image * gamma + delta
    cv2image[cv2image < 0] = 0
    cv2image[cv2image > 255] = 255
    cv2image= cv2image.astype(np.uint8)

    plotGraph(oldHistogram,grayFrame,minGrayScale,maxGrayScale)
    return (cv2image)

def plotGraph(hist,grayFrame,min_gray,max_gray) -> None:

    newHistogram = cv2.calcHist([grayFrame],[0],None,[256],[min_gray,max_gray])
    ax.set_xlim(0, 255)    
    ax.cla()
    ax.plot(hist)
    ax.plot(newHistogram)
    ax.legend(['OldHistogram', 'NewHistorgram'])
    display(fig);   ## toto vypisuje tu hlasku do autputu neviem preco neviem to vypnut vedel som to len pozastavit ; aby to nevypisovalo pocas behu
    clear_output(wait = True)
    plt.pause(0.1)



cap = cv2.VideoCapture(0)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)


while(True):
    # Capture frame-by-frame
    ret, cv2image = cap.read() 

    

    
    auto_result = automatic_brightness_and_contrast(cv2image)
    


    cv2.imshow('frame',cv2image)
    cv2.imshow('AutoResult',auto_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()