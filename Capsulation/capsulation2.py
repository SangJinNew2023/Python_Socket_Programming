def frame(start_ch, addr, seqNo, msg):
    addr = str(addr).zfill(2) #문자로 바꾸고 zfill을 이용해 앞부분을 0으로 채운 2바이트로 구성
    seqNo = str(seqNo).zfill(4)
    length = str(len(msg)).zfill(4)
    return chr(start_ch)+addr+seqNo+length+msg

if __name__ == '__main__':
    start_ch = 0x05
    addr = 2
    seqNo = 1

    msg = input('your message:')
    capsule = frame(start_ch, addr, seqNo, msg)
    print(capsule)
