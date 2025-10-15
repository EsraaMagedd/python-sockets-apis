import socket

# 1. Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Bind to an address and port
server_socket.bind(('localhost', 12345))

# 3. Listen for incoming connections
server_socket.listen(1)
print("Server is listening...")

# 4. Accept client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

# 5. Receive message from client
data = conn.recv(1024).decode()
print("Client says:", data)

# 6. Send a response back
reply = "Hello Client! Message received."
conn.send(reply.encode())

# 7. Close connection
conn.close()
