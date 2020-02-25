# Echo server program
import socket
import time
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 40008             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(3)

CONNECTIONS = []

def accept ():
    while True:

        CONNECTIONS.append(s.accept())

        thread2 = threading.Thread(target=recived, args=(CONNECTIONS[-1],))
        thread2.daemon = True
        thread2.start()


def recived(conn):
    while True:
        m = conn[0].recv(1024)
        for x in CONNECTIONS:

            if x[0] != conn[0]:
                x[0].sendall(m)
        if len(m.split("-")) == 2:

            if m.split("-")[0] == 'Bye\n':
                conn[0].close()
                CONNECTIONS.remove(conn)
                break


thread = threading.Thread(target=accept)
thread.start()

thread.join()
s.close()
