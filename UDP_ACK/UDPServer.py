from socket import *
import random

BUFFER = 1024
port = 2500

s_sock = socket(AF_INET, SOCK_DGRAM)
s_sock.bind(('', port))
print('Listening')

while True:
    data, address = s_sock.recvfrom(BUFFER)
    if random.randint(1, 10) < 4: #30%의 데이터 손실이 발생된것을 구현
        print('Packet from {} lost'.format(address))
        continue
    print('Message is {!r} from {}'. format(data.decode(), address))
#{!r}은 repr()함수와 같은 기능 data 값을 ''로 감싼 형태로 보여줌

    s_sock.sendto('ACK'.encode(), address)