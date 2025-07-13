To create a standalone Python script named `ghost_brain_upgrade.py`, which either creates a new file or repairs an existing file, you can use the following approach. This script uses simple file handling operations to ensure the presence of the critical file. If the file is missing, it creates it with some basic content; if it's corrupted or empty, it repairs the file by adding default content.

Here's an example script:

```python
import os

def is_file_corrupted(file_path):
    """Check if the file is empty or has invalid content indicating corruption."""
    try:
        with open(file_path, 'r') as file:
            content = file.read().strip()
            # Here, you can define criteria for what constitutes 'corrupted'
            # For simplicity, assume a valid file must have a specific keyword
            valid_content = "UPGRADE_VERSION"
            if valid_content in content:
                return False
            else:
                return True
    except Exception:
        return True

def create_or_repair_file(file_path):
    """Creates or repairs the critical autonomy file."""
    if not os.path.exists(file_path) or is_file_corrupted(file_path):
        print(f"Creating or repairing {file_path}...")
        with open(file_path, 'w') as file:
            # Adding some default critical content
            file.write("# Critical Autonomy File\n")
            file.write("UPGRADE_VERSION = '1.0.0'\n")
            file.write("\n")
            file.write("# Add further enhancements or patches below\n")
        print(f"{file_path} has been created or repaired successfully.")
    else:
        print(f"{file_path} is present and not corrupted.")

if __name__ == "__main__":
    file_name = "ghost_brain_upgrade.py"
    create_or_repair_file(file_name)
```

### How it works:
- **File Existence:** The script checks if `ghost_brain_upgrade.py` exists. If not, it creates it.
- **File Integrity:** The function `is_file_corrupted` checks if the file content is corrupted by looking for a specific keyword (`UPGRADE_VERSION`). You can customize the corruption criteria according to your needs.
- **Repair or Create:** If the file is missing or deemed corrupted, it creates or overwrites the file with some default content that signifies a minimal working file.

### Usage:
- Save the script to a file, e.g., `create_or_repair_ghost_brain.py`.
- Run the script using a Python interpreter to ensure the presence and integrity of `ghost_brain_upgrade.py`. This would typically be executed at a scheduled time or as part of a startup routine to safeguard the availability of critical files.
# 🔥 Auto-mutated at 2025-07-13T11:34:20.242653 with quantum pulse.