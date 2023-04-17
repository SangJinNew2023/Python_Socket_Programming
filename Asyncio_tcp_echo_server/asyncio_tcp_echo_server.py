import asyncio

#데이터 수신 처리 코루틴
#client와 연결되면 한번만 실행
async def handle_echo(reader, writer):
    data = await reader.read(100) # 데이터 수신
    message = data.decode()
    addr = writer.get_extra_info('peername') # writer의 name 정보, 상대방 주소
    print(f"{addr!r}에서 {message!r}를 수신함") #!r chooses repr to format the value

    print(f"송신: {message!r}")
    writer.write(data) #data 전송
    await writer.drain()  #writer buffer의 모든 내용 전송
    print("client socket close")
    writer.close()

svr = '127.0.0.1'
port = 2500

try:
    loop = asyncio.get_running_loop()
except:
    loop = asyncio.new_event_loop()

#client가 연결되면 handle_echo callback이 실행
# handle_echo는 StreamReader and StreamWriter의 수신과 전송을 처리하는 reader와 writer 객체를 전달 받음
coro = asyncio.start_server(handle_echo, svr, port, loop=loop)
server = loop.run_until_complete(coro) #코루틴 실행 예약
print('Serving on {}'.format(server.sockets[0].getsockname())) #getsockname() 소켓 주소 반환
try:
    loop.run_forever() #계속 연결
except KeyboardInterrupt: #ctrl+c
    pass

#서버 객체 close
server.close()
loop.close()



