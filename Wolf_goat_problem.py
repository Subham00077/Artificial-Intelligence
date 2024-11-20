from collections import deque
def is_valid(state):
    

    farmer, wolf, goat, cabbage = state

    
    if wolf == goat and farmer != wolf:
        return False
    if goat == cabbage and farmer != goat:  
        return False
    return True

def bfs_solution():

    initial_state = (0, 0, 0, 0)  
    goal_state = (1, 1, 1, 1)    
    
    queue = deque([(initial_state, [])])
    visited = set()  
    visited.add(initial_state)
    
    while queue:
        current_state, path = queue.popleft()
        farmer, wolf, goat, cabbage = current_state
        
    
        if current_state == goal_state:
            return path
        
        
        possible_moves = [
            (farmer ^ 1, wolf, goat, cabbage), 
            (farmer ^ 1, wolf ^ 1, goat, cabbage),  
            (farmer ^ 1, wolf, goat ^ 1, cabbage),  
            (farmer ^ 1, wolf, goat, cabbage ^ 1)   
        ]
        
        for new_state in possible_moves:
            if new_state not in visited and is_valid(new_state):
            
                visited.add(new_state)
                new_path = path + [new_state]
                queue.append((new_state, new_path))
    
    return None  

if __name__ == "__main__":
    solution = bfs_solution()
    
    if solution:
        print("Solution found:")
        for step in solution:
            farmer, wolf, goat, cabbage = step
            print(f"Farmer: {'Left' if farmer == 0 else 'Right'}, "
                  f"Wolf: {'Left' if wolf == 0 else 'Right'}, "
                  f"Goat: {'Left' if goat == 0 else 'Right'}, "
                  f"Cabbage: {'Left' if cabbage == 0 else 'Right'}")
    else:
        print("No solution found.")
