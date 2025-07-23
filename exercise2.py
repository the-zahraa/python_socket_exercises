# 🧠 Question: How can we create a basic server that 
# accepts a single connection and waits?


import socket 
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 9999))

server_socket.listen(1)

connection, address = server_socket.accept()

print("Connected!")

time.sleep(5)

connection.close()

server_socket.close()