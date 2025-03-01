import itertools

def calculate_total_distance(distance_matrix, path):
    """
    Calculate the total distance of the given path based on the distance matrix.
    """
    total_distance = 0
    for i in range(len(path) - 1):
        total_distance += distance_matrix[path[i]][path[i + 1]]
    total_distance += distance_matrix[path[-1]][path[0]]  # Returning to the starting city
    return total_distance

def traveling_salesman_bruteforce(distance_matrix):
    """
    Solve the Traveling Salesman Problem using a brute-force approach.
    """
    n = len(distance_matrix)
    # Generate all possible permutations of cities
    all_permutations = itertools.permutations(range(n))
    
    min_path = None
    min_distance = float('inf')
    
    for path in all_permutations:
        current_distance = calculate_total_distance(distance_matrix, path)
        if current_distance < min_distance:
            min_distance = current_distance
            min_path = path
    
    return min_path, min_distance

# Example distance matrix
distance_matrix = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

# Solve the TSP
path, distance = traveling_salesman_bruteforce(distance_matrix)
print(f"Shortest path: {path}")
print(f"Total distance: {distance}")
