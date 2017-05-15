from _1_list_edges_to_matrix_notw_noto import create_graph_from_edges_to_matrix_no

graph = create_graph_from_edges_to_matrix_no()

components = []

def bfs(graph, start, used):
    component = []
    used.add(start)
    queue = []
    queue.append(start)
    while queue:
        vertex = queue.pop(0)
        component.append(vertex)
        for j in range(len(graph)):
            if graph[vertex][j] == 1 and j not in used:
                queue.append(j)
                used.add(j)
    return component

used = set()
for node in range(len(graph)):
    if node not in used:
        components.append(bfs(graph, node, used))
for comp in components:
    print(' '.join(map(str, comp)))
