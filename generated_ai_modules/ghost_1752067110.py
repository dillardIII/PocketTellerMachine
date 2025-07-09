Here is a sample Python script that checks the configurations of your PTM system and auto-repairs them if any issues are found:

```python
def check_configs():
    # Check configurations for any issues
    config1 = load_config('config1.txt')
    config2 = load_config('config2.txt')
    
    if not config1:
        print('Error: config1 is missing or empty, auto-repairing...')
        repair_config('config1.txt')
    
    if not config2:
        print('Error: config2 is missing or empty, auto-repairing...')
        repair_config('config2.txt')
    
def load_config(filename):
    # Load configuration from a file
    try:
        with open(filename, 'r') as file:
            config = file.read()
            return config
    except FileNotFoundError:
        return None

def repair_config(filename):
    # Auto-repair configuration file
    default_config = get_default_config(filename)
    
    with open(filename, 'w') as file:
        file.write(default_config)
    
    print(f'{filename} has been repaired with default configuration')

def get_default_config(filename):
    # Get default configuration for the specified file
    if filename == 'config1.txt':
        return 'default_config1_data'
    elif filename == 'config2.txt':
        return 'default_config2_data'
    else:
        return ''

# Main function
if __name__ == '__main__':
    check_configs()
```

You can customize this script further based on your specific requirements and configurations. You may need to update the `get_default_config()` function to provide actual default configurations for your system, and also add more checks or repairs as needed. Make sure to test this script thoroughly before using it in a production environment.