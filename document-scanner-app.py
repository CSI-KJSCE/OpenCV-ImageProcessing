#!/usr/bin/env python3

from tkinter import *
import tkinter as tk
import tkinter.messagebox
import tkinter.font as font
import cv2
from tkinter import filedialog,Text
from PIL import ImageTk, Image, ImageDraw
import os.path
import numpy as np
import pytesseract
from pytesseract import Output


option=['Mean blur','Gaussian Blur','Bilateral Filter','Median']
filter_option=['Canny','sobel-x','sobel-y','Sharpening']

filename=""
array=[]
arr=[]
i=0

img=np.array([0],np.uint8)
display = np.array ([0], dtype = np.uint8)


def select_pic():

    print('Selected')
    global filename,img
    filename = filedialog.askopenfilename(initialdir = '.',title = 'Select an Image',filetypes = (('PNG','*.png'),('All files','*.*')))

    if os.path.exists(filename):
        img = cv2.imread(filename)
        if not img is None and len(img) > 0:
            cv2.imshow("Frame", img)
            cv2.waitKey(20)
            display=img
        else:
            response=tk.messagebox.showinfo("Message","Please select image")


def grey_image():

    global img,filename
 
    if os.path.exists(filename):
        
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        cv2.imshow('Frame',grey)
        cv2.waitKey(20)
        global display
        img=grey
        display=grey
    else:
        response=tk.messagebox.showinfo("Message","Please select image")

def blur_image(*args):

    global option,filename
    global display
    select=variable.get()

    if os.path.exists(filename):
        img=cv2.imread(filename)
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        if (select==option[1]):
            blur=cv2.GaussianBlur(grey,(25,25),2)
            cv2.imshow('Frame',blur)
            cv2.waitKey(20)
            display=blur

        elif(select==option[0]):
            kernel=np.ones((25,25))/625
            blur=cv2.filter2D(grey,-1,kernel)
            cv2.imshow('Frame',blur)
            cv2.waitKey(20)
            display=blur

        elif(select==option[2]):
            blur=cv2.bilateralFilter(grey,9,75,75)
            cv2.imshow('Frame',blur)
            cv2.waitKey(20)
            display=blur

        elif(select==option[3]):
            blur=cv2.medianBlur(grey,11)
            cv2.imshow('Frame',blur)
            cv2.waitKey(20)
            display=blur

        img=blur

    else:
        response=tk.messagebox.showinfo("Message","Please select image")



def callback(*args):

    global filename,filter_option
    global display
    option=variable1.get()
    print(option)

    if os.path.exists(filename):
        img=cv2.imread(filename)
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        if option==filter_option[0]:
            canny=cv2.Canny(grey,100,200)
            cv2.imshow('Frame',canny)
            cv2.waitKey(20)
            display=canny
            

        elif option==filter_option[1]:
            sobelx_kernel=np.array([-1,-2,-1,
                                   0,0,0,
                                   1,2,1])
            sobelx=cv2.filter2D(grey,-1,sobelx_kernel)
            cv2.imshow('Frame',sobelx)
            display=sobelx
            cv2.waitKey(20)

        elif option==filter_option[2]:
            sobely_kernel=np.array([-1,0,1,
                                   -2,0,2,
                                   -1,0,1])

            sobely=cv2.filter2D(grey,-1,sobely_kernel)
            display=sobely
            cv2.imshow('Frame',sobely)
            cv2.waitKey(20)

        elif option==filter_option[3]:
            sharp_kernel=np.array([-1,-1,-1,
                                  -1,9,-1,
                                  -1,-1,-1])
            sharp=cv2.filter2D(grey,-1,sharp_kernel)
            display=sharp
            cv2.imshow('Frame',sharp)
            cv2.waitKey(20)
        
    else:
        response=tk.messagebox.showinfo("Message","Please select image")

