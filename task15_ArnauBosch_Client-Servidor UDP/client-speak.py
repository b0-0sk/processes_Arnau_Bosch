# Echo client program
import socket

HOST = "localhost"    # The remote host
PORT = 50007              # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
  
  m = raw_input('Introduce algo: ')
  s.sendto(m, (HOST, PORT))
  
  if "bye" in m:
    break
s.close()
    