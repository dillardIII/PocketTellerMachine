# === Adapted for ghostmedic ===
# 👻 ghost_global_seeker.py – savage scanner & global seeker for PTM deployment

import socket
import random
import json
import time
import threading

TARGET_FILE = "ghost_targets.json"

def random_ip():
    return ".".join(str(random.randint(1, 254)) for _ in range(4))

def try_connect(ip, port, timeout=0.5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        sock.connect((ip, port))
        sock.close()
        return True
    except:
        return False

def scan_ip(ip):
    open_ports = []
    for port in [21, 22, 23, 80, 443, 8080]:
        if try_connect(ip, port):
            print(f"[Seeker] 🔥 Found open port {port} on {ip}")
            open_ports.append(port)
    return open_ports

def save_target(ip, ports):
    target_data = {"ip": ip, "ports": ports, "timestamp": time.time()}
    if not os.path.exists(TARGET_FILE):
        with open(TARGET_FILE, "w") as f:
            json.dump([], f)
    with open(TARGET_FILE, "r") as f:
        data = json.load(f)
    data.append(target_data)
    with open(TARGET_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Seeker] 💾 Saved target: {ip} with ports {ports}")

def savage_hunt_cycle():
    while True:
        ip = random_ip()
        print(f"[Seeker] 👻 Scanning IP: {ip}")
        open_ports = scan_ip(ip)
        if open_ports:
            save_target(ip, open_ports)
        time.sleep(random.uniform(0.2, 1.0))

def start_savage_seeker(threads=10):
    print("[Seeker] 🚀 Starting savage global seeker...")
    for _ in range(threads):
        t = threading.Thread(target=savage_hunt_cycle)
        t.daemon = True
        t.start()

    while True:
        time.sleep(60)

try:
    start_savage_seeker()
except KeyboardInterrupt:
    print("[Seeker] 🔥 Interrupted by ghost king. Standing down.")