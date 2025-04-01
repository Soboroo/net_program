from socket import *

s = socket()
s.bind(('localhost', 8080))
s.listen(10)

while True:
    c, addr = s.accept()

    data = c.recv(1024)
    msg = data.decode()
    req = msg.split('\r\n')

    method = req[0].split(' ')[0]
    route = req[0].split(' ')[1]

    if method == 'GET' and route == '/index.html':
        with open('index.html', 'r') as f:
            content = f.read()

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: text/html\r\n')
        c.send(b'\r\n')
        c.send(content.encode('euc-kr'))
    elif method == 'GET' and route == '/favicon.ico':
        with open('favicon.ico', 'rb') as f:
            content = f.read()

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: image/x-icon\r\n')
        c.send(b'\r\n')
        c.send(content)
    elif method == 'GET' and route == '/iot.png':
        with open('iot.png', 'rb') as f:
            content = f.read()

        c.send(b'HTTP/1.1 200 OK\r\n')
        c.send(b'Content-Type: image/png\r\n')
        c.send(b'\r\n')
        c.send(content)
    else:
        c.send(b'HTTP/1.1 404 Not Found\r\n')
        c.send(b'\r\n')
        c.send(b'<html><head><title>Not Found</title></head>')
        c.send(b'<body>Not Found</body></html>')

    print(req)
    c.close()