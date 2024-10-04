import socketserver
import time


class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        conn = self.request
        while True:
            data = conn.recv(1024).decode('utf-8')
            conn.send(data.upper().encode('utf-8'))
            time.sleep(2)


server = socketserver.ThreadingTCPServer(('127.0.0.1',9000), MyServer)
server.serve_forever()