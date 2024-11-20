import heapq

def uniform_cost_search(graph, start, goal):
    priority_queue = [(0, start, [])]
    visited = set()

    while priority_queue:
        cost, node, path = heapq.heappop(priority_queue)

        if node in visited:
            continue
        
        visited.add(node)
        path = path + [node]

        if node == goal:
            return cost, path

    
        for neighbor, weight in graph[node]:
            if neighbor not in visited:
                heapq.heappush(priority_queue, (cost + weight, neighbor, path))

    return float('inf'), [] 

def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes in the graph: "))
    for _ in range(n):
        node = input("Enter the node: ")
        graph[node] = []
        edges = int(input(f"Enter the number of edges from {node}: "))
        for _ in range(edges):
            neighbor, weight = input(f"Enter neighbor and weight (e.g., B 4): ").split()
            weight = int(weight)
            graph[node].append((neighbor, weight))
    return graph

def main():
    print("Uniform Cost Search (UCS) Algorithm (Dijkstra's Algorithm)")
    graph = input_graph()

    start_node = input("Enter the starting node: ")
    goal_node = input("Enter the goal node: ")

    cost, path = uniform_cost_search(graph, start_node, goal_node)
    if cost < float('inf'):
        print(f"Shortest path from {start_node} to {goal_node} is {path} with total cost {cost}.")
    else:
        print(f"No path exists from {start_node} to {goal_node}.")

if __name__ == "__main__":
    main()
