def is_clean(grid):
    for row in grid:
        if 'D' in row:
            return False
    return True

def dfs(grid, x, y, visited):
    if is_clean(grid):
        return True

    state = (x, y, tuple(tuple(row) for row in grid))

    if state in visited:
        return False

    visited.add(state)

    # Clean current cell
    if grid[x][y] == 'D':
        grid[x][y] = 'C'

    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            new_grid = [row[:] for row in grid]

            if dfs(new_grid, nx, ny, visited):
                return True

    return False

# Input Room
grid = [
    ['D', 'C'],
    ['D', 'D']
]

start_x, start_y = 0, 0
visited = set()

if dfs(grid, start_x, start_y, visited):
    print("All cells cleaned successfully!")
else:
    print("Could not clean all cells.")
