import socket
from pathlib import Path
import os
import time
import atexit

def newConnection():

    s = socket.socket() # new socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows faster reconnects
    host = socket.gethostname()
    port = 377
    s.bind((host,port))
    print("now listening on", host, port)
    s.listen()

    while True: # wait for robot to connect
        c, addr = s.accept()
        print("connection at", addr)
        print("listening for file at send/script.py")
        listenPath = Path("send/script.py")
        while True:
            try: # check if client disconnect
                c.send(bytes("","UTF-8")) 
            except socket.error: 
                print('client disconnected')
                try:
                    c.shutdown(socket.SHUT_RDWR)
                except:
                    pass
                try:
                    c.close()
                except:
                    pass
                return
            if listenPath.is_file(): # check if there is file to send
                try:
                    print("file detected, attempting to send")
                    f = open('send/script.py','rb')
                    l = f.read(1024)
                    while (l):
                        c.send(l)
                        l = f.read(1024)
                    c.send(b"EOD") # end of data indicator
                    print("transfer complete, deleting input file")
                    f.close()
                    os.remove("send/script.py")
                except:
                    print("error reading file. will reattempt in 1 second")
                    time.sleep(1)

while True:
    newConnection()
    # every time connection is lost, we attempt to reconnect