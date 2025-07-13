# === Adapted for ghostmedic ===
# 👻 ghost_arbitrage_sniper.py – hunts live price mismatches across DEX + CEX for savage profits

import time
import random
import requests

def get_price_from_binance(symbol="BTCUSDT"):
    r = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={symbol}")
    return float(r.json()["price"])

def get_price_from_coinbase(symbol="BTC-USD"):
    r = requests.get(f"https://api.coinbase.com/v2/prices/{symbol}/spot")
    return float(r.json()["data"]["amount"])

def savage_arbitrage_hunt():
    while True:
        binance_price = get_price_from_binance()
        coinbase_price = get_price_from_coinbase()
        print(f"[ArbSniper] Binance: {binance_price}, Coinbase: {coinbase_price}")
        spread = abs(binance_price - coinbase_price)
        if spread > 20:
            print(f"[ArbSniper] 💰 Arbitrage opportunity found! Spread: {spread}")
        time.sleep(random.uniform(3,7))

if __name__ == "__main__":
    savage_arbitrage_hunt()