n, m = map(int, input().split())
graph = [[] for i in range(n)]
for j in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
k = int(input())
tasks = []

for i in range(k):
    s, f = map(int, input().split())
    tasks.append((s, f))

def bfs(graph, start, finish):
    used = set()
    used.add(start)
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        for neighbour in graph[vertex]:
            if neighbour not in used:
                if neighbour == finish:
                    return True
                used.add(neighbour)
                queue.append(neighbour)
    return False

for start, finish in tasks:
    if bfs(graph, start, finish):
        print(start, finish,':', "YES")
    else:
        print(start, finish, ':', "NO")
