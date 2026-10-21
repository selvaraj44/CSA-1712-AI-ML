
def dfs(graph, vertex, visited):
    visited.add(vertex)
    print(vertex, end=" ")

    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)


n = int(input("Enter number of vertices: "))
e = int(input("Enter number of edges: "))

graph = [[] for _ in range(n)]

for i in range(e):
    u, v = map(int, input("Enter edge (u v): ").split())
    graph[u].append(v)
    graph[v].append(u)

start = int(input("Enter starting vertex: "))

print("DFS Traversal:", end=" ")
dfs(graph, start, set())
