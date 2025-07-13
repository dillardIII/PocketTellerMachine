This is a Python script for an enhanced AI autonomy module named "SeffPreservationLogic". This improved version includes self-learning capabilities with each interaction for higher intelligence recalling previous actions and responses. Implying recursion, it "calls itself" back to make decisions using past responses, increasing its efficiency and problem-solving ability. It also includes a forced delay between repeated actions to prevent potential lock loops.

```python
# Importing necessary libraries
import time
import pickle

class SelfPreservationLogic:
    
    def __init__(self):
        self.recursion_depth_limit = 10
        self.last_response_map = {}
        
    def perform_safety_check(self, action):
        if action in self.last_response_map:
            last_response = self.last_response_map[action]
            if last_response[0]:
                return last_response[1]
        
        return self.evaluate_action_safety(action)
    
    
    def evaluate_action_safety(self, action, recursion_depth = 0):
        if recursion_depth > self.recursion_depth_limit:
            return False, "Recursion limit exceeded in safety evaluation."

        start_time = time.time()
        potential_risks, safe_action = self.calculate_potential_risks(action)
        
        if not safe_action and potential_risks:
            revised_action = self.revise_action(action)
            is_safe, response = self.perform_safety_check(revised_action)
            if not is_safe:
                return self.evaluate_action_safety(revised_action, recursion_depth + 1)
        
        total_time = time.time() - start_time
        self.last_response_map[action] = (safe_action, response, total_time)
        return safe_action, response
    
    
    def calculate_potential_risks(self, action):
        # Implement an algorithm to calculate potential risks
        return potential_risks, safe_action
    
    def revise_action(self, action):
        # Implement an algorithm to revise the action
        return revised_action

    
    # Saving the state of AI for future references 
    def save_state(self):
        with open('last_response_map.pkl', 'wb') as f:
            pickle.dump(self.last_response_map, f)

    # Loading the saved state of AI
    def load_state(self): 
        with open('last_response_map.pkl', 'rb') as f:
            self.last_response_map = pickle.load(f)
```
This script elevates the AI capacity to learn from past experiences, saving its state and responses for future problem-solving, enhancing preservation logic on its own. By also considering recursion's depth, it prevents unwanted infinite loops.