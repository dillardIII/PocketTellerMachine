#!/usr/bin/env python3
# === savage_macro_orchestrator_pack.py ===
# 💀 Savage macro orchestrator linking everything

import json
import time
from datetime import datetime
import os

MACRO_QUEUE = "macro_queue.json"

def append_macro(task):
    if os.path.exists(MACRO_QUEUE):
        with open(MACRO_QUEUE, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append({"time": datetime.utcnow().isoformat(), "task": task})
    with open(MACRO_QUEUE, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Orchestrator] 💥 Macro added: {task}")

if __name__ == "__main__":
    while True:
        append_macro("trigger next savage realm spawn")
        append_macro("forge new ghost strategy modules")
        append_macro("reinforce HiveNet links")
        time.sleep(30)