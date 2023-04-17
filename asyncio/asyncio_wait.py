import asyncio
import random
import time

async def say(msg, delay=1):
    print(f'{msg!r} will be displayed in {delay} seconds')
    await asyncio.sleep(delay)
    return msg.upper()

async def main():
    messages = 'hello world apple banana cherry'.split()
    coros = [say(m, random.randrange(1,5)) for m in messages]

    start_time = time.time()
    done, pending = await asyncio.wait(coros)  #done은 완료된 pending은 미완료된 코루틴

    for task in done: #완료된 태스크의 값을 반환
        print(await task)
    print(f'{time.time() - start_time}') #총 소요시간

asyncio.run(main())
