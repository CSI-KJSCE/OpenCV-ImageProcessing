import cv2
import numpy as np

img = cv2.imread('opencv_csi/images/flower.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

kernel = np.ones((25,25))/625
blur = cv2.filter2D(img_gray,-1,kernel)

gaussian_kernel = np.array([1,2,1,
                            2,4,2,
                            1,2,1  ])/16

gaussian_blur = cv2.filter2D(img_gray,-1,gaussian_kernel)
gaussian_blur = cv2.GaussianBlur(img_gray,(25,25),2)

sharpening_kernel = np.array([-1,-1,-1,
                              -1,9,-1,
                              -1,-1,-1 ])

sharpened = cv2.filter2D(img_gray,-1,sharpening_kernel)


cv2.imshow('OG',img_gray)
cv2.imshow('Blur',blur)
cv2.imshow('Gaussian',gaussian_blur)
cv2.imshow('Sharpened',sharpened)
cv2.waitKey(0)
