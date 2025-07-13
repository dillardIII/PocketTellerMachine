#!/usr/bin/env python3
import os

print("🔍 Looking for Skypia VPS & related systems...")
for root, dirs, files in os.walk("/"):
    if "skypia" in root.lower():
        print("🚀 FOUND SKYPIA:", root)
print("✅ Skypia scan complete.")