# this code moves correct script.py into send folder on button click

import os
import shutil

# determine the appropriate file to copy here
srcfile = "/home/contourlineprinter/py_scripts/line.py"
# path to the send folder 
destroot = "/home/contourlineprinter/py_scripts/send"

assert not os.path.isabs(srcfile)
dstdir =  os.path.join(dstroot, os.path.dirname(srcfile))
shutil.copy(srcfile, dstdir)

