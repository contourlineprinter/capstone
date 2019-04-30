# Version of demo.py that takes file input as command line arguments
# slider = xy range, points to skip, min area

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, sys
import parseArguments_HQ
from ImageConversionClass_HQ import ImageConversion

#----------------------------------------- 
if len(sys.argv) < 2:
        print ("Please give a image name or image path as an argument")
        print ("usage: python3 convertFileInput.py [image name] ./ [svg path (optional)] [xy range (optional)] [point density (optional)] [min area (optional)]")
        exit()
if len(sys.argv) == 2:
        image = str(sys.argv[1])
        svg = "./"
        xyRange = -1
        skipPoints = -1
        minArea = -1
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
        print("\nInfo")
        print("Image : ", image)
        print("SVG : ",  svg)
        print("XY Range: ", xyRange)
        print("Skip: ", skipPoints)
        print("Min Area: ", minArea)
for i in range(len(sys.argv)):
        print(i, " - ", str(sys.argv[i]))

print ("\n", str(image))
print (str(svg))

#--------------------------------------------------------------------
# regular

# create an ImageConversion object
imgConvert = ImageConversion(image, svg)

# load in image
imgGray = imgConvert.readImageGrayscale(image) # turn on for regular
#img = imgConvert1.readImageOriginal(image) # turn on for background removal

# get height and width of image
height, width = imgConvert.getImageOrigHeightAndWidth()

# print info
imgConvert.printImgInfo()

# if the image is a certain size
if height >= 300 or width >= 300:

    # resize image    
    imgGray = imgConvert.resizeImageByHeightAndWidth(imgGray, None, None, desiredImgHeight = 200, desiredImgWidth = None)

# get image ready
eroImg = imgConvert.getImageReady(imgGray)

# find contour lines
conImgNoEdgeOld, conImgNoEdge, conNoEdgePoints = imgConvert.createContours(eroImg, 2, xyRange, skipPoints, minArea)

#--------------------------------------------------------------------
# with no background
##
### create an ImageConversion object
##imgConvert = ImageConversion(image, svg)
##
### load in image
##img = imgConvert.readImageOriginal(image) # turn on for background removal
##
### get height and width of image
##height, width = imgConvert.getImageOrigHeightAndWidth()
##
### print info
##imgConvert.printImgInfo()
##
### if the image is a certain size
##if height >= 300 or width >= 300:
##
##    # resize image    
##    img = imgConvert.resizeImageByHeightAndWidth(img, None, None, desiredImgHeight = 200, desiredImgWidth = None)
##
##imgGray = imgConvert.getImageReadyNoBackground(img) # background removal - need orig image
##
### get image ready
##eroImg = imgConvert.getImageReady(imgGray)
##
### find contour lines
##conImgNoEdgeOld, conImgNoEdge, conNoEdgePoints = imgConvert.createContours(eroImg, 2, xyRange, skipPoints, minArea)
##
