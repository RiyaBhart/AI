from collections import deque

class BidirectionalSearch:
    def __init__(self, graph):
        self.graph = graph

    def bidirectional_search(self, start, goal):
        if start == goal:
            return [start]

        front_visited = {start: None}
        back_visited = {goal: None}

        front_queue = deque([start])
        back_queue = deque([goal])

        while front_queue and back_queue:
            self.expand_layer(front_queue, front_visited, back_visited, direction="forward")
            self.expand_layer(back_queue, back_visited, front_visited, direction="backward")

            intersecting_node = self.find_intersection(front_visited, back_visited)
            if intersecting_node:
                return self.build_path(front_visited, back_visited, intersecting_node)
        return None

    def expand_layer(self, queue, visited, other_visited, direction):
        current = queue.popleft()
        for neighbor in self.graph.get(current, []):
            if neighbor not in visited:
                visited[neighbor] = current
                queue.append(neighbor)

    def find_intersection(self, front_visited, back_visited):
        return set(front_visited.keys()).intersection(back_visited.keys())

    def build_path(self, front_visited, back_visited, intersection):
        path = []
        current = intersection

        while current is not None:
            path.append(current)
            current = front_visited[current]

        path = path[::-1]
        current = back_visited[intersection]

        while current is not None:
            path.append(current)
            current = back_visited[current]

        return path


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C'],
    'G': ['C']
}

bidirectional = BidirectionalSearch(graph)
result = bidirectional.bidirectional_search('A', 'F')
print("Bidirectional Search Path:", result)
