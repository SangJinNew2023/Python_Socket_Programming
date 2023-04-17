import asyncio
import random

async def say(msg, delay=1):
    print(f'{msg!r} will be displayed in {delay} seconds')
    await asyncio.sleep(delay)
    return msg.upper()

async def main():
    messages = 'pear peach apple banana cherry'.split()

    #코루틴 list
    coros = [say(m, random.randrange(1,5)) for m in messages]

    #코루틴을 스케줄링하고 완료되는 순선대로 반환
    for coro in asyncio.as_completed(coros):
        msg = await coro
        print(msg)
asyncio.run(main())
