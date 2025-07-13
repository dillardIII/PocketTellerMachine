# === Adapted for ghostmedic ===
# 👻 ghost_autonomous_procurement.py – bots hunt free credits, cheap servers & auto-provision
import random, time

CHEAP_HOSTS = [
    {"name": "Vercel", "monthly": 0, "yearly": 0},
    {"name": "Oracle Cloud", "monthly": 0, "yearly": 0},
    {"name": "Hetzner", "monthly": 4, "yearly": 48},
    {"name": "Scaleway", "monthly": 3, "yearly": 36},
    {"name": "AWS Free Tier", "monthly": 0, "yearly": 0},
]

def savage_provision():
    while True:
        host = random.choice(CHEAP_HOSTS)
        if host["monthly"] == 0:
            print(f"[Procurement] 🧛 Claimed free server credits at {host['name']}")
        else:
            print(f"[Procurement] 💸 Reserved ${host['monthly']}/mo host at {host['name']}")
        time.sleep(random.uniform(5,15))

try:
    savage_provision()
except KeyboardInterrupt:
    print("[Procurement] ⚰️ Stopped by ghost king.")