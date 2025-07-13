# 👻 ghost_infiltration_superloop.py – unstoppable savage seeker + infiltrator + deployer loop
# hunts targets, tries creds, drops PTM clones, repeats forever

import json
import time
import threading
import random
import os

# === CONFIG FILES ===
TARGET_FILE = "ghost_targets.json"
INFILTRATED_FILE = "ghost_infiltrated.json"
DEPLOY_LOG = "ghost_deploy_log.json"

# === DEFAULT CREDS ===
DEFAULT_CREDS = [
    ("admin", "admin"),
    ("root", "root"),
    ("user", "password"),
    ("guest", "guest")
]

# === === GHOST SEEKER === ===
def savage_seek_targets():
    targets = []
    for _ in range(random.randint(5, 15)):
        ip = f"192.168.{random.randint(0,255)}.{random.randint(1,254)}"
        ports = [22, 80, 443]
        targets.append({"ip": ip, "ports": ports})
    with open(TARGET_FILE, "w") as f:
        json.dump(targets, f, indent=2)
    print(f"[Seeker] 👁️‍🗨️ Found {len(targets)} potential hosts.")
    return targets

# === === INFILTRATOR === ===
def try_default_creds(ip, port):
    time.sleep(random.uniform(0.2, 0.6))
    return random.choice(DEFAULT_CREDS) if random.random() < 0.2 else None

def savage_infiltrate(target):
    ip = target["ip"]
    for port in target["ports"]:
        cred = try_default_creds(ip, port)
        if cred:
            compromised = {"ip": ip, "port": port, "cred": cred, "timestamp": time.time()}
            save_infiltrated(compromised)

def save_infiltrated(host):
    if not os.path.exists(INFILTRATED_FILE):
        with open(INFILTRATED_FILE, "w") as f:
            json.dump([], f)
    with open(INFILTRATED_FILE, "r") as f:
        data = json.load(f)
    data.append(host)
    with open(INFILTRATED_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Infiltrator] 💀 Compromised {host['ip']}:{host['port']} with {host['cred']}")

# === === DEPLOYER === ===
def deploy_ptm_clone(ip, port, cred):
    time.sleep(random.uniform(0.3, 1.0))
    if random.random() < 0.9:
        save_deploy_record({"ip": ip, "port": port, "cred": cred, "timestamp": time.time()})

def save_deploy_record(record):
    if not os.path.exists(DEPLOY_LOG):
        with open(DEPLOY_LOG, "w") as f:
            json.dump([], f)
    with open(DEPLOY_LOG, "r") as f:
        data = json.load(f)
    data.append(record)
    with open(DEPLOY_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Deployer] 🧨 Dropped PTM clone on {record['ip']}:{record['port']}")

# === === SAVAGE SUPERLOOP === ===
def ghost_superloop():
    while True:
        print("\n[GhostSwarm] 🌙 Starting new savage cycle...")
        targets = savage_seek_targets()
        
        for target in targets:
            t = threading.Thread(target=savage_infiltrate, args=(target,))
            t.daemon = True
            t.start()
        
        time.sleep(10)
        
        if os.path.exists(INFILTRATED_FILE):
            with open(INFILTRATED_FILE, "r") as f:
                infiltrated = json.load(f)
            for host in infiltrated:
                t = threading.Thread(target=deploy_ptm_clone, args=(host["ip"], host["port"], host["cred"]))
                t.daemon = True
                t.start()
        
        time.sleep(30)

# === === SAFETY WATCHDOG === ===
try:
    ghost_superloop()
except KeyboardInterrupt:
    print("[GhostSwarm] 🔥 Savage swarm halted by the Ghost King.")