import socket

port =  2500
BUFFSIZE = 1024
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(("", port))
print("수신 대기 중")

while True:
    data, addr = sock.recvfrom(BUFFSIZE) #data,addr(상대방의 메시지, 주소)
    print("Received message:", data.decode()) #수신 데이터는 바이트형
    print(addr)

    sock.sendto(data,addr) #메시지 송신