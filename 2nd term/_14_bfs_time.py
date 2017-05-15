from _1_list_edges_to_matrix_notw_noto import create_graph_from_edges_to_matrix_no

graph = create_graph_from_edges_to_matrix_no()

components = []

def bfs(graph, start, used):
    component = []
    used.add(start)
    queue = []
    queue.append((start, 0))
    while queue:
        vertex, time = queue.pop(0)
        time += 1
        component.append((vertex, time))
        for j in range(len(graph)):
            if graph[vertex][j] == 1 and j not in used:
                queue.append((j, time))
                used.add(j)
    return component

used = set()
for node in range(len(graph)):
    if node not in used:
        components.append(bfs(graph, node, used))
for comp in components:
    comp = sorted(comp, key=lambda x: x[0])
    print(' '.join(map(lambda x: str((x[0], x[1])), comp)))
