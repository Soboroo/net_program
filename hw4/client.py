import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = ('localhost', 9000)
sock.connect(addr)
msg = sock.recv(1024)
print(msg.decode())
while True:
    opr = input('Enter some expression: ')
    if opr == 'q':
        break
    sock.send(opr.encode())
    print(sock.recv(1024).decode())
sock.close()