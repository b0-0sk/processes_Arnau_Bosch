# Echo client program
import socket

HOST = "localhost"    # The remote host
PORT = 50008          # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST,PORT))
          
while True:
  
  m = raw_input('Introduce algo: ')
  s.sendall(m)
  
  print s.recv(1024)
  #if "bye" in m:
 #   break
  
s.close()
    