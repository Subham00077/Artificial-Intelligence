from collections import deque, defaultdict

class Graph:
    def __init__(self):
        self.adj_list = defaultdict(list)

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        traversal = []

        while queue:
            vertex = queue.popleft()

            if vertex not in visited:
                visited.add(vertex)
                traversal.append(vertex)

                
                for neighbor in self.adj_list[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return traversal

    def display_graph(self):

        for key, value in self.adj_list.items():
            print(f"{key} -> {', '.join(map(str, value))}")


def main():
    print("Graph 1:")
    graph1 = Graph()
    graph1.add_edge(0, 1)
    graph1.add_edge(0, 2)
    graph1.add_edge(1, 3)
    graph1.add_edge(1, 4)
    graph1.add_edge(2, 5)
    graph1.add_edge(2, 6)
    graph1.display_graph()
    print("BFS Traversal from node 0:", graph1.bfs(0))

    print("\nGraph 2:")
    graph2 = Graph()
    graph2.add_edge('A', 'B')
    graph2.add_edge('A', 'C')
    graph2.add_edge('B', 'D')
    graph2.add_edge('B', 'E')
    graph2.add_edge('C', 'F')
    graph2.add_edge('E', 'G')
    graph2.display_graph()
    print("BFS Traversal from node 'A':", graph2.bfs('A'))

    print("\nGraph 3 (Disconnected Graph):")
    graph3 = Graph()
    graph3.add_edge(1, 2)
    graph3.add_edge(2, 3)
    graph3.add_edge(4, 5)
    graph3.display_graph()
    print("BFS Traversal from node 1:", graph3.bfs(1))
    print("BFS Traversal from node 4:", graph3.bfs(4))


if __name__ == "__main__":
    main()
