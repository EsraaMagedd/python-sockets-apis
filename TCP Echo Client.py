import socket

def echo_client(port):
    host = 'localhost'  # The server is running on the same machine
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the echo server
        sock.connect((host, port))
        message = "Hello from Client!"
        print("Sending:", message)

        # Send message to the server
        sock.sendall(message.encode())

        # Receive response from the server
        data = sock.recv(2048)
        print("Echoed back:", data.decode())

    except ConnectionRefusedError:
        print("Error: Could not connect to the server. Make sure the server is running on port", port)

    finally:
        # Always close the connection
        sock.close()


if __name__ == '__main__':
    echo_client(10000)
