import socket
import time

sk = socket.socket()
sk.connect(('127.0.0.1',9999))

while True:
    sk.send(b'Hello')
    msg = sk.recv(1024).decode('utf-8')
    print(msg)
    time.sleep(1)

sk.close()