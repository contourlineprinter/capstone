import numpy as np
import cv2
import matplotlib.pyplot as plt

class ImageConversion:    
    "Class to perform image conversion to contour, svg, and robot instructions\n"
#-----------------------------------------
    # constructor
    # parameters: orignal image name, orignal image path
    def __init__(self, origImgName, origImgPath):
        if isinstance(origImgName, str) and isinstance(origImgPath, str):
            self.origImgName = origImgName
            self.origImgPath = origImgPath
        else:
            print("Error: There is a problem with the input(s).")
#-----------------------------------------
    # print the image information
    def printImgInfo(self):
        try:
            print("Image Name: %s\n" \
                "Image Path: %s \n" % (self.origImgName, self.origImgPath))
            
        except Exception:
            print("Error: There is a problem printing out the information.")
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
#-----------------------------------------     
    # show image
    # parameters: name of the window, image to show
    def showImage(self, title, image):
        try:
            cv2.namedWindow(title, cv2.WINDOW_NORMAL)   # create a resizable window
            cv2.imshow(title, image)                    # show the image inside the window
            
        except Exception as e:
            print("Error: There is a problem with showing the image - \n" + e.args[0] )    
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
#-----------------------------------------
    # preprocess the image to find better edges
    # parameter: grayscale image to preprocess (note: image has be this type to work)
    # return: preprocessed image
    def getImageReady(self, image):
        try:
            # Gaussian Blur
            blurImage = cv2.GaussianBlur(image,(5,5),0)
            self.showImage("Blur Image", blurImage)
                
            # adaptive threshold
            # image, max pixel value, type of threshold,
            # neighborhood parameter indicating how far or what the localization of where the adaptive thresholding will act over,
            # mean subtraction from the end result
            # only the threshold picture
            adaptThresImage = cv2.adaptiveThreshold(blurImage, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 295, 1)
            self.showImage("Threshold Image", adaptThresImage)

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
                iterationValue = 5                  # do 6 iteration
                print ("height >= 1600")

            # taking a matrix of size n,n as the kernel 
            kernel = np.ones((kernelSizeRow, kernelSizeCol), np.uint8)            

            #dilation
            dilationImage = cv2.dilate(adaptThresImage, kernel, iterations = iterationValue)
            self.showImage("Dilation Image", dilationImage)

            #erosion
            erosionImage = cv2.erode(dilationImage, kernel, iterations = iterationValue)
            self.showImage("Erosion Image", erosionImage)

            return erosionImage
        
        except Exception as e:
            print("Error: There is a problem with preprocessing the image - \n" + e.args[0] ) 
#-----------------------------------------
    # find the edges using Canny edge detection
    # return: edge image
    def getEdges(self, image):
        try:
            edgeImge = cv2.Canny(image, 100, 200)
            return edgeImge
        
        except Exception as e:
            print("Error: There is a problem with getting the edges with Canny - \n" + e.args[0] ) 
#-----------------------------------------
    # find the contour of the image based on specific range of x and y coordinates
    # range is used to filter out some points in contour image:
    #   smaller range - more points, more lines in the image 
    #   larger range - less points, less lines in the image
    # parameters: image, range for x, range for y, line thickness in pixel
    # return: new contour image, old contour image
    def createContours(self, image, lineThickness = 2):
        try:
            contours, hierarchy = cv2.findContours(image, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)   # find countour
            print("Found %d objects in intial contour list." % len(contours))                       # length of the contour list

            height, width = image.shape[:2]     # get image size
            
            pointC = []                         # new set of points

            # filter points by size of image
            if (height <= 800):                     # if height is less than or equal to 800
                self.filterPoints(contours, pointC) # filter points
            elif (height < 1600):                   # if height is less than 1600
                self.filterPoints(contours, pointC, 10, 10, 600) # filter points
            else:                                   # for images greater than or equal to 1600
                self.filterPoints(contours, pointC, 15, 15, 1200) # filter points
                
            newContours = np.array([pointC])    # make a numpy array with the new points for contour image

            #don't sort - doesn't work?
            #vec = np.sort(np.array([pointC]))

            # draw the contour images
            blankCanvas1 = 255*np.ones((height, width, 3), np.uint8)                                        # make blank canvas
            blankCanvas2 = 255*np.ones((height, width, 3), np.uint8)                                        # make blank canvas
            imageContourOld = cv2.drawContours(blankCanvas1, contours, -1, (0,255,0), lineThickness)        # draw the contour image with old point
            imageContourNew = cv2.drawContours(blankCanvas2, newContours, -1, (0,255,0), lineThickness)     # draw the contour image with new point

            self.showTwoImages(imageContourOld, imageContourNew, "Contour Old", "Contour New")

            return imageContourNew, imageContourOld

        except Exception as e:
            print("Error: There is a problem with creating the contour image - \n" + e.args[0] ) 
