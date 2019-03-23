# this code moves correct script.py into send folder on button click

import os
import shutil

# determine the appropriate file to copy here
srcfile = "/var/lib/tomcat8/webapps/ROOT/robot/examples/Rectangle.py"
# path to the send folder
dstroot = "/var/lib/tomcat8/webapps/ROOT/network\ scripts/send"

assert not os.path.isabs(srcfile)
dstdir =  os.path.join(dstroot, os.path.dirname(srcfile))
shutil.copy(srcfile, dstdir)

