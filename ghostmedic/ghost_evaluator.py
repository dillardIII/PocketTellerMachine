# === Adapted for ghostmedic ===
# 👻 ghost_evaluator.py – savage intelligence auditor & module killer
import os
import json
import time
import random

BRAIN_FILE = "quantum_brain.json"
MODULE_DIR = "generated_modules"

def load_brain():
    if os.path.exists(BRAIN_FILE):
        with open(BRAIN_FILE, "r") as f:
            return json.load(f)
    return {"entropy": 0}

def savage_metric(file_name, brain_entropy):
    file_entropy = sum([ord(c) for c in file_name]) % 100
    decision = file_entropy + brain_entropy
    print(f"[GhostEvaluator] 🔍 File: {file_name}, Metric: {decision}")
    return decision

def evaluate_and_cull():
    brain = load_brain()
    brain_entropy = brain.get("entropy", 0)

    if not os.path.exists(MODULE_DIR):
        print(f"[GhostEvaluator] ⚠️ No module directory found: {MODULE_DIR}")
        return

    for file_name in os.listdir(MODULE_DIR):
        path = os.path.join(MODULE_DIR, file_name)
        if os.path.isfile(path):
            score = savage_metric(file_name, brain_entropy)
            if score < 100:
                os.remove(path)
                print(f"[GhostEvaluator] 💀 Culled weak file: {file_name}")
            else:
                print(f"[GhostEvaluator] 🧬 Retained strong file: {file_name}")

def savage_eval_loop():
    while True:
        print("[GhostEvaluator] 👻 Running ghost audit on modules...")
        evaluate_and_cull()
        print("[GhostEvaluator] 💤 Sleeping before next ghost audit...")
        time.sleep(random.randint(180, 600))

try:
    savage_eval_loop()
except KeyboardInterrupt:
    print("[GhostEvaluator] 🔥 Audit interrupted by ghost king.")