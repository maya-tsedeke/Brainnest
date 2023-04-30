import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# specify the server address and port to connect to
host = '127.0.0.1'
port = 40674

# connect to the server
s.connect((host, port))

# receive a message from the server
message = s.recv(1024)
print(message.decode())

# close the connection with the server
s.close()
