import socket
import time
from threading import Thread

sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen(5)


def html(conn):
    with open('test.html', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

def css(conn):
    with open('test.css', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

def js(conn):
    with open('test.js', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()

def ioc(conn):
    with open('../day2/jd.ico', 'rb') as f:
        data = f.read()
    conn.send(data)
    conn.close()






while True:
    conn,addr = sk.accept()
    from_b_msg = conn.recv(1024)
    str_data = from_b_msg.decode('utf-8')

    path = str_data.split('\r\n')[0].split(' ')[1]
    # print(path)
    url_partneer =[('/',html),('/test.css',css),('/test.js',js),('/favicon.ioc',ioc)]

    # print(str_data)
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    for i in url_partneer:
        if path == i[0]:
            t = Thread(target=i[1],args=(conn,))
            t.start()