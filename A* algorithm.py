import heapq

class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0  # Cost from start to this node
        self.h = 0  # Heuristic cost to the goal
        self.f = 0  # Total cost (g + h)

    def __lt__(self, other):
        return self.f < other.f

def astar_algorithm(start, goal, grid):
    # Define movements (up, down, left, right)
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    start_node = Node(start)
    goal_node = Node(goal)
    
    open_list = []
    closed_list = set()
    
    heapq.heappush(open_list, start_node)
    
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)
        
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        
        for move in movements:
            new_position = (current_node.position[0] + move[0], current_node.position[1] + move[1])
            
            if not (0 <= new_position[0] < len(grid) and 0 <= new_position[1] < len(grid[0])):
                continue
            
            if grid[new_position[0]][new_position[1]] == 1:
                continue
            
            if new_position in closed_list:
                continue
            
            neighbor = Node(new_position, current_node)
            neighbor.g = current_node.g + 1
            neighbor.h = abs(goal_node.position[0] - neighbor.position[0]) + abs(goal_node.position[1] - neighbor.position[1])
            neighbor.f = neighbor.g + neighbor.h
            
            if any(open_node.position == neighbor.position and open_node.g < neighbor.g for open_node in open_list):
                continue
            
            heapq.heappush(open_list, neighbor)
    
    return None

def print_grid(grid, path=None):
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if path and (row, col) in path:
                print('P', end=' ')
            elif grid[row][col] == 1:
                print('X', end=' ')
            else:
                print('.', end=' ')
        print()

# Example grid (0 = free space, 1 = obstacle)
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)
goal = (4, 4)

path = astar_algorithm(start, goal, grid)
print("Path found:")
print_grid(grid, path)
