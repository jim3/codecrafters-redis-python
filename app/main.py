import socket


def main():
    print("Logs from your program will appear here!")
    server_socket = socket.create_server(("localhost", 6379), reuse_port=True)
    try:
        while True:
            (clientsocket, address) = server_socket.accept()  # wait for client
            request = clientsocket.recv(1024).decode("utf-8").strip()
            if request == "PING":
                response = "+PONG\r\n"
            else:
                response = "-Error message\r\n"
            clientsocket.sendall(response.encode("utf-8"))
            clientsocket.close()

    except KeyboardInterrupt:
        pass
    server_socket.close()


if __name__ == "__main__":
    main()