def drag_and_crop(event, x, y, flags, param):

    global array
    global filename
    global display,img

    if event==cv2.EVENT_LBUTTONDOWN:
        array=[(x,y)]
        print(array)

    elif event==cv2.EVENT_LBUTTONUP:
        array.append((x,y))
        print(array)
        cv2.rectangle(img, array[0], array[1], (0, 255, 0), 2)
        roi=img[array[0][1]:array[1][1], array[0][0]:array[1][0]]
        display=roi
        cv2.imshow('Frame',img)
        cv2.imshow('Frame',roi)

     
def crop_image_btn():
    global array
    global img
    if os.path.exists(filename):
        cv2.namedWindow('Frame')
        cv2.setMouseCallback('Frame',drag_and_crop)
        cv2.imshow('Frame',img)
        cv2.waitKey(10000)
    else:
        response=tk.messagebox.showinfo("Message","Please select image")

def OCR_func():
    global filename
    global display
    if os.path.exists(filename):
        img=cv2.imread(filename)
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(grey,(5,5),0)
        x,frame=cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        text=pytesseract.image_to_string(frame,lang="eng")
        print(text)
        data=pytesseract.image_to_data(frame,output_type=Output.DICT)
        n=len(data['text'])
        print(len(data['text']))
        for i in range(n):
            if int(data['conf'][i])>60:
                x,y,w,h=data['left'][i],data['top'][i],data['width'][i],data['height'][i]
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,0),1)
                cv2.putText(img,data['text'][i],(x,y),cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0),1)
                cv2.imshow('Frame',img)
                cv2.waitKey(500)
    else:
        response=tk.messagebox.showinfo("Message","Please select image")
        display=img


def show_text():
    global text
    global filename
    if os.path.exists(filename):
        img=cv2.imread(filename)
        grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        blur=cv2.GaussianBlur(grey,(5,5),0)
        x,frame=cv2.threshold(blur,10,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
        ocr_text=pytesseract.image_to_string(frame,lang="eng")
        textbox = tk.Frame(text_frame,bg = 'white')
        textbox.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)
        text=Text(textbox,bg='#FDFFD6')
        text.insert('1.0',ocr_text)
        text.pack()
    else:
        response=tk.messagebox.showinfo("Message","Please select image")

    
def get_four_points(points):
    diff=np.diff(points,axis=1)
    point_sum=points.sum(axis=1)
    req_points=np.array([points[np.argmin(point_sum)],points[np.argmin(diff)],points[np.argmax(diff)],points[np.argmax(point_sum)]])
    return req_points


def warp_image(event,x,y,flags,param):
    global arr
    global filename,display
    img=cv2.imread(filename)
    
    if event==cv2.EVENT_LBUTTONDOWN:
        arr.append((x,y))
        print(arr)

    if len(arr)==4:
        pts1=np.array([(arr[0][0],arr[0][1]),(arr[1][0],arr[1][1]),(arr[2][0],arr[2][1]),(arr[3][0],arr[3][1])],np.float32)
        pts2=np.array([(0,0),(500,0),(0,600),(500,600)],np.float32)
        perspective=cv2.getPerspectiveTransform(pts1,pts2)
        trans=cv2.warpPerspective(img,perspective,(500,600))
        display=trans
        cv2.imshow('Frame',trans)

