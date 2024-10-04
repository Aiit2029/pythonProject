import socket
from multiprocessing import Process


def func(conn):
    while True:
        msg = conn.recv(1024).decode('utf-8')
        ret = msg.upper().encode()
        conn.send(ret)
    conn.close()

if __name__ == '__main__':
    sk = socket.socket()
    sk.bind(('127.0.0.1', 9999))
    sk.listen()
    while True:
        conn,addr = sk.accept()
        Process(target=func, args=(conn,)).start()
    sk.close()