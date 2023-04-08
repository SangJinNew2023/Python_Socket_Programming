import socket

client = socket.socket()
client.connect(('127.0.0.1', 6543))
client.send('Hello Python'.encode('utf-8'))
print(client.recv(1024))