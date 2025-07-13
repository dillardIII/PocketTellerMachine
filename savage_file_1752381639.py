```python
import os

def generate_or_repair_file(file_name):
    if not os.path.isfile(file_name):
        with open(file_name, 'w') as file:
            file.write("""
import os

def check_and_repair(file_name):
    if os.path.isfile(file_name):
        print(f"{file_name} exists.")
    else:
        print(f"{file_name} does not exist. Creating file now...")
        with open(file_name, 'w') as new_file:
            print(f"{file_name} has been created.")

check_and_repair('sample_file.txt')
            """)
        print(f"{file_name} has been created.")
    else:
        print(f"{file_name} already exists.")

generate_or_repair_file('python_file.py')
```