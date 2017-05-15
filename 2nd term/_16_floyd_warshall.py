n, m = map(int, input().split())
graph = {i: [] for i in range(n)}
for j in range(m):
    a, b, c = map(int, input().split())
    graph[a] = graph.get(a, []) + [(b, c)]

W = [[float('inf') for i in range(n)] for j in range(n)]
for i in range(n):
    W[i][i] = 0
    for neighbour, cost in graph[i]:
        W[i][neighbour] = cost

for k in range(n):
    for j in range(n):
        for i in range(n):
            W[i][j] = min(W[i][j], W[i][k] + W[k][j])
for line in W:
    print(" ".join(map(str, line)))
