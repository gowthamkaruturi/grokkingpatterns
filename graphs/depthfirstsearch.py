class DFS:
    def __init__(self, visited:set, graph : dict) -> None:
        self.visited = visited
        self.graph = graph

    def dfs(self,node):
        self.visited.add(node)
        for neighbor in self.graph[node]:
            if neighbor not in self.visited:
                self.dfs(neighbor)

    

if __name__ == "__main__":
    graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
    }
    dfs = DFS(set(),graph)
    dfs.dfs('A')