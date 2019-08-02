import socket
import time
import pickle

HEADER_SIZE = 10


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established!")

    dict = {1: "Hey", 2: "There"}
    msg = pickle.dumps(dict)

    msg = bytes(f'{len(msg):<{HEADER_SIZE}}', "utf-8")+msg

    clientsocket.send(msg)