def auto_wrap():
    global filename
    global display
    
    img=cv2.imread(filename)
    image=img.copy()
    grey=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    filter=cv2.bilateralFilter(grey,9,75,75)
    thres=cv2.adaptiveThreshold(filter,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,25,2)
    blur=cv2.medianBlur(thres,11)
    canny=cv2.Canny(blur,200,255)

    contours,hierarchy=cv2.findContours(canny,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    areas=[cv2.contourArea(c) for c in contours]
    max_index=np.argmax(areas)
    max_contour_area=contours[max_index]
    perimeter=cv2.arcLength(max_contour_area,True)
    ROI=cv2.approxPolyDP(max_contour_area,0.01*perimeter,True)
    cv2.drawContours(img,[ROI],-1,(0,255,0),2)

    if len(ROI)==4 and cv2.isContourConvex(ROI):
        required_page=ROI
        arr=get_four_points(required_page[:,0])
        pts1=np.array([(arr[0][0],arr[0][1]),(arr[1][0],arr[1][1]),(arr[2][0],arr[2][1]),(arr[3][0],arr[3][1])],np.float32)
        pts2=np.array([(0,0),(500,0),(0,600),(500,600)],np.float32)
        perspective=cv2.getPerspectiveTransform(pts1,pts2)
        trans=cv2.warpPerspective(image,perspective,(500,600))
        display=trans
        cv2.imshow('Frame',trans)
        cv2.waitKey(20)

    else:
        response=tk.messagebox.showinfo("Message","Auto-wrap is not available\nPlease select Manual wrap")

def manual_wrap():
    global filename

    if os.path.exists(filename):
        image=cv2.imread(filename)
        cv2.namedWindow('select')
        cv2.setMouseCallback('select',warp_image)
        cv2.imshow('select',image)
        cv2.waitKey(10000)
    else:
        response=tk.messagebox.showinfo("Message","Please select image")

def about_():
    about = tk.Frame(text_frame,bg = 'white')
    about.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)
    
    text=Text(about,bg='white')
    text.insert('1.0','This is a GUI Application.It uses tkinter and Opencv to select,blur,crop,warp and filter the images using opencv functions :-)\n\nClick on Instructions to understand what each button does')
    text.pack()

def _instruction_():
    instruction = tk.Frame(text_frame,bg = 'white')
    instruction.place(relx = 0.2,rely = 0.2,relwidth =0.6,relheight =0.6)
    text=Text(instruction,bg='#FDFFD6')
    text.insert('1.0','Instructions:\n 1:Please select the image by clicking on (Select Image)\n2:U can grey the image\n3:Blur and filter are dropdown menus to help u select what u want\n4: Crop the image by CLICK-DRAG method\n5:For manual warping select 4 pints on frame in order -TL->TR->BL->BR')
    text.pack()

def save_current():
    global display
    name = ''
    name = filedialog.asksaveasfilename (initialdir = '/home/krutika', title = 'Save File', filetypes = (('JPG', '*.jpg'), ('All files','*.*')))
    print (name)
    response=tk.messagebox.showinfo("Saved","Image saved successfully")

    if name != '':
        cv2.imwrite (name, display)

def show_original():
    global img,filename
    
    if os.path.exists(filename):
        img=cv2.imread(filename)
        cv2.imshow('Frame',img)
        cv2.waitKey(20)

window=tk.Tk()
canvas=tk.Canvas(window,height=600,width=850,bg='medium spring green')
canvas.pack()
menubar=Menu(canvas)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Open Image",command=select_pic)
filemenu.add_command(label="Save-as",command=save_current)
filemenu.add_separator()

filemenu.add_command(label="Exit", command=window.quit)
menubar.add_cascade(label="File", menu=filemenu)

helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about_)
helpmenu.add_command(label="Instructions", command=_instruction_)
menubar.add_cascade(label="help", menu=helpmenu)
window.config(menu=menubar)

text_frame=tk.Frame(canvas,bg='navajo white')
text_frame.place(bordermode=OUTSIDE,height=480,width=400,x=400,y=50)

myFont = font.Font(family='Helvetica',size=13, weight='bold')
select_frame=tk.Frame(canvas,bg='medium spring green')
select_frame.place(bordermode=OUTSIDE,height=150,width=100,x=150,y=40)
select_btn=Button(select_frame,text="Select\n Image",fg="black",width=10,height=2,justify=CENTER,cursor="hand2",font=myFont,bd=1,bg="gainsboro",command=select_pic)
select_btn.pack()

btn_frame=tk.Frame(canvas,bg='medium spring green')
btn_frame.place(bordermode=OUTSIDE,height=570,width=380,x=20,y=120)

