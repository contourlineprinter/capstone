# Version of demo.py that takes file input as command line arguments
# slider = xy range, points to skip, min area

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, sys
import parseArguments
from ImageConversionClass import ImageConversion

#----------------------------------------- 
if len(sys.argv) < 2:
        print ("Please give a image name or image path as an argument")
        print ("usage: python3 convertFileInput.py [image name] ./ [svg path (optional)] [xy range (optional)] [pts to skip (optional)] [min area (optional)]")
        exit()
if len(sys.argv) == 2:
        image = str(sys.argv[1])
        svg = "./"
elif len(sys.argv) == 3:
        image = str(sys.argv[1])
        svg = str(sys.argv[2])
        xyRange = -1
        skipPoints = -1
        minArea = -1
elif len(sys.argv) > 3:
        args = str(sys.argv[1])
        for i in sys.argv[2:]:
                args = args + " " + str(i)
        image, svg, xyRange, skipPoints, minArea = parseArguments.parseArguments(args)
        
for i in range(len(sys.argv)):
        print(i, " - ", str(sys.argv[i]))

print ("\n", str(image))
print (str(svg))

# create an ImageConversion object
imgConvert = ImageConversion(image, svg)

# print info
imgConvert.printImgInfo()

# convert to grayscale
imgGray = imgConvert.readImageGrayscale(image)

# resize image
#imgResize = imgConvert.resizeImageByHeightAndWidth(imgGray, None, None, desiredImgHeight = 400, desiredImgWidth = None)

# show image
#imgConvert.showImage("Original Image", image)

# get image ready
eroImg = imgConvert.getImageReady(imgGray)

# find contour lines not using Canny edges
conImgNoEdgeOld, conImgNoEdge, conNoEdgePoints = imgConvert.createContours(eroImg, 2, xyRange, skipPoints, minArea)

# close all windows
#imgConvert.closeAllWindows()


