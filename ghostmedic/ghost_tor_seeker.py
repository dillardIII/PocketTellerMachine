# === Adapted for ghostmedic ===
# 👻 ghost_tor_seeker.py – savage .onion recon for leaks, wallet dumps & pastebin creds

import time
import json
import random
from stem import Signal
from stem.control import Controller
import requests

OUTPUT_FILE = "tor_seeker_results.json"

def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate()
        controller.signal(Signal.NEWNYM)
    time.sleep(5)

def savage_tor_request(url):
    proxies = {
        'http': 'socks5h://localhost:9050',
        'https': 'socks5h://localhost:9050'
    }
    try:
        r = requests.get(url, proxies=proxies, timeout=15)
        return r.text
    except Exception as e:
        print(f"[Seeker] 💀 Failed on {url}: {e}")
        return ""

def savage_scan_onions():
    onions = [
        "http://duskgytldkxiuqc6.onion",  # example onion for demonstration
        "http://3g2upl4pq6kufc4m.onion",
        "http://zlal32teyptf4tvi.onion"
    ]
    found = []
    for url in onions:
        print(f"[Seeker] 👁️ Crawling {url}")
        page = savage_tor_request(url)
        if "wallet" in page or "private key" in page or "mnemonic" in page:
            found.append({"url": url, "content_snippet": page[:200]})
        renew_tor_ip()
    with open(OUTPUT_FILE, "w") as f:
        json.dump(found, f, indent=2)
    print(f"[Seeker] 👻 Completed savage TOR hunt. Results saved.")

if __name__ == "__main__":
    savage_scan_onions()