
import socket

from shared import SERVER_ADDRESS, SERVER_PORT, read_socket

def send_message(message):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((SERVER_ADDRESS, SERVER_PORT))
    client_socket.send(message.encode('utf-8'))
    print(f"Request sent: {message}")

    response = read_socket(client_socket)
    print(f"Server response: {response}\n")

    client_socket.close()

if __name__ == "__main__":
    while True:
        user_input = input("Enter a message for the server (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        if not user_input:
            continue

        send_message(user_input)
