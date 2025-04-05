import socket
import json
import random
import threading

s = socket.socket()
s.bind(('localhost', 8081))
s.listen(10)

def handling(c, addr):
    while True:
        try:
            opr = c.recv(1024)
            if opr == b'Request':
                c.send(json.dumps({
                    'Heartbeat': random.randrange(40, 141),
                    'Steps': random.randrange(2000, 6001),
                    'Cal': random.randrange(1000, 4001),
                }).encode())
            elif opr == b'Quit':
                c.close()
            else:
                c.send(b'Invalid operation')
                c.close()
        except:
            c.close()
            break

while True:
    c, addr = s.accept()
    h = threading.Thread(target=handling, args=(c, addr))
    h.start()

