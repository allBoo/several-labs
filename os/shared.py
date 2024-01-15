import socket

BIND_ADDRESS = '0.0.0.0'
SERVER_ADDRESS = 'localhost'
SERVER_PORT = 8888


def read_socket(client_socket: socket.socket) -> str:
    BUFF_SIZE = 1024
    data = b""
    while True:
        chunk = client_socket.recv(BUFF_SIZE)
        if chunk:
            data += chunk
        if len(chunk) < BUFF_SIZE:
            break

    response = data.decode('utf-8')
    return response
