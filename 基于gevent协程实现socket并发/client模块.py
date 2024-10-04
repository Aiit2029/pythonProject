from threading import Thread

from gevent import monkey
monkey.patch_all()
import socket
import gevent

def func():
    sk = socket.socket()

    sk.connect(('127.0.0.1', 9000))
    while True:
        sk.send(b'hello world')
        data = sk.recv(1024).decode('utf-8')
        print(data)

if __name__ == '__main__':
    for i in range(500):
        Thread(target=func).start()



