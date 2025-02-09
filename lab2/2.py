class TSP:
    def __init__(self, graph):
        self.graph = graph
        self.num_cities = len(graph)

    def ucs_tsp(self, start):
        queue = [(0, [start])]
        best_path = None
        min_cost = float('inf')

        while queue:
            cost, path = queue.pop(0)
            current_city = path[-1]

            if len(path) == self.num_cities:
                total_cost = cost + self.graph[current_city][start]
                if total_cost < min_cost:
                    min_cost = total_cost
                    best_path = path + [start]
                continue

            for neighbor in self.graph[current_city]:
                if neighbor not in path:
                    new_cost = cost + self.graph[current_city][neighbor]
                    new_path = path + [neighbor]
                    queue.append((new_cost, new_path))

        return best_path, min_cost

graph = {
    'A': {'B': 10, 'C': 15, 'D': 20},
    'B': {'A': 10, 'C': 35, 'D': 25},
    'C': {'A': 15, 'B': 35, 'D': 30},
    'D': {'A': 20, 'B': 25, 'C': 30}
}

tsp_solver = TSP(graph)
best_route, min_cost = tsp_solver.ucs_tsp('A')

print("Optimal Route:", " → ".join(best_route))
print("Minimum Cost:", min_cost)
