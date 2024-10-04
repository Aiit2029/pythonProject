import socket

sk = socket.socket()
sk.connect(('192.168.1.114',9000))
msg = sk.recv(10240)
print(msg.decode('utf-8'))
sk.send(b'888')


sk.close()