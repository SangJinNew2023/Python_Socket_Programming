import asyncio
import time

async def say(msg, delay):
    await asyncio.sleep(delay)
    print(msg)

try:
    loop=asyncio.get_running_loop() #실행 이벤트 루프를 가져옴
except:
    loop = asyncio.new_event_loop() #이벤트 루프가 없으면 새 루프 생성
print(f"started at {time.strftime('%X')}") #시간을 원하는 포맷에 맞춰 출력

#task 생성
task1 = loop.create_task(say('First hello', 2))
task2 = loop.create_task(say('Second hello', 3))

#task 완료시까지 루프 실행
loop.run_until_complete(task1)
loop.run_until_complete(task2)

print(f"finished at {time.strftime('%X')}")

loop.close()