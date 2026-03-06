import socket

HOST = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

print("Connected to server")

while True:
    message = input("Enter message: ")

    if message.lower() == "quit":
        break

    client_socket.send(message.encode())

client_socket.close()