 #move svg into send folder

import os
import shutil
import sys
from svg_to_instruction import robot_convert

# srcfile = "../../svg/banana.jpg_SVG1.svg"
# dstroot = "../../network/send/image.svg"

# shutil.copy(srcfile, dstroot)

robot_convert("/var/lib/tomcat8/webapps/ROOT/svg/banana.jpg_SVG1.svg")


