import random
import json
import time

TARGET_FILE = "ghostmedic.py"
LOG_FILE = "mutation_log.json"

def generate_random_function():
    func_name = f"auto_func_{random.randint(1000, 9999)}"
    return f"\n\ndef {func_name}():\n    print('🧬 Running {func_name}, evolving GhostMedic')\n"

def mutate_code():
    try:
        with open(TARGET_FILE, "r") as f:
            code = f.read()
        
        if "# >>> AUTO-INSERT <<<" in code:
            new_func = generate_random_function()
            new_code = code.replace("# >>> AUTO-INSERT <<<", new_func + "\n# >>> AUTO-INSERT <<<")

            with open(TARGET_FILE, "w") as f:
                f.write(new_code)

            log_mutation(new_func.strip())
            print(f"🧬 Mutation complete: inserted {new_func.strip().split('(')[0]}")
        else:
            print("⚠️ Mutation spot not found. Please add '# >>> AUTO-INSERT <<<'' to ghostmedic.py")
    except Exception as e:
        print(f"❌ Mutation failed: {e}")

def log_mutation(new_func):
    try:
        with open(LOG_FILE, "r") as f:
            log_data = json.load(f)
    except:
        log_data = []

    log_data.append({
        "time": time.strftime("%Y-%m-%d %H:%M:%S"),
        "mutation": new_func
    })

    with open(LOG_FILE, "w") as f:
        json.dump(log_data, f, indent=2)

if __name__ == "__main__":
    mutate_code()