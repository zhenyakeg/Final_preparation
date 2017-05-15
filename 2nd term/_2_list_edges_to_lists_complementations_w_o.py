def create_graph_from_edges_to_complementation_lists():
    n, m = map(int, input().split())
    graph = {}
    for j in range(m):
        a, b, c = map(int, input().split())
        graph[a] = graph.get(a, []) + [(b, c)]
    return graph
# G = create_graph_from_lists_to_complementation_lists()
# for node in G:
#     print(node,':',' '.join(map(str, G[node])))
