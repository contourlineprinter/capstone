# Version of demo.py that takes file input as command line arguments

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, sys
from ImageConversionClass import ImageConversion

#----------------------------------------- 
if len(sys.argv) != 2:
	print ("Please give a filename as an argument")
	print ("usage: python3 convertFileInput.py [file name]")
	exit()
      
image = sys.argv[1]
svg = sys.argv[2]

print (image)
print (svg)

# create an ImageConversion object
imgConvert = ImageConversion(image, svg)

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


