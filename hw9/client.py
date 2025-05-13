import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 2500))

def recv_data():
    while True:
        try:
            data = s.recv(1024)
            if not data:
                print("Server closed the connection")
                break
            print(data.decode())
        except Exception as e:
            print(f"Error receiving data: {e}")
            break

def send_data(id):
    while True:
        try:
            message = input()
            if message.lower() == 'exit':
                break
            s.send(f"{id}: {message}".encode())
        except Exception as e:
            print(f"Error sending data: {e}")
            break

id = input("Enter your ID:")

# Start the receiving thread
recv_thread = threading.Thread(target=recv_data)
recv_thread.start()
# Start the sending thread
send_thread = threading.Thread(target=send_data, args=(id,))
send_thread.start()
# Wait for threads to finish
recv_thread.join()
send_thread.join()
s.close()