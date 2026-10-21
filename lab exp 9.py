
from itertools import permutations

n = int(input("Enter number of cities: "))

print("Enter the cost matrix:")
cost = [list(map(int, input().split())) for _ in range(n)]

cities = list(range(1, n))
min_cost = float('inf')
best_path = []

for p in permutations(cities):
    path = [0] + list(p) + [0]
    total = 0

    for i in range(len(path) - 1):
        total += cost[path[i]][path[i + 1]]

    if total < min_cost:
        min_cost = total
        best_path = path

print("Minimum cost:", min_cost)
print("Optimal path:", " -> ".join(map(str, best_path)))
