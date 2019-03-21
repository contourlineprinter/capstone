import socket
from pathlib import Path
import os

s = socket.socket() # new socket object
host = "35.239.126.169"
port = 377
s.connect((host,port))

print("established connection to server on", host, port)

while True: # listen for new file data
    l = s.recv(1024)
    if (l):
        print("receiving file")
        f = open('receive/script.py','wb')
        while (l):
            f.write(l)
            l = s.recv(1024)
        f.close()
        print("file transfer complete")
