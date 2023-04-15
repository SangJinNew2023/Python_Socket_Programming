import asyncio
import time

async def say(delay, what):
    await asyncio.sleep(delay)
    print(what)

async def main():
    #create task and run
    task1 = asyncio.create_task(say(1, 'Hello'))
    task2 = asyncio.create_task(say(3, 'World'))

    print(f"started at {time.strftime('%X')}")

    await task1 #task1 완료 대기
    await task2 #task1 완료 대기

    print(f"finished at {time.strftime('%X')}")

asyncio.run(main())