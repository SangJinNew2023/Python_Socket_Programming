from socket import *

port = 2500
BUFSIZE = 1024

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost', port))
sock.listen(5)
print("Waiting for clients...")

conn, (remotehost, remoteport) = sock.accept()
print('connected by', remotehost, remoteport)
while True:
    try: #데이터 수신
        data = conn.recv(BUFSIZE)
    except:
        print("연결이 종료되었습니다.")
        conn.close() #연결 강제 종료
        break
    else:
        print(data.decode()) #수신데이터 출력
    try:
        conn.send(data)
    except:
        print("연결이 종료되었습니다.")
        conn.close()
        break

