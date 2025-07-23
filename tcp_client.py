import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect(("192.168.164.142", 80))  # Updated IP
    client.send(b"HELLO FROM CLIENT")
    response = client.recv(1024)
    print(f"Server response: {response.decode()}")
except Exception as e:
    print(f"Client error: {e}")
finally:
    client.close()