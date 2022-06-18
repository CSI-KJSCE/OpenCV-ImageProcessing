import cv2
import random
import time

# print(time.time())
start_time = time.time()

img = cv2.imread('opencv_csi/images/flower.jpg')

cv2.line(img,(0,0),(700,700),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),4)
cv2.circle(img,(500,500),50,(random.randint(0,255),random.randint(0,255),random.randint(0,255)),-1)
cv2.rectangle(img,(200,200),(500,500),(random.randint(0,255),random.randint(0,255),random.randint(0,255)),4)
# img[0:200,0:200] = [255,255,255]         Image Slicing and changing pixel values

cv2.putText(img,'Open CV',(100,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

cv2.imshow('Frame',img)
end_time = time.time()

diff = end_time - start_time
print("Time Difference",diff)

cv2.imwrite('First_img.jpg',img)      # Saving image
print("Image Shape :",img.shape)
cv2.waitKey(0)

