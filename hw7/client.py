import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.connect(('localhost', 8080))

while True:
    command = input('Enter the message("send mboxId message" or "receive mboxId"):')
    if command == 'quit':
        break
    sock.send(command.encode())
    data, addr = sock.recvfrom(1024)
    data = data.decode('utf-8')
    if data == 'OK':
        print('Message sent successfully')
    elif data == 'No messages':
        print('No messages available')
    else:
        print(f'Received message: {data}')
sock.close()
