import cv2
import numpy as np

img = cv2.imread('bookpage.jpg')
img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,global_thresh = cv2.threshold(img_gray,10,255,cv2.THRESH_BINARY)
mean_thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,25,2)
gaussian_thresh = cv2.adaptiveThreshold(img_gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,2)

cv2.imshow('OG',img)
cv2.imshow('Global Thresh',global_thresh)
cv2.imshow('Mean Thresh',mean_thresh)
cv2.imshow('Gaussian Thresh',gaussian_thresh)
cv2.waitKey(0)
