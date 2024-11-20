import random
N = 8
def fitness(board):
    attacking_pairs = 0
    for i in range(N):
        for j in range(i+1, N):
            
            if board[i] == board[j] or abs(board[i] - board[j]) == abs(i - j):
                attacking_pairs += 1
    return attacking_pairs

def generate_board():

    return random.sample(range(N), N)


def tournament_selection(population, tournament_size=3):

    selected_parents = []
    for _ in range(2):
        tournament = random.sample(population, tournament_size)
        tournament.sort(key=lambda x: fitness(x))  
        selected_parents.append(tournament[0])
    return selected_parents


def crossover(parent1, parent2):
    point = random.randint(1, N - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2


def mutation(child, mutation_rate=0.05):

    if random.random() < mutation_rate:
        i, j = random.sample(range(N), 2)
        child[i], child[j] = child[j], child[i]
    return child


def genetic_algorithm(generations=1000, population_size=100, mutation_rate=0.05, tournament_size=3):

    
    population = [generate_board() for _ in range(population_size)]
    
    for generation in range(generations):
    
        population.sort(key=lambda x: fitness(x))
        
        
        if fitness(population[0]) == 0:
            return population[0], generation
        
        
        next_generation = []
        
        while len(next_generation) < population_size:
            parent1, parent2 = tournament_selection(population, tournament_size)
            child1, child2 = crossover(parent1, parent2)
            next_generation.append(mutation(child1, mutation_rate))
            next_generation.append(mutation(child2, mutation_rate))
        
    
        population = next_generation

    return None, generations 

def print_board(board):

    for row in range(N):
        line = ['Q' if board[row] == col else '.' for col in range(N)]
        print(' '.join(line))
    print()

if __name__ == "__main__":
    solution, generation = genetic_algorithm()
    
    if solution:
        print(f"Solution found in generation {generation}:")
        print_board(solution)
    else:
        print("No solution found within the given number of generations.")
