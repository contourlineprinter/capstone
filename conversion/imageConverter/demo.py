import numpy as np
import cv2
import matplotlib.pyplot as plt
from ImageConversionClass import ImageConversion

#-----------------------------------------         
name = "1.jpg"
path = "./" + name

# create an ImageConversion object
imgConvert1 = ImageConversion(name, path)

# print class documentation
print ("ImageConversion.__doc__:", ImageConversion.__doc__)

# print employee
imgConvert1.printImgInfo()

# load in image
img = imgConvert1.readImageOriginal(name)
imgGray = imgConvert1.readImageGrayscale(name)

# show image
imgConvert1.showImage("Original Image", img)

# get image ready
eroImg = imgConvert1.getImageReady(imgGray)

# find contour lines not using Canny edges
conImgNoEdgeOld, conImgNoEdge, conNoEdgePoints = imgConvert1.createContours(eroImg)

# compare three images - original, edges found, final contour image 
imgConvert1.showThreeImages(img, conImgNoEdgeOld, conImgNoEdge, "Original", "Edges Found", "Final Contour")

# close all windows
imgConvert1.closeAllWindows()

#-----------------------------------------
