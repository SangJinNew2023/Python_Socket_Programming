import asyncio as aio

async def say(what,delay):
    await aio.sleep(delay)
    print(what)

async def stop_after(loop, delay):
    await aio.sleep(delay)
    loop.stop() #이벤트 루프 중단

try:
    loop = aio.get_running_loop() #코루틴에서 이벤트 루프를 얻을때
except:
    loop = aio.new_event_loop()

loop.create_task(say('first message',2))
loop.create_task(say('second message',1))
loop.create_task(say('third message',4))
loop.create_task(stop_after(loop, 3)) #loop.stop() 호출 delay가 3이라 third message 호출전 stop

loop.run_forever() #이벤트 루프 무한 반복 실행
loop.close()

