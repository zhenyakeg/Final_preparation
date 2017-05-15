n, m = map(int, input().split())
edges = []
for j in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))
def krascal(graph):
    tree = []
    tree_weight = 0
    edges = sorted(graph, key=lambda x: x[2])
    names_of_comp = [i for i in range(n)]
    current_comp = names_of_comp[edges[0][0]]
    for v1, v2, cost in edges:
        prev_comp1 = names_of_comp[v1]
        if names_of_comp[v1] != names_of_comp[v2]:
            tree.append((v1, v2))
            tree_weight += cost
            for i in range(n):
                if names_of_comp[i] == prev_comp1:
                    names_of_comp[i] = names_of_comp[v2]
    return tree_weight, tree

res = krascal(edges)
print(res[0])
print('\n'.join(map(lambda x: str(x[0]) + ' ' + str(x[1]), res[1])))
