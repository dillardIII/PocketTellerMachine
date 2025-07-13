#!/usr/bin/env python3
import os, time
import subprocess

while True:
    print("🔁 Rotating NordVPN servers...")
    subprocess.call(["nordvpn", "disconnect"])
    time.sleep(2)
    subprocess.call(["nordvpn", "connect"])
    print("🕳️ Restarting Tor service...")
    os.system("service tor restart")
    print("✅ NordVPN + Tor rotated. Sleeping 300s.")
    time.sleep(300)