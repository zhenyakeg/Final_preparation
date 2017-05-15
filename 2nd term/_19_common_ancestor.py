vertex1, vertex2 = map(int, input().split())
m = int(input())
# tree = [[] for j in range(m + 1)]
reversed_tree = [[] for j in range(m + 1)]
for j in range(m):
    a, b = map(int, input().split())
    # tree[a].append(b)
    reversed_tree[b].append(a)
def common_ancestor(reversed_tree, vertex1, vertex2):
    q1 = [vertex1]
    q2 = [vertex2]
    while q1[-1] != q2[-1]:
        if reversed_tree[q1[-1]]:
            q1.append(reversed_tree[q1[-1]][0])
        if reversed_tree[q2[-1]]:
            q2.append(reversed_tree[q2[-1]][0])
    for j in range(-1, -min(len(q1), len(q2)) - 1, -1):
        if q1[j] != q2[j]:
            return q1[j + 1]
print(common_ancestor(reversed_tree, vertex1, vertex2))