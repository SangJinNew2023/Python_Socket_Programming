class TCPServer:
    def __init__(self, port): #소켓 생성 및 바인딩 후 대기
        import socket
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.bind(('', port))
        self.sock.listen(5)
        self.connected= False

    def disconnect(self):
        self.connected = False
        self.c_sock.close()

    def accept(self): #연결 허용 후 client 소켓 및 주소 반환
        self.c_sock, self.c_addr = self.sock.accept()
        self.connected = True
        return self.c_sock, self.c_addr

    def send(self, msg):
        if self.connected:
            self.message = msg
            self.c_sock.send(self.message.encode())
            return True
        else:
            return False

    def receive(self, r_sock=None):
        if not r_sock:
            r_sock = self.c_sock
        try:
            data = r_sock.recv(1024)
            if not data:
                self.disconnect()
                return None
            return data.decode()
        except:
            self.disconnect()
            return None
