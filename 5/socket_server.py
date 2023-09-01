import socket


def main():
    # set up host and port for the demo
    host = "127.0.0.1"
    port = 12345

    # run a server using this socket info (host + port)
    run_server(host, port)


def run_server(host, port):
    # open a socket stream and listen to client requests
    # by binding host to given port
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen(1)
        print(f"Server is running on address {host} on port {port}")

        print("Server is listening...")
        print("-" * 80)

        # receive client's message
        client, address = s.accept()
        # keep receiving until client want to disconnect
        while True:
            # client is receiving 4096 bytes of data (4000 bytes / 4 KB)
            data = client.recv(4096)
            # message received was in bytes, convert to string
            message = data.decode()

            # if we don't receive data, means client is done sending message
            if not data:
                break

            # display the message
            print(f"Received message from {address}:\n{message}")

            # send client back their data, data  can be send in bytes so convert it from strnig to bytes
            response = f"Your message was: {message}"
            client.sendall(response.encode())

        print("-" * 80)

        # close the socket
        s.close()

        print("server stopped listening...")
    return None


if __name__ == "__main__":
    main()
