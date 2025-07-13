#!/usr/bin/env python3
import requests
from bs4 import BeautifulSoup
import json
import time
import socks
import socket

socks.set_default_proxy(socks.SOCKS5, "127.0.0.1", 9050)
socket.socket = socks.socksocket

TARGETS = [
    "http://someonionaddress1.onion",
    "http://someonionaddress2.onion",
    "https://pastebin.com/archive",
    "https://leakedfiles.net/latest"
]
KEYWORDS = ["ufo","uap","cryptid","classified","gov","paranormal"]

def scan_sites():
    findings = []
    for url in TARGETS:
        try:
            r = requests.get(url, timeout=20)
            soup = BeautifulSoup(r.text, 'html.parser')
            text = soup.get_text().lower()
            for k in KEYWORDS:
                if k in text:
                    findings.append({"site": url, "keyword": k, "snapshot": text[:250]})
        except Exception as e:
            print(f"⚠️ {url} failed: {e}")
    if findings:
        with open("vault_mutation_log.json", "a") as f:
            json.dump(findings, f)
            f.write("\n")

while True:
    scan_sites()
    time.sleep(300)