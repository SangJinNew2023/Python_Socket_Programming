from socket import *
import random

BUFFER = 1024
port = 2500
server = 'localhost'

c_sock = socket(AF_INET, SOCK_DGRAM)
c_sock.connect((server, port)) #UDP설정에서도 connect(),send(), recv() 사용가능, 연결(논리적, 가상)

for i in range(10):
    delay = 0.1
    data = 'Hello message'
    print('_______________')

    while True:
        c_sock.send(data.encode()) #서버로 메세지 전송
        print('Waiting up to {} seconds for a reply'.format(delay))
        c_sock.settimeout(delay) #settimeout(delay)에서 delay 값만큼 timeout 설정
        try:
            data = c_sock.recv(BUFFER) #데이터 수신을 0.1초 동안 기다림
        except timeout: #예외 발생시 dealy 값을 2배씩 늘리고 2.0에 도달하면 break
            delay *= 2
            if delay > 2.0:
                break
        else:
            print('Response', data.decode()) #data='ACK'
            break