n, m = map(int, input().split())
graph = [[] for i in range(n)]
rev_graph = [[] for p in range(n)]
for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    rev_graph[b].append(a)

def dfs1(graph, start, used, vector):
    used.add(start)
    for node in graph[start]:
        if node not in used:
            dfs1(graph, node, used, vector)
    vector.append(start)

def dfs2(inv_graph, start, used, component):
    used.add(start)
    # component.append(start)
    for neighbour in inv_graph[start]:
        if neighbour not in used:
            dfs2(inv_graph, neighbour, used, component)
    component.append(start)

vector = []
used = set()
components = []

for node in range(len(graph)):
    if node not in used:
        dfs1(rev_graph, node, used, vector)

used = set()

for i in range (len(vector)):
    vertex = vector[len(vector) - 1 - i]
    if vertex not in used:
        component = []
        dfs2(graph, vertex, used, component)
        components.append(component)

print(len(components))
for comp in components:
    print(*comp)
