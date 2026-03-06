import socket

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))

server_socket.listen()

print(f"Server running on {HOST}:{PORT}")

while True:
    client_socket, address = server_socket.accept()

    print(f"Client connected from {address}")

    while True:
        data = client_socket.recv(1024)

        if not data:
            break

        message = data.decode()
        print(f"Message received: {message}")

    client_socket.close()