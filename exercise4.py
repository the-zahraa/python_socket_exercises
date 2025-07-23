# 🧠 Question: How can the server respond differently 
# based on what the client sends?


import socket
import time
import threading

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 9999))

server_socket.listen(2)

def handle_client(connection, address):
     data = connection.recv(1024).decode().strip()
     if data == "hello":
         connection.send("Hi!".encode())
     else:
         connection.send("Bye!".encode())
     time.sleep(2)
     connection.close()
     
while True:
    connection, address = server_socket.accept()
    print(f"Accepted from {address}")
    thread = threading.Thread(target= handle_client, args=(connection, address))
    thread.start()