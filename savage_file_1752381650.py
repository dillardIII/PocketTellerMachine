```python
# Python file that executes the given task

def generate_or_repair_file(filename, data):
    try:
        with open(filename, 'x') as file: 
            file.write(data)
            print(f'File {filename} has been generated successfully.')
    except FileExistsError:
        with open(filename, 'w') as file: 
            file.write(data)
            print(f'File {filename} has been repaired successfully.')
    except Exception as e:
        print(f'Unable to generate or repair the file. Error: {str(e)}')

data = """
def say_hello():
    print('Hello, world!')

def calculate_sum(num1, num2):
    return num1 + num2

say_hello()
print(calculate_sum(3, 7))
"""

generate_or_repair_file('my_python_file.py', data)
```