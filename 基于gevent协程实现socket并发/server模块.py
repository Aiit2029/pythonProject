from gevent import monkey
monkey.patch_all()
import socket
import gevent

def func(conn):
    while True:
        data = conn.recv(1024).decode('utf-8')
        info = data.upper().encode('utf-8')
        conn.send(info)

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen()

while True:
    conn, addr = sk.accept()

    gevent.spawn(func,conn)

