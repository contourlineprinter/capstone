import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, sys
from ImageConversionClass import ImageConversion

#-----------------------------------------         
#image = "2.png"
image = "2.jpg"
#image = "water.jpg"
#image = "woman.png"
svg = "./"
xyRange = -1
skipPoints = -1
minArea = -1

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
#-----------------------------------------
