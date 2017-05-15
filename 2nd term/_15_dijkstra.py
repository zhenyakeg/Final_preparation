import heapq

def dijkstra(graph, start, finish=None):
    used = set()
    distances =  {start : float('inf') for start in graph}
    ways = {start : [start]}
    queue =[]
    heapq.heappush(queue, (0, start))

    while queue:
        dist, vertex = heapq.heappop(queue)
        used.add(vertex)
        if dist >= distances[vertex]:
            continue
        distances[vertex] = dist
        for neighbour, cost in graph[vertex]:
            l = dist + cost
            way = ways[vertex] + [neighbour]
            if l < distances[neighbour]:
                heapq.heappush(queue, (l, neighbour))
                ways[neighbour] = way
    if finish is None:
        return distances, ways
    else:
        return distances[finish], ways[finish]

n, m = map(int, input().split())
graph = {i: [] for i in range(n)}
for j in range(m):
    a, b, c = map(int, input().split())
    graph[a] = graph.get(a, []) + [(b, c)]
st, fin = tuple(map(int, input().split()))
if fin == -1:
    res = dijkstra(graph, st)
    print(' '.join(map(lambda x: str((str(st) + '-' + str(x[0]), x[1])), res[0].items())))
    print(' '.join(map(lambda x: str((str(st) + '-' + str(x[0]), ' '.join(map(str, x[1])))), res[1].items())))
else:
    res = dijkstra(graph, st, fin)
    print(str(st) + '-' + str(fin), res[0])
    print(str(st) + '-' + str(fin), ' '.join(map(str, res[1])))
