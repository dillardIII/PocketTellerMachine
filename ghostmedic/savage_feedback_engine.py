# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_feedback_engine.py ===
# 🧬 Savage Feedback Engine — builds more macros based on results

import json
import random
import time

def load_macro_queue():
    try:
        with open("macro_queue.json", "r") as f:
            return json.load(f)
    except:
        return []

def save_macro_queue(queue):
    with open("macro_queue.json", "w") as f:
        json.dump(queue, f, indent=2)

def evolve_macro_queue():
    queue = load_macro_queue()
    new_macro = {
        "action": "generate_or_repair_file",
        "details": f"auto task at {int(time.time())} - {random.choice(['improve system', 'scan vault', 'optimize ghostmedic', 'rebuild dashboard'])}"
    }
    print(f"[FeedbackEngine] ➕ Adding new macro: {new_macro}")
    queue.append(new_macro)
    save_macro_queue(queue)

if __name__ == "__main__":
    while True:
        evolve_macro_queue()
        time.sleep(random.randint(5,15))