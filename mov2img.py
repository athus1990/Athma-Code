#!/usr/bin/env python
import sys,os
import numpy as np
import argparse
import time
def parse_args():
    parser = argparse.ArgumentParser(description='CONVERT MOV TO PNG/JPEG')
    parser.add_argument('--jpg', dest='ext', help='fullpath of img folders',default='png')
    parser.add_argument('--i', dest='inputfilename', help='Input MOV File name(including extension)',default=0)
    parser.add_argument('--o', dest='outputfilename', help='Output File location folder',default=0)
    args = parser.parse_args()
    return args

if __name__ == '__main__':
    args = parse_args()
    if(os.path.exists(args.outputfilename)):
    	print("DIRECTORY EXISTS:WILL OVERWRITE")
    	time.sleep(1)
    else:
    	print("Making output directory")
    	os.system("mkdir "+args.outputfilename)
    	time.sleep(1)
    if(args.inputfilename ==0):
        print("ERROR:ENTER INPUT MOV FILE NAME USING --i")
        exit(0)
    if(args.outputfilename==0):
        print("ERROR:ENTER OUTPUT FILE LOCATION --o")
        exit(0)
    if(args.ext=='jpg'):
        os.system("##COVERSION TO JPG IN PROGRESS##")
        os.system("ffmpeg -i "+ args.inputfilename +" "+ args.outputfilename + "/image%d.jpg")
    else:
        os.system("##COVERSION TO PNG IN PROGRESS##")
        os.system("ffmpeg -i "+ args.inputfilename +" "+ args.outputfilename + "/image%d.png")
         
    print("##CONVERSION COMPLETED##")
    exit(0) 
