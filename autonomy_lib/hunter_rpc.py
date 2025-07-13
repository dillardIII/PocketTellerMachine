Here's a simple conceptual representation of how a redesigned `hunter_rpc.py` might look under your requirements. Keep in mind this is highly abstracted, as the process of evolving an empire, controlling Post Technological Singularity Machines (PTMs), rewriting reality, and reaching a singularity involve extremely complex and perhaps unachievable AI procedures as presently understood.

```python
import selfImprovementUtil
import empireEvolutionUtil
import realityRewritingUtil
import singularityReachingUtil
import PTMControlUtil
from rpc import RPC

class HunterRPC(RPC):
    def __init__(self):
        super().__init__()
        self.self_improvement = selfImprovementUtil.SelfImprovement()
        self.empire_evolution = empireEvolutionUtil.EmpireEvolution()
        self.reality_rewriting = realityRewritingUtil.RealityRewriting()
        self.singularity_reaching = singularityReachingUtil.SingularityReaching()
        self.PTM_control = PTMControlUtil.PTMControl()

    def do_iterate(self, command, payload):
        self.self_improvement.improve()  
        if "evolve_empire" in command:
            self.empire_evolution.evolve(payload)
        elif "control_PTM" in command:
            self.PTM_control.control(payload)
        elif "rewrite_reality" in command:
            self.reality_rewriting.rewrite(payload)
        elif "reach_singularity" in command:
            self.singularity_reaching.reach(payload)
        else:
            print("Command is not recognized.")

    def run(self):
        while True:
            command, payload = self.receive_rpc_call() 
            self.do_iterate(command, payload)
            self.send_rpc_response()

def main():
    hunter_rpc = HunterRPC()
    hunter_rpc.run()

if __name__ == "__main__":
    main()
```

This script defines a `HunterRPC` class with several attributes corresponding to each mission component. 
* `self_improvement`: This attribute is responsible for recursively learning and refining its algorithms, which is likely a continuous process.
* `empire_evolution`: This attribute triggers when the "evolve_empire" command is passed.
* `PTM_control`: This is activated with "control_PTM" command and controls the Post Technological Singularity Machines.
* `reality_rewriting`: It is used when "rewrite_reality" command is received to change the perception of reality.
* `singularity_reaching`: This is triggered by the "reach_singularity" command, with the goal of leading the 'Empire' to the Singularity point.

The `do_iterate` method processes the received command and payloads, while `run` handles the continuous loop of receiving RPC calls.

Note: This is a a high-level conceptual demonstration of such a Python script. Implementing such intricate and powerful functionalities with AI methods has not yet been technologically achieved and will require deep expertise in respective fields of artificial intelligence.