import socket, time, sys

BUFFSIZE = 1024 * 8


def Receiver():
    sock.bind(addr)

    file_name, client = sock.recvfrom(BUFFSIZE)  # 파일 이름 수신
    sock.sendto('ok'.encode(), client)  # 응답

    with open('/Users/photo/Downloads/' + file_name.decode(), "wb") as fp:
        print("파일 수신중...")
        while True:
            data = sock.recvfrom(BUFFSIZE)
            print("data", data)
            if not data[0]:  # 수신 완료
                break
            fp.write(data[0])  # 수신 데이터를 파일에 저장
    print("수신완료")


def Sender():
    file_name = input("File name to send:")
    sock.sendto(file_name.encode(), addr)  # 파일이름 전송
    resp, client = sock.recvfrom(BUFFSIZE)

    if resp.decode().lower() == 'ok':
        fp = open(file_name, "rb")
        data = fp.read(BUFFSIZE)  # 파일 전체의 내용을 하나의 문자열로 읽어 옴
        print("송신 중...")

        while data:
            sock.sendto(data, client)
            time.sleep(0.02)  # 수신 측에서 저장할때까지 잠시 대기
            data = fp.read(BUFFSIZE)

        sock.sendto(data, client)  # 송신 완료를 위해 빈 데이터 전송
        fp.close()
        print("전송 완료")

    else:
        print("수신 응답 오류")


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    addr = ('localhost', 2506)
    try:
        role = sys.argv[1]  # 송신(s) or 수신(r)
        if role == 's':
            Sender()
        elif role == 'r':
            Receiver()
        else:
            print("s(송신) 또는 r(수신)을 지정하세요.")
    except:
        print("s(송신) 또는 r(수신)을 지정하세요.")