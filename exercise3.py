# 🧠 Question: How can a server handle multiple connections using threading?


import socket
import threading
import time

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(("0.0.0.0", 9999))

server_socket.listen(2)

def handle_client(connection, address):
    thread_id = threading.current_thread().ident
    print(f"Thread {thread_id} handling {address}")
    time.sleep(5)
    print(f"Thread {thread_id} done with {address}")
    connection.close()
    
    
while True:
    connection, address = server_socket.accept()
    print(f"Accepted connection from {address}")
    
    thread = threading.Thread(target= handle_client, args=(connection, address))
    thread.start()