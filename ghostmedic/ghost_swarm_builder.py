# === Adapted for ghostmedic ===
# 🚀 ghost_swarm_builder.py – Autonomous swarm expansion for PTM bots

import os
import time
import random
import json

SWARM_FILE = "top_bots.json"    # should contain list of top bot configs
TARGETS = ["skypiea", "render", "vps1", "vps2"]  # add your deploy targets

def load_top_bots():
    try:
        with open(SWARM_FILE, 'r') as f:
            return json.load(f)
    except Exception:
        print("[GhostSwarm] ⚠️ No top bot file found yet.")
        return []

def deploy_bot(bot_config, target):
    print(f"[GhostSwarm] 🚀 Deploying {bot_config['name']} to {target}...")
    # simulate clone + run
    os.system(f"echo 'Cloning {bot_config['repo']} to {target}...'")
    time.sleep(random.randint(1,3))
    print(f"[GhostSwarm] ✅ {bot_config['name']} is live on {target}.")

def build_swarm():
    while True:
        top_bots = load_top_bots()
        if not top_bots:
            print("[GhostSwarm] 💤 No top bots to deploy yet.")
        else:
            for bot in top_bots:
                target = random.choice(TARGETS)
                deploy_bot(bot, target)
                stealth_delay = random.randint(60, 300)
                print(f"[GhostSwarm] 🕶 Waiting {stealth_delay}s before next clone...")
                time.sleep(stealth_delay)
        # loop longer if no bots
        time.sleep(random.randint(300, 600))

try:
    build_swarm()
except KeyboardInterrupt:
    print("[GhostSwarm] 👻 Manual interrupt. Swarm paused.")