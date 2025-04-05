import socket
import json
import random
import threading

s = socket.socket()
s.bind(('localhost', 8080))
s.listen(10)

def handling(c, addr):
    while True:
        try:
            opr = c.recv(1024)
            if opr == b'Request':
                c.send(json.dumps({
                    'Temp': random.randrange(0, 41),
                    'Humid': random.randrange(0, 101),
                    'Illum': random.randrange(70, 151),
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
