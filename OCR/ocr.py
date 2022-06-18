import cv2
import numpy as np
import pytesseract
from pytesseract import Output


pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img=cv2.imread('opencv_csi\images\TEXT.PNG')
#Step1: Binarising
grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

blur = cv2.GaussianBlur(grey_img,(5,5),0)
x,frame=cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

#Step2: Classification
text=pytesseract.image_to_string(frame,lang="eng")
print(text)
data=pytesseract.image_to_data(frame,output_type=Output.DICT)
n=len(data['text'])
print(len(data['text']))

for i in range(n):
    if int(float(data['conf'][i]))>40:
        #Drawing a box around the reconized word
        x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(img,data['text'][i],(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(255,0,0),1)
        cv2.imshow('FRAME',img)
        cv2.waitKey(500)
        
cv2.waitKey(0)