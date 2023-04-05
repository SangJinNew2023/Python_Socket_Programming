class TCPServer:
    def __init__(self, port): #소켓 생성 및 바인딩 후 대기
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(5)

    def Accept(self): #연결 허용 후 client 소켓 및 주소 반환
        self.c_sock, self.c_addr = self.sock.accept()
        return self.c_sock, self.c_addr

if __name__=='__main__':
    sock = TCPServer(2500)
    c.addr = sock.Accept()
    print('received message:', c.recv(1024).decode())
    msg = "Hello Client"
    c.send(msg.encode())
    c.close