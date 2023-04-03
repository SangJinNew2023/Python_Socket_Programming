import socket

port = int(input("Port No:"))
address = ("localhost", port)
BUFSIZE = 1024
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(address)
#송신
while True:
    msg = input("message to send:")
    try:
        n = s.send(msg.encode()) #메시지 전송
    except: #예외
        print("송신 연결이 종료되었습니다.")
        retry = input("계속?(y/n)")
        if retry == 'n': #연결 종료
            s.close()
            break
        else: #메세지 전송 계속
            continue
    else:
        print("{} byte sent".format(n)) #전송된 바이트 수
#수신
    try:
        data = s.recv(BUFSIZE) #데이터 수신
        if not data: #수신된 data가 빈 문자열이면 break, data=""은 정상적인 close의 경우
    except: #예외
        print("수신 연결이 종료되었습니다.")
        s.close()
        break
    else: #데이터 정상 수신
        print("Received message:%s" %data.decode())