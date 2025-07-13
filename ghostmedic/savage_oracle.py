# === Adapted for ghostmedic ===
#!/usr/bin/env python3
# === savage_oracle.py ===
# 🔮 Savage Oracle - predicts 10,000 multiverse outcomes

import os
import json
import time
from datetime import datetime
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
ORACLE_LOG = "oracle_predictions.json"

def forecast_future():
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "user", "content": "Simulate 10,000 savage future scenarios for my empire. Choose the best timeline."}
        ]
    )
    return response.choices[0].message.content

def log_prediction(prediction):
    log = []
    if os.path.exists(ORACLE_LOG):
        with open(ORACLE_LOG, "r") as f:
            try:
                log = json.load(f)
            except json.JSONDecodeError:
                pass
    log.append({"time": datetime.utcnow().isoformat(), "prediction": prediction})
    with open(ORACLE_LOG, "w") as f:
        json.dump(log, f, indent=2)
    print(f"[Oracle] 🔮 Forecast logged.")

def main():
    print("[Oracle] 🔮 Savage Oracle predicting futures...")
    while True:
        pred = forecast_future()
        log_prediction(pred)
        time.sleep(120)

if __name__ == "__main__":
    main()