import socket

table = {'1':'one','2':'two','3':'three','4':'four','5':'five',
         '6':'six','7':'seven','8':'eight','9':'nine','10':'ten'}

s=socket.socket()#socekt()은 AF_INET, SOCK_STEAM 와 같은 의미
address = ("",2500)
s.bind(address)
s.listen(1)
print('Waiting...')
c_socket, c_addr = s.accept()
print("Connection from", c_addr)
while True:
    data = c_socket.recv(1024).decode()
    try:
        resp = table[data] #1-10외에 숫자를 받으면 예외처리
    except:
        c_socket.send('Try again'.encode())
    else:
        c_socket.send(resp.encode())
