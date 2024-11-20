import heapq
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)] 

def get_neighbors(state):
    
    neighbors = []
    empty_pos = state.index(0)
    row, col = divmod(empty_pos, 3)  
    for move in MOVES:
        new_row, new_col = row + move[0], col + move[1]
        if 0 <= new_row < 3 and 0 <= new_col < 3:  
            new_pos = new_row * 3 + new_col
            new_state = list(state)
            
            new_state[empty_pos], new_state[new_pos] = new_state[new_pos], new_state[empty_pos]
            neighbors.append(tuple(new_state))
    return neighbors

def h2(state, goal):
    """Heuristic h2: number of misplaced tiles."""
    return sum(1 for i in range(9) if state[i] != goal[i] and state[i] != 0)

def h3(state, goal):
    """Heuristic h3: sum of Manhattan distances."""
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            x, y = divmod(i, 3)
            goal_x, goal_y = divmod(goal_pos, 3)
            distance += abs(x - goal_x) + abs(y - goal_y)
    return distance

def h4(state, goal):
    return h3(state, goal) + 10  

def a_star(start, goal, heuristic):
    open_list = []
    heapq.heappush(open_list, (0 + heuristic(start, goal), start))  
    g_cost = {start: 0}  
    came_from = {}  

    while open_list:
        _, current_state = heapq.heappop(open_list)

        if current_state == goal:
            path = []
            while current_state in came_from:
                path.append(current_state)
                current_state = came_from[current_state]
            path.append(start)
            return path[::-1]  

        for neighbor in get_neighbors(current_state):
            tentative_g_cost = g_cost[current_state] + 1  
            if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                g_cost[neighbor] = tentative_g_cost
                f_cost = tentative_g_cost + heuristic(neighbor, goal)
                heapq.heappush(open_list, (f_cost, neighbor))
                came_from[neighbor] = current_state

    return None  

if __name__ == "__main__":

    goal_state = (1, 2, 3, 4, 5, 6, 7, 8, 0)

    
    print("Enter the initial state as a tuple (e.g., (1, 2, 3, 4, 5, 6, 7, 8, 0)):")
    start_state = tuple(map(int, input().split()))

    print("Choose a heuristic function:")
    print("1. h1(n) = 0 (trivial heuristic)")
    print("2. h2(n) = Number of displaced tiles")
    print("3. h3(n) = Sum of Manhattan distances")
    print("4. h4(n) = Overestimated heuristic")
    heuristic_choice = int(input("Enter choice (1/2/3/4): "))

    if heuristic_choice == 1:
        heuristic_function = lambda state, goal: 0
    elif heuristic_choice == 2:
        heuristic_function = h2
    elif heuristic_choice == 3:
        heuristic_function = h3
    elif heuristic_choice == 4:
        heuristic_function = h4
    else:
        print("Invalid choice, using h2 as default.")
        heuristic_function = h2

    
    path = a_star(start_state, goal_state, heuristic_function)

    if path:
        print("Solution found:")
        for state in path:
            print(state[:3])
            print(state[3:6])
            print(state[6:])
            print()
    else:
        print("No solution found.")
