import socket

#  套接字

# 为什么是套接字

'''
物理层     线路，在里面是01010101的高低电平传输
数据链路层    mac 地址 arp 地址解析协议  二层交换机   交换机交换的是什么：是双方的 ip地址   (由应用层到物理层)
网络层       ip 地址  分别为 ipv4 ipv6 路由 三层交换机  交换机本来在二层的，三层交换机 具有路由功能   
传输层       port  端口号   四层交换机  四层路由器 
应用层 表示层 会话层     使用的  应用   例如 瓦罗兰特  python
'''

sk = socket.socket()
sk.bind(('192.168.2.2', 9000))
sk.listen()
while True:
    conn, addr = sk.accept()
    while True:
        send_msg = input('>>>').strip()
        conn.send(send_msg.encode('utf-8'))
        msg = conn.recv(10240).decode('utf-8')
        print(msg)
    conn.close()

sk.close()

#  发送文件， 打开文件，读取内容，传到客户端，然后再打包成文件
#  发送文件   直接发送文件，那边直接读取文件