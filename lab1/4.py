# utility based agent

class Environment:
    def __init__(self):
        self.components = ['safe', 'low risk vulnerable', 'high risk vulnerable',
                           'low risk vulnerable', 'safe', 'safe', 'low risk vulnerable',
                           'high risk vulnerable', 'safe']

    def get_percept(self, position):
        if self.components[position] == 'low risk vulnerable':
            return 'low risk vulnerable, can be saved'
        elif self.components[position] == 'high risk vulnerable':
            return 'requires purchasing a premium security service'
        elif self.components[position] == 'safe':
            return 'safe'

    def show_components(self):
        print(" | ".join(self.components))

    def patch(self, i):
        if self.components[i] == 'low risk vulnerable':
            self.components[i] = 'safe' 
        elif self.components[i] == 'high risk vulnerable':
            print(f"Component at position {i} requires a premium security service.")  # ✅ Notify without modifying

class Agent:
    def __init__(self):
        self.position = 0

    def act(self, percept, environment):
        environment.patch(self.position) 

    def move(self):
        if self.position < len(environment.components) - 1:
            self.position += 1

def RunAgent(agent, environment, steps):
    for i in range(steps):
        print(f'\nStep {i}:')
        percept = environment.get_percept(agent.position) 
        agent.act(percept, environment)  

        print(f"Agent Position {agent.position} -> Percept: {percept}")
        environment.show_components()
        
        agent.move() 

agent = Agent()
environment = Environment()
environment.show_components()
RunAgent(agent, environment, len(environment.components))
