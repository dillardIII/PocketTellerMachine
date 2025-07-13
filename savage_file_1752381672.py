```python
import os

def generate_or_repair_file(file_name, file_content):
    # Check if file exists
    if os.path.exists(file_name):
        # Open file in read mode and check its contents
        with open(file_name, 'r') as file:
            if file.read() != file_content:
                # If content is not equal to the specified one, rewrite file
                with open(file_name, 'w') as file:
                    file.write(file_content)
    else:
        # If file does not exist, create it with the specified content
        with open(file_name, 'w') as file:
            file.write(file_content)

# Specify file name and content
file_name = "example.py"
file_content = """
print('Hello, World!')
"""

# Perform the generation or repair of the file
generate_or_repair_file(file_name, file_content)
```