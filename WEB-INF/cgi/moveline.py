# this code moves correct script.py into send folder on button click

import os
import shutil

# determine the appropriate file to copy here
srcfile = "../../robot/examples/Line.py"
# path to the send folder
dstroot = "../../network/send/line.py"

#assert not os.path.isabs(srcfile)
#dstdir =  os.path.join(dstroot, os.path.dirname(srcfile))
shutil.copy(srcfile, dstroot)

