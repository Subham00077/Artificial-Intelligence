import copy
GOAL_STATE = [[1, 2, 3], [4, 5, 6], [7, 8, 'B']]


def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 'B':
                return i, j
    return None

def h1(state):
    misplaced = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 'B' and state[i][j] != GOAL_STATE[i][j]:
                misplaced += 1
    return misplaced


def h2(state):
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 'B':
                goal_i, goal_j = divmod(state[i][j] - 1, 3)
                total_distance += abs(i - goal_i) + abs(j - goal_j)
    return total_distance

def get_neighbors(state):
    neighbors = []
    blank_i, blank_j = find_blank(state)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  

    for di, dj in directions:
        new_i, new_j = blank_i + di, blank_j + dj
        if 0 <= new_i < 3 and 0 <= new_j < 3:
            new_state = copy.deepcopy(state)
            new_state[blank_i][blank_j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[blank_i][blank_j]
            neighbors.append(new_state)

    return neighbors


def hill_climbing(start_state, heuristic_func):
    current_state = start_state
    while True:
        neighbors = get_neighbors(current_state)
        if not neighbors:
            return None  
        
        
        neighbor_costs = [(neighbor, heuristic_func(neighbor)) for neighbor in neighbors]
        neighbor_costs.sort(key=lambda x: x[1])  
        
        
        best_neighbor, best_cost = neighbor_costs[0]
        
        
        if best_cost == 0:
            return best_neighbor
        
        
        if best_cost >= heuristic_func(current_state):
            return None  
        
        
        current_state = best_neighbor


def print_state(state):
    for row in state:
        print(' '.join([str(cell) for cell in row]))
    print()

if __name__ == "__main__":
    
    start_state = [[1, 2, 3], [4, 5, 6], [7, 'B', 8]]  
    
    print("Initial State:")
    print_state(start_state)
    

    print("Solving with h1 (Misplaced Tiles)...")
    solution_h1 = hill_climbing(start_state, h1)
    if solution_h1:
        print("Solution found with h1:")
        print_state(solution_h1)
    else:
        print("No solution found with h1.")


    print("Solving with h2 (Manhattan Distance)...")
    solution_h2 = hill_climbing(start_state, h2)
    if solution_h2:
        print("Solution found with h2:")
        print_state(solution_h2)
    else:
        print("No solution found with h2.")
