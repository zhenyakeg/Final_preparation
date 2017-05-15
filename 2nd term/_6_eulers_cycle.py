from _3_list_edges_to_lists_complementations_notw_noto import create_graph_from_lists_to_complementation_lists
import sys

G = create_graph_from_lists_to_complementation_lists()

def check_euler_cycle(graph):
    for node in graph:
        if len(graph[node]) % 2 != 0:
            return False
    return True

def dfs(vertex, data, path, used, result):
    if used == None:
        used = set()
    if path == None:
        path = []
    used.add(vertex)
    path.append(vertex)
    for node in data[vertex]:
        if node == path[0]:
            return path
        if node not in used:
            dfs(node, data, path, used)
    path.pop()

if check_euler_cycle(G):
    print('YES')
else:
    print('NO')