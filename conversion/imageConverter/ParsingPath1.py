# Version of demo.py that takes file input as command line arguments

import numpy as np
import cv2
import matplotlib.pyplot as plt
import os, sys
from ImageConversionClass import ImageConversion

args = "/var/lib/tomcat8/webapps/ROOT/conversion/imageConverter/convertFileInput-reg.py" + \
       " /var/lib/tomcat8/webapps/ROOT/images/banana.jpg /var/lib/tomcat8/webapps/ROOT/svg/ 95 95 9"
#path = "./"

# print the letters
#for c in path:
#        print("Letter: ", c)

# split by // or /
slash = "/"
combineFile = ""
combineImage = ""
combineSVG = ""
xyRange = ""
ptsToSkip = ""
minArea = ""

startIndex = 0
imageFound = 0
svgFound = 0
xyRangeFound = 0
ptsToSkipFound = 0
minAreaFound = 0

svgDirFoundSub = 0
saveNextString = ""

# check for single or double slash
if "//" in args: slash = "//"
else: slash = "/"

splitPath = args.split(slash) # delimit arguments by slash

for i in splitPath:
        
        print("Splits: ", i)
##        
##        #combineFile = combineFile + i
##        print("\nCurrent: ", combineFile)
##
##        splitSpace = i.split(" ") #split by space
##        print("Split: ", splitSpace)
##
##        if splitSpace is not None:
##                
##                for j in splitSpace:
##
##                        print("\nSub Current: ", j)
##
##                        if svgDirFoundSub == 0 and j is not "":
##                                test = combineFile + j
##
##                        if svgDirFoundSub > 0 and j is not "":
##                                saveNextString = j
##                                        
##
##                        print("Test: ", test)
##                        
##                        # check to see if the image is found
##                        if imageFound == 0:
##                                print("File?: ", os.path.isfile(test)) # test to see if it's a file
##                                if not os.path.isfile(test):
##                                        if j is not splitSpace[len(splitSpace)-1]:
##                                                combineFile = test + " "
##                                        else: combineFile = test
##                                        print("sub - not a file")
##                                else:
##                                        imageFound = 1
##                                        combineImage = test
##                                        combineFile = ""
##                                        print("sub - is a file")
##                        elif svgFound == 0:
##                                print("Directory?: ", os.path.isdir(test)) # test to see if it's a directory
##                                if not os.path.isdir(test):
##                                        combineFile = test + " "
##                                        if j is not splitSpace[len(splitSpace)-1]:
##                                                combineFile = test + " "
##                                        else: combineFile = test
##                                        print("sub - not a dir")
##                                else:
##                                        combineFile = test + slash
##                                        print("sub - is a dir")
##                                        svgDirFoundSub = 1
##
##                        elif xyRangeFound == 0:
##                                print("XY Range Found ", test)
##                                        
##
##                        else: continue
##
##        print("\nAfter spaces: ", combineFile)
##                        
##        # check to see if the image is found
##        if imageFound == 0:
####                print("File?: ", os.path.isfile(combineFile)) # test to see if it's a file
##                if not os.path.isfile(combineFile):
##                        #print("not a file")
##                        combineFile = combineFile + slash
##                else:
##                        imageFound = 1
##                        combineImage = combineFile
##                        combineFile = ""
##                        #print("is a file")
##        elif svgFound == 0:
##        #or i is splitPath[len(splitPath)-1]:
####                print("Out")
####                print("Directory?: ", os.path.isdir(combineFile)) # test to see if it's a directory
##                if os.path.isdir(combineFile):
##                        svgFound = 1
##                        combineSVG = combineFile
##                        combineFile = ""
##                        svgDirFoundSub == 0
##                elif not os.path.isdir(combineFile) and svgDirFoundSub == 1:
##                        print("Got here")
##                        #print("A directory for svg cannot be found. Please try again.")
##                   
##        else:
##                print("else")
##                continue
       
print("\nImage: ", combineImage)
print("SVG: ", combineSVG)
print("XY Range: ", xyRange)
print("Points to Skip: ", ptsToSkip)
print("Minimum Area: ", minArea)
        

