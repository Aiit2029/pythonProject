import socket
sk = socket.socket()
sk.bind(('127.0.0.1',9000))
sk.listen(5)
conn,addr = sk.accept()

from_b_msg = conn.recv(1024)
str_data = from_b_msg.decode('utf-8')
print(str_data)
conn.send(b'HTTP/1.1 200 OK\r\n\r\n')
conn.send(b'hello')