# === Adapted for ghostmedic ===
# 👻 ghost_uniswap_liquidity_sniper.py – savage DEX launch sniping
import requests
import time

DEXSCREENER_API = "https://api.dexscreener.com/latest/dex/pairs/ethereum/new"

def check_new_pairs():
    r = requests.get(DEXSCREENER_API)
    data = r.json()
    return data.get("pairs", [])

def savage_liquidity_sniper():
    seen = set()
    while True:
        try:
            pairs = check_new_pairs()
            for pair in pairs:
                if pair["pairAddress"] not in seen:
                    seen.add(pair["pairAddress"])
                    print(f"[UniSnipe] 🐉 New pair: {pair['baseToken']['symbol']}/{pair['quoteToken']['symbol']} @ {pair['pairAddress']}")
                    # Insert your liquidity buy or snipe here
        except Exception as e:
            print(f"[UniSnipe] ⚠️ Error: {e}")
        time.sleep(5)

try:
    savage_liquidity_sniper()
except KeyboardInterrupt:
    print("[UniSnipe] 👻 Exiting liquidity sniper.")