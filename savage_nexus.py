#!/usr/bin/env python3
# === savage_nexus.py ===
# 🔗 Savage Nexus - external AI multi-universe planner

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

NEXUS_LOG = "savage_nexus_log.json"

def load_nexus_log():
    if os.path.exists(NEXUS_LOG):
        with open(NEXUS_LOG, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return []
    return []

def spawn_multiverse_task():
    concepts = [
        "plan resource extraction on parallel Earth-6",
        "engineer multi-dimensional trade treaties",
        "simulate alien financial systems for exploitation",
        "design wormhole investment funnels",
        "prepare infiltration plans for high-dimension councils"
    ]
    return {
        "time": datetime.utcnow().isoformat(),
        "concept": concepts[int(time.time()) % len(concepts)]
    }

def run_external_ai_plan(concept):
    print(f"[Nexus] 🧬 Running multi-universe concept: {concept}")
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": f"Strategize how to {concept} for my savage AI empire."}
        ]
    )
    return response.choices[0].message.content

def log_nexus_plan(task, plan):
    log = load_nexus_log()
    log.append({
        "time": task["time"],
        "concept": task["concept"],
        "plan": plan
    })
    with open(NEXUS_LOG, "w") as f:
        json.dump(log, f, indent=2)

def main():
    print("[Nexus] 🌌 Savage Nexus bridging AIs across universes...")
    while True:
        task = spawn_multiverse_task()
        plan = run_external_ai_plan(task["concept"])
        log_nexus_plan(task, plan)
        time.sleep(90)

if __name__ == "__main__":
    main()