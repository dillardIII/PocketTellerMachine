# 🚀 ghost_autonomous_recruiter.py – savage autonomous scavenger for free servers

import time
import random
import json
import requests

CHEAP_LOG = "cheap_targets.json"
FREE_PLACES = [
    "https://replit.com", "https://glitch.com", "https://render.com/free",
    "https://fly.io", "https://clever-cloud.com", "https://vercel.com",
    "https://openresty.com", "https://public-iot.org", "https://shodan.io"
]

def scan_for_free_targets():
    print("[GhostRecruiter] 👻 Scanning known free tiers...")
    for place in FREE_PLACES:
        try:
            response = requests.get(place, timeout=3)
            if response.status_code == 200:
                print(f"[GhostRecruiter] ✅ Target available: {place}")
        except:
            print(f"[GhostRecruiter] ⚠️ Failed to reach {place}")
        time.sleep(random.randint(1, 3))

def search_for_super_cheap_vps():
    print("[GhostRecruiter] 💰 Looking for ultra-cheap VPS...")
    cheap = [
        {"name": "Contabo Micro", "cost_month": 3.99, "cost_year": 47.88},
        {"name": "Hetzner CPX11", "cost_month": 3.49, "cost_year": 41.88},
        {"name": "Vultr Micro", "cost_month": 5.00, "cost_year": 60.00},
        {"name": "Oracle Always Free", "cost_month": 0.00, "cost_year": 0.00}
    ]
    with open(CHEAP_LOG, "w") as f:
        json.dump(cheap, f, indent=2)
    for vps in cheap:
        print(f"[GhostRecruiter] 🪦 {vps['name']}: ${vps['cost_month']}/mo (${vps['cost_year']}/yr)")

def scavenge_open_cctvs():
    print("[GhostRecruiter] 📹 Looking for open CCTV / unsecured NAS...")
    try:
        result = requests.get("https://www.insecam.org/en/bycountry/US/", timeout=5)
        if "Live Cameras" in result.text:
            print("[GhostRecruiter] 👀 Found potential open cameras.")
    except:
        print("[GhostRecruiter] ⚠️ CCTV sweep failed.")

def autonomous_hunt():
    while True:
        scan_for_free_targets()
        search_for_super_cheap_vps()
        scavenge_open_cctvs()
        print("[GhostRecruiter] 😈 Sleeping before next savage sweep...")
        time.sleep(random.randint(300, 600))

try:
    autonomous_hunt()
except KeyboardInterrupt:
    print("[GhostRecruiter] 🔥 Manual abort by ghost king.")