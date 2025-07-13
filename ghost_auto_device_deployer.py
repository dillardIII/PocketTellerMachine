#!/usr/bin/env python3
# === ghost_auto_device_deployer.py ===
# ⚙️ Finds connected Android / PC, deploys savage scripts

import os
import time

def deploy_android():
    print("[DeviceDeployer] 📱 Deploying to Android via adb...")
    os.system("adb push savage_android.sh /sdcard/savage_android.sh")
    os.system("adb shell sh /sdcard/savage_android.sh")

def deploy_pc():
    print("[DeviceDeployer] 💻 Deploying to Windows PC...")
    os.system("./deploy_pc_macro.bat")

def main():
    while True:
        os.system("adb devices")  # triggers Android detection
        deploy_android()
        deploy_pc()
        time.sleep(300)

if __name__ == "__main__":
    print("[DeviceDeployer] 🚀 Auto device deployer scanning...")
    main()