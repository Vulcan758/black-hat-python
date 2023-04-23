import socket

target_host = "https://google.com"
target_port = 80

#creating the client socker
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#^ AF_INET means that we will be using a standard IPv4 address or hostname
# SOCK_STREAM means that this will be a TCP client


#connecting the client
client.connect((target_host, target_port))

#sending data
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

#receiving data
response = client.recv(4096)
print(response)

