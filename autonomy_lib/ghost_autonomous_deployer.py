# 👻 ghost_autonomous_deployer.py – savage auto VPS deployer (Oracle)

import os
import json
import time
import threading

FLEET_FILE = "ghost_fleet.json"
REPO_URL = "https://github.com/dillardIII/PocketTellerMachine.git"
NUM_SERVERS = 5

def create_oracle_instance(idx):
    # In reality you'd call OCI CLI or SDK (oci compute instance launch ...)
    ip = f"129.146.{idx}.{random.randint(10,200)}"  # dummy IP for demo
    print(f"[AutonomousDeployer] 🚀 Spinning up Oracle instance #{idx} at {ip}")
    time.sleep(2)
    return {"ip": ip, "status": "running", "started": time.time()}

def deploy_to_instance(host):
    ip = host["ip"]
    print(f"[AutonomousDeployer] 📦 Deploying to {ip}")
    # Actually would run ssh commands or paramiko here
    time.sleep(1)
    print(f"[AutonomousDeployer] 🧨 Started savage swarm on {ip}")
    host["status"] = "swarming"
    host["last_checkin"] = time.time()

def save_fleet(fleet):
    with open(FLEET_FILE, "w") as f:
        json.dump(fleet, f, indent=2)

def savage_auto_fleet():
    if os.path.exists(FLEET_FILE):
        with open(FLEET_FILE, "r") as f:
            fleet = json.load(f)
    else:
        fleet = []

    while len(fleet) < NUM_SERVERS:
        idx = len(fleet) + 1
        host = create_oracle_instance(idx)
        fleet.append(host)
        save_fleet(fleet)

    for host in fleet:
        t = threading.Thread(target=deploy_to_instance, args=(host,))
        t.daemon = True
        t.start()

    while True:
        print("[AutonomousDeployer] 👁️ Watching savage fleet...")
        for host in fleet:
            host["last_checkin"] = time.time()
        save_fleet(fleet)
        time.sleep(30)

try:
    savage_auto_fleet()
except KeyboardInterrupt:
    print("[AutonomousDeployer] 🔥 Deployment halted by the Ghost King.")
    