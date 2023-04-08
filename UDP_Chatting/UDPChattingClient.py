import socket

BUFFSIZE = 1024
port = 2500

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
ip_addr = input("Server IP address:")
if ip_addr =='':
    ip_addr = 'localhost'
addr = (ip_addr, port)

while True:
    msg = input("<-")
    sock.sendto(msg.encode(), addr)
    print("->", end='')
    data, addr = sock.recvfrom(BUFFSIZE)
    print(data.decode())
