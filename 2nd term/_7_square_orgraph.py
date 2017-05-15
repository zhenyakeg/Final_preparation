n, m =  map(int,input().split())
graph = [[] for j in range(n)]
for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

def make_square_orgraph(graph):
    sq_graph = [[] for j in range(len(graph))]
    def bfs(graph, start, sq_graph):
        used = set()
        used.add(start)
        queue = [(start, 0)]
        while queue:
            vertex, time = queue.pop(0)

            if time <= 2:
                sq_graph[start].append(vertex)
            else:
                break
            time += 1
            for neighbour in graph[vertex]:
                if neighbour not in used:
                    queue.append((neighbour, time))
                    used.add(neighbour)
        return sq_graph
    for vertex in range(len(graph)):
        sq_graph = bfs(graph, vertex, sq_graph)
    return sq_graph

sq_G = make_square_orgraph(graph)

matrix_sq_graph = [[0 for j in range(len(sq_G))] for i in range(len(sq_G))]
print(sq_G)
for node in range(len(sq_G)):
    for neighbour in sq_G[node]:
        matrix_sq_graph[node][neighbour] = 1
for line in matrix_sq_graph:
    print(' '.join(map(str, line)))
