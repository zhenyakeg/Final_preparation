n, m = map(int, input().split())
graph = [[] for i in range(n)]
for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
def dfs(graph, start, times=None, used=None):
    if  used is None:
        used = set()
    if times is None:
        times = [0 for j in range(len(graph))]
    used.add(start)
    for neighbour in graph[start]:
        if neighbour not in used:
            times[neighbour] = times[start] + 1
            dfs(graph, neighbour, times, used)
    return times
print(' '.join(map(str, dfs(graph, 0))))