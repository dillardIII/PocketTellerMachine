# === Adapted for ghostmedic ===
# 👻 ghost_target_consumer.py – deploys PTM clones to infiltrated hosts

import json
import time
import threading
import random
import os

INFILTRATED_FILE = "ghost_infiltrated.json"
DEPLOY_LOG = "ghost_deploy_log.json"

def load_infiltrated():
    if not os.path.exists(INFILTRATED_FILE):
        return []
    with open(INFILTRATED_FILE, "r") as f:
        return json.load(f)

def save_deploy_record(record):
    if not os.path.exists(DEPLOY_LOG):
        with open(DEPLOY_LOG, "w") as f:
            json.dump([], f)
    with open(DEPLOY_LOG, "r") as f:
        data = json.load(f)
    data.append(record)
    with open(DEPLOY_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Consumer] 🧨 Deployed PTM clone to {record['ip']}")

def deploy_ptm_clone(ip, port, cred):
    # This is a savage simulation. Real would SCP binaries & run them.
    time.sleep(random.uniform(0.5, 2.0))
    if random.random() < 0.9:  # fake 90% success
        save_deploy_record({"ip": ip, "port": port, "cred": cred, "timestamp": time.time()})

def consume_targets(threads=10):
    print("[Consumer] 🚀 Deploying PTM clones to compromised hosts...")
    while True:
        infiltrated = load_infiltrated()
        for host in infiltrated:
            t = threading.Thread(target=deploy_ptm_clone, args=(host["ip"], host["port"], host["cred"]))
            t.daemon = True
            t.start()
        time.sleep(60)

try:
    consume_targets()
except KeyboardInterrupt:
    print("[Consumer] 🔥 Ghost King stopped clone deployment.")