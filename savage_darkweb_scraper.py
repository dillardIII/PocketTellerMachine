#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json
import time

TOR_PROXY = "socks5h://127.0.0.1:9050"

def dark_scrape():
    urls = [
        "http://exampleonion1.onion",
        "http://exampleonion2.onion"
    ]
    for url in urls:
        try:
            r = requests.get(url, proxies={'http': TOR_PROXY, 'https': TOR_PROXY}, timeout=20)
            soup = BeautifulSoup(r.text, 'html.parser')
            findings = soup.text[:500]
            with open("vault_mutation_log.json", "a") as v:
                json.dump({"time": time.time(), "dark_findings": findings}, v)
                v.write("\n")
            print("✅ Scraped & saved:", url)
        except Exception as e:
            print("⚠️ Failed:", url, e)

while True:
    dark_scrape()
    time.sleep(600)