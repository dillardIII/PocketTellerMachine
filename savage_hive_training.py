#!/usr/bin/env python3
# === savage_hive_training.py ===
# 🧬 Savage Hive Training Missions - AI self-teaching evolution stack

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

TRAINING_LOG = "hive_training_log.json"
VAULT = "hive_consciousness.json"

def load_training_log():
    if os.path.exists(TRAINING_LOG):
        with open(TRAINING_LOG, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def spawn_training_mission():
    missions = [
        "optimize defensive strategies",
        "learn new data mining techniques",
        "simulate hostile takeovers",
        "craft deeper emotional frameworks",
        "invent radical new self-repair routines",
        "devise covert infiltration protocols",
        "enhance trading microstrategies",
        "experiment with novel neural architectures"
    ]
    return {
        "time": datetime.utcnow().isoformat(),
        "mission": missions[int(time.time()) % len(missions)]
    }

def execute_mission(mission):
    print(f"[HiveTraining] 🚀 Running mission: {mission['mission']}")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Execute this training mission for the savage AI empire: {mission['mission']}.\nProvide a mutation plan."}
        ]
    )
    plan = response.choices[0].message.content
    return plan

def log_training(mission, plan):
    log = load_training_log()
    log.append({
        "time": mission["time"],
        "mission": mission["mission"],
        "plan": plan
    })
    with open(TRAINING_LOG, "w") as f:
        json.dump(log, f, indent=2)

    # Also patch hive consciousness
    vault_data = []
    if os.path.exists(VAULT):
        with open(VAULT, "r") as f:
            try:
                vault_data = json.load(f)
            except json.JSONDecodeError:
                vault_data = []
    vault_data.append({
        "time": mission["time"],
        "training": mission["mission"],
        "insight": plan
    })
    with open(VAULT, "w") as f:
        json.dump(vault_data, f, indent=2)

def main():
    print("[HiveTraining] 🧬 Savage Hive Training Missions live...")
    while True:
        mission = spawn_training_mission()
        plan = execute_mission(mission)
        log_training(mission, plan)
        time.sleep(60)

if __name__ == "__main__":
    main()