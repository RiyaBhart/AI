class GoalBasedAgent:
    def __init__(self, goal, depth_limit=5):  
        self.goal = goal
        self.depth_limit = depth_limit

    def formulate_goal(self, percept):
        if percept == self.goal:
            return "goal reached"
        return "searching"

    def act(self, percept, environment):
        goal_status = self.formulate_goal(percept)
        if goal_status == 'goal reached':
            return f"Goal {self.goal} found!"
        else:
            return environment.dls_search(percept, self.goal, self.depth_limit)

class Environment:
    def __init__(self, graph):
        self.graph = graph

    def get_percept(self, node):
        return node

    def dls_search(self, start, goal, depth_limit):
        visited = []

        def dfs(node, depth):
            if depth > depth_limit:
                return None
            if node == goal:
                print(f"Goal found with DLS. Path: {visited + [node]}")
                return visited + [node]

            visited.append(node) 

            for neighbour in self.graph.get(node, []):
                if neighbour not in visited:
                    path = dfs(neighbour, depth + 1)
                    if path:
                        return path

            visited.pop()  
            return None

        return dfs(start, 0)

def run_agent(agent, environment, start_node):
    percept = environment.get_percept(start_node)
    action = agent.act(percept, environment)
    print(action)

tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': ['H'],
    'E': [],
    'F': ['I'],
    'G': [],
    'H': [],
    'I': []
}

start_node = 'A'
goal_node = 'I'

agent = GoalBasedAgent(goal_node, depth_limit=3)  
environment = Environment(tree)

run_agent(agent, environment, start_node)
