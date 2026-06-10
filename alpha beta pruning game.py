# Alpha-Beta Pruning Implementation

# Sample game tree
game_tree = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F', 'G'],
    'D': 3,
    'E': 5,
    'F': 2,
    'G': 9
}

def alpha_beta(node, depth, alpha, beta, maximizing_player):

    # Base case: leaf node
    if depth == 0 or not isinstance(game_tree[node], list):
        return game_tree[node]

    if maximizing_player:
        value = float('-inf')

        for child in game_tree[node]:
            value = max(value,
                        alpha_beta(child, depth - 1,
                                   alpha, beta, False))

            alpha = max(alpha, value)

            # Beta cut-off
            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in game_tree[node]:
            value = min(value,
                        alpha_beta(child, depth - 1,
                                   alpha, beta, True))

            beta = min(beta, value)

            # Alpha cut-off
            if beta <= alpha:
                break

        return value

# Execute Alpha-Beta Pruning
result = alpha_beta('A', 2, float('-inf'), float('inf'), True)

print("Optimal value:", result)
