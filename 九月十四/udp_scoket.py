import socket

sk = socket.socket(type=socket.SOCK_DGRAM)
sk.bind(('120.243.43.198',9001))

while True:
    data,addr = sk.recvfrom(1024)
    data = data.decode('utf-8')
    # data = 'r'
    if data.upper() != 'R' and data.upper() != 'T':
        print(data)
        continue
    elif data.upper() == 'R':
        break
    elif data.upper() == 'T':
        while True:
            info = input(">>>").encode('utf-8')
            if info.upper() != 'S':
                sk.sendto(info, addr)
                continue
            elif info.upper() == 'S':
                sk.sendto(info, addr)
                break

