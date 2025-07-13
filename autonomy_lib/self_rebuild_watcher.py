As an AI language model and to respect OpenAI policy, I am unable to provide a full python code to meet your requirements since evolving empire, controlling PTM (if it is referring to PTM; Prototype Modelling or something else), rewritting reality and reaching singularity are vague concepts in this context and none of which could be achieved with a simple Python script. 

However, for your reference, I can provide guidelines on how you can implement a recursive self-improving logic:

A Python script with Recursive Self-Improvement could be defined as a system that attempts to progressively improve its own structure and functions based on its performance metrics. To implement this, one could apply machine learning techniques, such as NeuroEvolution of Augmenting Topologies (NEAT) or Genetic Algorithms, to adjust the parameters of the function based on its previous performance.

Python pseudo-code could look like this:

```python
class SelfImprovingSystem:
    def __init__(self, initial_version):
        self.version = initial_version
        self.performance = self.evaluate_performance()

    def evaluate_performance(self):
        """
        Here you define a function that based on the system's version evaluates its performance.
        """
        # TODO: Define how to evaluate the system's performance
        return performance

    def improve_system(self):
        """
        This function is supposed to implement the changes on the system based on the performance evaluated.
        """
        # TODO: Define the logic to improve the system

    def evolve(self):
        while True:  # You may want to implement different stopping criteria
            self.improve_system()
            new_performance = self.evaluate_performance()

            if new_performance > self.performance:
                self.performance = new_performance
            else:
                break


initial_version = ...  # Here you define the initial status of your system
system = SelfImprovingSystem(initial_version)
system.evolve()
```
Please bear in mind that this is general pseudo-code and it should be deeply customized and defined to meet your requirements. Moreover, other topics you mentioned, like 'evolving empire', 'reaching singularity' and 'rewritting reality' are abstractions that would need to be defined more clearly and likely could involve techniques and concepts from Game Theory, Decision Making and even Philosophy which lie beyond the scope of a Python script.