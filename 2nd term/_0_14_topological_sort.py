import sys
n, m = map(int, input().split())
graph = [[] for j in range(n)]
for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def dfs(graph, vertex, stack=None, path=None, used= None):
    if used is None:
        used = set()
    if path is None:
        path = []
    if stack is None:
        stack = set()
    used.add(vertex)
    stack.add(vertex)
    for neighbour in graph[vertex]:
        if neighbour in stack:
            print('NO')
            sys.exit(0)
        if neighbour not in used:
            dfs(graph, neighbour, stack, path, used)
    stack.remove(vertex)
    path.append(vertex)

topologically_sorted_list = []
used = set()
for current in range(len(graph)):
    if current not in used:
        dfs(graph, current, path=topologically_sorted_list, used=used)
print(' '.join(map(str, topologically_sorted_list[::-1])))