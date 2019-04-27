import os, sys, ntpath, traceback

# parse the arguments to get the image and the svg folder for image conversion
# parameters: argument from the command line
# return: path or filename of the image, svg path
def parseArguments(args):
    
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
    savePreviousSVG = ""
    saveParameters = ""

    # check for single or double slash
    if "//" in args: slash = "//"
    else: slash = "/"

    splitPath = args.split(slash) # delimit arguments by slash

    for i in splitPath:
                    
        print("\nSplits: ", i)

##        if combineFile is None:
##                combineFile = i
##        else: combineFile = combineFile + i
        
        print("Current: ", combineFile)

        splitSpace = i.split(" ") #split by space
        print("Split: ", splitSpace)

        svgDirFoundSub = 0

        if splitSpace is not None:
                
            for j in splitSpace:
                                
                print("Sub Current: ", j)

                if combineFile is None and imageFound == 1 and svgFound == 0:
                    combineFile = slash
                    
                test = combineFile + j                                       
                print("Test: ", test)
        
                # check to see if the image is found
                if imageFound == 0:
                    print("File?: ", os.path.isfile(test)) # test to see if it's a file
                    if not os.path.isfile(test):
                        if j is not splitSpace[len(splitSpace)-1]:
                            combineFile = test + " "
                        else:
                            combineFile = test
                            print("sub - not a file")
                    else:
                        imageFound = 1
                        combineImage = test
                        combineFile = ""
                        print("sub - is a file")
                elif svgFound == 0 and imageFound == 1:
                    print("Directory?: ", os.path.isdir(test)) # test to see if it's a directory
                    if not os.path.isdir(test):
                        combineFile = test + " "
                        if j is not splitSpace[len(splitSpace)-1]:
                            combineFile = test + " "
                        else: combineFile = test
                            print("sub - not a dir")
                    elif os.path.isdir(test):
                        combineFile = test + slash
                        print("sub - is a dir")
                        svgDirFoundSub = 1
                    else: continue

            print("\nAfter spaces: ", combineFile)
                                    
            # check to see if the image is found
            if imageFound == 0:
##                print("File?: ", os.path.isfile(combineFile)) # test to see if it's a file
                if not os.path.isfile(combineFile):
                    #print("not a file")
                    combineFile = combineFile + slash
                else:
                    imageFound = 1
                    combineImage = combineFile
                    combineFile = ""
                    #print("is a file")
            elif svgFound == 0:
        #or i is splitPath[len(splitPath)-1]:
##                print("Out")
##                print("Directory?: ", os.path.isdir(combineFile)) # test to see if it's a directory
                if not os.path.isdir(combineFile) and svgDirFoundSub == 1:
                    print("SVG Not a File")
                    svgFound = 1
                    combineSVG = savedPreviousSVG
                    print("RESULT ", combineSVG)
                    combineFile = ""
                    savedParameters = i
                    splitSpace = i.split(" ") #split by space

                    for j in splitSpace:

                        if j is not None and str.isdigit(j):
                                
                            if xyRangeFound == 0:
                                print("XY Range Found")
                                print("xy ", j)
                                xyRange = j
                                xyRangeFound = 1
                                combineFile = ""
                                
                            elif ptsToSkipFound == 0:
                                print("Skip Points Found")
                                print("sk ", j)
                                ptsToSkip = j
                                ptsToSkipFound = 1
                                combineFile = ""
                                
                            elif minAreaFound == 0:
                                print("Min Area Found")
                                print("ma ", j) 
                                minArea = j
                                minAreaFound = 1
                                combineFile = ""
                            else: continue
                                    
                elif os.path.isdir(combineFile) and svgDirFoundSub == 1:
                    savedPreviousSVG = combineFile
                #print("A directory for svg cannot be found. Please try again.")
                else: continue
               
        else:
            print("else")
            continue
            print("-----------------------------------------------------------")

    if xyRange is None: xyRange = -1
    if ptsToSkip is None: ptsToSkip = -1
    if minArea is None: minArea = -1
    
    print("\nImage: ", combineImage)
    print("SVG: ", combineSVG)
    print("XY Range: ", xyRange)
    print("Points to Skip: ", ptsToSkip)
    print("Minimum Area: ", minArea)

    return str(combineImage), str(combineSVG), int(xyRange), int(skipPoints), int(minArea)

