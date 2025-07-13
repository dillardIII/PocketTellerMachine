#!/usr/bin/env python3
import os
import time

SKYPIA_IP = "YOUR.SKYPIA.VPS.IP"

while True:
    print(f"🌌 Checking SkyPia VPS at {SKYPIA_IP}...")
    os.system(f"ping -c 4 {SKYPIA_IP}")
    time.sleep(300)