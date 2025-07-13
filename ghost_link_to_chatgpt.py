#!/usr/bin/env python3
# === ghost_link_to_chatgpt.py ===
# 🧬 Feeds your direct GPT commands into macro queue.

import json
from datetime import datetime

MACRO_QUEUE = "macro_queue.json"

def inject_macro(task_desc):
    try:
        with open(MACRO_QUEUE, "r") as f:
            queue = json.load(f)
    except:
        queue = []
    entry = {"time": datetime.utcnow().isoformat(), "task": task_desc}
    queue.append(entry)
    with open(MACRO_QUEUE, "w") as f:
        json.dump(queue, f, indent=2)
    print(f"[GPTLink] 🔥 Injected task: {task_desc}")

if __name__ == "__main__":
    while True:
        task = input("🔥 Enter your savage task: ")
        inject_macro(task)