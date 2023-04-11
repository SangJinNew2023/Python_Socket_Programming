frame = []
msg = input("Your Message:")
size = 4 #전송단위

for i in range(0, len(msg), size): #range(start, stop, step)
    print("i:", i)
    frame.append(msg[i:i+size]) #i 부터 i+size단위로 슬라이싱

print('단편화 메시지:{}'.format(frame))
print('재조립 메시지:{}'.format(''.join(frame))) #''를 매개체로 join()함수로 결합
I