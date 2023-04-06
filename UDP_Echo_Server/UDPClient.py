import socket

BUFFSIZE = 1024
port = 2500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("송신 메시지:")
    sock.sendto(msg.encode(), ('localhost', port))
    data, addr = sock.recvfrom(BUFFSIZE)
    print("수신 메세지:", data.decode())