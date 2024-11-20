 def dfs_visit(u, G, color, p, D, F, time): 
color[u] = 'g' time[0] += 1 
D[u] = time[0] 
 
for i in range(len(G)): 
if G[u][i] == 1 and color[i] == 'w': p[i] = u 
dfs_visit(i, G, color, p, D, F, time) color[u] = 'b' time[0] += 1 
F[u] = time[0] 
 
def dfs(G, n, start, goal, node_mapping, output_filename): color, p, D, F, time = ['w'] * n, [None] * n, [0] * n, [0] * n, [0] dfs_visit(node_mapping[start], G, color, p, D, F, time) path = [] 
current = node_mapping[goal] while current is not None: path.append(current) current = p[current] 
path.reverse() 
 
 
with open(output_filename, 'w') as f: 
if path and path[0] == node_mapping[start]: 
f.write(f"Success: Path found.\nStart: {start}, Goal: {goal}\nOptimal Path: {' -> 
'.join([list(node_mapping.keys())[list(node_mapping.values()).index(i)] for i in path])}\n") 
else: 
f.write("Failure: No path found.\n") for i in range(n): 
f.write(f"Vertex: {i + 1} | Discovery time: {D[i]} | Finishing time: {F[i]} | Parent: {p[i]}\n") 
 
 
def read_graph_from_file(input_filename): 
with open(input_filename, 'r') as f: 
lines = f.readlines() 
 
start = lines[0].split(":")[1].strip() 
goal = lines[1].split(":")[1].strip() 
 
 
edges = [line.strip().split() for line in lines[2:]] 
nodes = set([node for edge in edges for node in edge]) node_mapping = {node: i for i, node in enumerate(sorted(nodes))} 
n = len(nodes) 
 
G = [[0] * n for _ in range(n)] for u, v in edges: 
G[node_mapping[u]][node_mapping[v]] = 1 
 
 
return G, node_mapping, start, goal 
 
 
def main(): 
input_filename = "input.txt" 
output_filename = "output.txt" 
 
G, node_mapping, start, goal = read_graph_from_file(input_filename) 
 
 
dfs(G, len(node_mapping), start, goal, node_mapping, output_filename) 
print("Results written to", output_filename) 
 
if  name 	== " main ": 
main() 
