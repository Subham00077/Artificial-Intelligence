from collections import deque 
visited = [False] * len(adj) 
parent = [-1] * len(adj)
q.append(s_index) 
while q: 
curr = q.popleft() 
break 
if not visited[neighbor]: visited[neighbor] = True parent[neighbor] = curr 
q.append(neighbor) 
curr = end_index 
while curr != -1: 
path.append(index_to_vertex[curr]) 
curr = parent[curr] 
 
return path[::-1] 
 
 
def add_edge(adj, u_index, v_index): adj[u_index].append(v_index) adj[v_index].append(u_index) 
 
def main(): 
input_filename = "input.txt" output_filename = "output.txt" 
 
vertex_to_index = {} index_to_vertex = [] 
 
with open(input_filename, 'r') as file: V = int(file.readline().strip()) adj = [[] for _ in range(V)] 
E = int(file.readline().strip()) 
 
 
for _ in range(E): 
u, v = file.readline().strip().split() if u not in vertex_to_index: vertex_to_index[u] = len(index_to_vertex) index_to_vertex.append(u) 
if v not in vertex_to_index: 
vertex_to_index[v] = len(index_to_vertex) index_to_vertex.append(v) 
add_edge(adj, vertex_to_index[u], vertex_to_index[v]) 
 
 
start_vertex = file.readline().strip() 
end_vertex = file.readline().strip() 
 
if start_vertex not in vertex_to_index or end_vertex not in vertex_to_index: 
print(f"Error: Start or end vertex not in graph.") 
return 
start_index = vertex_to_index[start_vertex] 
end_index = vertex_to_index[end_vertex] 
path = bfs(adj, start_index, end_index, index_to_vertex) 
file.write(" -> ".join(path) + "\n") 
 
if  name 	== " main ": 
main() 
 
