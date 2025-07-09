# === FILE: ptm_savior.py ===
# 🚀 PTM Savior – crawls existing PTM workspace, copies all files to ptm_savior_output
import os
import shutil

SOURCE_DIR = "./"
OUTPUT_DIR = "./ptm_savior_output"

if not os.path.exists(OUTPUT_DIR):
    os.makedirs(OUTPUT_DIR)

def savage_copy(src_dir, out_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.startswith('.') or file.endswith(('.pyc', '.log', '.sqlite')):
                continue
            full_src = os.path.join(root, file)
            relative_path = os.path.relpath(full_src, src_dir)
            out_path = os.path.join(out_dir, relative_path)
            out_folder = os.path.dirname(out_path)
            if not os.path.exists(out_folder):
                os.makedirs(out_folder)
            shutil.copy2(full_src, out_path)
            print(f"[PTMSavior] 🗂️ Saved: {relative_path}")

savage_copy(SOURCE_DIR, OUTPUT_DIR)
print("[PTMSavior] ✅ Complete. All savage files archived.")