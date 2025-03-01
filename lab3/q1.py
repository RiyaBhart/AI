from queue import PriorityQueue

class Node:
    def __init__(self, position, parent=None, cost=0, goals_left=None):
        self.position = position
        self.parent = parent
        self.cost = cost
        self.goals_left = goals_left if goals_left else set()

    def __lt__(self, other):
        return self.cost < other.cost

def heuristic(current_pos, goals_left):
    if not goals_left:
        return 0
    return min(abs(current_pos[0] - g[0]) + abs(current_pos[1] - g[1]) for g in goals_left)

def reconstruct_path(node):
    path = []
    while node:
        path.append(node.position)
        node = node.parent
    return path[::-1]

def best_first_search_multiple_goals(maze, start, goal_positions):
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start, None, 0, set(goal_positions))
    frontier = PriorityQueue()
    frontier.put((0, start_node))
    visited = set()

    while not frontier.empty():
        _, current_node = frontier.get()
        current_pos = current_node.position
        goals_left = current_node.goals_left.copy()

        if current_pos in goals_left:
            goals_left.remove(current_pos)

        if not goals_left:
            return reconstruct_path(current_node)

        visited.add((current_pos, frozenset(goals_left)))

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)

            if (0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and
                maze[new_pos[0]][new_pos[1]] == 0):

                new_node = Node(new_pos, current_node, current_node.cost + 1, goals_left)

                if (new_pos, frozenset(goals_left)) not in visited:
                    frontier.put((heuristic(new_pos, goals_left) + new_node.cost, new_node))

    return None

maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goal_positions = [(4, 4), (2, 3)]

path = best_first_search_multiple_goals(maze, start, goal_positions)
if path:
    print("Shortest Path covering all goals:", path)
else:
    print("No path found")
