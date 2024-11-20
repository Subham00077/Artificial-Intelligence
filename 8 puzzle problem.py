 from queue import PriorityQueue 
def find_blank_position(state): 
return state.index(0) 
 
 
def is_solvable(state):  
for j in range(i + 1, len(state)): 
if state[i] != 0 and state[j] != 0 and state[i] > state[j]: 
inv_count += 1 
return inv_count % 2 == 0 
 
def get_neighbors(state): 
neighbors = [] blank = find_blank_position(state) row, col = divmod(blank, 3) 
moves = { 
"up": (-1, 0), 
"down": (1, 0), 
"left": (0, -1), 
"right": (0, 1) 
} 
 
 
for move, (dx, dy) in moves.items(): 
new_row, new_col = row + dx, col + dy if 0 <= new_row < 3 and 0 <= new_col < 3: new_blank = new_row * 3 + new_col new_state = list(state) 
new_state[blank], new_state[new_blank] = new_state[new_blank], new_state[blank] neighbors.append(new_state) 
 
return neighbors 
 
 def h1(state, goal): 
"""Constant zero heuristic (Dijkstra's algorithm)""" 
return 0 
 
def h2(state, goal): 
"""Number of misplaced tiles heuristic""" 
return sum(1 for i in range(len(state)) if state[i] != 0 and state[i] != goal[i]) 
 
 def h3(state, goal): 
"""Sum of Manhattan distances heuristic""" total_distance = 0 for i in range(1, 9): 
current_pos = state.index(i) 
goal_pos = goal.index(i) current_row, current_col = divmod(current_pos, 3)
goal_row, goal_col = divmod(goal_pos, 3) 
total_distance += abs(current_row - goal_row) + abs(current_col - goal_col)
return total_distance 
 
def h4(state, goal): 
"""Overestimated heuristic (not admissible)"""
return 2 * h3(state, goal) 
 
def a_star_algorithm(start, goal, heuristic): 
if not is_solvable(start): 
return None, float('inf'), 0 
 
 
open_list = PriorityQueue() 
open_list.put((0, start)) 
g_score = {tuple(start): 0}
came_from = {tuple(start): None}
explored_nodes = 0 
 
while not open_list.empty(): _, current = open_list.get() explored_nodes += 1 
 
if current == goal: 
path = []
while current is not None: path.append(current)
current = came_from[tuple(current)]
return path[::-1], g_score[tuple(goal)], explored_nodes
for neighbor in get_neighbors(current): 
tentative_g_score = g_score[tuple(current)] + 1 
 
 
if tuple(neighbor) not in g_score or tentative_g_score < g_score[tuple(neighbor)]: 
came_from[tuple(neighbor)] = current g_score[tuple(neighbor)] = tentative_g_score f_score = tentative_g_score + heuristic(neighbor, goal) open_list.put((f_score, neighbor)) 
 
return None, float('inf'), explored_nodes 
 
 
def main(): 
print("Enter the start state in a single line (e.g., 1 2 3 4 5 6 7 8 0):") start_state = list(map(int, input().split())) print("Enter the goal state in a single line (e.g., 1 2 3 4 5 6 7 8 0):") goal_state = list(map(int, input().split())) 

print("Invalid input! Both states should have 9 values.") 
return 
 
print(f"Start state: {start_state}") 
print(f"Goal state: {goal_state}") 
 
 { 
"h1": h1, 
"h2": h2, 
"h3": h3, 
"h4": h4 
} 
 
 
print("\nChoose a heuristic function:") print("h1: Constant zero heuristic (Dijkstra's algorithm)") print("h2: Number of misplaced tiles heuristic") print("h3: Sum of Manhattan distances heuristic") 
print("h4: Overestimated heuristic (not admissible)") 
 
 
choice = input("Enter your choice (h1, h2, h3, or h4): ").strip() 
heuristic_function = heuristics.get(choice) 
 
if heuristic_function is None: print("Invalid choice! Defaulting to h1.") 
heuristic_function = h1 
 
 
path, cost, explored_nodes = a_star_algorithm(start_state, goal_state, heuristic_function) 
 
 if path: 
print("\nPath to solution:") for state in path: print(state[:3]) print(state[3:6]) print(state[6:]) print(f"Total cost: {cost}") print(f"Nodes explored: {explored_nodes}") 
else: 
print("No solution exists or the puzzle is unsolvable.")
 
 
if     name 	== " main ": 
main() 
