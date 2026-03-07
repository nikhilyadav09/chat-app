import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST, PORT))
server_socket.listen()

print(f"Server running on {HOST}:{PORT}")


def handle_client(client_socket, address):
    print(f"New connection from {address}")

    while True:
        try:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode()
            print(f"[{address}] {message}")

        except:
            break

    print(f"Client disconnected: {address}")
    client_socket.close()


while True:
    client_socket, address = server_socket.accept()

    client_thread = threading.Thread(
        target=handle_client,
        args=(client_socket, address)
    )

    client_thread.start()