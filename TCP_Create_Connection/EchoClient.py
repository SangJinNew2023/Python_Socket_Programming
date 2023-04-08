import socket
import sys

sock = socket.create_connection(('localhost', 2500)) #TCP 소켓 생성과 연결

message = "Client Message"
print('sending {}'.format(message))
sock.sendall(message.encode()) #송신 버퍼를 거치지 않고 데이터 모두 전송

data = sock.recv(1024)
print('received {}'.format(data.decode()))
print('closing socket')
sock.close()