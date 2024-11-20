from collections import defaultdict, deque

def bfs(graph, start_node):
    visited = set()
    queue = deque([start_node])
    traversal_order = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal_order.append(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)

    return traversal_order

def main():
    while True:
        graph = defaultdict(list)
        num_edges = int(input("Enter the number of edges in the graph: "))
        
        print("Enter each edge as 'node1 node2':")
        for _ in range(num_edges):
            u, v = input().split()
            graph[u].append(v)
            graph[v].append(u)  

        print("\nGraph representation:")
        for node, neighbors in graph.items():
            print(f"{node}: {neighbors}")

        start_node = input("\nEnter the starting node for BFS: ")
        if start_node not in graph:
            print(f"Node {start_node} is not present in the graph!")
            continue

        traversal_order = bfs(graph, start_node)
        print("\nBFS Traversal Order:", " -> ".join(traversal_order))

        another = input("\nWould you like to enter another graph? (yes/no): ").strip().lower()
        if another != 'yes':
            break

if __name__ == "__main__":
    main()
