import socketserver


class MyTheadTcpServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    """Наследование от  socketserver.ThreadingMixIn позволяет обрабатывать клиентов в разных потоках"""

    pass


class MyTcpServer(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request.recv(1024).strip()
        print("Addres: {}".format(self.client_address[0]))
        print("Data: {}".format(data.decode()))
        self.request.sendall(data)


if __name__ == "__main__":
    with MyTheadTcpServer(("127.0.0.1", 8001), MyTcpServer) as server:
        server.serve_forever()
