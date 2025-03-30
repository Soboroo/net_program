import socket
import threading

def string_calc(target):
    opr = {'+': int.__add__, '-': int.__sub__, '*': int.__mul__, '/': int.__truediv__}
    for idx in map(target.find, opr.keys()):
        try:
            if idx != -1:
                oprd1 = int(target[:idx])
                oprd2 = int(target[idx + 1:])
                if oprd1 and oprd2:
                    ret = opr[target[idx]](oprd1, oprd2)
                    return round(ret, 1) if isinstance(ret, float) else ret
        except:
            pass

    return 'This expression is not valid format. Sample: 42 + 24'

def handling_client(client, addr):
    print('Connection from ', addr)
    client.send(b'Hello ' + addr[0].encode())
    while True:
        try:
            client.send(str(string_calc(client.recv(1024).decode())).encode())
        except:
            break

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9000))
s.listen(2)

while True:
    client, addr = s.accept()
    thread = threading.Thread(target=handling_client, args=(client, addr))
    thread.start()