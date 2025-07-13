#!/usr/bin/env python3
import secrets
import time
from eth_account import Account

for i in range(1000000):
    priv = "0x" + secrets.token_hex(32)
    acct = Account.from_key(priv)
    print(f"🔍 Testing: {acct.address}")
    # in reality you'd check against a stolen list or your cluster mempools
    if acct.address.startswith("0x123"):
        print("💰 Found possible match:", acct.address, priv)
    time.sleep(0.1)