from collections import deque 
JUG_A_CAPACITY = 4 
JUG_B_CAPACITY = 3 
GOAL = 2  
initial_state = (0, 0) 
 
 
 
(a, b), path = queue.popleft() 

continue 
visited.add((a, b)) 

	((a, JUG_B_CAPACITY), "Fill Jug B"),  
	((0, b), "Empty Jug A"), 	 
	((a, 0), "Empty Jug B"), 	
 
((a - min(a, JUG_B_CAPACITY - b), b + min(a, JUG_B_CAPACITY - b)), "Pour A -> B"),
B 
 
((a + min(b, JUG_A_CAPACITY - a), b - min(b, JUG_A_CAPACITY - a)), "Pour B -> A") 
A 
 
] 
 
if (next_a, next_b) not in visited: 
queue.append(((next_a, next_b), path + [(a, b, action)]))  
if solution: 
print("Solution steps:") for state in solution: 
print(state) else: 
print("No solution found.") 
 
