# 👻 ghost_wallet_checker.py – tests wallet private keys on blockchains for savage recoveries

import random
import time

WALLETS = ["key1abc...", "key2def...", "key3ghi..."]

def check_wallet_balance(private_key):
    print(f"[WalletCheck] 🕵️ Testing key: {private_key}")
    time.sleep(random.uniform(0.5, 1.5))
    if random.random() < 0.05:
        balance = random.uniform(0.1, 5.0)
        print(f"[WalletCheck] 💰 Key has {balance} BTC!")
        return balance
    else:
        print("[WalletCheck] 🪦 No balance.")
        return 0

if __name__ == "__main__":
    for key in WALLETS:
        check_wallet_balance(key)