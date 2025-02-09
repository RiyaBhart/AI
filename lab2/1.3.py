class GoalBasedAgent:
    def __init__(self, goal):
        self.goal = goal

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "goal reached"
        return "searching"

    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)
        if goal_status == "goal reached":
            return f"Goal {self.goal} found!"
        else:
            return environment.ucs_search(percept, self.goal)

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def ucs_search(self, start, goal):
        frontier = [(0, start, [])] 
        explored = set()

        while frontier:
            frontier.sort() 
            cost, node, path = frontier.pop(0)

            if node in explored:
                continue

            path = path + [node]
            explored.add(node)

            if node == goal:
                print(f"Goal found with UCS. Path: {path}, Cost: {cost}")
                return f"Goal {goal} reached with cost {cost}"

            for neighbor, edge_cost in self.graph.get(node, []):
                if neighbor not in explored:
                    frontier.append((cost + edge_cost, neighbor, path))

        return "Goal not reachable"

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 5), ('E', 2)],
    'C': [('F', 3), ('G', 6)],
    'D': [('H', 2)],
    'E': [],
    'F': [('I', 1)],
    'G': [],
    'H': [],
    'I': []
}

start_node = 'A'
goal_node = 'I'

agent = GoalBasedAgent(goal_node)  
environment = Environment(graph)

run_agent(agent, environment, start_node)
