import socket

sk = socket.socket()
sk.bind(('127.0.0.1', 9000))
sk.listen(1)
while 1:
    conn,addr = sk.accept()
    ret = conn.recv(1024)
    print(ret.decode('utf-8'))
    conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
    with open('socket_html.html', mode='rb') as f:
        data = f.read()
    conn.send(data)
# conn.close()
# sk.close()