#-----------------------------------------
    # filter contour points based on minimum areas and specific range of x and y coordinates
    # range is used to filter out some points in contour image:
    #   smaller range - more points, more lines in the image 
    #   larger range - less points, less lines in the image
    # parameters: set of points that make up contour, range for x, range for y, minimum contour area accepted 
    def filterPoints(self, contourPoints, newContourPoints, rangeForX = 8, rangeForY = 8, minContourArea = 200):
        try:
            contoursToDelete = [] # list of indexes of contours to delete
            
            print("Inital Number of Objects: ", len(contourPoints))

            # look for the contours that don't fit the minimum area requirement
            for i in range(len(contourPoints)):
                
                contourArea = cv2.contourArea(contourPoints[i]) # find contour area

                # if the contour area is less than the minimum contour area
                if(contourArea < minContourArea):
                    contoursToDelete.append(i)  # save the index of that contour

            # delete all the contours that don't meet the area requirement
            contourPoints = np.delete(contourPoints, contoursToDelete)
                
            print("Inital Number of Objects: ", len(contourPoints))
            
            # set up things for processing points in contour
            x = y = []
            xsave = -1
            ysave = -1
            count = 0

            # process points in contour - remove some points based on x and y ranges
            for i in contourPoints:
                for j in i:
                    for k in j:
                        xget = k[0] #get x
                        yget = k[1] #get y
                        #print(xget)
                        #print(yget)

                        # if x and y found is within range of saved x and y, don't save it
                        if (abs(xsave-xget) <= rangeForX) or xget == xsave:
                            #print("got here - no")
                            continue
                        elif (abs(ysave-yget) <= rangeForY) or yget == ysave:
                            #print("got here - no")
                            continue
                        else:
                            #print("got here - yes")
                            xsave = xget
                            ysave = yget
                            newContourPoints.append(k)
                            count+=1

            print("Last saved x: %d" % xsave) # last save x
            print("Last saved y: %d" % ysave) # last save y
            print("Number of points in contour image: %d\n" % count) # number of points

        except Exception as e:
            print("Error: There is a problem with filtering the points - \n" + e.args[0] ) 
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
#imgConvert1.showImage("Gray Image", imgGray)

# show two images - original and gray
#imgConvert1.showTwoImages(img, imgGray, "Original Image", "Gray Image")

# get image ready
eroImg = imgConvert1.getImageReady(imgGray)
eroImg2 = eroImg.copy()

# find edges of image
edgeImg = imgConvert1.getEdges(eroImg)
imgConvert1.showImage("Edge Image", edgeImg)

# find contour lines using Canny edges
conImgEdge, conImgEdgeOld = imgConvert1.createContours(edgeImg)

# find contour lines not using Canny edges
conImgNoEdge, conImgNoEdgeOld = imgConvert1.createContours(eroImg2)

# compare three images - using Canny contour pic and not using Canny edge pic
#imgConvert1.showThreeImages(img, conImgEdge, conImgNoEdge, "Original Image", "Contour with Canny", "Contour without Canny")

# compare three images - original, edges found, final contour image 
imgConvert1.showThreeImages(img, conImgNoEdgeOld, conImgNoEdge, "Original", "Edges Found", "Final Contour")

# close all windows
imgConvert1.closeAllWindows()
