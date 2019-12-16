#!/usr/bin/env python3

import socket
from _thread import *
import threading 
import sys

HOST = '127.0.0.1'  # localhost, that is, only clients on the host can connect to this server
                    # if left empty, the server will accept connections from all available interfaces
PORT = int(sys.argv[1]) # Port to listen on (non-privileged ports are > 1023)

def connection(c):
    while True:
        data = conn.recv(1024)
        if not data:
            break # probably remove this too and add the functions to the log
##        print(data)

    # when the socket does not recveive any data, the connection was closed by the cient
    c.close()


# AF_INET is IPv4, and a SOCK_STREAM specify that the socket is TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT)) # used to associate the socket with a specific interface and port number
print('Listening...')
while True:
    s.listen()
    conn, addr = s.accept() # returns a new socket object
    # conn is a socket object different from the s socket above
    # for each accepted connection, a new socket is created
    print('Connected by', addr)

    # function to call and list of arguments
    start_new_thread(connection, (conn,))

s.close()
