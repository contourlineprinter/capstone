# Version of demo.py that takes file input as command line arguments


import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, sys
from ImageConversionClass import ImageConversion

#----------------------------------------- 


if len(sys.argv) != 3:
	print ("Please give a filename and path as arguments")
	print ("usage: python3 convertFileInput.py [file name] [path]")
	exit()
      
name = sys.argv[1]
path = sys.argv[2]


print (name)
print (path)


# create an ImageConversion object
imgConvert = ImageConversion(name, path)

# print info
imgConvert.printImgInfo()

# convert to grayscale
imgGray = imgConvert.readImageGrayscale(name)

# show image
#imgConvert.showImage("Original Image", img)

# get image ready
eroImg = imgConvert.getImageReady(imgGray)

# find contour lines not using Canny edges
conImgNoEdgeOld, conImgNoEdge, conNoEdgePoints = imgConvert.createContours(eroImg)


# close all windows
imgConvert.closeAllWindows()


