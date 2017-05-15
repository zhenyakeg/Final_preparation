n, m =  map(int,input().split())
graph = [[] for j in range(n)]
for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
t_graph = [[] for j in range(n)]
for vertex in range(len(graph)):
    for neighbour in graph[vertex]:
        t_graph[neighbour].append(vertex)
for vertex in range(len(t_graph)):
    print(vertex, ':', ' '.join(map(str,t_graph[vertex])))
