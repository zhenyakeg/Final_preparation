from _1_list_edges_to_matrix_notw_noto import create_graph_from_lists_to_matrix_no

graph = create_graph_from_lists_to_matrix_no()
components = []

def dfs(graph, start, component=None, used= None):
    if used is None:
        used = set()
    if component is None:
        component = []
    used.add(start)
    component.append(start)
    for j in range(len(graph)):
        if graph[start][j] == 1 and j not in used:
            dfs(graph, j, component, used)
    return component
used = set()
for vertex in range(len(graph)):
    if vertex not in used:
        components.append(dfs(graph, vertex, used=used))
for comp in components:
    print(' '.join(map(str, comp)))
