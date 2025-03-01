from queue import PriorityQueue

def greedy_best_first_delivery(graph, start, deliveries):
    pq = PriorityQueue()
    pq.put((0, start, []))
    visited = set()
    completed_deliveries = set()
    optimized_path = []

    while not pq.empty():
        cost, curr, curr_path = pq.get()

        if curr in visited:
            continue
        visited.add(curr)

        curr_path.append(curr)

        if curr in deliveries:
            completed_deliveries.add(curr)
            optimized_path.extend(curr_path)
            curr_path = []

        if completed_deliveries == deliveries:
            return optimized_path

        for neighbor, travel_cost in graph.get(curr, []):
            if neighbor not in visited:
                pq.put((travel_cost, neighbor, curr_path.copy()))

    return "Not all deliveries are possible."

delivery_graph = {
    'A': [('B', 3), ('C', 5)],
    'B': [('D', 2), ('E', 4)],
    'C': [('E', 1), ('F', 7)],
    'D': [('G', 6)],
    'E': [('G', 3)],
    'F': [('G', 2)],
    'G': []
}

start_location = 'A'
delivery_points = {'D', 'E', 'G'}

delivery_path = greedy_best_first_delivery(delivery_graph, start_location, delivery_points)

print("Optimized Delivery Route:", delivery_path)
