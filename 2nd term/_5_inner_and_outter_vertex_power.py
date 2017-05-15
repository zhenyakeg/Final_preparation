from _1_list_edges_to_matrix_notw_noto import create_graph_from_lists_to_matrix_o

G = create_graph_from_lists_to_matrix_o()
powers = [[0, 0] for j in range(len(G))]
for node in range(len(G)):
    for j in range(len(G)):
        powers[node][1] += G[node][j]
        powers[node][0] += G[j][node]
for vertex in range(len(G)):
    print(vertex, ':', ' '.join(map(str, powers[vertex])))
