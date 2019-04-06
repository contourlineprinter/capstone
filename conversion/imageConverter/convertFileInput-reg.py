# Version of demo.py that takes file input as command line arguments

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, sys
from ImageConversionClass import ImageConversion

#----------------------------------------- 
if len(sys.argv) < 2:
        print ("Please give a image name or image path as an argument")
        print ("usage: python3 convertFileInput.py [image name] ./ [svg path (optional)]")
        exit()
if len(sys.argv) == 2:
        image = sys.argv[1]
        svg = "./"
elif len(sys.argv) == 3:
        image = sys.argv[1]
        svg = sys.argv[2]
elif len(sys.argv) > 3:
        image = sys.argv[1]
        svg = ""
        for i in range(len(sys.argv[2:])):
                svg = svg + str(sys.argv[i])
for i in range(len(sys.argv)):
        print(i, " - ", str(sys.argv[i]))

print (str(image))
print (str(svg))

# create an ImageConversion object
imgConvert = ImageConversion(image, svg)

# print info
imgConvert.printImgInfo()

# convert to grayscale
imgGray = imgConvert.readImageGrayscale(image)

# show image
#imgConvert.showImage("Original Image", image)

# get image ready
eroImg = imgConvert.getImageReady(imgGray)

# find contour lines not using Canny edges
conImgNoEdgeOld, conImgNoEdge, conNoEdgePoints = imgConvert.createContours(eroImg)

# close all windows
imgConvert.closeAllWindows()


