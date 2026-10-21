
board = [" "] * 9

def winner(p):
    wins = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]
    return any(all(board[i] == p for i in w) for w in wins)

def alphabeta(max_player, alpha, beta):
    if winner("O"):
        return 1
    if winner("X"):
        return -1
    if " " not in board:
        return 0

    if max_player:
        best = -100
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = alphabeta(False, alpha, beta)
                board[i] = " "
                best = max(best, score)
                alpha = max(alpha, best)
                if beta <= alpha:
                    break
        return best
    else:
        best = 100
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = alphabeta(True, alpha, beta)
                board[i] = " "
                best = min(best, score)
                beta = min(beta, best)
                if beta <= alpha:
                    break
        return best

def display():
    for i in range(0, 9, 3):
        print(board[i], "|", board[i+1], "|", board[i+2])
        if i < 6:
            print("--+---+--")

while True:
    display()
    move = int(input("Enter position (1-9): ")) - 1

    if move < 0 or move > 8 or board[move] != " ":
        print("Invalid move!")
        continue

    board[move] = "X"

    if winner("X"):
        display()
        print("You win!")
        break

    if " " not in board:
        display()
        print("Match Draw!")
        break

    best_score = -100
    best_move = -1

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = alphabeta(False, -100, 100)
            board[i] = " "

            if score > best_score:
                best_score = score
                best_move = i

    board[best_move] = "O"
    print("Computer chooses:", best_move + 1)

    if winner("O"):
        display()
        print("Computer wins!")
        break

    if " " not in board:
        display()
        print("Match Draw!")
        break
