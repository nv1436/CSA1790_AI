def dfs_recursive(current_pos, goal, grid, path, visited):
    # Define movements (up, down, left, right)
    movements = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    
    rows, cols = len(grid), len(grid[0])
    
    # Base cases
    if current_pos == goal:
        return path + [goal]
    
    visited.add(current_pos)
    
    for move in movements:
        new_row = current_pos[0] + move[0]
        new_col = current_pos[1] + move[1]
        new_pos = (new_row, new_col)
        
        if (0 <= new_row < rows and
            0 <= new_col < cols and
            grid[new_row][new_col] == 0 and
            new_pos not in visited):
            
            result = dfs_recursive(new_pos, goal, grid, path + [new_pos], visited)
            if result:
                return result
    
    return None

def dfs(start, goal, grid):
    visited = set()
    return dfs_recursive(start, goal, grid, [start], visited)

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

path = dfs(start, goal, grid)
print("Path found:")
print_grid(grid, path)
