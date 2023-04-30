import socket

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

# bind to local address and specified port
host = ''
port = 40674
s.bind((host, port))
print(f"Socket bound to {port}")

# listen for incoming connections
s.listen(5)
print("Socket listening...")

while True:
    # accept a new connection from a client
    c, addr = s.accept()
    print(f"Got connection from {addr}")

    # send a message to the client
    message = "Thank you for connecting"
    c.send(message.encode())

    # close the connection with the client
    c.close()

