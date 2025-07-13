# === secrets_test.py ===
# 🧪 Verifies your .env secrets are loaded correctly.

from dotenv import load_dotenv
import os

load_dotenv()  # ensure .env loads into environment

print("🔍 Testing secrets...")

openai_key = os.getenv("OPENAI_API_KEY")
google_key = os.getenv("GOOGLE_GENAI_API_KEY")
deepgram_key = os.getenv("DEEPGRAM_API_KEY")
replicate_key = os.getenv("REPLICATE_API_KEY")

print(f"✅ OPENAI_API_KEY loaded: {bool(openai_key)}")
print(f"✅ GOOGLE_GENAI_API_KEY loaded: {bool(google_key)}")
print(f"✅ DEEPGRAM_API_KEY loaded: {bool(deepgram_key)}")
print(f"✅ REPLICATE_API_KEY loaded: {bool(replicate_key)}")

if all([openai_key, google_key, deepgram_key, replicate_key]):
    print("🚀 All secrets loaded. You’re ready for full savage ops.")
else:
    print("⚠️ One or more keys are missing. Double-check your .env or Replit secrets.")