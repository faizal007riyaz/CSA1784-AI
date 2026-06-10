# Minimax Algorithm Implementation

# Sample game tree (leaf node values)
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 9
}

# Minimax function
def minimax(node, depth, maximizing_player):
    
    # Base case: leaf node
    if depth == 0 or not isinstance(game_tree[node], list):
        return game_tree[node]

    if maximizing_player:
        best_value = float('-inf')
        for child in game_tree[node]:
            value = minimax(child, depth - 1, False)
            best_value = max(best_value, value)
        return best_value

    else:
        best_value = float('inf')
        for child in game_tree[node]:
            value = minimax(child, depth - 1, True)
            best_value = min(best_value, value)
        return best_value

# Execute Minimax from root node
result = minimax('A', 2, True)

print("Optimal value:", result)
