# 🧠 Question: How can we limit the number of concurrent 
# and total client connections to a server?


import socket, time, threading

server = socket.socket()
server.bind(("0.0.0.0", 9999))
server.listen(5)

active_connections = 0
attempts_per_ip = {}    # lifetime count
lock = threading.Lock()
MAX_CONCURRENT = 3
MAX_TOTAL = 3

def handle_client(conn, addr):
    global active_connections
    try:
        data = conn.recv(1024).decode().strip()
        conn.send(b"Hi!" if data=="hello" else b"Bye!")
        time.sleep(2)
    finally:
        conn.close()
        with lock:
            active_connections -= 1

while True:
    conn, addr = server.accept()
    ip = addr[0]

    with lock:
        attempts_per_ip[ip] = attempts_per_ip.get(ip, 0) + 1
        if attempts_per_ip[ip] > MAX_TOTAL:
            conn.send(b"Too many total attempts")
            conn.close()
            continue

        if active_connections >= MAX_CONCURRENT:
            conn.send(b"Too many concurrent connections")
            conn.close()
            continue

        active_connections += 1

    print("Accepted from", addr)
    threading.Thread(target=handle_client, args=(conn, addr), daemon=True).start()
