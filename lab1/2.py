# A data center runs multiple servers, each hosting different services. These services are
# either underloaded, balanced, or overloaded based on the system's load. The Load
# Balancer Agent is responsible for redistributing tasks across the servers to ensure
# optimal system performance.
# Task:
# ● Create a system with 5 servers.
# ● Each server has a load state of "Underloaded", "Balanced", or "Overloaded".
# ● The Load Balancer Agent must scan the system and move tasks from overloaded
# servers to underloaded ones to balance the load.
# ● After balancing the load, display the updated load status of each server.

import random

class Environment:
    def __init__(self):
        # self.servers = [random.choice(['underloaded', 'balanced', 'overloaded']) for _ in range(5)]
        self.servers=['underloaded','overloaded','balanced','balanced','underloaded']

    def get_percept(self,i):
        return self.servers[i]

    def balance_load(self):
        overloaded = [i for i, state in enumerate(self.servers) if state == 'overloaded']
        underloaded = [i for i, state in enumerate(self.servers) if state == 'underloaded']

        while overloaded and underloaded:
            o_index = overloaded.pop(0)
            u_index = underloaded.pop(0)

            self.servers[o_index] = 'balanced'
            self.servers[u_index] = 'balanced'

    def display_servers(self):
        print(" | ".join(self.servers))

class ReflexAgent:
    def __init__(self):
        self.position = 0

    def act(self, percept, environment):
        environment.balance_load() 

    def move(self):
        if self.position < 4:
            self.position += 1

def RunAgent(agent, environment, steps):
    for step in range(steps):
        print(f"\nStep {step + 1}:")
        percept = environment.get_percept(step)
        agent.act(percept, environment) 

        print(f"Agent Position {agent.position} -> Percept: {percept}")
        environment.display_servers()
        
        agent.move() 


agent = ReflexAgent()
environment = Environment()
RunAgent(agent, environment, 5)
