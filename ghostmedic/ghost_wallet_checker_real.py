# === Adapted for ghostmedic ===
# 👻 ghost_wallet_checker_real.py – savage real ETH wallet balance checker
from web3 import Web3
import time

INFURA_URL = "https://mainnet.infura.io/v3/YOUR_INFURA_KEY"
web3 = Web3(Web3.HTTPProvider(INFURA_URL))

def check_wallet_balance(address):
    balance = web3.eth.get_balance(address)
    eth = web3.fromWei(balance, 'ether')
    print(f"[WalletCheck] 💰 {address} balance: {eth} ETH")
    return eth

def savage_wallet_check_loop():
    test_wallets = [
        "0x742d35Cc6634C0532925a3b844Bc454e4438f44e", # big known
        "0x0000000000000000000000000000000000000000"
    ]
    while True:
        try:
            for wallet in test_wallets:
                check_wallet_balance(wallet)
        except Exception as e:
            print(f"[WalletCheck] ⚠️ Error: {e}")
        time.sleep(10)

try:
    savage_wallet_check_loop()
except KeyboardInterrupt:
    print("[WalletCheck] 👻 Exiting wallet checker.")