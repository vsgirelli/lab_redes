import socket
import thread
import threading
import sys
import csv
from time import sleep, time

if len(sys.argv) is not 2:
    print("Wrong number of arguments: python3 server.py <server_port>")
    exit()


host = ''  # localhost, that is, only clients on the host can connect to this server
                    # if left empty, the server will accept connections from all available interfaces
port = int(sys.argv[1]) # Port to listen on (non-privileged ports are > 1023)
data = ['v']*64000
size = sys.getsizeof(' '.join(data))

val_read = 0

def log_thread():
    filename = 'log_' + str(port) + '.csv'
    with open(filename,'w') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        old_val = 0
        while True:
            val = val_read
            row = [0,0]
            row[0] = int(time())
            row[1] = val - old_val
            old_val = val
            writer.writerow(row)
            sleep(1)


# AF_INET is IPv4, and a SOCK_STREAM specify that the socket is TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port)) # used to associate the socket with a specific interface and port number

print('Listening...')
s.listen(1)

thread.start_new_thread(log_thread, ())

while True:
    conn, addr = s.accept() # returns a new socket object
    # conn is a socket object different from the s socket above
    # for each accepted connection, a new socket is created
    print('Connected by', addr[1])

    while True:
        rcv = conn.recv(size)
        if not rcv:
            break
        val_read += sys.getsizeof(rcv)

