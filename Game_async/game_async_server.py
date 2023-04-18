import socket, pickle
import asyncio
from game_player import Player

#create two players objects
players = [Player(220, 250, 30, (255, 0, 0)), Player(300, 250, 30, (0, 0, 255))] #player for circle
currentPlayer = 0
svr = "127.0.0.1"
port = 5555

#It is coroutine for client connection
async def handler(reader, writer):
    global currentPlayer
    player = currentPlayer
    writer.write(pickle.dumps(players[player])) #send the first connected player object
    await writer.drain()

    currentPlayer += 1 # 다음 플레이어
    reply=""
    while True:
        try:
            data = pickle.loads(await reader.read(2048)) #플레이어 객체 수신
            players[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = players[0]
                else:
                    reply = players[1]
            writer.write(pickle.dumps(reply)) # 다른 클라이언트에게 플레이어 객체 전송
            await writer.drain()
        except:
            break
    print("Lost connection")
    writer.close()

#서버 객체를 만들고 연결을 기다린다. 이 과정은 무한 반복된다.
async def main():
    server = await asyncio.start_server(handler, host=svr, port=port)
    async with server:
        await server.serve_forever()

        asyncio.run(main())


