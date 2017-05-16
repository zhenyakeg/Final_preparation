n, m = map(int, input().split())
graph = [[] for j in range(n)]
for j in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def prim(graph, start):
    costs = [float('inf') for i in range(len(graph))]
    costs[start] = 0
    tree_nodes = [start]
    tree_edges = []
    tree_weight = 0
    for i in range(len(graph) - 1):
        curr_min_cost = float('inf')
        for node in tree_nodes:
            for neighbour, price in graph[node]:
                if price < curr_min_cost and neighbour not in tree_nodes:
                    curr_min_cost = price
                    curr_edge = (node, neighbour)
                    curr_vertex = neighbour
        tree_nodes.append(curr_vertex)
        tree_weight += curr_min_cost
        tree_edges.append(curr_edge)
    return tree_weight, tree_edges

res = prim(graph, 0)
print(res[0])
print(*res[1], sep='\n')

