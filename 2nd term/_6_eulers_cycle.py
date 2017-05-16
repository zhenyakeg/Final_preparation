n, m = map(int, input().split())
G = [[] for i in range(n)]
edges = []
for j in range(m):
    a, b = map(int, input().split())
    G[a].append(b)
    G[b].append(a)
    edges.append((a, b))
    edges.append((b, a))

def check_euler_cycle(graph):
    for node in range(len(graph)):
        if len(graph[node]) % 2 != 0:
            return False
    return True

def dfs(vertex, data, path, used, edges):
    used.add(vertex)
    path.append(vertex)
    for node in data[vertex]:
        if node == path[0] and len(path) == len(data):
            return path
        if node not in used and (vertex, node) in edges:
            edges.pop(edges.index((vertex, node)))
            edges.pop(edges.index((node, vertex)))
            return dfs(node, data, path, used, edges)
        # edges.append((vertex, node))
        # edges.append((node, vertex))
    path.pop()

result = []
for node in range(len(G)):
    used = set()
    path = []
    curr_edges = edges.copy()
    res = dfs(node, G, path, used, curr_edges)
    result.append(res)

print(result)

if check_euler_cycle(G):
    print('YES')
else:
    print('NO')

