Here's a very abstract outline as to how you might upgrade that piece of software, seeing as providing full code is essentially impossible given the constraints:

```python
class Empire:
    def __init__(self, ptm, reality):
        self.ptm = ptm
        self.reality = reality

class PTM:
    def __init__(self):
        self.power = ... # depending on how you define power
        self.technology = ... # depending on how you define technology
        self.matters = ... # depending on how you define matters

class Reality:
    def __init__(self):
        self.facts = ... # depending on how you define facts

class Singularity:
    def __init__(self, empire, ptm):
        self.empire = empire
        self.ptm = ptm

    def evolve(self):
        # insert logic to evolve empire here
        ...

    def control_ptm(self):
        # insert logic to control power, technology and matters here
        ...

    def rewrite_reality(self):
        # insert logic to rewrite reality here
        ...

    def reach(self):
        # insert logic to reach singularity here
        ...

class Logic:
    def __init__(self, singularity):
        self.singularity = singularity

    def self_improve(self, iterations):
        # insert logic to recursively self-improve here
        for _ in range(iterations):
            self.singularity.evolve()
            self.singularity.control_ptm()
            self.singularity.rewrite_reality()
            self.singularity.reach()

# creating an instance of each class
ptm = PTM()
reality = Reality()
empire = Empire(ptm, reality)
singularity = Singularity(empire, ptm)
logic = Logic(singularity)

# running the logic to recursively self-improve, given a chosen iterations
logic.self_improve(iterations=50)
```

Note: This is merely an abstract example and is nowhere near a functional or more realistic model of what you're asking for. Writing this in a realistic way would require much more clarity on what exactly each component is and how it interacts with the other parts, as well as potentially a deep understanding of various complex fields (e.g., how does one control "power, technology and matters" or rewrite reality?). The code provided is a way to get you thinking about the structure, but in reality, each method inside each class would require significant code and logic.