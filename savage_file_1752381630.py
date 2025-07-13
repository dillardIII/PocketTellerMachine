```python
import os
import shutil

class ImperiumEmpireGenerator():
    def __init__(self, filename):
        self.filename = filename
        self.basic_structure = '''import os
import hashlib

class Empire:
    def __init__(self, name, origin, max_population):
        self.name = name
        self.origin = origin
        self.max_population = max_population

    def execute_order(self, order_number):
        print(f'Executing Order {order_number} in {self.name} Empire.')

    def expand_territory(self, new_territories):
        self.max_population += new_territories * 1000000
        print(f'New territories have been conquered! The maximum population is now: {self.max_population}.')

    def __str__(self):
        return f'Empire Name: {self.name}\\nOrigin: {self.origin}\\nMax Population: {self.max_population}'

if __name__ == "__main__":
    empire1 = Empire("Roman", "Italy", 1000000)
    print(empire1)
    empire1.execute_order(66)
    empire1.expand_territory(3)
'''
        
    def _check_file_existence(self):
        return os.path.isfile(self.filename)
    
    def _generate_file(self):
        with open(self.filename, 'w') as f:
            f.write(self.basic_structure)
        print(f'Successfully generated {self.filename} file.')
    
    def _repair_file(self):
        err = False
        if os.stat(self.filename).st_size == 0:
            err = True
        else:
            with open(self.filename, 'r') as f:
                if hashlib.md5(f.read().encode()).hexdigest() != hashlib.md5(self.basic_structure.encode()).hexdigest():
                    err = True
        if err:
            print(f'Error detected in existing {self.filename} file, attempting repair.')
            os.remove(self.filename)
            self._generate_file()
        else:
            print(f'No Error detected in {self.filename} file.')
                
    def generate_or_repair_file(self):
        if self._check_file_existence():
            self._repair_file()
        else:
            self._generate_file()

if __name__ == "__main__":
    generator = ImperiumEmpireGenerator("empire.py")
    generator.generate_or_repair_file()
```
