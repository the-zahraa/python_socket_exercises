import socket

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(("127.0.0.1", 5000))
    server.listen(5)
    print("Server listening on 127.0.0.1:5000...")
    while True:
        client, addr = server.accept()
        print(f"Connection from {addr}")
        client.close()

if __name__ == "__main__":
    start_server()