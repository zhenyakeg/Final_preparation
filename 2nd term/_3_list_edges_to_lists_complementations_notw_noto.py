def create_graph_from_edges_to_complementation_lists():
    n, m = map(int, input().split())
    graph = {}
    for j in range(m):
        a, b = map(int, input().split())
        graph[a] = graph.get(a, []) + [b]
        graph[b] = graph.get(b, []) + [a]
    return graph


# G = create_graph_from_edges_to_complementation_lists()
# for node in G:
#     print(node, ':', ' '.join(map(str, G[node])))
