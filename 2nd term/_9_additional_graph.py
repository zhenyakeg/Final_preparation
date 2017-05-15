n, m = map(int, input().split())
graph = []
add_graph = []
for j in range(m):
    a, b = map(int, input().split())
    graph.append((a, b))
for i in range(n):
    for j in range(n):
        if i != j and \
                        (i, j) not in graph and\
                        (j, i) not in graph and\
                        (i, j) not in add_graph and\
                        (j, i) not in add_graph:
            add_graph.append((i, j))
for edge in add_graph:
    print(*edge)

