#this is a standard multi-threaded tcp server.

import socket
import threading

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port)) #ip and port we want our server to listen on

server.listen(5) #server starts with max connections to 5 
print("[*] Listening on %s:%d" % (bind_ip, bind_port))

#this is our client-handling thread
def handle_client(client_socket):
    #req that our client sends
    req = client_socket.recv(1024)
    print("[*] Received: %s" % req)
    
    #send an acknowledgement packet
    client_socket.send("ACK!")
    client_socket.close()

while True:
    client, addr = server.accept() #the client variable contains the client socket that connected to this server
    print(f"[*] Accepted connection from {addr[0]}:{addr[1]}")

    #start our client handle thread to handle incoming data
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()
    #everytime a client connects a new thread is made that handles the connected client socket
    