from collections import deque

# Goal state
goal = "123456780"

# Possible moves
moves = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def bfs(start):
    queue = deque([(start, [])])
    visited = {start}

    while queue:
        state, path = queue.popleft()

        if state == goal:
            return path + [state]

        zero = state.index("0")

        for move in moves[zero]:
            new_state = list(state)
            new_state[zero], new_state[move] = new_state[move], new_state[zero]
            new_state = "".join(new_state)

            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, path + [state]))

    return None


# Get input
print("Enter the puzzle row by row")
print("Use 0 for the blank space")

start = ""

for i in range(3):
    row = input("Enter row " + str(i + 1) + ": ")
    start += row.replace(" ", "")

# Solve puzzle
solution = bfs(start)

if solution:
    print("\nSolution:")
    for state in solution:
        print(state[0], state[1], state[2])
        print(state[3], state[4], state[5])
        print(state[6], state[7], state[8])
        print()
else:
    print("No solution found.")
