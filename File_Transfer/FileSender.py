import socket
import sys

port = 2500
s = socket.socket()
host = ""
s.bind((host, port))
s.listen(1)

print("Waiting for connection...")

c_sock, addr = s.accept()
print('Connected from', addr)

msg = c_sock.recv(1024)
print(msg.decode())

filename = input('Filename to send(c:/test/sample.bin):') #'\' 대신 '/' 사용하여 경로 구분, 파일 경로를 지정
print(f"Sending '{filename}'")
fn = filename.split('/') #'filename'을 /로 분리하여 리스트로 저장\

c_sock.sendall(fn[-1].encode()) # 'fn[-1]' 즉 파일이름만을 전송

with open(filename, 'rb')as f:
    c_sock.sendfile(f, 0) #sendfile()을 쓰거나 (f.read() and sendall()) 사용

    #data = f.read()
    #while data:
        #c_sock.sendall(data)
        #data = f.read()

print("Sending complete")
c_sock.close()
