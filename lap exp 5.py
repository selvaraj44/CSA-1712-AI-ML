from collections import deque

def is_valid(m, c):
    # Invalid if missionaries are outnumbered
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    if (3 - m) > 0 and (3 - m) < (3 - c):
        return False

    return True


def solve():
    # State = (missionaries, cannibals, boat)
    # boat = 0 -> left, 1 -> right

    start = (3, 3, 0)
    goal = (0, 0, 1)

    queue = deque([(start, [])])
    visited = set()

    moves = [
        (1, 0),   # 1 missionary
        (2, 0),   # 2 missionaries
        (0, 1),   # 1 cannibal
        (0, 2),   # 2 cannibals
        (1, 1)    # 1 missionary and 1 cannibal
    ]

    while queue:
        state, path = queue.popleft()

        if state in visited:
            continue

        visited.add(state)
        path = path + [state]

        if state == goal:
            for s in path:
                print(s)
            return

        m, c, boat = state

        for dm, dc in moves:
            if boat == 0:
                new_state = (m - dm, c - dc, 1)
            else:
                new_state = (m + dm, c + dc, 0)

            if is_valid(new_state[0], new_state[1]):
                if new_state not in visited:
                    queue.append((new_state, path))


solve()
