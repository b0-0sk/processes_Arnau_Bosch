# -*- encoding: utf-8 -*-

# Tcp Chat server

import socket, select
from threading import Thread

#Function to broadcast chat messages to all connected clients
def broadcast_data (sock, message):
    #Do not send the message to master socket and the client who has send us the message
    for socket in CONNECTION_LIST:
        if socket != server_socket and socket != sock :
            try :
                socket.send(message)
            except :
                # broken socket connection may be, chat client pressed ctrl+c for example
                socket.close()
                CONNECTION_LIST.remove(socket)

if __name__ == "__main__":
    
    # List to keep track of socket descriptors
    CONNECTION_LIST = []
    USERNAMES = []
    
    RECV_BUFFER = 4096 # Advisable to keep it as an exponent of 2
    PORT = 9999
    HOST=''
    
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # this has no effect, why ?
    server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    server_socket.bind((HOST, PORT))
    server_socket.listen(3)

    # Add server socket to the list of readable connections
    
    def add_con():
        
        MESSAGE_USERNAME = 'Server : Introdueix el teu nom\r\n'
        while True:
            
            CONNECTION_LIST.append(server_socket.accept())
            if (len(USERNAMES) == 0):
                    CONNECTION_LIST[-1][0].sendto(MESSAGE_USERNAME, CONNECTION_LIST[-1][1])    
                    username = CONNECTION_LIST[-1][0].recv(1024)
                    USERNAMES.append((username,CONNECTION_LIST[-1][1][1]))
                    
            else:
                for user in CONNECTION_LIST:
                    for username in USERNAMES:
                        if user[1][1] != username[1]:
                            user[0].sendto(MESSAGE_USERNAME,user[1])
                            u = user[0].recv(1024)
                            USERNAMES.append(u,user[1][1])
                            
            Thread(target=sendTo,args=(CONNECTION_LIST[-1][0],CONNECTION_LIST[-1][1])).start()
                        
    
    print ("Chat server started on port " + str(PORT))
    
    def sendTo(clientSocket,addr):
        while True:
            m = clientSocket.recv(1024)
            for user in CONNECTION_LIST:
                if addr[1] != user[1][1]:
                    for username in USERNAMES:
                        if addr[1] == username[1]:
                            user[0].sendto(str(username[0]+": " + m), addr)
    
            if m[:-1].lower() == "bye":
                for i in range(len(CONNECTION_LIST)):
                    if addr[1] == CONNECTION_LIST[i][1][1]:
                        CONNECTION_LIST.pop(i)
                        break
                for i in range(len(USERNAMES)):
                    if addr[1] == USERNAMES[i][1]:
                        USERNAMES.pop(i)
                        break
                break

thread = Thread(target = add_con(), args = ( ))

thread.start()



thread.join()
s.close()