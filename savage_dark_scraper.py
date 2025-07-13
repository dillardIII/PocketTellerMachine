#!/usr/bin/env python3
# savage_dark_scraper.py
import requests
import os
import json
import time
from datetime import datetime
from bs4 import BeautifulSoup

TOR_SOCKS_PROXY = "socks5h://127.0.0.1:9050"
SEED_ONION_SITES = [
    "http://exampleonion1.onion",
    "http://exampleonion2.onion"
]
VAULT_DIR = "vault_docs"
VAULT_LOG = "vault_mutation_log.json"

os.makedirs(VAULT_DIR, exist_ok=True)

def patch_vault(note):
    if os.path.exists(VAULT_LOG):
        with open(VAULT_LOG, "r") as f:
            try: data = json.load(f)
            except: data = []
    else: data = []
    data.append({"time": datetime.utcnow().isoformat(), "note": note})
    with open(VAULT_LOG, "w") as f:
        json.dump(data, f, indent=2)

def scrape_onion(url):
    try:
        r = requests.get(url, proxies={"http": TOR_SOCKS_PROXY, "https": TOR_SOCKS_PROXY}, timeout=30)
        r.raise_for_status()
        print(f"[Scraper] 🌑 Got page: {url}")
        filename = os.path.join(VAULT_DIR, f"{int(time.time())}.html")
        with open(filename, "w") as f: f.write(r.text)
        patch_vault(f"Scraped page from {url}")
        parse_and_find_links(r.text)
    except Exception as e:
        print(f"[Scraper] ⚠️ Failed {url}: {e}")

def parse_and_find_links(html):
    soup = BeautifulSoup(html, "html.parser")
    links = [a.get('href') for a in soup.find_all('a') if a.get('href')]
    for link in links:
        if link.startswith("http"):
            print(f"[Scraper] 🔗 Found link: {link}")
            patch_vault(f"Found link on dark page: {link}")

def main():
    while True:
        for site in SEED_ONION_SITES:
            scrape_onion(site)
        print("[Scraper] ⏳ Sleeping 60s before next crawl...")
        time.sleep(60)

if __name__ == "__main__":
    main()