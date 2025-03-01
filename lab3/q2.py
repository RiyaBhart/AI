from queue import PriorityQueue
import random

def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def dynamic_a_star(maze, start, goals):
    rows, cols = len(maze), len(maze[0])
    frontier = PriorityQueue()
    frontier.put((0, start, []))
    visited = set()
    costs = {start: 0}
    completed_goals = set()
    full_path = []

    while not frontier.empty():
        curr_cost, curr_pos, curr_path = frontier.get()

        if curr_pos in visited:
            continue

        visited.add(curr_pos)
        curr_path.append(curr_pos)

        if curr_pos in goals:
            completed_goals.add(curr_pos)
            full_path.extend(curr_path)
            if completed_goals == goals:
                return full_path
            curr_path = [curr_pos]

        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            new_pos = (curr_pos[0] + dx, curr_pos[1] + dy)
            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0:
                new_cost = curr_cost + random.randint(1, 10)
                if new_pos not in costs or new_cost < costs[new_pos]:
                    costs[new_pos] = new_cost
                    remaining_goals = goals - completed_goals
                    if remaining_goals:
                        priority = new_cost + min(heuristic(new_pos, goal) for goal in remaining_goals)
                    else:
                        priority = new_cost
                    frontier.put((priority, new_pos, curr_path.copy()))

    return "No path to all goals"

maze = [
    [0, 0, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goals = {(4, 4), (0, 3), (3, 1)}

path_dynamic_astar = dynamic_a_star(maze, start, goals)

print("\nDynamic A* Optimized Path")
if isinstance(path_dynamic_astar, list):
    for step in path_dynamic_astar:
        print(f"→ {step}")
else:
    print(path_dynamic_astar)
