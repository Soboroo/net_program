import socket, select

socks = []
BUFFER = 1024
PORT = 2500

s_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s_sock.bind(('', PORT))
s_sock.listen(5)

socks.append(s_sock)
print(f"Server started on port {PORT}")

while True:
    r_sock, w_sock, e_sock = select.select(socks, [], [])
    for s in r_sock:
        if s == s_sock:
            c_sock, addr = s_sock.accept()
            socks.append(c_sock)
            print(f"Connection from {addr}")
        else:
            try:
                data = s.recv(BUFFER)
                if not data:
                    print(f"Client {s.getpeername()} disconnected")
                    socks.remove(s)
                    s.close()
                else:
                    print(f"Received from {s.getpeername()}: {data.decode()}")
                    for sock in socks:
                        if sock != s_sock and sock != s:
                            try:
                                sock.send(data)
                            except Exception as e:
                                print(f"Error sending data to {sock.getpeername()}: {e}")
            except Exception as e:
                print(f"Error: {e}")
                socks.remove(s)
                s.close()