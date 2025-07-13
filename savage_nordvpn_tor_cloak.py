#!/usr/bin/env python3
import os
import time
import random

NORDVPN_COUNTRIES = ['us', 'uk', 'de', 'sg', 'nl', 'ca']

def cycle_nordvpn():
    country = random.choice(NORDVPN_COUNTRIES)
    print(f"🔥 Connecting NordVPN to: {country.upper()}")
    os.system(f"nordvpn connect {country}")

def restart_tor():
    print("🌀 Restarting Tor for new identity...")
    os.system("systemctl restart tor")

while True:
    cycle_nordvpn()
    restart_tor()
    time.sleep(300)