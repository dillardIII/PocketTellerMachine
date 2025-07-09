# === FILE: cost_auditor.py ===
print("[CostAuditor] 💵 Calculating savage empire burn rate...")

services = {
    "Replit": 20,
    "Render": 5,
    "ElevenLabs": 15,
    "NordVPN": 12,
    "Skypiea VPS": 50
}

base_cost = sum(services.values())
print(f"[CostAuditor] 🔥 1 PTM base cost: ${base_cost}/month")
print(f"[CostAuditor] 🚀 10 PTMs: ${base_cost*10}/month")
print(f"[CostAuditor] 🧨 1000 PTMs: ${base_cost*1000}/month")