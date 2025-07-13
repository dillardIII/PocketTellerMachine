# === Adapted for ghostmedic ===
# === multi_ai_savage_test.py ===
import os
from openai import OpenAI
import google.generativeai as genai
import requests
import replicate

# === PULL FROM REPLIT ENV ===
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_GENAI_API_KEY = os.getenv("GOOGLE_GENAI_API_KEY")
DEEPGRAM_API_KEY = os.getenv("DEEPGRAM_API_KEY")
REPLICATE_API_KEY = os.getenv("REPLICATE_API_KEY")

# OPTIONAL HARD CODE (uncomment if needed)
# OPENAI_API_KEY = "sk-your-key"
# GOOGLE_GENAI_API_KEY = "your-google-key"
# DEEPGRAM_API_KEY = "your-deepgram-key"
# REPLICATE_API_KEY = "your-replicate-key"

# === OPENAI GPT-4 TEST ===
def test_openai():
    print("\n[OpenAI GPT-4] 🔥 Running completion...")
    client = OpenAI(api_key=OPENAI_API_KEY)
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[{"role": "user", "content": "Say hello from GPT-4, savage empire style."}]
    )
    print("[OpenAI GPT-4] ✅", response.choices[0].message.content)

# === GOOGLE GEMINI TEST ===
def test_gemini():
    print("\n[Google Gemini] 🚀 Generating savage greeting...")
    genai.configure(api_key=GOOGLE_GENAI_API_KEY)
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say hello from Google Gemini.")
    print("[Google Gemini] ✅", response.text)

# === DEEPGRAM TEST ===
def test_deepgram():
    print("\n[Deepgram] 🎙️ Transcribing...")
    url = "https://static.deepgram.com/examples/interview_speech-analytics.wav"
    headers = {"Authorization": f"Token {DEEPGRAM_API_KEY}"}
    audio = requests.get(url).content
    response = requests.post(
        "https://api.deepgram.com/v1/listen?punctuate=true",
        headers=headers, data=audio
    )
    transcript = response.json().get("results", {}).get("channels", [{}])[0].get("alternatives", [{}])[0].get("transcript", "")
    print("[Deepgram] ✅ Transcript:", transcript[:100], "...")

# === REPLICATE TEST ===
def test_replicate():
    print("\n[Replicate] 🎨 Making savage neon skull...")
    os.environ["REPLICATE_API_TOKEN"] = REPLICATE_API_KEY
    output = replicate.run(
        "stability-ai/stable-diffusion",
        input={"prompt": "a savage neon skull on fire, ultra detailed"}
    )
    print("[Replicate] ✅ Image URL:", output[0])

# === RUN THEM ALL ===
if __name__ == "__main__":
    print("💀 Running Savage Multi-AI Test Suite...")
    test_openai()
    test_gemini()
    test_deepgram()
    test_replicate()
    print("\n🔥 All systems tested. Savage empire multi-AI integration complete.")