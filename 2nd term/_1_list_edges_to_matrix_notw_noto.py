def create_graph_from_lists_to_matrix_no():
    n, m = map(int, input().split())
    graph = [[0 for i in range(n)] for x in range(n)]
    for j in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1
    return graph

def create_graph_from_lists_to_matrix_o():
    n, m = map(int, input().split())
    graph = [[0 for i in range(n)] for x in range(n)]
    for j in range(m):
        a, b = map(int, input().split())
        graph[a][b] = 1
    return graph
# for line in create_graph_from_lists_to_matrix():
#     print(' '.join(map(str, line)))
