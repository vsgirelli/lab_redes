#!/usr/bin/env python3

import socket
import sys

HOST = '127.0.0.1'   # The server's hostname or IP address
                     # Testing in the lab, change for the other computer IP
PORT = int(sys.argv[1]) # The port used by the server
data = "Hello, world".encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    s.sendall(data)

print('Sent:', repr(data))
