import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST_NAME = socket.gethostname()
PORT = 12345

s.bind((HOST_NAME, PORT))

s.listen(4)

while True:
    client, address = s.accept()
    print("connected....", address)
