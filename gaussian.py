import math
import cv2
import numpy as np
def gausskernel(size,k,sigma):
    gausskernel = np.zeros((size,size),np.float32)
    for i in range (size):
        for j in range (size):
            norm = math.pow(i-k,2) + pow(j-k,2)
            gausskernel[i,j] = math.exp(-norm/(2*math.pow(sigma,2)))/2*math.pi*pow(sigma,2)
    sum = np.sum(gausskernel)
    kernel = gausskernel/sum 
    return kernel

def mygaussFilter(img_gray,kernel):
    h,w = img_gray.shape
    k_h,k_w = kernel.shape
    for i in range(int(k_h/2),h-int(k_h/2)):
        for j in range(int(k_h/2),w-int(k_h/2)):
            sum = 0
            for k in range(0,k_h):
                for l in range(0,k_h):
                    sum += img_gray[i-int(k_h/2)+k,j-int(k_h/2)+l]*kernel[k,l]
            img_gray[i,j] = sum
    return img_gray

if __name__ == '__main__':
    img = cv2.imread("D:\\Tomas\\ING\\Pocitacove_videnie_spracovanie_obrazu\\proj\\ZadaniePVSO2\\field.png")
    img_gray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    img_g = img_gray.copy()
    k=1
    size = 2*k+1
    kernel = gausskernel(size,k,1.5)
    print(kernel)
    img_B,img_G,img_R = cv2.split(img)
    img_gauss_B = mygaussFilter(img_B,kernel)
    img_gauss_G = mygaussFilter(img_G,kernel)
    img_gauss_R = mygaussFilter(img_R,kernel)
    img_gauss = cv2.merge([img_gauss_B,img_gauss_G,img_gauss_R])

    img_comp = np.hstack((img,img_gauss))
    cv2.imshow("gauss",img_comp)
    cv2.waitKey(0)