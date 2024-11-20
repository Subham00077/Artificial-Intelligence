from collections import deque

def is_goal_state(state):

    return state[0] == 2 or state[1] == 2

def water_jug_problem(capacity_4, capacity_3):
    
    initial_state = (0, 0)
    visited = set()
    queue = deque([(initial_state, [])])  
    
    while queue:
        (jug_4, jug_3), path = queue.popleft()

    
        if is_goal_state((jug_4, jug_3)):
            return path + [(jug_4, jug_3)]
        
        
        if (jug_4, jug_3) in visited:
            continue
        visited.add((jug_4, jug_3))

        
        next_states = [
        
            (capacity_4, jug_3),
            
            (jug_4, capacity_3),
            
            (0, jug_3),
            
            (jug_4, 0),
            
            (max(0, jug_4 - (capacity_3 - jug_3)), min(capacity_3, jug_3 + jug_4)),
            
            (min(capacity_4, jug_4 + jug_3), max(0, jug_3 - (capacity_4 - jug_4)))
        ]
        
        
        for state in next_states:
            if state not in visited:
                queue.append((state, path + [(jug_4, jug_3)]))
    
    return None  

if __name__ == "__main__":
    capacity_4 = 4  
    capacity_3 = 3 

    result = water_jug_problem(capacity_4, capacity_3)
    
    if result:
        print("Solution found:")
        for step in result:
            print(f"Jug 4: {step[0]} liters, Jug 3: {step[1]} liters")
    else:
        print("No solution found.")
