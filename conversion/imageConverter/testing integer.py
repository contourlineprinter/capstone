arg = " -1 90 -1"

arg = str(arg)
t = arg.split(" ")
a = "-1"
b = "-1"
c = "-1"

print(c)

##if int(c) < 0:
##
##    print("Value ", c)
slash = "/"
combineFile = ""
combineImage = ""
combineSVG = ""
xyRange = None
ptsToSkip = None
minArea = None

startIndex = 0
imageFound = 0
svgFound = 0
xyRangeFound = 0
ptsToSkipFound = 0
minAreaFound = 0

svgDirFoundSub = 0
savePreviousSVG = ""
saveParameters = ""
    
for i in t:
    
    if len(i) != 0:
        
        if xyRangeFound == 0:
            print("\nXY Range Found")
            print("xy ", i)
            xyRange = i
            xyRangeFound = 1
            combineFile = ""
        
        elif ptsToSkipFound == 0:
            print("\nSkip Points Found")
            print("sk ", i)
            ptsToSkip = i
            ptsToSkipFound = 1
            combineFile = ""
        
        elif minAreaFound == 0:
            print("\nMin Area Found")
            print("ma ", i) 
            minArea = i
            minAreaFound = 1
            combineFile = ""

        if isinstance(i, str):
            print("string")
            
        elif isinstance(i, int):
            print("integer")

print("\nImage: ", combineImage)
print("SVG: ", combineSVG)
print("XY Range: ", xyRange)
print("Points to Skip: ", ptsToSkip)
print("Minimum Area: ", minArea)
print("")    
if int(a) < 0: print("Value ", a)
if a is not None: print("Not None")
