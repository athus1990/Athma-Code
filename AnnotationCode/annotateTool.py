#!/usr/bin/env python

import sys,os
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
from scipy.io import savemat
from scipy.io import loadmat
import argparse
import pickle
from cv2.cv import *
import cv2


global startpointx,startpointy,rectangle,img
global p
global boundingbox
global imgnumber,boxnumber,imgfullpath,imgfullpathlist


refPt = []
cropping = False
imgnumber=0;
 
def click_and_draw(event, x, y, flags, param):
    # grab references to the global variables
    global refPt, cropping,img
    global boundingbox
    global imgnumber,boxnumber
    if event == cv2.EVENT_LBUTTONDOWN:
        refPt = [(x, y)]
        cropping = True
 
    elif event == cv2.EVENT_LBUTTONUP:
        refPt.append((x, y))
        cropping = False
 
        # draw a rectangle around the region of interest
        print([refPt,imgnumber,boxnumber])
        boundingbox.append([refPt,imgnumber])
        boxnumber=boxnumber+1
        cv2.rectangle(img, refPt[0], refPt[1], (0, 255, 0), 2)
        cv2.imshow("image", img)


def parse_args():
    parser = argparse.ArgumentParser(description='ANNOTATE AN IMAGE SEQUENCE')
    parser.add_argument('--img', dest='imgloc', help='fullpath of img folders')
    #parser.add_argument('--imgnumber', dest='imgnm', help='What image number to start with?(default=0)',default=0, type=int)
    args = parser.parse_args()
    return args

def plotimg(path,f):
    global img
    global boundingbox
    global imgnumber,boxnumber,imgfullpath,imgfullpathlist

    print(os.path.join(path,f))
    imgfullpath=os.path.join(path,f)
    imgfullpathlist.append(imgfullpath)
    img=mpimg.imread(imgfullpath)
    clone = img.copy()
    # set window for the image
    cv2.namedWindow("image")
    cv2.setMouseCallback("image", click_and_draw)
    # mouse callback
    while True:
    # display the image and wait for a keypress
        cv2.imshow("image", img)
        key = cv2.waitKey(1) & 0xFF
 
    # if the 'r' key is pressed, reset the cropping region
        if key == ord("r"):
            for x in range(0, boxnumber):
                boundingbox.pop()
            boxnumber=0;
            img = clone.copy()

    # if the 'c' key is pressed, break from the loop
        elif key == ord("c"):
            boxnumber=0
            break

        elif key == ord("q"):
            print(len(boundingbox))
            print('#######')
            print((boundingbox))
            print('#######')
            print "No of images Annotated=%d" %(boundingbox[-1][-1])
            with open('outputfile', 'wb') as f:
                pickle.dump(boundingbox, f)
            exit(0)

    if len(refPt) == 2:
        cv2.waitKey(0)
        # close all open windows
        cv2.destroyAllWindows()
 
    

if __name__ == '__main__':
    args = parse_args()
    path = args.imgloc
    listing = os.listdir(path)
    listing.sort()
    imgnumber=0;
    boxnumber=0;
    imgfullpathlist=[];
    filepath=os.path.join(os.getcwd(),'outputfile')
    print(filepath)
    if os.path.isfile(filepath):
        print("## FILE FOUND LOADING EXISTING MAT FILE:outputfile")
        with open('outputfile', 'rb') as f:
            boundingbox = pickle.load(f)
        print(boundingbox)
        startimgno=boundingbox[-1][-1]
        imgnumber=boundingbox[-1][-1]
    else:
        print("## CREATING NEW MAT FILE:outputfile")
        boundingbox = [[]]
        startimgno=0
        print("##STARING ANNOTATION FROM IMAGE 1")

    for j in range(startimgno, len(listing)):
        imgnumber=imgnumber+1;
        plotimg(path,listing[j])
         
     
