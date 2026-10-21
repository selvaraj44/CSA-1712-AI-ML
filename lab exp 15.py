
def display():
    print()
    print(board[0], "|", board[1], "|", board[2])
    print("--+---+--")
    print(board[3], "|", board[4], "|", board[5])
    print("--+---+--")
    print(board[6], "|", board[7], "|", board[8])

board = [str(i) for i in range(1, 10)]

wins = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],
    [0, 3, 6], [1, 4, 7], [2, 5, 8],
    [0, 4, 8], [2, 4, 6]
]

player = "X"

for turn in range(9):
    display()
    pos = int(input("Player " + player + ", enter position (1-9): "))

    if pos < 1 or pos > 9 or board[pos - 1] in ["X", "O"]:
        print("Invalid position! Try again.")
        continue

    board[pos - 1] = player

    if any(all(board[i] == player for i in win) for win in wins):
        display()
        print("Player", player, "wins!")
        break

    player = "O" if player == "X" else "X"
else:
    display()
    print("Match Draw!")
