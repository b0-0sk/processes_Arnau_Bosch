# Echo server program
import socket
import time
import threading

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 40001             # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((HOST,PORT))
s.listen(3)

#CREA LLISTA
llistaCon = []

#ACEPTA CLIENTS
def acceptClient ():
    while True:
        llistaCon.append(s.accept())

        t2 = threading.Thread(target=recibir, args=(llistaCon[-1],))
        t2.daemon = True
        t2.start()


#INTERCEPTA MISSATGES
def recibir(conn):
    while True:
        m = conn[0].recv(1024)
        for x in llistaCon:

            if x[0] != conn[0]:
                x[0].sendall(m)
        if len(m.split(";")) == 2:
            #print m.split(";")[0]

            if m.split(";")[0] == 'Bye\n':
                conn[0].close()
                llistaCon.remove(conn)
                break

#CREA THREAD

t = threading.Thread(target=acceptClient)
t.start()

t.join()
s.close()
