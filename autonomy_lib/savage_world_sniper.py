#!/usr/bin/env python3
# === savage_world_sniper.py ===
# 🌍 Savage World Sniper - pulls global data feeds for swarm intelligence

import os
import json
import time
from datetime import datetime
import requests

SNIPER_LOG = "world_sniper_data.json"
TARGETS = [
    "https://api.coindesk.com/v1/bpi/currentprice.json",
    "https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT",
    "https://api.github.com/events",
    "https://newsapi.org/v2/top-headlines?country=us&apiKey=YOUR_NEWS_API_KEY"
]

def fetch_data(url):
    try:
        response = requests.get(url, timeout=8)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": f"Status {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}

def log_data(feed):
    if os.path.exists(SNIPER_LOG):
        with open(SNIPER_LOG, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                data = []
    else:
        data = []
    data.append(feed)
    with open(SNIPER_LOG, "w") as f:
        json.dump(data, f, indent=2)

def main():
    print("[WorldSniper] 🌍 Savage World Sniper is live...")
    while True:
        for target in TARGETS:
            result = fetch_data(target)
            entry = {
                "time": datetime.utcnow().isoformat(),
                "source": target,
                "data": result
            }
            print(f"[WorldSniper] 🎯 Pulled data from: {target}")
            log_data(entry)
        time.sleep(120)

if __name__ == "__main__":
    main()