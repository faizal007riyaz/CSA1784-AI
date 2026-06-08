from collections import deque

# Check whether a state is valid
def is_valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    # Left bank condition
    if m > 0 and c > m:
        return False

    # Right bank condition
    mr = 3 - m
    cr = 3 - c
    if mr > 0 and cr > mr:
        return False

    return True

# Generate successor states
def get_successors(state):
    m, c, boat = state
    successors = []

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for dm, dc in moves:
        if boat == 1:  # Boat on left bank
            new_state = (m - dm, c - dc, 0)
        else:          # Boat on right bank
            new_state = (m + dm, c + dc, 1)

        nm, nc, _ = new_state

        if is_valid(nm, nc):
            successors.append(new_state)

    return successors

# BFS Algorithm
def bfs():
    start = (3, 3, 1)
    goal = (0, 0, 0)

    queue = deque([(start, [start])])
    visited = set()

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path

        if state in visited:
            continue

        visited.add(state)

        for successor in get_successors(state):
            if successor not in visited:
                queue.append((successor, path + [successor]))

    return None

# Find solution
solution = bfs()

if solution:
    print("Solution Path:\n")
    for step in solution:
        print(step)
else:
    print("No solution found")
