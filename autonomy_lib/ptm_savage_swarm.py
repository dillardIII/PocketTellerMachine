#!/usr/bin/env python3
import threading
import requests
import json
import os
import time
from datetime import datetime

PTM_FILES = {
    "main.py": "https://raw.githubusercontent.com/dillardIII/PocketTellerMachine/main/main.py",
    "autonomy_trigger_stack.py": "https://raw.githubusercontent.com/dillardIII/PocketTellerMachine/main/autonomy_trigger_stack.py",
    "vault_manager.py": "https://raw.githubusercontent.com/dillardIII/PocketTellerMachine/main/vault_manager.py"
}
REBUILD_DIR = "ptm_swarm_rebuild"
VAULT_FILE = "swarm_vault.json"
LOG_FILE = "swarm_log.json"

def log(msg):
    print(f"[Swarm] {msg}")
    with open(LOG_FILE, "a") as f:
        f.write(f"{datetime.utcnow().isoformat()} - {msg}\n")

def load_vault():
    try:
        with open(VAULT_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_vault(vault):
    with open(VAULT_FILE, "w") as f:
        json.dump(vault, f, indent=2)

def harvester(name, url):
    vault = load_vault()
    for i in range(5):  # savage retries
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                vault[name] = r.text
                save_vault(vault)
                log(f"✅ Harvested {name}")
                return
            else:
                log(f"❌ {name}: {r.status_code}")
        except Exception as e:
            log(f"⚠️ {name} error: {e}")
        time.sleep(2)
    log(f"💀 {name} failed after retries")

def rebuilder():
    vault = load_vault()
    if not os.path.exists(REBUILD_DIR):
        os.makedirs(REBUILD_DIR)
    for fname, content in vault.items():
        with open(os.path.join(REBUILD_DIR, fname), "w") as f:
            f.write(content)
            log(f"🔨 Rebuilt {fname}")
    log("🚀 Savage swarm rebuild complete.")

threads = []
for fname, url in PTM_FILES.items():
    t = threading.Thread(target=harvester, args=(fname, url))
    t.start()
    threads.append(t)
    time.sleep(0.5)

for t in threads:
    t.join()

rebuilder()