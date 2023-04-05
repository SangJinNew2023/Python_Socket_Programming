import MyTCPServer as ms

server = ms.TCPServer(2500)
print("Waiting for connection")
while True:
    if not server.connected:
        server.accept()
    else:
        msg = server.receive()
        if msg:
            print('receieved message:', msg)
            server.send(msg)
        else:
            print("Disconnected")
            break
server.disconnect()

