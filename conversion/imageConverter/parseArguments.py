import os, sys, ntpath, traceback

# parse the arguments to get the image and the svg folder for image conversion
# parameters: argument from the command line
# return: path or filename of the image, svg path
def parseArguments(args):
    
    slash = "/"
    combineFile = ""
    combineImage = ""
    combineSVG = ""
    startIndex = 0
    imageFound = 0
    svgFound = 0

    # check for single or double slash
    if "//" in args: slash = "//"
    else: slash = "/"

    splitPath = args.split(slash) # delimit arguments by slash

    for i in splitPath:
            
            print("Splits: ", i)
            
            #combineFile = combineFile + i
            print("\nCurrent: ", combineFile)

            splitSpace = i.split(" ") #split by space
            print("Split: ", splitSpace)

            if splitSpace is not None:
                    
                    for j in splitSpace:

##                                print("\nSub Current: ", j)

                            if j is not "":
                                    test = combineFile + j

##                                print("Test: ", test)
                            
                            # check to see if the image is found
                            if imageFound == 0:
##                                        print("File?: ", os.path.isfile(test)) # test to see if it's a file
                                    if not os.path.isfile(test):
                                            if j is not splitSpace[len(splitSpace)-1]:
                                                    combineFile = test + " "
                                            else: combineFile = test
##                                                print("sub - not a file")
                                    else:
                                            imageFound = 1
                                            combineImage = test
                                            combineFile = ""
##                                                print("sub - is a file")
                            else:
##                                        print("Directory?: ", os.path.isdir(test)) # test to see if it's a directory
                                    if not os.path.isdir(test):
                                            combineFile = test + " "
                                            if j is not splitSpace[len(splitSpace)-1]:
                                                    combineFile = test + " "
                                            else: combineFile = test
##                                                print("sub - not a dir")
                                    else:
                                            combineFile = test + slash
##                                                print("sub - is a dir")

##                print("\nAfter spaces: ", combineFile)
                            
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
            elif svgFound == 0 and i is splitPath[len(splitPath)-1]:
    ##                print("Out")
    ##                print("Directory?: ", os.path.isdir(combineFile)) # test to see if it's a directory
                    if os.path.isdir(combineFile):
                            svgFound = 1
                            combineSVG = combineFile
                            combineFile = ""
                    else:
                            print("A directory for svg cannot be found. Please try again.")
                            sys.exit(0)
            else: continue

    print("\nImage: ", combineImage)
    print("SVG: ", combineSVG)

    return combineImage, combineSVG
