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

# img = cv2.imread('Flower2.jpg')
# img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# # kernel = np.ones((25,25))/625
# # blur = cv2.filter2D(img_gray,-1,kernel)

# # gaussian_kernel = np.array([1,2,1,
# #                             2,4,2,
# #                             1,2,1  ])/16

# # gaussian_blur = cv2.filter2D(img_gray,-1,gaussian_kernel)
# # gaussian_blur = cv2.GaussianBlur(img_gray,(25,25),2)

# # sharpening_kernel = np.array([-1,-1,-1,
# #                               -1,9,-1,
# #                               -1,-1,-1 ])

# # sharpened = cv2.filter2D(img_gray,-1,sharpening_kernel)


# # cv2.imshow('OG',img_gray)
# # cv2.imshow('Blur',blur)
# # cv2.imshow('Gaussian',gaussian_blur)
# # cv2.imshow('Sharpened',sharpened)
# # cv2.waitKey(0)

# soblelx_kernel = np.array([  -1,-2,-1,
#                               0,0,0,
#                               1,2,1 ])

# soblely_kernel = np.array([  -1,0,1,
#                               -2,0,2,
#                               -1,0,1 ])
    
# soblelx = cv2.filter2D(img_gray,-1,soblelx_kernel)
# soblely = cv2.filter2D(img_gray,-1,soblely_kernel)

# canny = cv2.Canny(img_gray,12,50)

# cv2.imshow('Soble X',soblelx)
# cv2.imshow('Soble Y',soblely)
# cv2.imshow('Canny',canny)
# cv2.imshow('OG',img_gray)

# cv2.waitKey(0)
