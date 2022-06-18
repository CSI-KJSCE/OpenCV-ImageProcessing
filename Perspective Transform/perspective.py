import cv2
import numpy as np

img = cv2.imread('opencv_csi\images\perspective.png')

print(img.shape)
pts_1 = np.array([(134, 237), (389, 137), (304, 612), (520, 487)],np.float32)

pts_2 = np.array([(0, 0), (500, 0), (0, 400), (500, 400)],np.float32)

perspective = cv2.getPerspectiveTransform(pts_1,pts_2)
transformed = cv2.warpPerspective(img, perspective, (500,400))     

for val in pts_1:
    cv2.circle(img,(val[0],val[1]),5,(0,255,0),-1)

cv2.imshow("image",img)

cv2.imshow('img',transformed)

cv2.waitKey(0)

# cap = cv2.VideoCapture(0)

# def mouse(event,x,y,flags,param):
    
#     if event == cv2.EVENT_LBUTTONDOWN:
#         print(frame[x,y])

# cv2.namedWindow('img')
# cv2.setMouseCallback('img',mouse)

# while True:
#     x,frame = cap.read()
#     cv2.imshow('img',frame)

#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break