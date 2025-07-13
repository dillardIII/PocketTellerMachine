# 👻 ghost_arbitrage_sniper_real.py – savage real-time price sniper across CEX & DEX
import requests
import time

BINANCE_API = "https://api.binance.com/api/v3/ticker/price?symbol=ETHUSDT"
UNISWAP_API = "https://api.dexscreener.com/latest/dex/pairs/ethereum/0x0000000000000000000000000000000000000000"

def get_binance_price():
    r = requests.get(BINANCE_API)
    return float(r.json()["price"])

def get_uniswap_price():
    # This needs to be configured with actual pool or pair IDs
    r = requests.get(UNISWAP_API)
    data = r.json()
    return float(data["pair"]["priceUsd"])

def savage_sniper_loop():
    while True:
        try:
            binance = get_binance_price()
            uniswap = get_uniswap_price()
            diff = abs(binance - uniswap)
            print(f"[ArbSniper] 🔍 Binance: {binance} | Uniswap: {uniswap} | Diff: {diff}")
            if diff > 5:  # Adjust for your spread + fees
                print(f"[ArbSniper] 🚀 Savage opportunity found! Arbitrage diff: ${diff}")
                # Insert your trade execution here
        except Exception as e:
            print(f"[ArbSniper] ⚠️ Error: {e}")
        time.sleep(3)

try:
    savage_sniper_loop()
except KeyboardInterrupt:
    print("[ArbSniper] 👻 Exiting savage sniper.")