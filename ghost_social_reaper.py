# 👻 ghost_social_reaper.py – savage style
# creates bot swarms on social & DeFi for farming, scam liquidation

import time
import random
import json
import os

SOCIAL_LOG = "ghost_social_log.json"
FAKE_SOCIALS = ["twitter", "telegram", "discord", "tiktok"]
DEFI_APPS = ["Uniswap", "SushiSwap", "PancakeSwap", "Aave"]

def farm_social_tokens():
    platform = random.choice(FAKE_SOCIALS)
    earned = round(random.uniform(0.01, 1.0), 3)
    log_reap("social", {"platform": platform, "earned": earned})
    print(f"[Reaper] 🕷 Farmed {earned} tokens on {platform}")

def liquidate_scam():
    app = random.choice(DEFI_APPS)
    bounty = round(random.uniform(0.1, 5.0), 2)
    if bounty > 0.5:
        log_reap("liquidation", {"app": app, "bounty": bounty})
        print(f"[Reaper] ☠️ Liquidated scam on {app} for {bounty} bounty.")

def log_reap(source, data):
    if not os.path.exists(SOCIAL_LOG):
        with open(SOCIAL_LOG, "w") as f:
            json.dump([], f)
    with open(SOCIAL_LOG, "r") as f:
        logs = json.load(f)
    logs.append({
        "source": source,
        "data": data,
        "timestamp": time.time()
    })
    with open(SOCIAL_LOG, "w") as f:
        json.dump(logs, f, indent=2)

def savage_reaper_loop():
    while True:
        farm_social_tokens()
        liquidate_scam()
        time.sleep(random.randint(3, 10))

try:
    savage_reaper_loop()
except KeyboardInterrupt:
    print("[Reaper] 🔥 Social reaper halted by the Ghost King.")