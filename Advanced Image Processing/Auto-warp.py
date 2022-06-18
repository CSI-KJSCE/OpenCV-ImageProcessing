#  This are some advance Functions for future study
#Question2
#Automatic warping image using countours
#Here U get the auto warp by single click  on the image to make it functional

import cv2
import numpy as np

my_img=cv2.imread('opencv_csi/images/bill.PNG')
img=my_img.copy()
ROI=[]
def Region_of_interest():
    global img
    grey_img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    filter_img=cv2.bilateralFilter(grey_img,9,75,75)#Preserving edges
    #Using Gaussian Adaptive Thresholding
    thres=cv2.adaptiveThreshold(filter_img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,2)

    blur=cv2.medianBlur(thres,11)
    #Used canny for edge detection
    canny=cv2.Canny(blur,200,255)

    contours,hierarchy=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    #Find the maximum contour area
    areas=[cv2.contourArea(c) for c in contours]
    max_index=np.argmax(areas)
    max_contour_area=contours[max_index]

    #Get the Region of interest by use of approxPolyDP
    perimeter=cv2.arcLength(max_contour_area,True)
    ROI=cv2.approxPolyDP(max_contour_area,0.01*perimeter,True)

    return ROI

def Comapre_edges(ROI):#Check if the array size is 4 for four corners of the pages
    
    if len(ROI)==4 and cv2.isContourConvex(ROI):

        maxArea=cv2.contourArea(ROI)
        required_page=ROI

        return required_page

def get_four_points(points):# Get the 4 corners of the page
    
    #The logic for points is as follow:
    #Top-left:The sum (x+y)is least
    #Top-Right:The diff (y-x) is minimum
    #Bottom_left:the diff y-x is max
    #Bottom-right:(x+y) is max

    diff=np.diff(points,axis=1)
    point_sum=points.sum(axis=1)
    req_points=np.array([points[np.argmin(point_sum)],points[np.argmin(diff)],points[np.argmax(diff)],points[np.argmax(point_sum)]])

    return req_points

def click_(event,x,y,flags,param):
    global ROI
    global my_img

    if event==cv2.EVENT_LBUTTONDOWN:#On button click
        required_page=Comapre_edges(ROI)
        arr=get_four_points(required_page[:,0])

        pts1=np.array([(arr[0][0],arr[0][1]),(arr[1][0],arr[1][1]),(arr[2][0],arr[2][1]),(arr[3][0],arr[3][1])],np.float32)
        pts2=np.array([(0,0),(500,0),(0,600),(500,600)],np.float32)

        perspective=cv2.getPerspectiveTransform(pts1,pts2)
        trans=cv2.warpPerspective(my_img,perspective,(500,600))

        cv2.imshow('Wrap',trans)
        cv2.waitKey(0)
        

ROI=Region_of_interest()
cv2.drawContours(img,[ROI],-1,(0,255,0),2)#The image is shown with contours drawn on it

cv2.namedWindow('Frame')
cv2.setMouseCallback('Frame',click_)

cv2.imshow('Frame',img)
cv2.waitKey(0)