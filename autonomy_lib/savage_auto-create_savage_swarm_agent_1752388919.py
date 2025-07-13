Below is your mutated Python script:

```python
import concurrent.futures
from threading import Thread

class SavageSwarmAgent:
    def __init__(self, agent_id):
        self.agent_id = agent_id
        self.state = "IDLE"

    def execute_action(self, action, target):
        """
        Execute the specified action on given target.
        """
        # Modify this placeholder function with the desired action
        self.state = "BUSY"
        print(f"Agent {self.agent_id} executing {action} on {target}")
        # Simulate action and update state upon completion
        self.state = "IDLE"

    def gather_info(self, source):
        """
        Gather info from the specified source
        """
        # Modify this placeholder function with desired info gathering 
        self.state = "BUSY"
        print(f"Agent {self.agent_id} gathering information from {source}")
        # Simulate info gathering update state upon completion
        self.state = "IDLE"


class SavageEmpire:
    def __init__(self):
        self.swarm_agents = []

    def auto_create_savage_swarm_agent(self):
        new_id = len(self.swarm_agents)
        new_agent = SavageSwarmAgent(new_id)
        self.swarm_agents.append(new_agent)
        print(f"New Savage Swarm Agent {new_id} created!")

    def assign_task(self, action, target):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            free_agents = [agent for agent in self.swarm_agents if agent.state == "IDLE"]
            if free_agents:
                executor.map(lambda agent: agent.execute_action(action, target), free_agents)
            else:
                print("All agents are busy.")

    def gather_info(self, source):
        with concurrent.futures.ThreadPoolExecutor() as executor:
            free_agents = [agent for agent in self.swarm_agents if agent.state == "IDLE"]
            if free_agents:
                executor.map(lambda agent: agent.gather_info(source), free_agents)
            else:
                print("All agents are busy.")

# Create a new instance and auto-generate agents
savage_empire = SavageEmpire()
for _ in range(10):
    savage_empire.auto_create_savage_swarm_agent()
```

In this mutated script, the SavageSwarmAgent's `execute_action` and `gather_info` functions have been transformed to perform tasks with concurrent execution by forming use of python’s built-in `concurrent.futures.ThreadPoolExecutor`. The `assign_task` and `gather_info` functions inside the SavageEmpire class ensure that only free agents (i.e., those not in the "BUSY" state are assigned tasks).