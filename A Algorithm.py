import time 
from queue import PriorityQueue 
 
 
def a_star_algorithm(graph, start, goal, h): 
open_list = PriorityQueue() open_list.put((0, start)) came_from = {start: None} 
g_score = {start: 0} 
states_explored = 0 
 
 
while not open_list.empty(): 
current_priority, current_node = open_list.get() states_explored += 1 
 
if current_node == goal: 
path = [] 
while current_node is not None: path.append(current_node) current_node = came_from[current_node] 
return path[::-1], g_score[goal], states_explored 
  
for neighbor, cost in graph[current_node].items(): 
tentative_g_score = g_score[current_node] + cost 
 
if neighbor not in g_score or tentative_g_score < g_score[neighbor]: 
came_from[neighbor] = current_node g_score[neighbor] = tentative_g_score f_score = tentative_g_score + h(neighbor, goal) 
open_list.put((f_score, neighbor)) 
return None, float('inf'), states_explored 
 
 
def heuristic(node, goal): 
return 0 
 
def read_graph_from_file(input_filename): 
graph = {} with open(input_filename, 'r') as f: 
start = f.readline().strip().split(":")[1].strip() goal = f.readline().strip().split(":")[1].strip() 
for line in f: 
node1, node2, cost = line.split() cost = int(cost) if node1 not in graph: 
graph[node1] = {} if node2 not in graph: 
graph[node2] = {} graph[node1][node2] = cost 
graph[node2][node1] = cost return graph, start, goal 
def write_output_to_file(output_filename, path, total_cost, states_explored, time_taken, success, start, goal, heuristic_name="None"): 
with open(output_filename, 'w') as f: if success: 
f.write("Success: Path found\n") 
f.write(f"Heuristic: {heuristic_name}\n") 
f.write(f"Start state: {start}\n") 
f.write(f"Goal state: {goal}\n") 
f.write(f"Optimal path: {' -> '.join(path)}\n") 
f.write(f"Total cost of the path: {total_cost}\n") 
else: 
f.write("Failure: No path found\n") 
f.write(f"Total number of states explored: {states_explored}\n") 
f.write(f"Total time taken: {time_taken:.4f} seconds\n") 
 
def main(input_filename, output_filename): 
time_taken = end_time - start_time 
write_output_to_file(output_filename, path if success else [], cost, states_explored, 
time_taken, success, start, goal, heuristic_name="Simple Heuristic")  
main(input_filename, output_filename) 
