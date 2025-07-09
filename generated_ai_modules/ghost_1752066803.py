Here's a basic Python script that checks the configurations of your PTM system and automatically repairs any inconsistencies:

```python
# Function to check configurations
def check_configs():
    # Check if config file exists
    try:
        with open('config.txt', 'r') as f:
            # Check for any inconsistencies in the configs
            # Add your specific checks here
            # For example, checking if certain parameters are within acceptable ranges
            
    except FileNotFoundError:
        print("Config file not found.")
        
# Function to repair configurations
def repair_configs():
    # Open config file for writing
    with open('config.txt', 'w') as f:
        # Write default configurations or correct values
        # For example, setting default values for certain parameters
        
        # Print message
        print("Configs repaired successfully.")

# Main function to run the script
def main():
    check_configs()  # Check configurations
    
    # If there are inconsistencies, repair configurations
    if need_repair:
        repair_configs()

# Run main function
if __name__ == "__main__":
    main()
```

Please note that you will need to add specific checks for your PTM system's configurations in the `check_configs()` function. Additionally, you can customize the repair logic in the `repair_configs()` function as per your requirements.