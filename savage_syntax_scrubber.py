#!/usr/bin/env python3
# savage_syntax_scrubber.py
import os
import ast

AUTONOMY_DIR = "autonomy_lib"

for fname in os.listdir(AUTONOMY_DIR):
    if not fname.endswith(".py"):
        continue
    path = os.path.join(AUTONOMY_DIR, fname)
    try:
        with open(path, "r") as f:
            code = f.read()
            # quick string checks
            if any(s in code for s in ["Here's a", "As an AI language model", "Please note", "Below is an example"]):
                raise ValueError("Bad GPT snippet detected")
            # try parse
            ast.parse(code)
        print(f"✅ {fname} is clean.")
    except Exception as e:
        print(f"💀 Removing {fname}: {e}")
        os.remove(path)