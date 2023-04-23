import socket

target_host = "127.0.0.1"
target_port = 80

client = socket.socket(socket.AF_INET, socket.SOCK_DRGAM)

client.sendto("eyhfefe", (target_host, target_port))

#UDP is a connectionless protocol so we dont call connect()

data, addr = client.recvfrom(4096)

print(data)