# -*- coding: utf-8 -*-
import numpy as np
import cv2
import matplotlib.pyplot as plt
import svgwrite
import os, sys, ntpath, traceback
import math

class ImageConversion:    
    "Class to perform image conversion to contour, svg, and robot instructions\n"
    
#-----------------------------------------
    # constructor
    # parameters: orignal image name (if in same directory) or path, svg path
    def __init__(self, origImg, svgPath):
        try:
            if not isinstance(origImg, str):
                self.origImg = str(origImg)
            else: self.origImg = str(origImg)
            if not isinstance(svgPath, str):
                self.svgPath = str(svgPath)
            else: self.svgPath = str(svgPath)
            self.origHeight = -1
            self.origWidth = -1
        except Exception as e:
            print("Error: There is a problem with creating the class - \n" + e.args[0] )
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # print the image information
    def printImgInfo(self):
        try:
            print("Image: %s\n" \
                "SVG: %s " % (self.origImg, self.svgPath))
            if self.origHeight is -1 :
                print("Height has not been set. Try loading in the image.")
            else:
                print("Height: ", self.origHeight)
            if self.origWidth is -1 :
                print("Width has not been set. Try loading in the image.")
            else:
                print("Width: ", self.origWidth)
            print("")
            
        except Exception:
            print("Error: There is a problem with printing the information - \n" + e.args[0] )
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # read in an image in with original colors
    # parameter: image filename (if in current directory) or image path
    # return: original image
    def readImageOriginal(self, image):
        try:
            imgOriginal = cv2.imread(image, 1)          # read in image original colors
            height, width = imgOriginal.shape[:2]       # get height and width
            if height: self.origHeight = height         # set height
            if width: self.origWidth = width            # set width
            return imgOriginal
        
        except Exception as e:
            print("Error: There is a problem with reading in image - \n" + e.args[0] )
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # read in an image in as grayscale
    # parameter: image filename (if in current directory) or image path
    # return: image in grayscale
    def readImageGrayscale(self, image):
        try:
            imgGray = cv2.imread(image, 0)              # read in image grayscale
            height, width = imgGray.shape[:2]           # get height and width
            if height: self.origHeight = height         # set height
            if width: self.origWidth = width            # set width
            return imgGray
        
        except Exception as e:
            print("Error: There is a problem with reading in image - \n" + e.args[0] )
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------     
    # show image
    # parameters: name of the window, image to show
    def showImage(self, title, image):
        try:
            cv2.namedWindow(title, cv2.WINDOW_NORMAL)   # create a resizable window
            cv2.imshow(title, image)                    # show the image inside the window
            
        except Exception as e:
            print("Error: There is a problem with showing the image - \n" + e.args[0] )    
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # show two images with matplotlib
    # paramters: image 1, image 2, image 1 window name, image 2 window name
    def showTwoImages(self, image1, image2, title1, title2):
        try:
            # convert images to RGB for matplotlib - OpenCV uses BGR
            RGB_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
            RGB_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)

            # display image 1
            plt.subplot(1,2,1)      # index 1 in 1 row, 2 columns
            plt.title(title1)       # set image 1 title
            plt.imshow(RGB_image1)  # set image 1
            plt.xticks(list(plt.xticks()[0]))
            plt.yticks(list(plt.yticks()[0]))

            # display image 2
            plt.subplot(1,2,2)      # index 2 in 1 row, 2 columns
            plt.title(title2)       # set image 2 title
            plt.imshow(RGB_image2)  # set image 2 
            plt.xticks(list(plt.xticks()[0]))
            plt.yticks(list(plt.yticks()[0]))

            # show both image
            plt.show()
            
        except Exception as e:
            print("Error: There is a problem with showing the two images - \n" + e.args[0] )    
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # show three images with matplotlib
    # paramters: image 1, image 2, image 3, image 1 window name, image 2 window name, image 3 window name
    def showThreeImages(self, image1, image2, image3, title1, title2, title3):
        try:
            # convert images to RGB for matplotlib - OpenCV uses BGR
            RGB_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2RGB)
            RGB_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2RGB)
            RGB_image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2RGB)

            # display image 1
            plt.subplot(1,3,1)      # index 1 in 2 row, 2 columns
            plt.title(title1)       # set image 1 title
            plt.imshow(RGB_image1)  # set image 1
            plt.xticks(list(plt.xticks()[0]))
            plt.yticks(list(plt.yticks()[0]))

            # display image 2
            plt.subplot(1,3,2)      # index 2 in 2 row, 2 columns
            plt.title(title2)       # set image 2 title
            plt.imshow(RGB_image2)  # set image 2 
            plt.xticks(list(plt.xticks()[0]))
            plt.yticks(list(plt.yticks()[0]))

            # display image 3
            plt.subplot(1,3,3)      # index 3 in 2 row, 2 columns
            plt.title(title3)       # set image 3 title
            plt.imshow(RGB_image3)  # set image 3
            plt.xticks(list(plt.xticks()[0]))
            plt.yticks(list(plt.yticks()[0]))

            # show the three images
            plt.show()
            
        except Exception as e:
            print("Error: There is a problem with showing the three images - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # close all windows
    def closeAllWindows(self):
        cv2.waitKey(0)      # wait till any key is press
        cv2.destroyAllWindows() # destroy all windows
#-----------------------------------------
    # convert image to grayscale
    # parameter: color image to be turned gray
    # return: grayscale image
    def turnImageGray(self, image):
        try:
            grayImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert to grayscale
            return grayImage
        
        except Exception as e:
            print("Error: There is a problem with turning the image gray - \n" + e.args[0] )    
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # remove the background
    # parameter: image to used for background removal
    # return: image with background removed
    def removeBackground(self, image):

        try:
            
            BLUR = 15
            DILATE = 8
            ERODE = 8
            THRESH1 = 15
            THRESH2 = 180
            COLOR = (1.0, 1.0, 1.0)

            type = 4

            x1 = 0.1
            x2 = 0.9
            y1 = 0.1
            y2 = 0.9

            # Converting image to rgb
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

            # Finding it's width and height
            height, width = image_rgb.shape[:2]

            # Marking rectangle considering main object to be within this rectangle.
            rectangle = (int(width*x1), int(height*y1), int(width*x2), int(height*y2))

            # Creating a mask
            mask = np.zeros(image_rgb.shape[:2], np.uint8)

            # Background mask
            bgdModel = np.zeros((1, 65), np.float64)

            # Foreground mask
            fgdModel = np.zeros((1, 65), np.float64)

            # Applying grab cut on the image using rectangle and mask
            cv2.grabCut(image_rgb, mask, rectangle,bgdModel,fgdModel,5,cv2.GC_INIT_WITH_RECT)

            # Creating another mask where mask=2
            mask_2 = np.where((mask==2) | (mask==0), 0, 1).astype('uint8')

            # Applying mask on the original image
            image_rgb_nobg = image_rgb * mask_2[:, :, np.newaxis]

            return image_rgb_nobg        

        except Exception as e:
            print("Error: There is a problem with removing the image background - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # find the edges using Canny edge detection
    # return: edge image
    def getEdges(self, image):
        try:

            CANNY_THRESH_1 = 10
            CANNY_THRESH_2 = 200
            edgeImage = cv2.Canny(image=image, threshold1=CANNY_THRESH_1, threshold2=CANNY_THRESH_2)

            # taking a matrix of size n,n as the kernel
            kernelSizeRow = 2
            kernelSizeCol = 2
            kernel = np.ones((kernelSizeRow, kernelSizeCol), np.uint8)
            
            edgeImage = cv2.dilate(edgeImage, None)
            edgeImage = cv2.erode(edgeImage, None)
            
            return edgeImage
        
        except Exception as e:
            print("Error: There is a problem with getting the edges with Canny - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # resize image by height and width
    # parameter: image, original height, original width, desired height, desired width
    # return: resized image
    def resizeImageByHeightAndWidth(self, image, origImgHeight, origImgWidth, desiredImgHeight, desiredImgWidth):
        try:

            #ratio = W / H → W = H * ratio → H = W / ratio
            
            # if the image orig size is not specified
            if origImgHeight is None:
                origImgHeight = self.origHeight
            if origImgWidth is None:
                origImgWidth = self.origWidth

            ratio = abs(origImgWidth/origImgHeight) # get the ratio of the image at original size - ratio = w/h

            # if the user specified the desired height and width
            if desiredImgHeight is not None and desiredImgWidth is not None:
                print("Height and width found")
                dimension = (desiredImgWidth, desiredImgHeight) # resize based on desired height and width
                
            # if the user specified the desired height only
            elif desiredImgHeight is not None:
                print("Height found")
                dimension = (abs(int(ratio*desiredImgHeight)), abs(desiredImgHeight)) # resize based on desired height and width
                
            # if the user specfied the desired width
            elif desiredImgWidth is not None:
                print("Width found")
                dimension = (desiredImgWidth, abs(int(ratio*desiredImgWidth))) # resize based on desired height and width

            # else return the image at original size
            else:
                print("Image is not changed. Missing parameters.")
                return image

            if dimension is not None:
                resizeImg = cv2.resize(image, dimension, interpolation = cv2.INTER_AREA)
                newHeight, newWidth = resizeImg.shape[:2]
                print("\nNew Height: ", newHeight)
                print("New Width: ", newWidth)
                print("")
                
            return resizeImg
        
        except Exception as e:
            print("Error: There is a problem with resizing the image - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # get original image height and width
    # return: height and width
    def getImageOrigHeightAndWidth(self):
        try:

            return self.origHeight, self.origWidth
        
        except Exception as e:
            print("Error: There is a problem with getting the image height and width - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # preprocess the image to find better edges
    # parameter: grayscale image to preprocess (note: image has be this type to work)
    # return: preprocessed image
    def getImageReady(self, image):
        try:
            # Gaussian Blur
            blurImage = cv2.GaussianBlur(image,(5,5),0)
            #self.showImage("Blur Image", blurImage)
            #cv2.moveWindow("Blur Image",0,0)
                
            # adaptive threshold
            # image, max pixel value, type of threshold,
            # neighborhood parameter indicating how far or what the localization of where the adaptive thresholding will act over,
            # mean subtraction from the end result
            # only the threshold picture
            adaptThresImage = cv2.adaptiveThreshold(blurImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 295, 1)
            #self.showImage("Threshold Image", adaptThresImage)
            #cv2.moveWindow("Threshold Image",300,0)

            height, width = image.shape[:2]         # get image size

            # determine kernel size and iteration by image size            
            if (height <= 800):                     # if height is less than or equal to 800
                kernelSizeRow = 3                   # kernel size - 3 rows
                kernelSizeCol = 3                   # kernel size - 3 columns
                iterationValue = 1                  # do 1 iteration
                print ("height <= 800")
            elif (height < 1600):                   # if height is less than 1600
                kernelSizeRow = 4                   # kernel size - 4 rows
                kernelSizeCol = 4                   # kernel size - 4 columns
                iterationValue = 4                  # do 4 iterations
                print ("height < 1600")
            else:                                   # if height is greater than or equal to 1600
                kernelSizeRow = 5                   # kernel size - 5 rows
                kernelSizeCol = 5                   # kernel size - 5 columns
                iterationValue = 5                  # do 5 iteration
                print ("height >= 1600")

            # taking a matrix of size n,n as the kernel 
            kernel = np.ones((kernelSizeRow, kernelSizeCol), np.uint8)            

            #dilation
            dilationImage = cv2.dilate(adaptThresImage, kernel, iterations = iterationValue)
            #self.showImage("Dilation Image", dilationImage)
            #cv2.moveWindow("Dilation Image",600,0)


            #erosion
            erosionImage = cv2.erode(dilationImage, kernel, iterations = iterationValue)
            #self.showImage("Erosion Image", erosionImage)
            #cv2.moveWindow("Erosion Image",900,0)

            #get edges
            edgeImage = self.getEdges(erosionImage)
            #self.showImage("Erosion Image", erosionImage)
            #cv2.moveWindow("Erosion Image",900,0)

            return erosionImage
            #return edgeImage
        
        except Exception as e:
            print("Error: There is a problem with preprocessing the image - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # preprocess the image to find better edges and remove the background
    # parameter: color image to preprocess (note: image has be this type to work)
    # return: preprocessed image with background removal
    def getImageReadyNoBackground(self, image):
        try:

            # remove the background
            noBackgroundImage = self.removeBackground(image)

            # turn image gray
            gray = self.turnImageGray(noBackgroundImage)

            # get preprocess image
            #edgeImage = self.getImageReady(gray)
    
            return gray
        
        except Exception as e:
            print("Error: There is a problem with removing the background and preprocessing the image - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # find the contour of the image based on specific range of x and y coordinates and save as svg file
    # range is used to filter out some points in contour image:
    #   smaller range - more points, more lines in the image 
    #   larger range - less points, less lines in the image
    # parameters: image, line thickness, x and y range, skip points, min area
    # return: old contour image, new contour image, points for new contours
    def createContours(self, image, lineThickness = 2, xyRange = -1, skipPoints = -1, minArea = -1):
        try:

            contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   # find countour
            #print("Create Contours", contours)
            
            print("Found %d objects in intial contour list." % len(contours))                       # length of the contour list

            height, width = image.shape[:2]     # get image size
            pointC = []                         # new set of points

            # filter points
            self.filterPoints(contours, pointC, hierarchy, xyRange, xyRange, skipPoints, minArea) 
            
            # filter points by size of image
##            if (height <= 800):                     # if height is less than or equal to 800
##                self.filterPoints(contours, pointC) # filter points
##            elif (height < 1600):                   # if height is less than 1600
##                self.filterPoints(contours, pointC, 10, 10, 600) # filter points
##            else:                                   # for images greater than or equal to 1600
##                self.filterPoints(contours, pointC, 15, 15, 1200) # filter points
##
            attempt = 0

            # try again if pointC is empty
            if len(pointC) == 0 and attempt == 0 :
                pointC = []
                self.filterPoints(contours, pointC, hierarchy) # filter points
                attempt = 1
                            
            newContours = np.array([pointC])                    # make a numpy array with the new points for contour image

            #print("newContours: ", newContours)

            # make svg of contour - for gallery
            nameSVG = str(ntpath.basename(self.origImg))                    # set filename for svg file
            path = str(self.svgPath)                                        # set directory path for svg file
            self.drawSVG(newContours, height, width, nameSVG, path, 2)      # draw it in the svg

            print("got to ROOT/next")
    
            # make svg of contour - ROOT/next
            nameSVG2 = "imageSVG"                                           # set filename for svg file
            path2 = "/var/lib/tomcat8/webapps/ROOT/next"         # set directory path for svg file

            # if folder for svg doesn't exist
            if not os.path.exists(path2):
                print("Folder doesn't exist for: ", path2)
                print("A new folder will be created")
                os.makedirs(path2)

            self.drawSVG(newContours, height, width, nameSVG2, path2, 2)    # draw it in the svg            

            #don't sort - doesn't work?
            #vec = np.sort(np.array([pointC]))

            # draw the contour images
            blankCanvas1 = 255*np.ones((height, width, 3), np.uint8)                                        # make blank canvas
            blankCanvas2 = 255*np.ones((height, width, 3), np.uint8)                                        # make blank canvas
            imageContourOld = cv2.drawContours(blankCanvas1, contours, -1, (0,255,0), lineThickness)        # draw the contour image with old point
            imageContourNew = cv2.drawContours(blankCanvas2, newContours, -1, (0,255,0), lineThickness)     # draw the contour image with new point

            #self.showTwoImages(imageContourOld, imageContourNew, "Contour Old", "Contour New")

            return imageContourOld, imageContourNew, newContours

        except Exception as e:
            print("Error: There is a problem with creating the contour image - \n" + e.args[0] )
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # count the number of contour points
    # parameters: set of points that make up contour
    # return: the number of points found
    def countPoints(self, contourPoints):
        try: 
            count = 0

            for i in contourPoints:
                for j in i:
                    for k in j:
                        count += 1

            return count

        except Exception as e:
            print("Error: There is a problem with counting the contour points - \n" + e.args[0] )    
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # print the contour contour information
    # parameters: set of points that make up contour
    def print_contours(self, contours):
        try:
            print("Found %d objects." % len(contours)) # print the number of contour objects

            for (i, c) in enumerate(contours):
                print("\tSize of contour %d: %d" % (i, len(c))) # print the size of each contour element
                
        except Exception as e:
            print("Error: There is a problem with getting information on the contour points - \n" + e.args[0] )  
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # get the start and end points and indexes in a set of contour elements
    # parameters: set of points that make up contour
    # return: set with a list of values for each start and end point of a contour element
    #       -> [x, y, contour element number, point number within the element]
    def getStartEndPoints(self, contourPoints):
        try:
            
            startEndPoint = []
           
            # process points in contour - get the last two points
            for i in range(len(contourPoints)):
                
                for j in range(len(contourPoints[i])):
    
                    # if it is the first or last point in the contour element
                    if j == 0 or j == (len(contourPoints[i])-1):

##                        print("Point Start: ", contourPoints[i][j][0][0])
##                        print("Point End: ", contourPoints[i][j][0][1])
                        startEndPoint.append([contourPoints[i][j][0][0], contourPoints[i][j][0][1], i,j]) # [x, y, contour element #, point #]      

##            for i in startEndPoint:
##                print("StartEndPoint: ", i)

            #startEndPoint = np.array(startEndPoint) # change into a numpy array

            # testing
##            print("Print Start End Points: ",  startEndPoint) # print array
##            print(startEndPoint[:,2]) # print the i index - 2nd column
##            print(startEndPoint[:,3]) # print the j index - 3rd column
##            print(startEndPoint[1::2,2]) # ever other row, start with 1 - get 2rd column value
##            print(startEndPoint[::2,3]) # ever other row, start with 0 - get 3rd column value
##            print(startEndPoint[1::2,3]) # ever other row, start with 1 - get 3rd column value

            # print the points in startEndPoint
            #for s in startEndPoint:
             #   print("Start-End: ", s)

            # testing
##            elementNo = startEndPoint[1::2,2]
##            lastIndex = startEndPoint[1::2,3]
##            combine = startEndPoint[:,2:4]
##            startPt = startEndPoint[::2,0]
##            print("***", startPt)

            return startEndPoint
        
        except Exception as e:
            print("Error: There is a problem with getting the start and end points - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # get the smallest point by y-coordinate
    # parameters: set of points [[[x1,y1]],[[x2,y2]]...[[xn,yn]]]
    # return: minimum y value, x at the minimum y value
    def getMinY(self, setOfPoints):
        try:

            minY = setOfPoints[0][0][1]
            xAtMinY = setOfPoints[0][0][0]
            #print("\nStarting min Y: ", minY)
           
            # process points in contour - get the last two points
            for j in range(len(setOfPoints)):
                        
                foundY = setOfPoints[j][0][1]
                #print("FoundY: ", foundY)

                #print("J - ", setOfPoints[j][0][1])
                if foundY < minY:
                    #print("New Min Y")
                    minY = foundY
                    xAtMinY = setOfPoints[j][0][0]
                        
            return minY, xAtMinY
        
        except Exception as e:
            print("Error: There is a problem with getting the minimum y points - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # get the indices of the smallest
    # parameters: set of points that make up contour
    # return: sorted contourPoints
    def getSortedIndexListBySmallestY(self, contourPoints):
        try:

            listOfMinYs = [] # [contour element #, min y, x at min y]
            for i in range(len(contourPoints)):

                minY, xAtMinY = self.getMinY(contourPoints[i])
                #print("Minimum Found in ", i, ": ", minY)
                listOfMinYs.append([i, minY, xAtMinY])

            print(listOfMinYs)

            listOfMinYs = np.array(listOfMinYs) # change into a numpy array

            # sort the contour element by y, then x
            orderElement = []
            for i in np.argsort(listOfMinYs[:,1]):
                orderElement.append(i)
                #print("Sort", i)
            #print("\nOrdered Elements: ", orderElement)
            #print("")

            # check for null
            if contourPoints is None:
                print("Something wrong here")
                
            #print("Before: ", contourPoints[3])
            contourPoints = contourPoints[orderElement] # order the elements
            #print("After: ", contourPoints[3])

            # check for null
            if contourPoints is None:
                print("Something wrong here")
            
            return contourPoints

        
        except Exception as e:
            print("Error: There is a problem with sortng points by min y - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # sort the parent, the parent's first child, the first child's first child, etc indices by level in the hierarchy
    # parameters:   parent, parent level,
    #               hierarchy [[ [], [], ... , [] ]] ,
    #               list where sorted results will be located [ [], [], ... , [] ] ,
    #               list where indices involved will be added to [ , ... , ] .
    def sortParentFirstChildByLevel(self, parent, level, hierarchy, lvlList, finishList):
        try:

            # if the level or parent has no value, set to 0
            if level is None: level = 0
            if parent is None: parent = 0

            # base case
            if parent == -1:
                return

            else:
                #print("")
                
                # go through each element in the hierarchy list
                for i in hierarchy:
                    
                    lvlList[level].append(parent)   # add the parent to the list at index = level
                    finishList.append(parent)       # add the parent to the finish list - indicate it's been processed
                    child = i[parent][2]            # get the child of the parent
                    #print("Child of parent: ", child)   
                    level+=1                        # increment the level                    
                    self.sortParentFirstChildByLevel(child, level, hierarchy, lvlList, finishList)    # sort the first child for that child

                return

        except Exception as e:
            print("Error: There is a problem with soring parent-child by level - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # get the level of the element in the hierarchy
    # parameters: target element, list to be searched [ [], [], ... , [] ] 
    # return: level of target element
    def getLevel(self, target, searchList):
        try:

            if target is None: target = 0 
                   
            # go through each level
            for i in range(len(searchList)): 
                #print("\n I", i)

                # for the elements at that level
                for j in searchList[i]:
                    #print("\n j target: ", j) 

                    # if the the target is found
                    if target is j:
                      
                        return i # return the level
                      
                return 0 # if the target is not found, return level = 0

        except Exception as e:
            print("Error: There is a problem getting the level of the element - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # get the parent of the element in a list where index = parent and values = children
    # parameters: target element, list to be searched [[ [], [],..., [] ]] 
    # return: parent of target element
    def getParent(self, target, searchList):
        try:

            if target is None: target = 0
               
            # go through list
            for i in searchList:

                # for each parent in the list
                for j in range(len(i)):
                    #print("\n parent target: ", j)

                    # for all the children of that parent
                    for k in i[j]:

                        # if target element is a child of the parent
                        if target is k:
                            return j    # return the value of the parent
                      
            return -1   # if the parent is not found, return -1


        except Exception as e:
            print("Error: There is a problem getting the parent of the element - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # get the list of elements sorted by the level in the hiearchy they are in
    # parameters:   parent-children list where index = parents, values = children -> [[ [], [],..., [] ]] 
    #               hierarchy from findContours -> [[ [], [],..., [] ]]
    # return: level list based on hierarchy, index = level, values = elements -> [ [], [],..., [] ]
    def getHierarchyLevelList(self, parentChildList, hierarchy):
        try:

            finishList = []
            lvlList = []


            # create a level list to put elements in -> [ [], [],..., [] ]
            for i in hierarchy:
                      
                # create a list with the number of contour elements
                # level
                lvlList = [[] for j in range(len(i))] 


            # go through parent-child list
            for i in parentChildList:

                # for each parent
                for j in range(len(i)):

                    #print("\n X: ", i[j], " at ", j)

                    # if the list is not empty
                    if i[j]:

                        # for each child of that parent
                        for k in i[j]:

                            # if the child hasn't been processed
                            if k not in finishList:
                                parent = self.getParent(k, parentChildList)  # get parent of the child
                                level = self.getLevel(parent, lvlList)       # get level of parent
                                #print("Level of k's parent: ", level)   
                                #print("Level of k: ", level+1)
                                self.sortParentFirstChildByLevel(k, level+1, hierarchy, lvlList, finishList)    # sort the child and
                                                                                                    # first child/descendants
                                                                                                    # at the next level
                    #for k in range(len(j)): # children numbers

            # go through hierarchy list
            for i in hierarchy:

                # for each element
                for j in range(len(i)):

                    # if j has not been processed
                    if j not in finishList:

                        finishList.append(j)
                        parent = self.getParent(k, parentChildList)
                        level  = self.getLevel(parent, lvlList)
                        
                        if j not in lvlList[level]:
                            lvlList[level].append(j)


            return lvlList

        except Exception as e:
            print("Error: There is a problem getting the hierarchy level list - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # check if the element meets the min area and approx polynomial requirements
    # parameters:   element to be checked, contour points list, minimum contour area
    # return: true = 1  or false = 0 depending if element meets requirement
    def meetMinAreaPolynomialReq(self, target, contourPoints, minContourArea):
        try:
            contourArea = cv2.contourArea(contourPoints[target]) # find contour area
                
            # we can use this epsilon instead of fixed 2 in approxPolyDP
            epsilon = 0.001 * cv2.arcLength(contourPoints[target], False)
            # approx = cv2.approxPolyDP(c, epsilon, True)

            # applying polygon approximation on the current contour.
            approx2 = cv2.approxPolyDP(contourPoints[target], 2, False)

            # if there are extact four points in the contour, most likely it a sqaure
            # so ignoring such contour
            # if the contour area is less than the minimum contour area
            if (contourArea < minContourArea) or len(approx2) == 4: return 0
            else: return 1

        except Exception as e:
            print("Error: There is a problem with the min area - approx polynomial requirements - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # filter contour points based on minimum areas and specific range of x and y coordinates
    # range is used to filter out some points in contour image:
    #   smaller range - more points, more lines in the image 
    #   larger range - less points, less lines in the image
    # parameters:   set of points that make up contour, range for x, range for y,
    #               skip points (negative value = default),  minimum contour area accepted
    def filterPoints(self, contourPoints, newContourPoints, hierarchy, rangeForX = 5, rangeForY = 5, skipPoints = -1, minContourArea = -1):
        try:

            # find the largest area
            areaList = max(contourPoints, key = cv2.contourArea)
            #print("Largest Area", largestArea)

            areaLarge = -1
            
            if len(areaList) != 0:
                for i in areaList:
                    for j in i:
                        if areaLarge < j[0] :
                            areaLarge = j[0]

            print("Largest Area", areaLarge)

            if minContourArea < 0:
                minContourArea = int(areaLarge/3)
                print("Min Area", minContourArea)
            if rangeForX < 0: rangeForX = 5
            if rangeForY < 0: rangeForY = 5

            # hierarchy
            # - info about the image topology
            # - has as many elements as the number of contours.
            # - For each i-th contour contours[i] ,
            #   hierarchy[i][0] - next
            #   hiearchy[i][1]  - previous
            #   hiearchy[i][2]  - first child
            #   hiearchy[i][3]  - parent 
            # - [Next, Previous, First_Child, Parent]
            # - 0 -> same hierarchical level
            # - negative number -> does not exist
            
            #print(hierarchy[[0,1,2,3]])
            #print("Contours: ", contours)
            #print("Hierarchy: ", hierarchy)

            
            parentChild = [] # parent-child list

            # organize hierarchy info - get the parents and all children
            for i in hierarchy:

##                print("I length: ", len(i))

                l = [[] for j in range(len(i))] # create a list with the number of contour elements

                # for each contour element
                for j in range(len(i)):
                    #print("J: ", j) 
                    
                    #for k in j:
                        #print("K: ", k)

                    # if the contour element has a parent
                    if i[j][3] >= 0:
                        
                        child = j               # get the child
                        parent = i[j][3]        # get the parent
##                        print("Parent found: ", parent, " at child : ", child)   
                        l[parent].append(child) # add to list -> index = parent, value = child
                        
                parentChild.append(l) # add the results to parent-child list

            if parentChild:
                print("\nParent-Child List: ", parentChild, "\n")


            # get hierarchy level
            lvlList = self.getHierarchyLevelList(parentChild, hierarchy)
            print("Level List: ", lvlList)


            deleteChildren = []
            #startChildIndex = 3

            # for each level
            for i in range(len(lvlList)): # [, , ]

                if lvlList[i]:

                    # if the level contains values and if level > 1
                    if i == 1 :
                        for j in range(len(lvlList[i])):
                            #if j > 5 and lvlList[i][j]:
                            if lvlList[i][j]:
                                 
                                get = lvlList[i][j]

                                # if the contour element doesn't meet the min area and contour Points requirement
                                if self.meetMinAreaPolynomialReq(get, contourPoints, minContourArea) == 0:
                                    deleteChildren.append(get) # add the children to be deleted
                
                    elif i > 1:

                        #print("To be deleted I: ", i)
                    
                        for j in range(len(lvlList[i])):
                            if lvlList[i][j]:
                                get = lvlList[i][j]
                                deleteChildren.append(get) # add the children to be deleted
                        

##            # get the children to be deleted
##            for i in parentChild:
##                for j in i:
##                    
##                    #startChildIndex = int(len(j)/2)
##                    #print("Length: ", startChildIndex)
##
##                    for k in range(len(j)):
##                        if len(j) <= 3:
##                            #startChildIndex = 2
##                            continue
##                        elif len(j) > 10:
##                            startChildIndex = 5
##                        elif len(j) > 50: 
##                            startChildIndex = 6
##                        elif len(j) > 100: 
##                            startChildIndex = 8
##                        elif len(j) > 500: 
##                            startChildIndex = 10
##                        
##                        
##                        if k >= startChildIndex and j[k] not in deleteChildren:
##                            deleteChildren.append(j[k])

##            
##            if deleteChildren:
##                print("\nChildren to delete: ", deleteChildren)
##                print("")

##                # delete the children conours
##                contourPoints = np.delete(contourPoints, deleteChildren)

            if deleteChildren:
                contourPoints = np.delete(contourPoints, deleteChildren)
                deleteChildren = np.array(deleteChildren)
                print("\nChildren to delete: ", deleteChildren)
                print("")
#----------------------------------------------------------------------------
##            contoursToDelete = []
##            
##            for i in range(len(hierarchy)):
##
##                for j in hierarchy[i]:
##
##                    print("J in hierarchy: ", j)
##                    parent = j[3]
##                    firstChild = j[2]
##
##                    # if the element doesn't have a parent = 0
##                    # if the element has a parent > 0
##                    # if the element has a child
##                        # if the child 
##                        
##            # delete all the contours that don't meet the requirements
##            contourPoints = np.delete(contourPoints, contoursToDelete)        


#----------------------------------------------------------------------------------------------------------------------------------------
            #--filter contour elements by area, polygon approximation--#
                
            contoursToDelete = [] # list of indexes of contours to delete
            print("Inital Number of Objects: ", len(contourPoints))
            origObjCount = self.countPoints(contourPoints)

            # testing min contourArea
##            minContourArea = max(contourPoints, key = cv2.contourArea)/10
##            print(minContourArea)

            
            
            # look for the contours that don't fit the minimum area requirement
            for i in range(len(contourPoints)):
                
                    # if the contour element doesn't meet the min area and contour Points requirement
                    if self.meetMinAreaPolynomialReq(i, contourPoints, minContourArea) == 0:
                        contoursToDelete.append(i)  # save the index of that contour

            # if the first contour element isn't in the deleted index, add it
            #if 0 not in contoursToDelete: contoursToDelete.append(0)

##            for i in deleteChildren:
##                if i not in contoursToDelete:
##                    contoursToDelete.append(i)

            if contoursToDelete:
                print("Contours to delete reached: " , contoursToDelete)
                # delete all the contours that don't meet the requirements
                contourPoints = np.delete(contourPoints, contoursToDelete)
                #contourPoints = np.delete(contourPoints, 0) # delete the first contour element - polygon takes care of this
#----------------------------------------------------------------------------------------------------------------------------------------
            # printing current state of countour points
            #self.print_contours(contourPoints)

##            # process points in contour - get the last two points
##            startEndPoint = np.array(self.getStartEndPoints(contourPoints)) # change into a numpy array
##
##            # sort the contour element
##            orderElement = []
##            for i in np.argsort(startEndPoint[::2,0]): # skip every other element, sort by x
##                orderElement.append(i)
##                #print("Sort", i)
##            #print(orderElement)
##
##            #print(contourPoints[0])
##            contourPoints = contourPoints[orderElement] # order the elements

            #print("Here")      

            #print("\nLength of Contour Points[i] Before: ", contourPoints[3])
#----------------------------------------------------------------------------------------------------------------------------------------                
            #--get the contour elements ordered--#

            contourPoints = self.getSortedIndexListBySmallestY(contourPoints)   # sort the contour elements
            #print("Starting start end points...")
            startEndPoint = self.getStartEndPoints(contourPoints)               # get the start and end points
            
#----------------------------------------------------------------------------------------------------------------------------------------
            #--filter points by x and y ranges, point alternation--#

            # set up things for processing points in contour
            x = y = []
            xsave = -1
            ysave = -1
            count = 0
            alternate = 0
            pointsToSkip = 0
            numberOfPointsContourElement = 0
            
            # process points in contour - remove some points based on x and y ranges
            for i in range(len(contourPoints)):

                #if i == 0: continue # gets rid of the first contour element

                
#---------------------------------------
                    
                # if points to skip is -1, use default mode
                if skipPoints < 0:
                
                        # testing skipping points
                        if len(contourPoints[i] > 500):
                            pointsToSkip = int(len(contourPoints[i])/10)

                        elif len(contourPoints[i] <= 500) and len(contourPoints[i] > 250):
                            
                            pointsToSkip = int(len(contourPoints[i])/10)

                        elif len(contourPoints[i] <= 250) and len(contourPoints[i] > 125):
                            
                            pointsToSkip = int(len(contourPoints[i])/10)

                        elif len(contourPoints[i] <= 125) and len(contourPoints[i] > 62):
                            
                            pointsToSkip = int(len(contourPoints[i])/10)
                        
                        elif len(contourPoints[i] <= 62) and len(contourPoints[i] > 31):
                            
                            pointsToSkip = int(len(contourPoints[i])/10)
                            
                        else: pointsToSkip = int(len(contourPoints[i])/20)

                else: pointsToSkip = skipPoints

                #pointsToSkip = int(len(contourPoints[i])/5)
##                print("\nLength of Contour Points[i]: ", len(contourPoints[i]))
##                print("Points to skip: ", pointsToSkip)
#---------------------------------------
                
                for j in range(len(contourPoints[i])):
                    
                    #for k in contourPoints[i][j]:
                    xget = contourPoints[i][j][0][0] #get x
                    yget = contourPoints[i][j][0][1] #get y
                    #print("X Found: ", xget)
                    #print("Y Found: ", yget)
                    
                    for c in startEndPoint:
                        #print("Combine Individual: ", c)

                        if i == c[2] and j == c[3]:

                            xsave = xget
                            ysave = yget
                            newContourPoints.append([xget,yget])
                            count+=1
                        
                        else:

                                
                            # if x and y found is within range of saved x and y, don't save it
                            if (abs(c[0]-xget) <= rangeForX) or (abs(xsave-xget) <= rangeForX) or xget == xsave:
                                #print("got here - no")
                                continue
                            elif (abs(c[1]-yget) <= rangeForY) or (abs(ysave-yget) <= rangeForY) or yget == ysave:
                                #print("got here - no")
                                continue
                            else:
      
                                if alternate == pointsToSkip:
                                    xsave = xget
                                    ysave = yget
                                    newContourPoints.append([xget,yget])
                                    count+=1
                                    alternate = 0
                                else:
                                    alternate+=1
                                    continue
##
##                                #print("got here - yes")
##                                xsave = xget
##                                ysave = yget
##                                newContourPoints.append([xget,yget])
##                                count+=1

#----------------------------------------------------------------------------------------------------------------------------------------
                                
            #print("Inital Number of Objects after processing: ", len(contourPoints))
            print("\nLast saved x: %d" % xsave)  # last save x
            print("Last saved y: %d" % ysave)  # last save y
            print("\nNumber of points in old contour image: %d" % origObjCount)  # number of points
            print("Number of points in process contour image: %d" % self.countPoints(contourPoints))  # number of points
            print("Number of points in contour image: %d\n" % count)  # number of points
            
        except Exception as e:
            print("Error: There is a problem with filtering the points - \n" + e.args[0] ) 
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # write a svg file with all the contour points found in the original image
    # parameters: the list of sequence of contour points, height of image, width of image,
    #               image name, directory of svg file,
    #               mode -> 1 = do not overwrite files with same name, other number = overwrite files with same name
    def drawSVG(self, contourPoints, height, width, name = "contour_SVG", path = "./", mode = 1):
        try:

            path = str(path)
            print("::", path)  

            # make sure the path is ready
            if "/" in path:
                if not path.endswith("/"):
                    path = str(path) + "/"
            elif "\\" in path:
                if not path.endswith("\\"):
                    path = str(path) + "\\"
            else: path = "./"
                                     

            print("Path in drawSVG", path)
            # make sure the path is a directory path
            if not os.path.isdir(path):
                print("The path is not a directory.")

                # if the path is a file
                if os.path.isfile(path):
                    print("File detected. The location of the file will be used.")
                    path, file = ntpath.split(path)


            # set up for svg
            extension = ".svg"  # extension for svg

            if mode == 1:
                number = str(self.getNextFileNumber(path, name, extension)) # get the next file number
                location = str(path) + str(name) + str(number) + str(extension)
            else:
                location = str(path) + str(name) + str(extension)
            
            #create a svg file
            #print("SVG to: ", str(path+name+number+extension))
            
            #percentage of resizing
            if (self.origHeight != -1 or self.origWidth != -1):
                percentx = self.origWidth * 100/width
                percenty = self.origHeight * 100/height
                height = self.origHeight
                width = self.origWidth
            else:
                percentx = 100
                percenty = 100

            dwg = svgwrite.Drawing(location, size=(width, height))
            shapes = dwg.add(dwg.g(id="shapes", fill="none"))
            
            print("percentx and percenty: ", percentx, percenty)
            
            #interatively write points into the svg file
            lengthOfTheList = len(contourPoints[0]) - 1
            for x in range(lengthOfTheList):
                #print(contourPoints[0][x][0],contourPoints[0][x][1],contourPoints[0][x+1][0],contourPoints[0][x+1][1])
                #shapes.add(dwg.line(start = (str(contourPoints[0][x][0]), str(contourPoints[0][x][1])), 
                #                 end = (str(contourPoints[0][x+1][0]),str(contourPoints[0][x+1][1])), 
                #                 stroke=svgwrite.rgb(10, 10, 16, "%")
                #))
                x1 = math.floor(contourPoints[0][x][0] * percentx/100)           #resize x1
                x2 = math.floor(contourPoints[0][x+1][0] * percentx/100)         #resize x2
                y1 = math.floor(contourPoints[0][x][1] * percenty/100)           #resize y1
                y2 = math.floor(contourPoints[0][x+1][1] * percenty/100)         #resize y2
                shapes.add(dwg.line(start = (str(x1), str(y1)), 
                    end = (str(x2),str(y2)), 
                    stroke=svgwrite.rgb(10, 10, 16, "%")
                ))                
            
            #save the file
            dwg.save()
            
        except Exception as e:
            print("Error: There is a problem with writing a svg file - \n" + e.args[0] )
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------
    # get the next highest number in filename
    # parameters: directory path where file is located, name of the file to look for, extension of the file to look for
    # return the next highest number in filename
    def getNextFileNumber(self, path = "./", name = "", extension = ""):
        try:

            # return the value of 1 if the name and/or the extension is/are not found
            if name is None or extension is None:
                print("Error: Name and/or extension cannot be found")
                return 1

            path = str(path)

            # make sure the path is ready
            if "/" in path:
                if not path.endswith("/"):
                    path = path + "/"
            elif "\\" in path:
                if not path.endswith("\\"):
                    path = path + "\\"
            else: path = "./"
    
            highest = 0    # the highest number, intialized to 0

            # open the directory
            dirs = os.listdir(path)

            # print all the files and directories in the path
            for file in dirs:
                # print (file)
                
                #if filename exists and contains numbers at the end, check the number
                if name in file[:len(name)] \
                and file.endswith(extension) \
                and file[len(name):len(file)-len(extension)].isdigit():
                    digitFound = int(file[len(name):len(file)-len(extension)])  # save the number as digit found
                    print("Digit found: ", digitFound) 
                    if digitFound > highest:                                    # if the digit found is greater than the highest number
                        highest = digitFound                                    # set as the new highest number

            highest+=1 # increment count at the end for new file        
            print("New highest number: ", highest)
            return highest

        except Exception as e:
            print("Error: There is a problem with getting the next file number - \n" + e.args[0] )
            exc_type, exc_obj, exc_tb = sys.exc_info()
            tb = traceback.extract_tb(exc_tb)[-1]
            print(exc_type, tb[2], tb[1])
#-----------------------------------------       
