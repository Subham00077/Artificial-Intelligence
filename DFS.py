class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def dfs(self, start, visited=None):
        
        if visited is None:
            visited = set()

        visited.add(start)
        print(start, end=" ")

        for neighbor in self.graph.get(start, []):
            if neighbor not in visited:
                self.dfs(neighbor, visited)


if __name__ == "__main__":

    g1 = Graph()
    g1.add_edge(0, 1)
    g1.add_edge(0, 2)
    g1.add_edge(1, 2)
    g1.add_edge(2, 0)
    g1.add_edge(2, 3)
    g1.add_edge(3, 3)

    print("DFS for Graph 1 starting from vertex 2:")
    g1.dfs(2)
    print("\n")


    g2 = Graph()
    g2.add_edge("A", "B")
    g2.add_edge("A", "C")
    g2.add_edge("B", "D")
    g2.add_edge("C", "D")
    g2.add_edge("D", "E")
    g2.add_edge("E", "A")

    print("DFS for Graph 2 starting from vertex 'A':")
    g2.dfs("A")
    print("\n")

    g3 = Graph()
    g3.add_edge(1, 2)
    g3.add_edge(2, 3)
    g3.add_edge(4, 5)

    print("DFS for Graph 3 starting from vertex 1:")
    g3.dfs(1)
    print("\n")
    
    print("DFS for Graph 3 starting from vertex 4:")
    g3.dfs(4)
    print("\n")
