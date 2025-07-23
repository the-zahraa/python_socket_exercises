# 🧠 Question: How can a Python client connect 
# to a website and read its response using sockets?

import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

target_host = "www.google.com"
target_ip = socket.gethostbyname(target_host)
target_port = 80
client_socket.connect((target_ip, target_port))

request = "GET / HTTP/1.1\r\nHost:www.google.com\r\nConnection: close\r\n\r\n"
client_socket.send(request.encode())


response = ""

while True:
    
    data = client_socket.recv(4096)
    if not data:
        break
    response += data.decode('utf-8', errors= 'ignore')
    
print(response)

client_socket.close()
