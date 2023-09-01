import socket


def main():
    # use this host and port to connect to server
    host = "localhost"
    port = 12345

    message = str.strip(input("What message do you want to send to the server?\n"))

    # run the client and send the message to server
    run_client(host, port, message)


def run_client(host, port, message):
    # create a socket using this host and port
    with socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) as s:
        s.connect((host, port))

        # message can be only send using bytes (not string)
        s.sendall(message.encode())

        # message is sent now
        print("Message sent successfully...")

        # check if we received anything from client upto 4KB, and convert it back from bytes to string
        response = s.recv(4096)
        print("-" * 80)
        print(f"Received message:\n{response.decode()}")
        print("-" * 80)

        # close the socket
        s.close()


if __name__ == "__main__":
    main()
