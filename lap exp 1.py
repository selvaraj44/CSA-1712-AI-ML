from heapq import heappush, heappop

# Goal state
goal = (1, 2, 3, 4, 5, 6, 7, 8, 0)

# Manhattan distance heuristic
def heuristic(state):
    distance = 0

    for i in range(9):
        if state[i] != 0:
            goal_pos = goal.index(state[i])
            distance += abs(i // 3 - goal_pos // 3)
            distance += abs(i % 3 - goal_pos % 3)

    return distance


# Generate possible moves
def get_neighbors(state):
    neighbors = []

    zero = state.index(0)
    row = zero // 3
    col = zero % 3

    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for dr, dc in moves:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < 3 and 0 <= new_col < 3:
            new_zero = new_row * 3 + new_col

            new_state = list(state)
            new_state[zero], new_state[new_zero] = \
                new_state[new_zero], new_state[zero]

            neighbors.append(tuple(new_state))

    return neighbors


# A* algorithm
def solve(start):
    priority_queue = []

    heappush(priority_queue, (heuristic(start), 0, start, []))

    visited = set()

    while priority_queue:

        f, cost, state, path = heappop(priority_queue)

        if state in visited:
            continue

        visited.add(state)

        path = path + [state]

        if state == goal:
            return path

        for neighbor in get_neighbors(state):
            if neighbor not in visited:
                new_cost = cost + 1
                new_f = new_cost + heuristic(neighbor)

                heappush(
                    priority_queue,
                    (new_f, new_cost, neighbor, path)
                )

    return None


# Print puzzle
def print_puzzle(state):
    for i in range(0, 9, 3):
        print(state[i], state[i+1], state[i+2])
    print()


# Input
print("Enter the initial state (use 0 for blank):")

numbers = list(map(int, input().split()))
start = tuple(numbers)

# Solve
solution = solve(start)

if solution:
    print("\nSolution found!")
    print("Number of moves:", len(solution) - 1)

    for step in solution:
        print_puzzle(step)
else:
    print("No solution found.")
