#move svg into send folder

import os
import shutil

srcfile = "../../svg/banana.jpg_SVG1.svg"
dstroot = "../../network/send/image.svg"

shutil.copy(srcfile, dstroot)
