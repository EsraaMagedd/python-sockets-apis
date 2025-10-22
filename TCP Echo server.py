import socket

def echo_server(port):
    host = 'localhost'
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(5)
    print(f"Echo Server running on {host}:{port}")

    while True:
        client, address = sock.accept()
        print(f"Connection from {address}")
        try:
            data = client.recv(2048)
            if data:
                print(f"Received: {data.decode()}")
                # Echo the message back to the client
                client.send(data)
        except Exception as e:
            print("Error while communicating:", e)
        finally:
            client.close()


if __name__ == '__main__':
    echo_server(10000)
