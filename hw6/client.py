import socket
import json
import datetime

s1, s2 = socket.socket(), socket.socket()
s1.connect(('localhost', 8080))
s2.connect(('localhost', 8081))

while True:
    device_id = input('Enter device id: ')
    res = ''
    if device_id == '1':
        s1.send(b'Request')
        res = json.loads(s1.recv(1024).decode())
    elif device_id == '2':
        s2.send(b'Request')
        res = json.loads(s2.recv(1024).decode())
    elif device_id == 'quit':
        s1.send(b'Quit')
        s2.send(b'Quit')
        break
    else:
        print('Invalid device id')
        continue

    print(res)
    with open('data.txt', 'a') as f:
        f.write(f'{datetime.datetime.now().ctime()}: Device{device_id}: {", ".join([f"{i}={res[i]}" for i in res])}\n')