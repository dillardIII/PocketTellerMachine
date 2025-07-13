Below is an example of a Python code which could fit into the context of a game focused on a savage empire, baseline of 'GhostMedic' class which helps your units to recover their health after they have been damaged:

```python

class GhostMedic:
  def __init__(self, health=100, healing_power=10):
    self.health = health
    self.healing_power = healing_power

  def take_damage(self, damage):
    self.health -= damage
    if self.health <= 0:
      self.health = 0
      print("GhostMedic has fallen.")
    else:
      print(f"GhostMedic took {damage} points of damage.")
      print(f"GhostMedic's current health: {self.health}")


  def heal(self, other):
    if self.health <= 0:
      print("GhostMedic cannot heal others because it has fallen.")
      return
    if other.health <= 0:
      print(f"{other.__class__.__name__} cannot be healed because it has fallen.")
      return

    healing_done = min(self.healing_power, other.max_health - other.health)
    other.health += healing_done
    print(f"GhostMedic healed {other.__class__.__name__} for {healing_done} points.")


  def get_status(self):
    if self.health > 70:
      return "Healthy"
    elif self.health > 30:
      return "Injured"
    else:
      return "Critical"

# test the class
ghost_medic = GhostMedic()
```

This code initializes a GhostMedic instance with a certain amount of health and healing power. It provides methods to take damage, heal other instances, and check its health status. 

Please modify it to make it more suitable for your game.