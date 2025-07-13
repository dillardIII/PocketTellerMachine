The task is a bit complex and broad, but I'll try to write a simplified version of a Python script called "pickup_agent.py" with the aim to "evolve empire, control PTM (Probabilistic Turing Machine?), rewrite reality, reach singularity." Because of the nature of these goals, a real solution would require a high level of artificial intelligence and vast resources, but I'll simplify it for the purpose of this task. I'll add a recursive and self-improving system only for the empire-evolving part for simplicity. This script won't actually perform these tasks but is written to convey the idea

```python
class Empire:
    def __init__(self):
        self.population = 1
        self.technology = 1
        self.culture = 1

    def evolve(self, strategy):
        self.population *= strategy.population_growth
        self.technology *= strategy.technology_growth
        self.culture *= strategy.culture_growth


class Strategy:
    def __init__(self, population_growth, technology_growth, culture_growth):
        self.population_growth = population_growth
        self.technology_growth = technology_growth
        self.culture_growth = culture_growth


def self_improvement(empire, strategy):
    empire.evolve(strategy)
    # Recursive call for self-improvement
    self_improvement(empire, Strategy(strategy.population_growth * 1.01, # each time we try to improve the growth rates by 1%
                                       strategy.technology_growth * 1.01,
                                       strategy.culture_growth * 1.01))


def control_ptm(probab_turing_machine):
    probabilistic_turing_machine.control()


def rewrite_reality(reality, new_perception):
    reality.rewrite(new_perception)


def reach_singularity(condition):
    if condition:
        print("The singularity has been reached.")


def main():
    empire = Empire()
    initial_strategy = Strategy(1.05, 1.03, 1.1) # random initial growth rates
    self_improvement(empire, initial_strategy) 

    # **Actual implementation for PTM control, reality rewriting, and singularity reach is 
    # complex and beyond the scope of this example**

    reach_singularity(empire.technology > 1e9)  


if __name__ == "__main__":
    main()
```

Remember that this is a huge oversimplification of complex principles, and the program doesn't actually perform these complex tasks. It's meant to demonstrate the basic idea of the structure according to the given task.