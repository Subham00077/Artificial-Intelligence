def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=' ')
    
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    for _ in range(n):
        node = input("Enter the node: ")
        neighbors = input(f"Enter neighbors of {node} separated by space: ").split()
        graph[node] = neighbors
    return graph

def main():
    print("Depth First Search (DFS) Algorithm")
    num_graphs = int(input("Enter the number of graphs to input: "))
    
    for i in range(num_graphs):
        print(f"\nGraph {i + 1}:")
        graph = input_graph()
        start_node = input("Enter the starting node for DFS: ")
        
        print("DFS traversal:", end=' ')
        dfs(graph, start_node)
        print()

if __name__ == "__main__":
    main()
    """Depth First Search (DFS) Algorithm
Enter the number of graphs to input: 1

Graph 1:
Enter the number of nodes in the graph: 4
Enter the node: A
Enter neighbors of A separated by space: B C
Enter the node: B
Enter neighbors of B separated by space: D
Enter the node: C
Enter neighbors of C separated by space: D
Enter the node: D
Enter neighbors of D separated by space: 

Enter the starting node for DFS: A
DFS traversal: A B D C
"""
