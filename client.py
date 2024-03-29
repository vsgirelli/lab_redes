#!/usr/bin/env python3

import socket
import sys

if len(sys.argv) is not 3:
    print("Wrong number of arguments: python3 client.py <server_ip> <server_port>")
    exit()

host = sys.argv[1]  # The server's hostname or IP address
                    # Testing in the lab, change for the other computer IP
port = int(sys.argv[2]) # The port used by the server
data = ['v']*64000
data = ' '.join(data).encode()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))

while True:
    #t2 = time.time()
    s.send(data)
    #t3 = time.time()

    #throughput = size / (t3 - t2)
    #print(throughput)

s.close()
