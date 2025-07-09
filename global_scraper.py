# === FILE: global_scraper.py ===
import os
import requests
import json
from random import choice
from datetime import datetime

targets = [
    "magic ritual pdf", "enochian scripts", "ethereum private keys",
    "ufo military leaks", "sigil databases", "occult trading logs"
]

proxies = {
    "http": "socks5h://localhost:9050",
    "https": "socks5h://localhost:9050"
}

def scrape(term):
    try:
        r = requests.get(f"https://duckduckgo.com/html/?q={term}", proxies=proxies, timeout=15)
        if r.status_code == 200:
            print(f"[Scraper] ✅ Got hits for '{term}'")
            with open("4TB_WD/vault_results.json", "a") as f:
                json.dump({"term": term, "time": datetime.utcnow().isoformat(), "data": r.text[:500]}, f)
        else:
            print(f"[Scraper] ⚠️ Failed {r.status_code} for '{term}'")
    except Exception as e:
        print(f"[Scraper] ❌ Error for '{term}': {e}")

while True:
    scrape(choice(targets))