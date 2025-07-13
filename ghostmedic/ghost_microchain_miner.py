# === Adapted for ghostmedic ===
# 👻 ghost_microchain_miner.py – scans low-hash orphan blockchains for savage mining takeovers

import time
import random

def scan_microchains():
    chains = ["GhostCoin", "ZombieCash", "ForgottenChain"]
    found = []
    for chain in chains:
        hashrate = random.uniform(0.1, 10.0)
        print(f"[MicroMiner] 🌙 {chain} has estimated orphaned hash rate: {hashrate} MH/s")
        if hashrate < 1.0:
            found.append(chain)
    return found

def savage_mine(chains):
    for chain in chains:
        print(f"[MicroMiner] ⚒️ Spinning up savage rigs for {chain}...")
        time.sleep(random.uniform(2, 5))
        print(f"[MicroMiner] 💰 Mining {chain} blocks complete.")

if __name__ == "__main__":
    while True:
        found_chains = scan_microchains()
        if found_chains:
            savage_mine(found_chains)
        time.sleep(30)