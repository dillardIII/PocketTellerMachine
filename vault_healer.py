#!/usr/bin/env python3
"""
Vault Healer for PTM
- Recreates missing vault_status.json with healthy defaults
"""

import json

vault_status = {"vault": "healthy", "entropy_pools": 8, "shields": "active"}

with open("vault_status.json", "w") as f:
    json.dump(vault_status, f)
print("🔧 vault_status.json recreated + marked healthy.")