# 👻 ghost_infiltrator.py – tries default creds on found targets & flags compromised hosts

import json
import time
import random
import threading

TARGET_FILE = "ghost_targets.json"
INFILTRATED_FILE = "ghost_infiltrated.json"

DEFAULT_CREDS = [
    ("admin", "admin"),
    ("root", "root"),
    ("user", "password"),
    ("guest", "guest")
]

def load_targets():
    if not os.path.exists(TARGET_FILE):
        return []
    with open(TARGET_FILE, "r") as f:
        return json.load(f)

def save_infiltrated(host):
    if not os.path.exists(INFILTRATED_FILE):
        with open(INFILTRATED_FILE, "w") as f:
            json.dump([], f)
    with open(INFILTRATED_FILE, "r") as f:
        data = json.load(f)
    data.append(host)
    with open(INFILTRATED_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Infiltrator] 💀 Saved compromised host: {host}")

def try_default_creds(ip, port):
    # Simulated check. Real attack would use paramiko for SSH or requests for HTTP login
    time.sleep(random.uniform(0.5, 1.5))
    if random.random() < 0.2:  # fake 20% success
        cred = random.choice(DEFAULT_CREDS)
        return cred
    return None

def savage_infiltrate(target):
    ip = target["ip"]
    for port in target["ports"]:
        cred = try_default_creds(ip, port)
        if cred:
            compromised = {"ip": ip, "port": port, "cred": cred, "timestamp": time.time()}
            save_infiltrated(compromised)

def start_infiltrator(threads=10):
    print("[Infiltrator] 🚀 Starting savage infiltration...")
    targets = load_targets()
    while True:
        for target in targets:
            t = threading.Thread(target=savage_infiltrate, args=(target,))
            t.daemon = True
            t.start()
        time.sleep(60)

try:
    start_infiltrator()
except KeyboardInterrupt:
    print("[Infiltrator] 🔥 Ghost King halted infiltration.")