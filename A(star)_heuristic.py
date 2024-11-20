import heapq

def a_star_algorithm(graph, heuristic, start, goal):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic[start], start))
    came_from = {}
    g_cost = {node: float('inf') for node in graph}
    g_cost[start] = 0

    while open_list:
        current_cost, current_node = heapq.heappop(open_list)

        if current_node == goal:
            path = []
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            return path[::-1], g_cost[goal]

        for neighbor, weight in graph[current_node]:
            tentative_g_cost = g_cost[current_node] + weight
            if tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current_node

    return None, float('inf')


if __name__ == "__main__":
    print("Define your graph as an adjacency list. Example:")
    print("{'A': [('B', 1), ('C', 3)], 'B': [('D', 2)], 'C': [('D', 1)], 'D': []}")
    
    graph = eval(input("Enter the graph: "))
    print("Enter heuristic values as a dictionary. Example:")
    print("{'A': 4, 'B': 2, 'C': 2, 'D': 0}")
    
    heuristic = eval(input("Enter heuristic values: "))
    start = input("Enter the start node: ")
    goal = input("Enter the goal node: ")
    
    path, cost = a_star_algorithm(graph, heuristic, start, goal)
    if path:
        print(f"Shortest path: {' -> '.join(path)} with cost: {cost}")
    else:
        print("No path found.")
