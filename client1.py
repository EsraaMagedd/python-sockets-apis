import socket

# 1. Create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 2. Connect to server
client_socket.connect(('localhost', 12345))

# 3. Send message to server
message = "Hello Server! This is the client."
client_socket.send(message.encode())

# 4. Receive reply from server
reply = client_socket.recv(1024).decode()
print("Server says:", reply)

# 5. Close connection
client_socket.close()
