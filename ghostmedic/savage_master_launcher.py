# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_master_launcher.py ===
# 🧬 Master Launcher for Savage Empire - runs entire stack

import threading
import os
import time

def run(cmd):
    print(f"[Master] 🚀 Running: {cmd}")
    os.system(cmd)

threads = [
    threading.Thread(target=run, args=("python3 ghost_autonomy_kernel.py",)),
    threading.Thread(target=run, args=("python3 savage_blackhole_ai.py",)),
    threading.Thread(target=run, args=("python3 savage_oracle.py",)),
]

for t in threads:
    t.start()
    time.sleep(2)

for t in threads:
    t.join()

print("[Master] 👽 Savage Empire running at full omniversal autonomy.")