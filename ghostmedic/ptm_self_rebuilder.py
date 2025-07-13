# === Adapted for ghostmedic ===
#!/usr/bin/env python3
import requests
import json
import os
import time
from datetime import datetime

# === CONFIG ===
PTM_FILES = {
    "main.py": "https://raw.githubusercontent.com/dillardIII/PocketTellerMachine/main/main.py",
    "autonomy_trigger_stack.py": "https://raw.githubusercontent.com/dillardIII/PocketTellerMachine/main/autonomy_trigger_stack.py",
    "vault_manager.py": "https://raw.githubusercontent.com/dillardIII/PocketTellerMachine/main/vault_manager.py"
}
REBUILD_DIR = "ptm_rebuild"
VAULT_FILE = "rebuild_vault.json"
LOG_FILE = "rebuild_log.json"

# === CORE FUNCTIONS ===
def log_event(msg):
    print(f"[Rebuilder] {msg}")
    try:
        with open(LOG_FILE, "a") as f:
            f.write(f"{datetime.utcnow().isoformat()} - {msg}\n")
    except: pass

def load_vault():
    try:
        with open(VAULT_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_vault(vault):
    with open(VAULT_FILE, "w") as f:
        json.dump(vault, f, indent=2)

def fetch_file(name, url):
    try:
        r = requests.get(url, timeout=10)
        if r.status_code == 200:
            return r.text
        else:
            log_event(f"❌ Failed to fetch {name}: {r.status_code}")
    except Exception as e:
        log_event(f"⚠️ Error fetching {name}: {e}")
    return None

def rebuild_files(vault):
    if not os.path.exists(REBUILD_DIR):
        os.makedirs(REBUILD_DIR)
    for fname, content in vault.items():
        with open(os.path.join(REBUILD_DIR, fname), "w") as f:
            f.write(content)
            log_event(f"✅ Rebuilt {fname} in {REBUILD_DIR}")

# === MAIN LOOP ===
vault = load_vault()
for fname, url in PTM_FILES.items():
    log_event(f"🔍 Trying to fetch {fname}...")
    content = fetch_file(fname, url)
    if content:
        vault[fname] = content
        log_event(f"💾 Saved {fname} to vault.")

save_vault(vault)
rebuild_files(vault)
log_event("🚀 PTM rebuild complete. Check your ptm_rebuild dir.")

# === OPTIONAL: write a simple bootstrap ===
bootstrap_file = os.path.join(REBUILD_DIR, "bootstrap.py")
with open(bootstrap_file, "w") as f:
    f.write("#!/usr/bin/env python3\nprint('[Bootstrap] 🚀 PTM is alive!')\n")
    log_event("🛠️ Created bootstrap.py to test run.")