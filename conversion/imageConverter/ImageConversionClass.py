import numpy as np
import cv2
import matplotlib.pyplot as plt
import svgwrite
import os, sys, ntpath, traceback

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
                "SVG: %s \n" % (self.origImg, self.svgPath))
            
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
            imgOriginal = cv2.imread(image, 1)  # read in image original colors
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
            imgGray = cv2.imread(image, 0)  # read in image grayscale
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
            # properties
            BLUR = 15               # blur size
            DILATE = 8
            ERODE = 8
            THRESH1 = 15
            THRESH2 = 180
            COLOR = (1.0, 1.0, 1.0) # mask color

            # using canny, dilate and erode together to detect edges
            if (len(image.shape) == 3):
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
            else: gray = image
            
            edges = cv2.Canny(gray, THRESH1, THRESH2)
            edges = cv2.dilate(edges, None)
            edges = cv2.erode(edges, None)

            c_info = []

            # finding contours
            contours, hierarchy = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

            for c in contours:
                c_info.append((c, cv2.isContourConvex(c), cv2.contourArea(c),))

            # sorting contours based on area
            c_info = sorted(c_info, key=lambda c: c[2], reverse=True)

            # idea is to draw an empty mask
            # and drawing a filled polygon of largest contour
            # on it
            max_contour = c_info[0]
            image_mask = np.zeros(edges.shape)
            cv2.fillConvexPoly(image_mask, max_contour[0], (255))

            # smoothing the mask
            image_mask = cv2.dilate(image_mask, None, iterations=DILATE)
            image_mask = cv2.erode(image_mask, None, iterations=ERODE)
            
            # applying gaussian blur to the mask
            image_mask = cv2.GaussianBlur(image_mask, (BLUR, BLUR), 0)
            mask_stack = np.dstack([image_mask] * 3)
            mask_stack = mask_stack.astype('float32') / 255.0
            image = image.astype('float32') / 255.0

            # blending original image with the mask
            masked = (mask_stack * image) + ((1 - mask_stack) * COLOR)
            masked = (masked * 255).astype('uint8')

            # rewriting image back
            #cv2.imwrite(formatted_path, masked)

            print("Mask: ", len(masked.shape)) 

            return masked

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
            edgeImage = cv2.dilate(edgeImage, None)
            edgeImage = cv2.erode(edgeImage, None)
            return edgeImage
        
        except Exception as e:
            print("Error: There is a problem with getting the edges with Canny - \n" + e.args[0] ) 
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

            return edgeImage
        
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
            edgeImage = self.getImageReady(gray)
    
            return edgeImage
        
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
    # parameters: image, range for x, range for y, line thickness in pixel
    # return: old contour image, new contour image, points for new contours
    def createContours(self, image, lineThickness = 2):
        try:
            contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   # find countour
            print("Found %d objects in intial contour list." % len(contours))                       # length of the contour list

            height, width = image.shape[:2]     # get image size
            
            pointC = []                         # new set of points

            self.filterPoints(contours, pointC,0,0) # filter points - no range

            # filter points by size of image
            if (height <= 800):                     # if height is less than or equal to 800
                self.filterPoints(contours, pointC) # filter points
            elif (height < 1600):                   # if height is less than 1600
                self.filterPoints(contours, pointC, 10, 10, 600) # filter points
            else:                                   # for images greater than or equal to 1600
                self.filterPoints(contours, pointC, 15, 15, 1200) # filter points
                
            newContours = np.array([pointC])                    # make a numpy array with the new points for contour image

            # make svg of contour
            nameSVG = str(ntpath.basename(self.origImg)) + "_SVG"    # set filename for svg file
            path = self.svgPath                                 # set directory path for svg file
            self.drawSVG(newContours, height, width, nameSVG, path) # draw it in the svg

            #don't sort - doesn't work?
            #vec = np.sort(np.array([pointC]))

            # draw the contour images
            blankCanvas1 = 255*np.ones((height, width, 3), np.uint8)                                        # make blank canvas
            blankCanvas2 = 255*np.ones((height, width, 3), np.uint8)                                        # make blank canvas
            imageContourOld = cv2.drawContours(blankCanvas1, contours, -1, (0,255,0), lineThickness)        # draw the contour image with old point
            imageContourNew = cv2.drawContours(blankCanvas2, newContours, -1, (0,255,0), lineThickness)     # draw the contour image with new point

            self.showTwoImages(imageContourOld, imageContourNew, "Contour Old", "Contour New")

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
    # filter contour points based on minimum areas and specific range of x and y coordinates
    # range is used to filter out some points in contour image:
    #   smaller range - more points, more lines in the image 
    #   larger range - less points, less lines in the image
    # parameters: set of points that make up contour, range for x, range for y, minimum contour area accepted 
    def filterPoints(self, contourPoints, newContourPoints, rangeForX = 5, rangeForY = 5, minContourArea = 200):
        try:

            contoursToDelete = [] # list of indexes of contours to delete
            print("Inital Number of Objects: ", len(contourPoints))
            origObjCount = self.countPoints(contourPoints)
            
            # look for the contours that don't fit the minimum area requirement
            for i in range(len(contourPoints)):
                
                contourArea = cv2.contourArea(contourPoints[i]) # find contour area
                
                # we can use this epsilon instead of fixed 2 in approxPolyDP
                epsilon = 0.001 * cv2.arcLength(contourPoints[i], False)
                # approx = cv2.approxPolyDP(c, epsilon, True)
                
                # applying polygon approximation on the current contour.
                approx2 = cv2.approxPolyDP(contourPoints[i], 2, False)
                
                # if there are extact four points in the contour, most likely it a sqaure
                # so ignoring such contour
                # if the contour area is less than the minimum contour area
                if(contourArea < minContourArea) or len(approx2) == 4:
                    contoursToDelete.append(i)  # save the index of that contour

            # delete all the contours that don't meet the area requirement
            contourPoints = np.delete(contourPoints, contoursToDelete)
            
            # set up things for processing points in contour
            x = y = []
            xsave = -1
            ysave = -1
            count = 0

            # printing current state of countour points
            #self.print_contours(contourPoints)

            # process points in contour - get the last two points
            startEndPoint = np.array(self.getStartEndPoints(contourPoints)) # change into a numpy array

            # sort the contour element
            orderElement = []
            for i in np.argsort(startEndPoint[::2,0]):
                orderElement.append(i)
                #print("Sort", i)
            #print(orderElement)

            #print(contourPoints[0])
            contourPoints = contourPoints[orderElement] # order the elements

            #print("Here")      

            startEndPoint = self.getStartEndPoints(contourPoints) # get the start and end points again
   
                            
            # process points in contour - remove some points based on x and y ranges
            for i in range(len(contourPoints)):

                if i == 0: continue # gets rid of the first contour element

                for j in range(len(contourPoints[i])):
                                            
                    #for k in contourPoints[i][j]:
                    xget = contourPoints[i][j][0][0] #get x
                    yget = contourPoints[i][j][0][1] #get y
                    #print("X Found: ", xget)
                    #print("Y Found: ", yget)
