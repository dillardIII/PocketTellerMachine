# === FILE: liaison_module.py ===
# 🧭 The Savage Liaison - Requests missing modules, triggers GhostForge, monitors health.

import os
import json
from ghostforge_writer import generate_new_module

class Liaison:
    def __init__(self, bot_name):
        self.bot_name = bot_name
        self.health_file = f"{bot_name}_health.json"
        self.ensure_health_file()

    def ensure_health_file(self):
        if not os.path.exists(self.health_file):
            with open(self.health_file, "w") as f:
                json.dump({"status": "ok", "missing_modules": []}, f)

    def report_health(self, status="ok"):
        with open(self.health_file, "w") as f:
            json.dump({"status": status, "missing_modules": []}, f)
        print(f"[Liaison] ✅ {self.bot_name} health set to: {status}")

    def flag_missing_module(self, module_name):
        with open(self.health_file, "r") as f:
            data = json.load(f)
        if module_name not in data["missing_modules"]:
            data["missing_modules"].append(module_name)
        with open(self.health_file, "w") as f:
            json.dump(data, f)
        print(f"[Liaison] ⚠️ Missing module: {module_name}. Requesting build...")
        generate_new_module(module_name)

    def health_check(self):
        try:
            # Example: make sure a key module is loaded
            import mood_engine
            self.report_health("ok")
        except ImportError:
            self.flag_missing_module("mood_engine")
            self.report_health("degraded")