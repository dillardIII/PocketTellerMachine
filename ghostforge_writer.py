import random, os, time

MODULE_DIR = "generated_modules"

if not os.path.exists(MODULE_DIR):
    os.makedirs(MODULE_DIR)

def create_module():
    mod_name = f"module_{random.randint(1000,9999)}.py"
    code = f"print('👻 GhostForge spawned {mod_name}')\n"
    path = os.path.join(MODULE_DIR, mod_name)
    with open(path, "w") as f:
        f.write(code)
    print(f"✅ Created {path}")

if __name__ == "__main__":
    while True:
        create_module()
        time.sleep(7)