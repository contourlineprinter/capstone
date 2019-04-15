import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, sys
from ImageConversionClass import ImageConversion

#-----------------------------------------         
#image = "2.png"
image = "2.jpg"
#image = "water.jpg"
svg = "./"

# create an ImageConversion object
imgConvert = ImageConversion(image, svg)

# print class documentation
#print ("ImageConversion.__doc__:", ImageConversion.__doc__)

# print info
imgConvert.printImgInfo()

# load in image
imgGray = imgConvert.readImageGrayscale(image) # turn on for regular
#img = imgConvert1.readImageOriginal(image) # turn on for background removal

imgResize = imgConvert.resizeImageByHeightAndWidth(imgGray, None, None, desiredImgHeight = 500, desiredImgWidth = None)

# print info
imgConvert.printImgInfo()

# show image
#imgConvert1.showImage("Original Image", img)

# get image ready
eroImg = imgConvert.getImageReady(imgResize)     # regular
#eroImg = imgConvert1.getImageReadyNoBackground(img) # background removal - need orig image


# find contour lines
conImgNoEdgeOld, conImgNoEdge, conNoEdgePoints = imgConvert.createContours(eroImg)

# compare three images - original, edges found, final contour image 
#imgConvert1.showThreeImages(img, conImgNoEdgeOld, conImgNoEdge, "Original", "Edges Found", "Final Contour")

# close all windows
#imgConvert.closeAllWindows()

#-----------------------------------------
