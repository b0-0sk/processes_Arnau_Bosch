# Echo server program
import socket
import time
from time import sleep

HOST = 'localhost'                 # Symbolic name meaning all available interfaces
PORT = 50008              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

conn,addr = s.accept()
conn.sendall("Conectat")


while True:

  data = conn.recv(1024)
  
  if "bye" in data:
    s.sendall("Desconectat")
    sleep(1)
    s.close()
    break
  else:
    print data
  
