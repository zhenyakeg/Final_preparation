from _1_list_edges_to_matrix_notw_noto import create_graph_from_lists_to_matrix_no

G = create_graph_from_lists_to_matrix()

for node in range(len(G)):
    node_power = 0
    for j in range(len(G)):
        node_power += G[node][j]
    print(node, ':', node_power)