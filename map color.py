# Map Coloring using CSP and Backtracking

# Define the map and adjacency relationships
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

# Available colors
colors = ['Red', 'Green', 'Blue']

# Check if assigning a color is valid
def is_safe(region, color, assignment):
    for neighbor in graph[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

# Backtracking function
def map_coloring(assignment):
    # If all regions are assigned
    if len(assignment) == len(graph):
        return assignment

    # Select an unassigned region
    unassigned = [r for r in graph if r not in assignment]
    region = unassigned[0]

    # Try each color
    for color in colors:
        if is_safe(region, color, assignment):
            assignment[region] = color

            result = map_coloring(assignment)
            if result:
                return result

            # Backtrack
            del assignment[region]

    return None

# Solve the problem
solution = map_coloring({})

# Display result
if solution:
    print("Color Assignment:")
    for region, color in solution.items():
        print(region, "->", color)
else:
    print("No solution found.")