test_frame1=tk.Frame(canvas,bg='coral')
test_frame1.place(bordermode=OUTSIDE,height=60,width=110,x=30,y=138)
variable=tk.StringVar(test_frame1)
variable.set('Blur')
opt=tk.OptionMenu(test_frame1,variable,*option)
variable.trace("w", blur_image)
opt.config(width=8,height=2,font=myFont)
opt.pack()

btn_frame.grid_columnconfigure(1,minsize=100)
grey=Button(btn_frame,text="Grey",fg="black",justify=CENTER,cursor="hand2",width=10,height=2,bd=1,bg="gainsboro",font=myFont,command=grey_image,padx=1,pady=1).grid(row=0,column=2,padx=10,pady=20)
btn_frame.grid_rowconfigure(1,minsize=20)
crop=Button(btn_frame,text="Crop",fg="black",justify=CENTER,cursor="hand2",width=10,height=2,bd=1,bg="gainsboro",font=myFont,command=crop_image_btn,padx=1,pady=1).grid(row=2,column=0,padx=10,pady=20)
auto_wrap=Button(btn_frame,text="Auto\nWrap",fg="black",justify=CENTER,cursor="hand2",width=10,height=2,bd=1,bg="gainsboro",font=myFont,command=auto_wrap,padx=1,pady=1).grid(row=2,column=2,padx=10,pady=20)
btn_frame.grid_rowconfigure(3,minsize=20)
Manual_wrap=Button(btn_frame,text="Manual\nWrap",fg="black",justify=CENTER,cursor="hand2",width=10,height=2,bd=1,bg="gainsboro",font=myFont,command=manual_wrap,padx=1,pady=1).grid(row=4,column=0,padx=10,pady=20)
OCR=Button(btn_frame,text="OCR",fg="black",justify=CENTER,cursor="hand2",width=10,height=2,bd=1,bg="gainsboro",font=myFont,command=OCR_func,padx=1,pady=1).grid(row=4,column=2,padx=10,pady=20)
btn_frame.grid_rowconfigure(5,minsize=20)
Show_text=Button(btn_frame,text="Show Text",fg="black",justify=CENTER,cursor="hand2",width=10,height=2,bd=1,bg="gainsboro",font=myFont,command=show_text,padx=1,pady=1).grid(row=6,column=0,padx=10,pady=20)

test_frame=tk.Frame(canvas,bg='coral')
test_frame.place(bordermode=OUTSIDE,height=60,width=110,x=253,y=480)
variable1=tk.StringVar(test_frame)
variable1.set('Filter')
opt1=tk.OptionMenu(test_frame,variable1,*filter_option)
variable1.trace("w", callback)
opt1.config(width=8,height=2,font=myFont)
opt1.pack()

save_frame=tk.Frame(canvas,bg='medium spring green')
save_frame.place(bordermode=OUTSIDE,height=50,width=400,x=400,y=540)

save_btn=Button(save_frame,text="Save",fg="red",justify=CENTER,cursor="hand2",width=8,height=1,bd=1,bg="gainsboro",font=myFont,command=save_current,padx=1,pady=1).grid(row=0,column=0,padx=10,pady=10)
save_frame.grid_columnconfigure(1,weight=5)
show_btn=Button(save_frame,text="Show original",fg="red",justify=CENTER,cursor="hand2",width=13,height=1,bd=1,bg="gainsboro",font=myFont,command=show_original,padx=1,pady=1).grid(row=0,column=2,padx=10,pady=10)
save_frame.grid_columnconfigure(3,weight=5)
Exit_btn=Button(save_frame,text="Exit",fg="red",justify=CENTER,cursor="hand2",width=8,height=1,bd=1,bg="gainsboro",font=myFont,command=window.quit,padx=1,pady=1).grid(row=0,column=4,padx=10,pady=10)

window.mainloop()