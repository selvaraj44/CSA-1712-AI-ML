
import heapq

def astar(graph, heuristic, start, goal):
    pq = [(heuristic[start], 0, start)]
    parent = {}
    cost = {start: 0}

    while pq:
        f, g, node = heapq.heappop(pq)

        if g != cost[node]:
            continue

        if node == goal:
            path = []
            while node in parent:
                path.append(node)
                node = parent[node]
            path.append(start)
            path.reverse()
            return path, g

        for neighbor, weight in graph[node]:
            new_cost = g + weight

            if new_cost < cost.get(neighbor, float('inf')):
                cost[neighbor] = new_cost
                parent[neighbor] = node
                f = new_cost + heuristic[neighbor]
                heapq.heappush(pq, (f, new_cost, neighbor))

    return None, -1


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

for i in range(e):
    u, v, w = map(int, input("Enter edge (u v cost): ").split())
    graph[u].append((v, w))
    graph[v].append((u, w))

heuristic = list(map(int, input("Enter heuristic values: ").split()))

start = int(input("Enter start vertex: "))
goal = int(input("Enter goal vertex: "))

path, total_cost = astar(graph, heuristic, start, goal)

if path:
    print("Optimal path:", " -> ".join(map(str, path)))
    print("Total cost:", total_cost)
else:
    print("No path found")
