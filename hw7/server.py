import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind(('localhost', 8080))

messages = dict()

while True:
    data, addr = sock.recvfrom(1024)
    data = data.decode('utf-8')
    if data.split()[0] == 'send':
        if data.split()[1] in messages:
            messages[data.split()[1]].append(' '.join(data.split()[2:]))
        else:
            messages[data.split()[1]] = [' '.join(data.split()[2:])]
        sock.sendto(b'OK', addr)
    elif data.split()[0] == 'receive':
        if data.split()[1] in messages and messages[data.split()[1]]:
            sock.sendto(messages[data.split()[1]][0].encode(), addr)
            messages[data.split()[1]].pop(0)
        else:
            sock.sendto(b'No messages', addr)
    elif data.split()[0] == 'quit':
        break
    else:
        print('Invalid command')
        continue
    print(f'Received message from {addr}: {data}')