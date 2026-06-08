import heapq

# Goal state
GOAL = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Manhattan Distance Heuristic
def manhattan(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_pos = state[i] - 1
            distance += abs(i // 3 - goal_pos // 3) + abs(i % 3 - goal_pos % 3)
    return distance

# Generate neighboring states
def get_neighbors(state):
    neighbors = []
    blank = state.index(0)

    moves = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
        3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
        6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
    }

    for move in moves[blank]:
        new_state = list(state)
        new_state[blank], new_state[move] = new_state[move], new_state[blank]
        neighbors.append(tuple(new_state))

    return neighbors

# A* Search Algorithm
def a_star(start):
    frontier = []
    heapq.heappush(frontier, (manhattan(start), 0, start, []))
    visited = set()

    while frontier:
        f, g, current, path = heapq.heappop(frontier)

        if current in visited:
            continue

        visited.add(current)
        path = path + [current]

        if current == GOAL:
            return path

        for neighbor in get_neighbors(current):
            if neighbor not in visited:
                new_g = g + 1
                new_f = new_g + manhattan(neighbor)
                heapq.heappush(frontier, (new_f, new_g, neighbor, path))

    return None

# Example Start State
start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

solution = a_star(start_state)

if solution:
    print("Solution found in", len(solution) - 1, "moves:\n")
    for step in solution:
        for i in range(0, 9, 3):
            print(step[i:i+3])
        print()
else:
    print("No solution exists.")
