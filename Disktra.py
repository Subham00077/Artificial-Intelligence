import heapq 
def dijkstra(graph, source, destination, V): 
path[source] = [source]  
while priority_queue: 
curr_distance, curr_vertex = heapq.heappop(priority_queue) 
if curr_vertex == destination: 
print(f"Shortest distance from {source} to {destination}: {curr_distance}")
print(f"Path: {' -> '.join(map(str, path[curr_vertex]))}") 
return 
distance = curr_distance + weight 
path[neighbor] = path[curr_vertex] + [neighbor]  
print(f"No path exists from {source} to {destination}.") 
graph[u][v] = w 
graph[v][u] = w 
 
 if     name 	== "   main    ": 
V = int(input("Enter the number of vertices: ")) 
E = int(input("Enter the number of edges: "))  
u, v, w = map(int, input().split()) add_edge(graph, u, v, w) 
destination = int(input("Enter the destination vertex: ")) 
