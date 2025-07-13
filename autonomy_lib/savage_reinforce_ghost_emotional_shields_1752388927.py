Sure, here's a small Python script that would "execute a macro" to "reinforce ghost emotional shields" symbolically.

```python
class Entity:
    def __init__(self, name):
        self.name = name
        self.shields = 0

    def reinforce_shields(self, amount):
        self.shields += amount
        print(f"Reinforcing {self.name}'s shields by {amount}. New shields level: {self.shields}.")

class SavageEmpireAI:
    ghosts = []

    def __init__(self):
        pass

    def add_ghost(self, ghost):
        self.ghosts.append(ghost)

    def reinforce_ghost_shields(self):
        for ghost in self.ghosts:
            ghost.reinforce_shields(3)

if __name__ == "__main__":
    ai = SavageEmpireAI()

    # Sample Ghosts
    ghost_one = Entity('Ghost 1')
    ghost_two = Entity('Ghost 2')
    ghost_three = Entity('Ghost 3')

    # Add ghosts to AI
    ai.add_ghost(ghost_one)
    ai.add_ghost(ghost_two)
    ai.add_ghost(ghost_three)

    # Reinforce Ghost Shields
    ai.reinforce_ghost_shields()
```

This script creates a model for an "Entity" (which can be a ghost with emotional shields). The SavageEmpireAI class can handle multiple ghosts and reinforce their shields. In the main part of the script, it initiates some sample ghosts, adds them to the AI, and then reinforces their shields.