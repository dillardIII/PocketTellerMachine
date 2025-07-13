# === Adapted for ghostmedic ===
# === savage_macro_dashboard.py ===
# 🚀 Savage Macro Dashboard - safer, fully tolerant of missing keys

import json
import time
import os

def load_json(file_name):
    try:
        with open(file_name, "r") as f:
            return json.load(f)
    except:
        return []

def clear_screen():
    os.system("clear" if os.name == "posix" else "cls")

def show_dashboard():
    clear_screen()
    print("=== 🚀 Savage Macro Dashboard ===")
    macros = load_json("macro_queue.json")
    log = load_json("mutation_log.json")

    print("\n[Macro Queue]")
    if not macros:
        print("  (empty)")
    for m in macros:
        task = m.get("task", "Unknown")
        details = m.get("details", "No details")
        print(f"  ▶ {task} - {details}")

    print("\n[Mutation Log]")
    if not log:
        print("  (no mutations yet)")
    for l in log[-5:]:
        file = l.get("file", "unknown_file")
        status = l.get("status", "unknown_status")
        print(f"  📝 {file} - {status}")

    print("\n[Heartbeat] 💓 Savage Empire is running...")

if __name__ == "__main__":
    while True:
        show_dashboard()
        time.sleep(5)