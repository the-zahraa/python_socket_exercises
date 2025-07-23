# 🧠 Question: How can we log all connections and rejections 
# while enforcing connection rules?


import socket
import time
import threading
import datetime

# Create server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("0.0.0.0", 9999))
server.listen(5)

# Shared state
active_connections = 0
attempts_per_ip = {}
lock = threading.Lock()
MAX_CONCURRENT = 3
MAX_TOTAL = 3

# Logging function
def log_connection(addr, action):
    timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open('connection_log.txt', 'a') as f:
        f.write(f"[{timestamp}] {addr[0]}:{addr[1]} - {action}\n")

# Client handler
def handle_client(conn, addr):
    global active_connections
    try:
        data = conn.recv(1024).decode().strip()
        conn.send(b"Hi!" if data == "hello" else b"Bye!")
        time.sleep(2)
    finally:
        conn.close()
        with lock:
            active_connections -= 1

# Main loop
while True:
    conn, addr = server.accept()
    ip = addr[0]
    accepted = False
    action = ""

    with lock:
        attempts_per_ip[ip] = attempts_per_ip.get(ip, 0) + 1

        if attempts_per_ip[ip] > MAX_TOTAL:
            conn.send(b"Too many total attempts")
            conn.close()
            action = "Rejected with Too many total attempts"

        elif active_connections >= MAX_CONCURRENT:
            conn.send(b"Too many concurrent connections")
            conn.close()
            action = "Rejected with Too many concurrent connections"

        else:
            active_connections += 1
            accepted = True

    if accepted:
        print("Accepted from", addr)
        log_connection(addr, "Accepted")
        threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
    else:
        log_connection(addr, action)