##                    xsave = xget
##                    ysave = yget
##                    newContourPoints.append([xget,yget])
                    
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
                                #print("got here - yes")
                                xsave = xget
                                ysave = yget
                                newContourPoints.append([xget,yget])
                                count+=1

                                
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
    # parameters: the list of sequence of contour points, height of image, width of image, image name, directory of svg file
    def drawSVG(self, contourPoints, height, width, name = "contour_SVG", path = "./"):
        try:

            path = str(path)

            # make sure the path is ready
            if "/" in path:
                if not path.endswith("/"):
                    path = path + "/"
            elif "\\" in path:
                if not path.endswith("\\"):
                    path = path + "\\"
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
            number = str(self.getNextFileNumber(path, name, extension)) # get the next file number
            location = str(path) + str(name) + str(number) + str(extension)
            #create a svg file
            #print("SVG to: ", str(path+name+number+extension))
            dwg = svgwrite.Drawing(location, size=(width, height))
            shapes = dwg.add(dwg.g(id="shapes", fill="none"))

            #add a starting point
            shapes.add(dwg.line(start = ('0',str(height)), 
                             end = (str(contourPoints[0][0][0]),str(contourPoints[0][0][1])), 
                             stroke=svgwrite.rgb(10, 10, 16, "%")
            ))
            
            #interatively write points into the svg file
            lengthOfTheList = len(contourPoints[0]) - 1
            for x in range(lengthOfTheList):
                #print(contourPoints[0][x][0],contourPoints[0][x][1],contourPoints[0][x+1][0],contourPoints[0][x+1][1])
                shapes.add(dwg.line(start = (str(contourPoints[0][x][0]), str(contourPoints[0][x][1])), 
                                 end = (str(contourPoints[0][x+1][0]),str(contourPoints[0][x+1][1])), 
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
