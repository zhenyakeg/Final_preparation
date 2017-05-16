n, m = map(int, input().split())
graph = [[] for j in range(n)]
weight_matrix = [[0 for j in range(n)] for i in range(n)]
for j in range(m):
    a, b, c = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    weight_matrix[a][b] = c
    weight_matrix[b][a] = c

def hamilton(graph, vertex, way=None, visited=None):
    if visited is None:
        visited = [False for i in range(n)]
    if way is None:
        way = []
    way.append(vertex)
    if len(way) == len(graph):
        if way[0] in graph[way[-1]]:
            return True
        else:
            way.pop()
            return False
    visited[vertex] = True
    for next in range(len(graph)):
        if next in graph[vertex]  and not visited[next]:
            if hamilton(graph, next, way, visited):
                return True
    visited[vertex] = False
    way.pop()
    return False

def all_hamiltons(graph, vertex, paths, curr_price=0, visited=None, way=None):
    if visited is None:
        visited = [False for i in range(len(graph))]
    if paths is None:
        paths = []
    if way is None:
        way = []
    way.append(vertex)
    visited[vertex] = True
    if len(graph) == len(way):
        if way[0] in graph[way[-1]]:
            paths.append((way.copy(), curr_price + weight_matrix[way[-1]][way[0]]))
    else:
        for next in graph[vertex]:
            if not visited[next]:
                all_hamiltons(graph, next, paths, curr_price + weight_matrix[vertex][next], visited, way)
    visited[vertex] = False
    way.pop()
paths = []

all_hamiltons(graph, 0, paths)

result = min(paths, key=lambda x: x[1])
print(result[1], ' '.join(map(str, result[0])), sep='\n')








