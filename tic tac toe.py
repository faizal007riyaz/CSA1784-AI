# Tic Tac Toe Game for Two Players

# Display the board
def display_board(board):
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])
    print()

# Check for winner
def check_winner(board, player):
    win_patterns = [
        [0,1,2], [3,4,5], [6,7,8],  # Rows
        [0,3,6], [1,4,7], [2,5,8],  # Columns
        [0,4,8], [2,4,6]            # Diagonals
    ]

    for pattern in win_patterns:
        if all(board[pos] == player for pos in pattern):
            return True
    return False

# Main game function
def tic_tac_toe():
    board = [' '] * 9
    current_player = 'X'

    while True:
        display_board(board)

        try:
            position = int(input(f"Player {current_player}, enter position (1-9): ")) - 1

            if position < 0 or position > 8:
                print("Invalid position! Try again.")
                continue

            if board[position] != ' ':
                print("Position already occupied! Try again.")
                continue

            board[position] = current_player

            # Check for winner
            if check_winner(board, current_player):
                display_board(board)
                print(f"Player {current_player} wins!")
                break

            # Check for draw
            if ' ' not in board:
                display_board(board)
                print("The game is a draw!")
                break

            # Switch player
            current_player = 'O' if current_player == 'X' else 'X'

        except ValueError:
            print("Please enter a valid number.")

# Start the game
tic_tac_toe()
