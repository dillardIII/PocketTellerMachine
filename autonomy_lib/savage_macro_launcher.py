# === savage_macro_launcher.py ===
# 🧬 Launches Macro Orchestrator with your dashboard so you can watch builds happen

import threading
import os
import time

def run_macros():
    os.system("python3 savage_macro_orchestrator.py")

def run_dashboard():
    os.system("python3 ghost_dashboard.py")

threads = [
    threading.Thread(target=run_macros),
    threading.Thread(target=run_dashboard)
]

for t in threads:
    t.start()
    time.sleep(2)

for t in threads:
    t.join()