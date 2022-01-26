import socket

HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 2345        # Port to listen on (non-privileged ports are > 1023)
print("start")
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1024)
            print(data)
            if not data:
                break
            conn.sendall(data)
