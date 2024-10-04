import socket

sk = socket.socket(type=socket.SOCK_DGRAM)

server =('120.243.43.198',9001)
while True:
    info_send = input('>>>')
    if info_send.upper() == 'R':
        sk.sendto(info_send.encode('utf-8'), server)
        break
    elif info_send.upper() != 'R' and info_send.upper() !='T':
        sk.sendto(info_send.encode('utf-8'), server)
        continue
    elif info_send.upper() == 'T':
        sk.sendto(info_send.encode('utf-8'), server)
        while True:
            info_recv = sk.recv(1024).decode('utf-8')
            if info_recv.upper() == 'S':
                break
            elif info_recv.upper() != 'S':
                print(info_recv)
                continue
