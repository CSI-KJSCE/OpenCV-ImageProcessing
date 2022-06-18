#Debugging the code
import cv2
import numpy as np

cap=cv2.VideoCapture(0)

def mouse(event,x,y,flags,param):
	if event==cv2.EVENT_LBUTTONDOWN:
		print(x,y) #This gives x and y coordinate
		print(frame[x,y]) #This gives BGR values

cv2.namedWindow('img')
cv2.setMouseCallback('img',mouse)

while True:
	x,frame=cap.read()
	cv2.imshow('img',frame)
	if cv2.waitKey(1)&0xFF==ord('q'):
		break