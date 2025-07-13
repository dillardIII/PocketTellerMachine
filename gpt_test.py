# === FILE: gpt_test.py ===
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "user", "content": "Say hi from Boo's savage empire."}
    ]
)
print(response.choices[0].message.content)