import cv2
import numpy as np

img = cv2.imread('opencv_csi\images\perspective.png')


def mouse(event,x,y,flags,param):
    
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)

cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse)


cv2.imshow('img',img)

cv2.waitKey(0)