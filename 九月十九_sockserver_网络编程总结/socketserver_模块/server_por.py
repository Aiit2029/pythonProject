import socket
import time

sk = socket.socket()
sk.bind(('127.0.0.1',9000))

sk.listen()
while True:
    conn,_ = sk.accept()
    while True:
        data = conn.recv(1024).decode('utf-8')

        conn.send(data.upper().encode('utf-8'))
        time.sleep(1)
