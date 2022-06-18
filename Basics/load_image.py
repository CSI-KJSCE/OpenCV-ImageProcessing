import cv2

img = cv2.imread("opencv_csi/images/flower.jpg")   # Load the image
# print(img)

cv2.imshow('Frame',img)
cv2.waitKey(0)