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

robot_convert("/var/lib/tomcat8/webapps/ROOT/next/imageSVG.svg",1)


