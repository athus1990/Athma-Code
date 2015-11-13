# Annotation Code
Pyhton code used for drawing  for drawing bounding boxes to sequence of images present in folder

**annotateTool.py**

Argument: **--img** fullpath of folder containing jpg/png images.

Output:   **outputfile** in current directory containing the bounding boxes(can be read into matlab/pyhton for future use)

### Version
1.0.1

### Installation
##### General : Usually preintalled
* numpy
* matplotlib
* scipy
* argparse
* pickle

##### Additional dependencies
* annoteTool
    * OpenCV(cv2)

### How to use
Once the first image in folder opens draw as many bounding boxes as needed.Use following keyboard keys to sift through images
  - **cc** (double 'c') to continue to next image once u are sure of the bounding boxes
  - **r** to redraw incase of mistake
  - **q** to save the current annotated images and exit
  
Please have a look as the demo.flv video for a demo on usage

### Tip/Feature
You do not have to annotate all files in folder at once.When u finish say 20/100 images and need to take a break.Quit using 'q key' and the output is saved.U can resume calling the code again and it will resume as long as the output file is not moved or damaged.!

There is no previous key(as it messes with output file and complicates it).Therefore be sure that annotation is correct and press **'double cc key'** when you are sure of th annotation.If u did make a mistake u always have the redraw option(**'r key'**).



