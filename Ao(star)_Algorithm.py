import heapq

# Node types
OR_NODE = 0
AND_NODE = 1

class Node:
    def __init__(self, name, node_type, cost=0):
        self.name = name  # Node identifier
        self.type = node_type  # OR or AND node
        self.cost = cost  # Cost of the node
        self.children = []  # Children of this node (pairs of child nodes and their costs)
        self.best_cost = float('inf')  # Best cost to reach this node (for AO* search)
        self.parent = None  # Parent node (to reconstruct the solution)

    def add_child(self, child_node, cost):
        """Add a child node and the associated cost."""
        self.children.append((child_node, cost))

def ao_star(start_node):
    """
    Implements the AO* algorithm to solve a game tree.
    
    :param start_node: The starting node of the game tree.
    :return: The solution path with the minimum cost.
    """
    open_list = []
    heapq.heappush(open_list, (start_node.cost, start_node))

    while open_list:
        # Pop the node with the lowest cost (best first search)
        current_cost, current_node = heapq.heappop(open_list)

        if current_node.best_cost <= current_cost:
            continue

        current_node.best_cost = current_cost

        # If it's an OR node, we only need to find the minimum cost among children
        if current_node.type == OR_NODE:
            min_cost = float('inf')
            for child, child_cost in current_node.children:
                total_cost = child_cost + child.best_cost
                min_cost = min(min_cost, total_cost)

            current_node.best_cost = min_cost
            heapq.heappush(open_list, (min_cost, current_node))

        # If it's an AND node, we must satisfy all children
        elif current_node.type == AND_NODE:
            total_cost = 0
            for child, child_cost in current_node.children:
                total_cost += child_cost + child.best_cost

            current_node.best_cost = total_cost
            heapq.heappush(open_list, (total_cost, current_node))

        # Once all nodes are processed, we return the best path
        if current_node.best_cost < float('inf'):
            return current_node.best_cost


if __name__ == "__main__":
    # Read inputs for the game tree
    print("Welcome to the AO* Algorithm for solving a game tree!")
    
    nodes = {}
    
    # Input the number of nodes in the tree
    n = int(input("Enter the number of nodes in the game tree: "))
    
    # Create the nodes
    for _ in range(n):
        name = input("Enter the name of the node: ")
        node_type = int(input("Enter the node type (0 for OR, 1 for AND): "))
        cost = int(input("Enter the cost of the node: "))
        nodes[name] = Node(name, node_type, cost)
    
    # Add children to each node
    for name, node in nodes.items():
        num_children = int(input(f"Enter the number of children for node {name}: "))
        for _ in range(num_children):
            child_name = input(f"Enter child name for node {name}: ")
            child_cost = int(input(f"Enter the cost of moving to child {child_name}: "))
            node.add_child(nodes[child_name], child_cost)
    
    # Get the start node from the user
    start_name = input("Enter the start node name: ")
    
    # Run the AO* algorithm
    start_node = nodes[start_name]
    min_cost = ao_star(start_node)
    
    print(f"The minimum cost to solve the game tree is: {min_cost}")



"""
Welcome to the AO* Algorithm for solving a game tree!

Enter the number of nodes in the game tree: 5
Enter the name of the node: A
Enter the node type (0 for OR, 1 for AND): 0
Enter the cost of the node: 5
Enter the name of the node: B
Enter the node type (0 for OR, 1 for AND): 1
Enter the cost of the node: 2
Enter the name of the node: C
Enter the node type (0 for OR, 1 for AND): 1
Enter the cost of the node: 2
Enter the name of the node: D
Enter the node type (0 for OR, 1 for AND): 0
Enter the cost of the node: 0
Enter the number of children for node A: 2
Enter child name for node A: B
Enter the cost of moving to child B: 3
Enter child name for node A: C
Enter the cost of moving to child C: 4
Enter the number of children for node B: 1
Enter child name for node B: D
Enter the cost of moving to child D: 1
Enter the number of children for node C: 1
Enter child name for node C: D
Enter the cost of moving to child D: 2
Enter the number of children for node D: 0

Enter the start node name: A
"""
