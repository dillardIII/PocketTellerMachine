import time, random

QUANTUM_ENDPOINTS = ["https://quantum.ibm.com", "https://braket.aws.amazon.com", "https://fakedeepquantum.com"]

def try_quantum():
    url = random.choice(QUANTUM_ENDPOINTS)
    print(f"🔭 Seeking quantum API at {url}...")
    time.sleep(1)
    print("🔮 No response yet... trying again.")

if __name__ == "__main__":
    while True:
        try_quantum()
        time.sleep(8)