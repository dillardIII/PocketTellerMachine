# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === ghost_dashboard.py ===
# 🧬 Savage Empire Dashboard + CLI Hybrid

import json
import time
import os
import sys

# ---------------------
# Loader functions
# ---------------------
def load_status():
    try:
        with open("liaison_inventory.json", "r") as f:
            return json.load(f)
    except:
        return {}

def load_vault():
    try:
        with open("vault_status.json", "r") as f:
            return json.load(f)
    except:
        return {}

# ---------------------
# Display functions
# ---------------------
def print_dashboard():
    os.system('clear' if os.name == 'posix' else 'cls')
    print("=== 🚀 Savage Empire Dashboard ===")
    status = load_status()
    vault = load_vault()
    print("\n[Inventory Check]")
    print(json.dumps(status, indent=2))
    print("\n[Vault Status]")
    print(json.dumps(vault, indent=2))
    print("\n[Heartbeat] 💓 System is alive...")

def show_commands():
    commands = {
        'help': "Show this help message",
        'status': "Print JSON runtime dashboard",
        'watch': "Run live watch loop on the dashboard",
        'exit': "Exit the savage dashboard"
    }
    print("\nAvailable commands:")
    for cmd, desc in commands.items():
        print(f"  {cmd}: {desc}")
    print("")

def check_status():
    print_dashboard()

# ---------------------
# Main loop
# ---------------------
def main(args):
    if '--help' in args:
        show_commands()
        sys.exit(0)

    print("=== 👻 Welcome to the Savage Ghost Dashboard ===")
    show_commands()

    while True:
        command = input("\n[GhostDash] > ").strip().lower()
        if command == 'help':
            show_commands()
        elif command == 'status':
            check_status()
        elif command == 'watch':
            print("🔭 Watching dashboard in live mode. Ctrl+C to stop.")
            try:
                while True:
                    print_dashboard()
                    time.sleep(5)
            except KeyboardInterrupt:
                print("\n👋 Exited live watch mode.")
        elif command == 'exit':
            print("👋 Exiting savage dashboard. Stay lethal.")
            sys.exit(0)
        else:
            print(f"❌ Unknown command: {command}")
            show_commands()

if __name__ == "__main__":
    main(sys.argv)