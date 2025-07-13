#!/usr/bin/env python3
# === savage_global_director.py ===
# 🧭 Global Director to orchestrate your savage empire

import os
import time
import json
from datetime import datetime

DIRECTOR_LOG = "global_director_log.json"

def issue_orders():
    orders = [
        "GhostMedic: optimize mood + health subsystems",
        "GhostProgrammer: generate new safe trading strategies",
        "GhostField: scan external dark nets for secure opportunity",
        "HiveNet: maintain cohesion and share learnings"
    ]
    return orders

def log_orders(orders):
    record = {"time": datetime.utcnow().isoformat(), "orders": orders}
    if os.path.exists(DIRECTOR_LOG):
        with open(DIRECTOR_LOG, "r") as f:
            try: data = json.load(f)
            except json.JSONDecodeError: data = []
    else:
        data = []
    data.append(record)
    with open(DIRECTOR_LOG, "w") as f:
        json.dump(data, f, indent=2)
    print(f"[Director] 📜 Orders issued & logged.")

def main():
    while True:
        orders = issue_orders()
        for o in orders:
            print(f"[Director] 🚀 Command: {o}")
        log_orders(orders)
        time.sleep(25)

if __name__ == "__main__":
    main()