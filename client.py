import socket
import pickle

HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))

while True:
    full_msg = b""
    new_msg = True
    while True:
        msg = s.recv(16)
        if new_msg:
            print(f'new message length: {msg[:HEADER_SIZE]}')
            msglen = int(msg[:HEADER_SIZE])
            new_msg = False

        full_msg += msg

        if len(full_msg)-HEADER_SIZE == msglen:
            print("full msg recvd")
            print(full_msg[HEADER_SIZE:])

            dict = pickle.loads(full_msg[HEADER_SIZE:])
            print(dict)

            new_msg = True
            full_msg = b''

print(full_msg)
