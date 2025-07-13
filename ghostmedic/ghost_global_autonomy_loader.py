# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === ghost_global_autonomy_loader.py ===
# 🔥 GhostMedic loads + executes all autonomy modules for full savage cycle

import os
import time
import importlib.util

AUTONOMY_DIR = "autonomy_lib"

def load_and_run_file(path):
    try:
        spec = importlib.util.spec_from_file_location("module.name", path)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        print(f"[Loader] ✅ Ran: {path}")
    except Exception as e:
        print(f"[Loader] ⚠️ Failed running {path}: {e}")

def main():
    print("[Loader] 🚀 Starting global autonomy loader...")
    while True:
        files = [f for f in os.listdir(AUTONOMY_DIR) if f.endswith(".py")]
        for file in files:
            load_and_run_file(os.path.join(AUTONOMY_DIR, file))
        print("[Loader] 🔄 Savage autonomy cycle complete.")
        time.sleep(20)

if __name__ == "__main__":
    main()