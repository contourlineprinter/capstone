import socket
from pathlib import Path
import os

s = socket.socket() # new socket object
host = socket.gethostname()
print (host)
port = 377
s.bind((host,port))

print("now listening on", host, port)
s.listen()

while True: # wait for robot to connect
    c, addr = s.accept()
    print("connection at", addr)
    print("listening for file at send/script.py")
    listenPath = Path("send/script.py") # for final implementation
    listenPathLine = Path("send/line.py") # line for demo1
    listenPathCircle = Path("send/circle.py") # circle for demo1
    listenPathRectangle = Path("send/rectangle.py") # rectangle for demo1
    while True: # check if there is file to send
        if listenPath.is_file():
            print("file detected, attempting to send")
            f = open('send/script.py','rb')
            l = f.read(1024)
            while (l):
                c.send(l)
                l = f.read(1024)
            print("transfer complete, deleting input file")
            f.close()
            os.remove("send/script.py")
        if listenPathLine.is_file():
            print("file detected, attempting to send")
            f = open('send/line.py','rb')
            l = f.read(1024)
            while (l):
                c.send(l)
                l = f.read(1024)
            print("transfer complete, deleting input file")
            f.close()
            os.remove("send/line.py")
        if listenPathCircle.is_file():
            print("file detected, attempting to send")
            f = open('send/circle.py','rb')
            l = f.read(1024)
            while (l):
                c.send(l)
                l = f.read(1024)
            print("transfer complete, deleting input file")
            f.close()
            os.remove("send/circle.py")
        if listenPathRectangle.is_file():
            print("file detected, attempting to send")
            f = open('send/rectangle.py','rb')
            l = f.read(1024)
            while (l):
                c.send(l)
                l = f.read(1024)
            print("transfer complete, deleting input file")
            f.close()
            os.remove("send/rectangle.py")
