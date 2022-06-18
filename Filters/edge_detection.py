import cv2
import numpy as np

img = cv2.imread('opencv_csi/images/flower.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

soblelx_kernel = np.array([  -1,-2,-1,
                              0,0,0,
                              1,2,1 ])

soblely_kernel = np.array([  -1,0,1,
                              -2,0,2,
                              -1,0,1 ])
    
soblelx = cv2.filter2D(img_gray,-1,soblelx_kernel)
soblely = cv2.filter2D(img_gray,-1,soblely_kernel)

canny = cv2.Canny(img_gray,12,50)        # The 2nd and 3rd params is MinVal & MaxVal

cv2.imshow('Soble X',soblelx)
cv2.imshow('Soble Y',soblely)
cv2.imshow('Canny',canny)
cv2.imshow('OG',img_gray)

cv2.waitKey(0)