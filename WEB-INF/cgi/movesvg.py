 #move svg into send folder

import os
import shutil
import sys
from svg_to_instruction import robot_convert
# import cgi

# fs = cgi.FieldStorage()
# for key in fs.keys():
#	print (key, fs[key].value)

# srcfile = "../../svg/banana.jpg_SVG1.svg"
# dstroot = "../../network/send/image.svg"

# shutil.copy(srcfile, dstroot)

# scale = 1
# try:
#     #open the file we're writing to
#     with open('/var/lib/tomcat8/webapps/ROOT/next/scale.txt','r') as file:
#         num = float(file.read().trim())
# except:
#     pass # suppressing errors is not cool, but if there is an error, then use default scale = 1

robot_convert("/var/lib/tomcat8/webapps/ROOT/next/imageSVG.svg",scale)


