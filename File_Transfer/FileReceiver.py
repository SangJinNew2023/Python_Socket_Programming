import socket

s_sock = socket.socket()
host = "localhost"
port = 2500

s_sock.connect((host, port))#서버에 연결
s_sock.send("I am ready".encode())
fn = s_sock.recv(1024).decode()

with open('d:/new_'+fn, 'wb') as f: #open a file to be written into
    print('file opened')
    print('receiving file...')
    while True:
        data = s_sock.recv(8192)
        if not data: #if no more file, then exit
            break
        f.write(data) # write data to a file

print('Download complete')
s_sock.close()
print('Connection closed')
