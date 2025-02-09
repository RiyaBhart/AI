class GraphTree:
    def __init__(self, graph):
        self.graph = graph

    def dls(self, node, goal, depth):
        if depth == 0:
            return [node] if node == goal else None
        if depth > 0:
            for neighbor in self.graph.get(node, []):
                result = self.dls(neighbor, goal, depth - 1)
                if result:
                    return [node] + result
        return None

    def iddfs(self, start, goal, max_depth):
        for depth in range(max_depth + 1):
            result = self.dls(start, goal, depth)
            if result:
                return result
        return None


graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': [],
    'E': [],
    'F': [],
    'G': []
}

gt = GraphTree(graph)
result = gt.iddfs('A', 'F', max_depth=3)
print("IDDFS Path:", result)
