class Environment:
    def __init__(self):
        self.rooms = ['no fire', 'no fire', 'fire', 
                      'no fire', 'fire', 'no fire', 
                      'no fire', 'no fire', 'fire']

    def get_percept(self, position):
        return self.rooms[position]

    def extinguish_fire(self, position):
        self.rooms[position] = 'no fire'

    def show_rooms(self):
        visual_representation = ["🔥" if room == "fire" else " " for room in self.rooms]
        print(" | ".join(visual_representation))

class Agent:
    def __init__(self):
        self.position = 0

    def act(self, percept, environment):
        if percept == "fire":
            print(f"🔥 Fire detected in Room {self.position}! Extinguishing...")
            environment.extinguish_fire(self.position)

    def move(self):
        if self.position < len(environment.rooms) - 1: 
            self.position += 1

def RunAgent(agent, environment):
    for i in range(len(environment.rooms)):
        print(f"\nStep {i}:")
        percept = environment.get_percept(agent.position)  
        agent.act(percept, environment)  

        print(f"Agent Position {agent.position} -> Percept: {percept}")
        environment.show_rooms()
        agent.move()

agent = Agent()
environment = Environment()
print("\n🔥 Initial Environment:")
environment.show_rooms()
RunAgent(agent, environment)
print("\n✅ Final Environment (All fires extinguished):")
environment.show_rooms()
