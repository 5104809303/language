# Chess Game

# Create the chess board
board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
         ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
         ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]

# Function to print the board
def print_board(board):
    for row in board:
        print(' '.join(row))

# Function to check if a move is valid
def is_valid_move(move):
    # Check if move is within the board boundaries
    if move[0] < 0 or move[0] > 7 or move[1] < 0 or move[1] > 7:
        return False

    # Check if there is a piece at the selected position
    if board[move[0]][move[1]] == ' ':
        return False

    return True

# Main game loop
while True:
    # Print the board
    print_board(board)

    # Get input from the player
    source_row = int(input("Enter the source row (0-7): "))
    source_col = int(input("Enter the source column (0-7): "))
    dest_row = int(input("Enter the destination row (0-7): "))
    dest_col = int(input("Enter the destination column (0-7): "))

    # Check if the move is valid
    if is_valid_move((source_row, source_col)) and is_valid_move((dest_row, dest_col)):
        # Perform the move
        piece = board[source_row][source_col]
        board[source_row][source_col] = ' '
        board[dest_row][dest_col] = piece
    else:
        print("Invalid move! Try again.")
