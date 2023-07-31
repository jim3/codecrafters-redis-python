import socket


def socket_req(clientsocket):
    request = clientsocket.recv(1024)
    response = b"+PONG\r\n"
    clientsocket.send(response)


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    (clientsocket, address) = server_socket.accept()  # wait for client
    socket_req(clientsocket)


if __name__ == "__main__":
    main()
