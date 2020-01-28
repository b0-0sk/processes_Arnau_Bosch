# Echo server program
import socket
import time
from time import sleep

HOST = ''                 # Symbolic name meaning all available interfaces
PORT = 50007              # Arbitrary non-privileged port
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))


while True:
  data, addr = s.recvfrom(1024) # buffer size is 1024 bytes
  print addr, data
  if "bye" in data:
    print "dew"
    sleep(1)
    s.close()
    break