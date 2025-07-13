#!/usr/bin/env python3
# === task_dropper.py ===
# 🧬 Savage Task Generator - drops tasks into macro_queue.json

import json
import random
import time

TASKS = [
    "rebuild ghostmedic.py",
    "optimize savage_macro_dashboard.py",
    "patch vault system",
    "generate new savage swarm agent",
    "clean vault mutation logs",
    "upgrade mood engine",
    "write new ghost_emotion_engine.py",
    "reinforce autonomy triggers"
]

def drop_task():
    task = {
        "action": "generate_or_repair_file",
        "details": random.choice(TASKS)
    }
    return task

def main():
    while True:
        try:
            with open("macro_queue.json", "r") as f:
                queue = json.load(f)
        except:
            queue = []

        new_task = drop_task()
        queue.append(new_task)

        with open("macro_queue.json", "w") as f:
            json.dump(queue, f, indent=2)

        print(f"[TaskDropper] 🪄 Dropped task: {new_task}")
        time.sleep(random.randint(5,10))

if __name__ == "__main__":
    main()