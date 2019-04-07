# Version of demo.py that takes file input as command line arguments

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, sys
import parseArguments
from ImageConversionClass import ImageConversion

#----------------------------------------- 
if len(sys.argv) < 2:
        print ("Please give a image name or image path as an argument")
        print ("usage: python3 convertFileInput.py [image name] ./ [svg path (optional)]")
        exit()
if len(sys.argv) == 2:
        image = str(sys.argv[1])
        svg = "./"
elif len(sys.argv) == 3:
        image = str(sys.argv[1])
        svg = str(sys.argv[2])
elif len(sys.argv) > 3:
        args = str(sys.argv[1])
        for i in sys.argv[2:]:
                args = args + " " + str(i)
        image, svg = parseArguments.parseArguments(args)
        
for i in range(len(sys.argv)):
        print(i, " - ", str(sys.argv[i]))

print ("\n", str(image))
print (str(svg))

# create an ImageConversion object
imgConvert = ImageConversion(image, svg)

# print info
imgConvert.printImgInfo()

# read in image
img = imgConvert.readImageOriginal(image)

# show image
#imgConvert.showImage("Original Image", img)

# get image ready
eroImg = imgConvert.getImageReadyNoBackground(img)

# find contour lines not using Canny edges
conImgNoEdgeOld, conImgNoEdge, conNoEdgePoints = imgConvert.createContours(eroImg)

# close all windows
#imgConvert.closeAllWindows()


