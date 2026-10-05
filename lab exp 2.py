def is_safe(board, row, col):
    # Check same column
    for i in range(row):
        if board[i] == col:
            return False

    # Check diagonals
    for i in range(row):
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


def solve(board, row):
    # All queens placed
    if row == 8:
        print_board(board)
        return True

    # Try each column
    for col in range(8):
        if is_safe(board, row, col):
            board[row] = col

            if solve(board, row + 1):
                return True

            board[row] = -1

    return False


def print_board(board):
    for row in range(8):
        for col in range(8):
            if board[row] == col:
                print("Q", end=" ")
            else:
                print(".", end=" ")
        print()


# Main program
board = [-1] * 8

if solve(board, 0):
    print("Solution found!")
else:
    print("No solution found.")
