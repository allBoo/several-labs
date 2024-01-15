
import socket
import threading

from shared import BIND_ADDRESS, SERVER_PORT, read_socket


def handle_client(client_socket):
    request = read_socket(client_socket)
    print(f"Received from {client_socket.getpeername()}: {request}\n")

    words = request.split()
    shortest_word = min(words, key=len) if words else ''
    longest_word = max(words, key=len) if words else ''

    response = f"Shortest word: {shortest_word}\nLongest word: {longest_word}"
    client_socket.send(response.encode('utf-8'))
    client_socket.close()


def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((BIND_ADDRESS, SERVER_PORT))
    server_socket.listen()

    print("Server listening on port 8888...")

    while True:
        client_socket, addr = server_socket.accept()
        print(f"Accepted connection from {addr}")

        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()


if __name__ == "__main__":
    start_server()

