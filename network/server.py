<<<<<<< HEAD
import socket
from pathlib import Path
import os
import datetime
import time
import atexit

def closeConnection(sock):
    try:
        sock.shutdown(socket.SHUT_RDWR)
    except:
        pass
    try:
        sock.close()
    except:
        pass

def newConnection():

    s = socket.socket() # new socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows faster reconnects
    host = socket.gethostname()
    port = 3774
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
                c.settimeout(1)
                if not (c.recv(1024)):
                    print("## Socket disconnected! ##")
                    c.settimeout(None)
                    closeConnection(c)
                    return
            except Exception as e:
                print(e)
                c.settimeout(None)
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
                    print("error transferring file. will reattempt in 3 seconds")
                    time.sleep(3)

while True:
    newConnection()
=======
import socket
from pathlib import Path
import os
import datetime
import time
import atexit

def closeConnection(sock):
    try:
        sock.shutdown(socket.SHUT_RDWR)
    except:
        pass
    try:
        sock.close()
    except:
        pass

def newConnection():

    s = socket.socket() # new socket object
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # allows faster reconnects
    host = socket.gethostname()
    port = 3774
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
                c.settimeout(1)
                if not (c.recv(1024)):
                    print("## Socket disconnected! ##")
                    c.settimeout(None)
                    closeConnection(c)
                    return
            except Exception as e:
                print(e)
                c.settimeout(None)
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
                    print("error transferring file. will reattempt in 3 seconds")
                    time.sleep(3)

while True:
    newConnection()
>>>>>>> 852b0405eb1025a2ed2c4da5c57543a82f621ee7
    # every time connection is lost, we attempt to reconnect