#!/usr/bin/env python3
# === savage_cross_device_operator.py ===
# 🔗 Controls Android + PC to run real scripts

import os
import time

ANDROID_CMD = "adb shell am start -n com.example/.MainActivity"
PC_SCRIPT = "./run_pc_macro.sh"

def run_android():
    print("[CrossDevice] 🤖 Sending Android command...")
    os.system(ANDROID_CMD)

def run_pc():
    print("[CrossDevice] 💻 Running PC macro...")
    os.system(PC_SCRIPT)

if __name__ == "__main__":
    print("[CrossDevice] 🌐 Savage cross-device operator live...")
    while True:
        run_android()
        run_pc()
        time.sleep(1800)  # every 30 min